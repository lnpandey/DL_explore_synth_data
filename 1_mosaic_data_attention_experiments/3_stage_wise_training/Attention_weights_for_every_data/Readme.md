### Learning attention weights for every data point CIFAR data


- init1  attention weights from normal distribution
- init2 equal attention weights for each object i.e. (1/9) 

#### Table A1: Simultaneous Model Performance (in percentage)
| \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| Train | 70.93 	 | 29.07 |	73.690000 |	24.933333 |	0.300000 |	1.076667 | 
| Test | 67.48	 |  32.52 |	66.16 |	17.39 |	4.10 |	12.35 |




#### Table A2.1 : learning attention weights as well as what net (init 1)
LR for learning what net parameters is fixed 0.001

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 15.91 |	84.08	 |  16.39 |	80.88 |	0.216	|  2.51 |
| 0.1 | 54.87 | 	45.13 |	19.65 |78.36 |	0.216	 | 1.76 |
| 1 |99.68 |	0.31 | 21.12 |	56.67 |	2.04 |	20.17 |
| 10 | 100 |	0	 | 19.89 |	54.78 |	2.35 |	22.97 |



#### Table A2.2 : learning attention weights as well as what net (init 2)

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 |0.0033 |	99.99 |	24.51 |	73.83 |	0.37 | 1.28 |
| 0.1 | 28.52 |	71.47 |	26.56 |	71.35 |	0.31 |	1.76 |
| 1  | 94.92 |	5.07 | 27.37 |	67.38 |	0.46 | 	4.78 |
| 10 | 99.95 |	0.04 | 25.44 | 64.65	| 0.94 | 8.96  |




#### Now we are fixing the what net with final weights of simultaneous trained what net

#### Table A3.1: Fixed what net learning only attention weights for each data point (init 1)
| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 12.95 | 	87.04 |	16.25 |	77.56 |	0.16 |	6.01 |
| 0.1 | 41.61 |	58.39 |	23.82 |	73.89	 | 0.016 |	2.27 |
| 1 | 87.77	| 12.22 |	28.2 |	55.65 |	0.436 |	15.71 |
| 10  | 94.73 |	5.26	 | 26.52	| 47.42	 | 0.84	| 25.20 |

#### Table A3.2: Fixed what net learning only attention weights for each data point (init 2)
| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 0.01 |	99.99 |	19.97 |	76.33 |	0.37 |	3.31 |
| 0.1 | 16.31 |	83.68 |	26.63 |	71.09 |	0.09 |	2.17 |
| 1 | 77.16|	22.83 |	28.94 |	54.10 |	0.51 |	16.44 |
| 10  | 90.30	| 9.70 |	26.13 |	46.02 |	0.85 |	26.99 |

#### Table A4.1: learning both attention weights and what net (init 1) with pretrained what

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 11.39	| 88.60	| 14.76 |	83.20	 | 0.146	 | 1.88 |
| 0.1 | 52.44	| 47.55 |	26.90 |	71.32| 0.116 |	1.65 |
| 1 | 99.76	| 0.24 |	29.42 |	55.67 |1.16 |	13.73 |
| 10 | 100 |	0	| 24.94 |	52.7 |	1.58 |	20.77 |



#### Table A4.2: learning both attention weights and what net (init 2) with pretrained what

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 0.0 |	100.0 |	24.78 |	72.61 |	0.52 |	2.07 |
| 0.1 | 21.82 |	78.18 |	33.45 |	64.74 |	0.11 |	1.68 |
| 1 | 98.49 |	1.51 |	37.07 |	55.77 |	0.50 |	6.66 |
| 10 | 99.98 |	0.013 |	31.35 |	54.59 |	0.80  |	13.25 |





### Learning attention weights for every data point type4 data


#### Table B1: Simultaneous Model Performance (in percentage)
| \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF | decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | -- |
| Train |- | -|84.366667	| 15.6 |	0.033333 |	0.0 | <img src= ./type4_data/db.png width="450"> |





