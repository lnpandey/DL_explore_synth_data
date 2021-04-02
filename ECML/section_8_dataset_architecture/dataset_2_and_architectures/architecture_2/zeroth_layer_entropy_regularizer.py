# -*- coding: utf-8 -*-
"""zeroth_layer_entropy_regularizer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13egBagoLjs_PdgYabBSQFt44sKvCAeOK
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd

import torch
import torchvision
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from matplotlib import pyplot as plt

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)
# %matplotlib inline

class MosaicDataset1(Dataset):
  """MosaicDataset dataset."""

  def __init__(self, mosaic_list, mosaic_label,fore_idx):
    """
      Args:
        mosaic_list : list of mosaic instances
        mosaic_label : list of labels asscociated with respective mosaic instance
        fore_idx : list of indices of foreground data in respective mosaic instance
    """
    self.mosaic = mosaic_list
    self.label = mosaic_label
    self.fore_idx = fore_idx
    
  def __len__(self):
    return len(self.label)

  def __getitem__(self, idx):
    return self.mosaic[idx] , self.label[idx] , self.fore_idx[idx]

# load mosaic data
data = np.load("mosaic_data.npy",allow_pickle=True)
mosaic_list_of_images = data[0]["mosaic_list"]
mosaic_label = data[0]["mosaic_label"]
fore_idx = data[0]["fore_idx"]

batch = 250
msd = MosaicDataset1( mosaic_list_of_images, mosaic_label, fore_idx )
train_loader = DataLoader( msd,batch_size= batch ,shuffle=True )

class Focus_deep(nn.Module):
    '''
       deep focus network averaged at zeroth layer with input-6-12-output architecture
       input : elemental data
    '''
    def __init__(self,inputs,output,K,d):
        super(Focus_deep,self).__init__()
        self.inputs = inputs
        self.output = output
        self.K = K
        self.d  = d
        self.linear1 = nn.Linear(self.inputs,6)  #,self.output)
        self.linear2 = nn.Linear(6,12)
        self.linear3 = nn.Linear(12,self.output) 
    def forward(self,z):
        batch = z.shape[0]
        x = torch.zeros([batch,self.K],dtype=torch.float64)
        y = torch.zeros([batch,5], dtype=torch.float64)   # number of features of output
        features = torch.zeros([batch,self.K,5],dtype=torch.float64)
        x,y = x.to(device),y.to(device)
        features = features.to(device)
        for i in range(self.K):
            alp,ftrs = self.helper(z[:,i] )  # self.d*i:self.d*i+self.d
            x[:,i] = alp[:,0]
            features[:,i]  = ftrs 
        log_x = F.log_softmax(x,dim=1)  # log_alphas
        x = F.softmax(x,dim=1)   # alphas
        
        for i in range(self.K):
            x1 = x[:,i]          
            y = y+torch.mul(x1[:,None],features[:,i])  # self.d*i:self.d*i+self.d
        return y , x,log_x 
    def helper(self,x):
      x1 = x
      x = self.linear1(x)
      x = F.relu(x) 
      x = self.linear2(x)
      x = F.relu(x)
      x = self.linear3(x)
      return x,x1

class Classification_deep(nn.Module):
    '''
       input : elemental data
       deep classification module data averaged at zeroth layer with architecture input-6-12-output
    '''
    def __init__(self,inputs,output):
        super(Classification_deep,self).__init__()
        self.inputs = inputs
        self.output = output
        self.linear1 = nn.Linear(self.inputs,6)
        self.linear2 = nn.Linear(6,12)
        self.linear3 = nn.Linear(12,self.output)

    def forward(self,x):
      x = F.relu(self.linear1(x))
      x = F.relu(self.linear2(x))
      x = self.linear3(x)
      return x

# cross_entropy_loss + entropy regularizer
criterion = nn.CrossEntropyLoss()
def my_cross_entropy(x, y,alpha,log_alpha,k):
    """
    returns regularized_loss, CrossEntropy Loss, Entropy_loss
    """
    loss = criterion(x,y)
    b = -1.0* alpha * log_alpha
    b =  torch.mean(torch.sum(b,dim=1))
    closs = loss
    entropy = b 
    loss = (1-k)*loss + ((k)*b)
    return loss,closs,entropy

def calculate_attn_loss(dataloader,what,where,k):
  """
  returns regularized_loss, CrossEntropy, Entropy, analysis(FTPT,FFPT,FTPF,FFPF) 
  """
  what.eval()
  where.eval()
  r_loss = 0
  cc_loss = 0
  cc_entropy = 0 
  alphas = []
  lbls = []
  pred = []
  fidices = []
  with torch.no_grad():
    for i, data in enumerate(dataloader, 0):
      inputs, labels,fidx = data
      lbls.append(labels)
      fidices.append(fidx)
      inputs = inputs.double()
      inputs, labels = inputs.to("cuda"),labels.to("cuda")
      avg,alpha,log_alpha = where(inputs)
      outputs = what(avg)
      _, predicted = torch.max(outputs.data, 1)
      pred.append(predicted.cpu().numpy())
      alphas.append(alpha.cpu().numpy())
      loss,closs,entropy = my_cross_entropy(outputs,labels,alpha,log_alpha,k)
      r_loss += loss.item()
      cc_loss += closs.item()
      cc_entropy += entropy.item()
  alphas = np.concatenate(alphas,axis=0)
  pred = np.concatenate(pred,axis=0)
  lbls = np.concatenate(lbls,axis=0)
  fidices = np.concatenate(fidices,axis=0)
  analysis = analyse_data(alphas,lbls,pred,fidices)
  return r_loss/i,cc_loss/i,cc_entropy/i,analysis

def analyse_data(alphas,lbls,predicted,f_idx):
    '''
       analysis data is created here ,ie FTPT,FFPT ...
    '''
    batch = len(predicted)
    amth,alth,ftpt,ffpt,ftpf,ffpf = 0,0,0,0,0,0
    for j in range (batch):
      focus = np.argmax(alphas[j])
      if(alphas[j][focus] >= 0.5):
        amth +=1
      else:
        alth +=1
      if(focus == f_idx[j] and predicted[j] == lbls[j]):
        ftpt += 1
      elif(focus != f_idx[j] and predicted[j] == lbls[j]):
        ffpt +=1
      elif(focus == f_idx[j] and predicted[j] != lbls[j]):
        ftpf +=1
      elif(focus != f_idx[j] and predicted[j] != lbls[j]):
        ffpf +=1
    #print(sum(predicted==lbls),ftpt+ffpt)
    return [ftpt,ffpt,ftpf,ffpf,amth,alth]

# Training Starts
number_runs = 20
full_analysis = [] 
FTPT_analysis = pd.DataFrame(columns = ["FTPT","FFPT", "FTPF","FFPF"])

k = 0.005 # regualrization parameter

r_loss = []   # stores regularized loss
r_closs = []  # stores CrossEntropy loss
r_centropy = [] # stores Entropy
for n in range(number_runs):
  print("--"*40)
  
  # instantiate focus and classification Model
  torch.manual_seed(n)
  where = Focus_deep(5,1,9,5).double()
  torch.manual_seed(n)
  what = Classification_deep(5,3).double()
  where = where.to("cuda")
  what = what.to("cuda")



  # instantiate optimizer
  optimizer_where = optim.Adam(where.parameters(),lr =0.01)#,momentum=0.9)
  optimizer_what = optim.Adam(what.parameters(), lr=0.01)#,momentum=0.9)


  acti = []
  analysis_data = []
  loss_curi = []
  cc_loss_curi = []
  cc_entropy_curi = []
  
  
  epochs = 500   # no of epochs for each run


  # calculate zeroth epoch loss and FTPT values
  running_loss,_,_,anlys_data = calculate_attn_loss(train_loader,what,where,k)
  loss_curi.append(running_loss)
  analysis_data.append(anlys_data)

  print('epoch: [%d ] loss: %.3f' %(0,running_loss)) 

  # training starts 
  for epoch in range(epochs): # loop over the dataset multiple times
    ep_lossi = []
    running_loss = 0.0
    what.train()
    where.train()
    for i, data in enumerate(train_loader, 0):
      # get the inputs
      inputs, labels,_ = data
      inputs = inputs.double()
      inputs, labels = inputs.to("cuda"),labels.to("cuda")

      # zero the parameter gradients
      optimizer_where.zero_grad()
      optimizer_what.zero_grad()
      
      # forward + backward + optimize
      avg, alpha,log_alpha = where(inputs)
      outputs = what(avg)
      loss,_,_ = my_cross_entropy( outputs,labels,alpha,log_alpha,k)

      # print statistics
      running_loss += loss.item()
      loss.backward()
      optimizer_where.step()
      optimizer_what.step()

    running_loss,ccloss,ccentropy,anls_data = calculate_attn_loss(train_loader,what,where,k)
    analysis_data.append(anls_data)
    print('epoch: [%d] loss: %.3f celoss: %.3f entropy: %.3f' %(epoch + 1,running_loss,ccloss,ccentropy)) 
    loss_curi.append(running_loss)   #loss per epoch
    cc_loss_curi.append(ccloss)
    cc_entropy_curi.append(ccentropy)
    if running_loss<=0.01:
      break
  print('Finished Training run ' +str(n))
  analysis_data = np.array(analysis_data)
  FTPT_analysis.loc[n] = analysis_data[-1,:4]/30
  full_analysis.append((epoch, analysis_data))
  r_loss.append(np.array(loss_curi))
  r_closs.append(np.array(cc_loss_curi))
  r_centropy.append(np.array(cc_entropy_curi))
  
  
  correct = 0
  total = 0
  with torch.no_grad():
    for data in train_loader:
      images, labels,_ = data
      images = images.double()
      images, labels = images.to("cuda"), labels.to("cuda")
      avg, alpha,_ = where(images)
      outputs  = what(avg)
      _, predicted = torch.max(outputs.data, 1)
      total += labels.size(0)
      correct += (predicted == labels).sum().item()

  print('Accuracy of the network on the 3000 train images: %d %%' % (  100 * correct / total))

cnt=1
for epoch, analysis_data in full_analysis:
  analysis_data = np.array(analysis_data)
  # print("="*20+"run ",cnt,"="*20)
  
  plt.figure(figsize=(6,6))
  plt.plot(np.arange(0,epoch+2,1),analysis_data[:,0],label="ftpt")
  plt.plot(np.arange(0,epoch+2,1),analysis_data[:,1],label="ffpt")
  plt.plot(np.arange(0,epoch+2,1),analysis_data[:,2],label="ftpf")
  plt.plot(np.arange(0,epoch+2,1),analysis_data[:,3],label="ffpf")

  plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
  plt.title("Training trends for run "+str(cnt))
  cnt+=1

print(np.mean(np.array(FTPT_analysis),axis=0))  # Average over number of runs for FTPT, FFPT, FTPF, FFPF

FTPT_analysis.to_csv("zeroth.csv",index=False)  #  save the file