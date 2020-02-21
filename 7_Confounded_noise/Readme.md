# Confounded Noise
  - a cluster of Linearly separable Data at corner with noise 
  - a cluster of Linearly separable Data at center with noise
  - a non-linealry separable data with noise
## Linearly separable at Corner with noise 
- Original Data

    ![](sep_data_cor.png)
    
- Data with noise

    ![](spe_cor_noise.png)
    
- TABLE 2 : Analysis with size of true data

|true data  | Corrupted Data | Total Data | Training Accuracy | Test Accuracy |  Data Acc with no noise | 
|-----------| ---------------| ---------- | ----------------- |---------------| ----------------------- |
| 30        | 240            | 270        |   97              |   57          |  100                    |
| 60        | 240            | 300        |   96              |   61          |  100                    | 
| 90        | 240            | 330        |   96              |   66          |  100                    | 
| 120       | 240            | 360        |   98              |   67          |  100                    | 

-True Data size: 30

![](data30.png)

-True Data size: 60

![](data60.png)

-True Data size: 90

![](data90.png)

-True Data size: 120

![](data120.png)




## Accuracy with 2 hidden layer (64-> 64->2)
   - Training   - 73
   - Test   - 61
   - no noise - 100


![](simple2.png)




## Accuracy with linear model
   - Training - 60
   - Test - 59 
   - no noise  - 50



![](linear.png)




## Accuracy with 1 hidden layer (256->2)
   - Training   - 74
   - Test   - 55 
   - no noise - 100


![](simple1.png)



## Linearly separable at Center with noise

- Original Data

    ![](og_data_center.png)
    
- Data with noise

    ![](og_data_cntr_noise.png)
    
   
 - Prediction
     
      ![](cen_pred.png)
      
      
## Moon Data with noise
   - Original Data
   
   ![](og1.png)
      
      
   - Data with Noise
   
   ![](og1_noise.png)
   
   
   - Prediction 
   
   ![](pred1.png)