#### Table B2.1 : learning attention weights as well as what net (init 1)
LR for learning what net parameters is fixed 0.001

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF | decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | --- |
| 0.01 | 22.26 |	77.73 |	16.26 |	81.83 |	0.70 |	1.200000 | <img src= ./type4_data/init_1/both_random_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1  |  75.36 |	24.63 |	19.20 |	80.10 |	0.66 |	0.03 | <img src= ./type4_data/init_1/both_random_what/lr_0.1/decision_boundary.png width="450"> |
| 1 | 99.93 |	0.06 |	4.93 |	88.83 |	0.70 |	5.53 | <img src= ./type4_data/init_1/both_random_what/lr_1/decision_boundary.png width="450"> |
| 10 | 100 |	0 |	4.16 |	84.86 |	0.76 |	10.20 | <img src= ./type4_data/init_1/both_random_what/lr_10/decision_boundary.png width="450"> |



#### Table B2.2 : learning attention weights as well as what net (init 2)

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF | decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | --- |
| 0.01 | 0.23 |	99.76 |	12.13 |	86.46 |	0.83 |	0.57 | <img src= ./type4_data/init_2/both_random_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1  | 66.86 |	33.13 |	21.46 |	77.86 |	0.63 |	0.03  | <img src= ./type4_data/init_2/both_random_what/lr_0.1/decision_boundary.png width="450"> |
| 1 | 99.80  | 0.20 |	4.83 |	88.70 |	0.53 |	5.93 | <img src= ./type4_data/init_2/both_random_what/lr_1/decision_boundary.png width="450"> |
| 10 | 100.0 |	0 |	4.50 |	84.43 |	0.53 |	10.53  | <img src= ./type4_data/init_2/both_random_what/lr_10/decision_boundary.png width="450"> |



#### Now we are fixing the what net with final weights of simultaneous trained what net

#### Table B3.1: Fixed what net learning only attention weights for each data point (init 1)
| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |  decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | ---- |
| 0.01 | 12.26 |	87.73 |	17.80 |	80.73 |	0.36 |	1.10 | <img src= ./type4_data/init_1/only_attn_wts_pretrained_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1 | 	26.96 |	73.03 |	23.13 |	76.10 |	0.23 |	0.53 | <img src= ./type4_data/init_1/only_attn_wts_pretrained_what/lr_0.1/decision_boundary.png width="450">   |
| 1 | 59.50 |	40.50 |	21.13 |	74.60 |	2.16 |	2.10 | <img src= ./type4_data/init_1/only_attn_wts_pretrained_what/lr_1/decision_boundary.png width="450">   |
| 10  | 68.3 |	31.70 |	21.06 |	69.30 |	4.60 |	5.03 | <img src= ./type4_data/init_1/only_attn_wts_pretrained_what/lr_10/decision_boundary.png width="450">   |



#### Table B3.2: Fixed what net learning only attention weights for each data point (init 2)
| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |  decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | ---- |
| 0.01 | 0.16 |	99.83 |	2.46 |	95.66 |	1.60 |	0.26 | <img src= ./type4_data/init_2/only_attn_wts_pretrained_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1 | 1.16 |	98.83 |	16.76 |	82.33 |	0.50 |	0.40	 | <img src= ./type4_data/init_2/only_attn_wts_pretrained_what/lr_0.1/decision_boundary.png width="450">   |
| 1 | 32.33 |	67.66 |	9.50 |	85.30 |	2.13 |	3.06 | <img src= ./type4_data/init_2/only_attn_wts_pretrained_what/lr_1/decision_boundary.png width="450">   |
| 10  | 40.96 |	59.03 |	11.73 |	78.16 |	4.86 |	5.23 | <img src= ./type4_data/init_2/only_attn_wts_pretrained_what/lr_10/decision_boundary.png width="450">   |

