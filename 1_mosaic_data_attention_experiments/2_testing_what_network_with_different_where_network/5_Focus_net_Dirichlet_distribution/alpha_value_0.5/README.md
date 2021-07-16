### Focus net output as Dirichlet Distribution

- alpha value = 0.5


### Creation of datasets
- First, we have created 20000 Mosaic images.
- Labels of every Mosaic image is the class of foreground image present in that image.
- Dataset 'i' will contain 10000 image. Where each image is weighted average of 9 images present in Mosaic image. 
- Dataset 1 to Dataset 9 are made from same 10k Mosaic Images.
- Dataset 10 is made from 10000 to 20000 Mosaic Images which only contains the true Foreground Image present in every Mosaic Image.
- We have modeled the output of Focus network using the Dirichlet distribution with parameters alpha 
- 
- Since we know exactly where the foreground image is present in the Mosaic image, there fore Dataset 'i', weight_of_foreground_image = a_i*alpha and weight_of_background_image = alpha. 
- Therefore Average Image in Dataset 'i' = w_fg * I_fg + sum_over_all_background_images( w_bg * I_bg ) 
- Where w_fg = weight_of_foreground_image, w_bg = weight_of_background_image, I_fg = Foreground_Image, I_bg = Background_Image
- w_fg = a_i*alpha, w_bg= alpha

### Datasets:
- Parameter of distribution for Dataset 1 will be alpha for every image from mosaic.
- Parameter of distribution for Dataset 2 will be 16/7*alpha for foreground image from mosaic and alpha for backgroud image.
- Parameter of distribution for Dataset 3 will be 4*alpha for foreground image from mosaic and alpha for backgroud image.
- Parameter of distribution for Dataset 4 will be 32/5*alpha for foreground image from mosaic and alpha for backgroud image.
- Parameter of distribution for Dataset 5 will be 10*alpha for foreground image from mosaic and alpha for backgroud image.
- Parameter of distribution for Dataset 6 will be 16*alpha for foreground image from mosaic and alpha for backgroud image.
- Parameter of distribution for Dataset 7 will be 28*alpha for foreground image from mosaic and alpha for backgroud image.
- Parameter of distribution for Dataset 8 will be 64*alpha for foreground image from mosaic and alpha for backgroud image.
- Parameter of distribution for Dataset 9 will be 1*alpha for foreground image from mosaic and 0*alpha for backgroud image.
- Dataset 10 will contain true foreground images of Mosaic Images from 10000 to 20000.

### Experiment brief:
- Model ( what network) is trained on Dataset 'i', and Tested on all Dataset 'j', where j is not equal to i, j belongs to 1 to 9.
- We want to see, as the "Where" network perform better, i.e from Dataset 1 to Dataset 9 ( "Where" network learns to focus better),  how the "what" network behaves.
- Mini inception net has been used to train the classification network.

#### Weights and Datasets of Experiment can be found here :
>
### Analysis of Accuracy on Training & Testing Data

| train\ test  | test on dataset 1 | test on dataset 2 | test on dataset 3 | test on dataset 4 | test on dataset 5 | test on dataset 6 | test on dataset 7 | test on dataset 8 | test on dataset 9| test on dataset 10 |
|----------|-----|-----|-----|-----|-----|-----|-----|-----|----|----|
| train dataset 1      | - | 46 | 51 | 55 | 58 | 60 | 61 | 61 | 61 | 59 |
| train dataset 2      | 44 | - | 61 | 68 | 73 | 76 | 78 | 78 | 78 | 74 |
| train dataset 3      | 45 | 57 | - | 79 | 85 | 89 | 90 | 90 | 90 | 86 |     
| train dataset 4      | 45 | 57 | 71 | - | 90 | 94 | 96 | 96 | 96 | 91 |
| train dataset 5      | 44 | 57 | 71 | 84 | - | 96 | 98 | 98 | 98 | 93 |
| train dataset 6      | 42 | 55 | 69 | 82 | 90 | - | 98 | 98 | 98 | 94 |
| train dataset 7      | 43 | 55 | 69 | 82 | 91 | 97 | - | 99 | 99 | 95 |
| train dataset 8      | 42 | 54 | 68 | 81 | 89 | 96 | 99 | - | 99 | 95 |
| train dataset 9      | 41 | 53 | 66 | 79 | 88 | 95 | 98 | 99 | - | 95 |



### Plot of Training loss for all the Datasets :
 ![](Figure.png)
 
### Observations