#### Table B4.1: learning both attention weights and what net (init 1) with prtrained what

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |  decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | ---- |
| 0.01 | 	28.36 |	71.63 |	13.80 |	85.23 |	0.70 |	0.26 | <img src= ./type4_data/init_1/both_pretrained_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1 | 	29.73 |	70.26 |	28.10 |	70.56 |	0.10 |	1.23 | <img src= ./type4_data/init_1/both_pretrained_what/lr_0.1/decision_boundary.png width="450">   |
| 1 | 68.66 |	31.33 |	26.16 |	72.63 |	0.30 |	0.90 | <img src= ./type4_data/init_1/both_pretrained_what/lr_1/decision_boundary.png width="450">   |
| 10 | 90.90  | 9.10 |	21.56 |	76.30 |	0.26 |	1.86 | <img src= ./type4_data/init_1/both_pretrained_what/lr_10/decision_boundary.png width="450">   |


#### Table B4.2: learning both attention weights and what net (init 2) with prtrained what

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |  decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | ---- |
| 0.01 | 0.23 |	99.76 |	11.66 |	86.46 |	1.66 |	0.20	 | <img src= ./type4_data/init_2/both_pretrained_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1 | 1.76 |	98.23 |	20.50 |	78.50 |	0.76 |	0.23	 | <img src= ./type4_data/init_2/both_pretrained_what/lr_0.1/decision_boundary.png width="450">   |
| 1 | 44.26 |	55.73 |	21.0 |	78.06 |	0.30 |	0.63 | <img src= ./type4_data/init_2/both_pretrained_what/lr_1/decision_boundary.png width="450">   |
| 10 | 65.23 |	34.76 |	21.03 |	77.80 |	0.30 |	0.86  | <img src= ./type4_data/init_2/both_pretrained_what/lr_10/decision_boundary.png width="450">   |


### Learning attention weights for every data point blob data


#### Table C1: Simultaneous Model Performance (in percentage)
| \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| Train | -	 | -  |	99.9 |	0.1 |	0 |	0 | 




#### Table C2.1 : learning attention weights as well as what net (init 1)
LR for learning what net parameters is fixed 0.001

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 17.26	| 82.73 |	5.23	| 93.26 |	0.43 |	1.06 |
| 0.1 | 75.83 |	24.16 |	6.8 |	91.83 |	0.66 |	0.7 |
| 1 | 99.96 |	0.04	 | 12.96	 | 59.96 |	1.9 |	25.16 |
| 10 | 100 |	0	 | 12.16	| 52.7 |	2.36 |	32.76 | 



#### Now we are fixing the what net with final weights of simultaneous trained what net

#### Table C3.1: Fixed what net learning only attention weights for each data point (init 1)
| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 15.4 |	84.6	| 21	 | 76.23 |	0.36 |	2.4 |
| 0.1 | 28.5 |	71.5 |	24.06 |	74.66 |	0.3	| 0.96 |
| 1 | 57.13	| 42.86 |	23.4 |	74.96 |	0 |	1.63 |
| 10  | 67.03 |	32.96	 | 19.9 |	75 |	0	 |5.1 |

#### Table C4.1: learning both attention weights and what net (init 1 ) with prtrained what

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 	15.96 | 84.03|	13.63	| 84.7 |	0.26	|  1.4 |
| 0.1 | 32.93 | 67.06	|21.06	| 77.16	| 0.2	| 1.56 |
| 1 | 89.86	| 10.13	| 29.23 | 63.83	| 0.2	 | 6.73 |
| 10 | 99.16	| 0.83	| 24.83	| 56.83	| 0.5	 | 17.83 |



### transformed gradient with Exponential Kernel type4 data 


#### Table D2.1: learning attention weights as well as what net (init 1)
LR for learning what net parameters is fixed 0.001

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF | decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | --- |
| 0.01 | 24.16 |	75.83 |	25.53 |	21.50  |	17.06 |	35.90 | <img src= ./type4_data/init_1/exp_kernel/both_random_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1  |  100.0 |	0	|99.86 |	0	| 0.13 |	0 | <img src= ./type4_data/init_1/exp_kernel/both_random_what/lr_0.1/decision_boundary.png width="450"> |
| 1 | 99.26 |	0.73 |	66.83 |	32.40 |	0.067	| 0.70 | <img src= ./type4_data/init_1/exp_kernel/both_random_what/lr_1/decision_boundary.png width="450"> |
| 10 | 99.80 |	0.20  |	30.16 |	30.90| 	0.10	| 38.83 | <img src= ./type4_data/init_1/exp_kernel/both_random_what/lr_10/decision_boundary.png width="450"> |



#### Now we are fixing the what net with final weights of simultaneous trained what net

#### Table D3.1: Fixed what net learning only attention weights for each data point
| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |  decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | ---- |
| 0.01 | 15.80 |	84.20 |	14.76 |	29.33 |	12.73 |	43.16 | <img src= ./type4_data/init_1/exp_kernel/only_attn_wts_pretrained_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1 | 96.93 |	3.06 |	85.16 |	4.20 |	9.80 |	0.83	 | <img src= ./type4_data/init_1/exp_kernel/only_attn_wts_pretrained_what/lr_0.1/decision_boundary.png width="450">   |
| 1 | 99.10 |	0.90 |	86.0 |	3.1 |	10.56 |	0.33 | <img src= ./type4_data/init_1/exp_kernel/only_attn_wts_pretrained_what/lr_1/decision_boundary.png width="450">   |
| 10  | 99.80 |	0.20 |	37.20 |	9.23 |	10.03 |	43.53 | <img src= ./type4_data/init_1/exp_kernel/only_attn_wts_pretrained_what/lr_10/decision_boundary.png width="450">   |

#### Table D4.1:  learning both attention weights and what net with prtrained what

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |  decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | ---- |
| 0.01 | 21.33 |	78.66 |	24.13 |	24.50 |	13.50 |	37.86	 | <img src= ./type4_data/init_1/exp_kernel/both_pretrained_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1 | 92.03 | 7.96 |	87.93 |	10.53 |	0.63 |	0.90	 | <img src= ./type4_data/init_1/exp_kernel/both_pretrained_what/lr_0.1/decision_boundary.png width="450">   |
| 1 | 97.83 |	2.16 |	92.43 |	5.63 |	0.03 |	1.90 | <img src= ./type4_data/init_1/exp_kernel/both_pretrained_what/lr_1/decision_boundary.png width="450">   |
| 10 | 99.80 |	0.20 |	46.70 |	24.60 |	0 |	28.70 | <img src= ./type4_data/init_1/exp_kernel/both_pretrained_what/lr_10/decision_boundary.png width="450">   |



### transformed gradient with distance Kernel type4 data 


#### Table E2.1 : learning attention weights as well as what net (init 1)
LR for learning what net parameters is fixed 0.001

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF | decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | --- |
| 0.01 | 99.50 |	0.50 |	98.46 |	0.20 |	1.30 |	0.033333 | <img src= ./type4_data/init_1/distance_kernel/both_random_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1  |99.63 |	0.36 |	66.93 |	29.20 |	0.30 |	3.56  | <img src= ./type4_data/init_1/distance_kernel/both_random_what/lr_0.1/decision_boundary.png width="450"> |
| 1 | 100 |	0 |	66.90 |	27.13 |	0.26 |	5.70 | <img src= ./type4_data/init_1/distance_kernel/both_random_what/lr_1/decision_boundary.png width="450"> |
| 10 | 100 |	0 |	66.10 |	29.63 |	0.20 |	4.066667  | <img src= ./type4_data/init_1/distance_kernel/both_random_what/lr_10/decision_boundary.png width="450"> |


#### Now we are fixing the what net with final weights of simultaneous trained what net

#### Table E3.1: Fixed what net learning only attention weights for each data point
| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |  decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | ---- |
| 0.01 | 81.60 |18.40 |	75.40 |	10.53 |	10.0 |4.06 | <img src= ./type4_data/init_1/distance_kernel/only_attn_wts_pretrained_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1 | 95.50	| 4.50 |	81.73 |	10.80 |	6.23 |1.23 | <img src= ./type4_data/init_1/distance_kernel/only_attn_wts_pretrained_what/lr_0.1/decision_boundary.png width="450">   |
| 1 | 99.70 |	0.30 |	81.13  |	10.36 |	6.53 |	1.96 | <img src= ./type4_data/init_1/distance_kernel/only_attn_wts_pretrained_what/lr_1/decision_boundary.png width="450">   |
| 10 | 100 | 0 |	69.53 |	14.86 |	13.30 |	2.30  |  <img src= ./type4_data/init_1/distance_kernel/only_attn_wts_pretrained_what/lr_10/decision_boundary.png width="450">   |


#### Table E4.1:  learning both attention weights and what net  with prtrained what

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |  decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | ---- |
| 0.01 | 71.20 | 28.80 | 	74.70 |	9.40 |	9.76 |	6.13  | <img src= ./type4_data/init_1/distance_kernel/both_pretrained_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1 | 93.96 |	6.03 |	93.63 |	4.53 |	1.40	 | 0.43	 | <img src= ./type4_data/init_1/distance_kernel/both_pretrained_what/lr_0.1/decision_boundary.png width="450">   |
| 1 | 99.43 |	0.56 |	96.23 |	2.96 |	0.60 |	0.20 | <img src= ./type4_data/init_1/distance_kernel/both_pretrained_what/lr_1/decision_boundary.png width="450">   |
| 10 | 99.90 |	0.10 |	87.83 |	11.33 |	0.20 |	0.63 | <img src= ./type4_data/init_1/distance_kernel/both_pretrained_what/lr_10/decision_boundary.png width="450">   |



### transformed gradient with Neural Tangent Kernel type4 data 


#### Table F2.1 : learning attention weights as well as what net (init 1)
LR for learning what net parameters is fixed 0.0001

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF | decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | --- |
| 0.01 | 16.20 |	83.80 |	13.23 |	30.23 |	6.96 |	49.56 | <img src= ./type4_data/init_1/ntk/both_random_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1  | 89.13 |	10.86 |	71.66 |	17.83 |	2.90 |	7.60   | <img src= ./type4_data/init_1/ntk/both_random_what/lr_0.1/decision_boundary.png width="450"> |
| 1 | 98.06 |	1.93 |	84.83 |	8.70 |	0.93 |	5.53 | <img src= ./type4_data/init_1/ntk/both_random_what/lr_1/decision_boundary.png width="450"> |
| 10 | - | -| -|  -|- |-  | <img src= ./type4_data/init_1/ntk/both_random_what/lr_10/decision_boundary.png width="450"> |


#### Now we are fixing the what net with final weights of simultaneous trained what net

#### Table F3.1: Fixed what net learning only attention weights for each data point
| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |  decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | ---- |
| 0.01 | 20.06 |	79.93 |	11.40 |	31.50 |	8.36 |	48.73 | <img src= ./type4_data/init_1/ntk/only_attn_wts_pretrained_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1 | 92.50 |	7.50 |	25.30 |	19.33 |	1.60 |	53.76	 | <img src= ./type4_data/init_1/ntk/only_attn_wts_pretrained_what/lr_0.1/decision_boundary.png width="450">   |
| 1 | 65.23 |	34.76 |	14.46 |	18.16 |	0.10 |	67.26 | <img src= ./type4_data/init_1/ntk/only_attn_wts_pretrained_what/lr_1/decision_boundary.png width="450">   |
| 10 | - | -| -|  -|- |-  |  <img src= ./type4_data/init_1/ntk/only_attn_wts_pretrained_what/lr_10/decision_boundary.png width="450">   |



#### Table F4.1: learning both attention weights and what net with prtrained what

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |  decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | ---- |
| 0.01 |  17.73 |	82.26 |	5.96 |	31.50 |	7.70 |	54.83 | <img src= ./type4_data/init_1/ntk/both_pretrained_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1 | 84.16 |	15.83 |	36.03 |	40.63 |	1.93 |	21.40 | <img src= ./type4_data/init_1/ntk/both_pretrained_what/lr_0.1/decision_boundary.png width="450">   |
| 1 | 98.66 |	1.33 |	0.06 |	33.20 |	1.76 |	64.96 | <img src= ./type4_data/init_1/ntk/both_pretrained_what/lr_1/decision_boundary.png width="450">   |
| 10 | - | -| -|  -|- |- | <img src= ./type4_data/init_1/ntk/both_pretrained_what/lr_10/decision_boundary.png width="450">   |