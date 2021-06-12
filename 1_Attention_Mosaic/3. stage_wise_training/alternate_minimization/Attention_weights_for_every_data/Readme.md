### Learning attention weights for every data point CIFAR data


#### Table A1: Simultaneous Model Performance (in percentage)
| \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| Train | 70.93 	 | 29.07 |	73.690000 |	24.933333 |	0.300000 |	1.076667 | 
| Test | 67.48	 |  32.52 |	66.16 |	17.39 |	4.10 |	12.35 |




#### Table A2 : learning attention weights as well as what net(random)
LR for learning what net parameters is fixed 0.001

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 15.91 |	84.08	 |  16.39 |	80.88 |	0.216	|  2.51 |
| 0.1 | 54.87 | 	45.13 |	19.65 |78.36 |	0.216	 | 1.76 |
| 1 |99.68 |	0.31 | 21.12 |	56.67 |	2.04 |	20.17 |
| 10 | 100 |	0	 | 19.89 |	54.78 |	2.35 |	22.97 |



#### Now we are fixing the what net with final weights of simultaneous trained what net

#### Table A3: Fixed what net learning only attention weights for each data point
| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 12.95 | 	87.04 |	16.25 |	77.56 |	0.16 |	6.01 |
| 0.1 | 41.61 |	58.39 |	23.82 |	73.89	 | 0.016 |	2.27 |
| 1 | 87.77	| 12.22 |	28.2 |	55.65 |	0.436 |	15.71 |
| 10  | 94.73 |	5.26	 | 26.52	| 47.42	 | 0.84	| 25.20 |

#### Table A4: Fixed what net learning both attention weights and what net 

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 11.39	| 88.60	| 14.76 |	83.20	 | 0.146	 | 1.88 |
| 0.1 | 52.44	| 47.55 |	26.90 |	71.32| 0.116 |	1.65 |
| 1 | 99.76	| 0.24 |	29.42 |	55.67 |1.16 |	13.73 |
| 10 | 100 |	0	| 24.94 |	52.7 |	1.58 |	20.77 |





### Learning attention weights for every data point type4 data


#### Table B1: Simultaneous Model Performance (in percentage)
| \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF | decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | -- |
| Train |- | -|84.366667	| 15.6 |	0.033333 |	0.0 | <img src= ./type4_data/db.png width="450"> |





#### Table B2 : learning attention weights as well as what net (random)
LR for learning what net parameters is fixed 0.001

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF | decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | --- |
| 0.01 | 22.36 |	77.63 |	16.5 |	81.83 |	0.6 |	1.06 | <img src= ./type4_data/both_random_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1  |  75 |	25 |	20.53 |	78.8 |	0.66	 |0 | <img src= ./type4_data/both_random_what/lr_0.1/decision_boundary.png width="450"> |
| 1 | 99.9 |	0.1	 | 4.86	| 88.93 |0.7 |	5.5 | <img src= ./type4_data/both_random_what/lr_1/decision_boundary.png width="450"> |
| 10 | 100 |	0	 | 4.16 |	84.86 | 0.76 |	10.2 | <img src= ./type4_data/both_random_what/lr_10/decision_boundary.png width="450"> |



#### Now we are fixing the what net with final weights of simultaneous trained what net

#### Table B3: Fixed what net learning only attention weights for each data point
| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |  decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | ---- |
| 0.01 | 12.33 |	87.66 |	17.93 |	80.7 |	0.33 |	1.033 | <img src= ./type4_data/only_attn_wts_pretrained_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1 | 	26.96	| 2191	| 694 |	76.1 | 0.23|	0.53 | <img src= ./type4_data/only_attn_wts_pretrained_what/lr_0.1/decision_boundary.png width="450">   |
| 1 | 59.5 |	40.5 |	21.13 |	74.56 |	2.2 |	2.1 | <img src= ./type4_data/only_attn_wts_pretrained_what/lr_1/decision_boundary.png width="450">   |
| 10  | 68.3 |	31.7 |	21.06 |	69.3 |	4.6 |	5.03 | <img src= ./type4_data/only_attn_wts_pretrained_what/lr_10/decision_boundary.png width="450">   |

#### Table B4: Fixed what net learning both attention weights and what net 

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |  decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | ---- |
| 0.01 | 	28.6 |	71.4 |	13.83 |	85.4 | 17.30 |	0.2 | <img src= ./type4_data/both_pretrained_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1 | 	29.73	 | 70.26 |	28.1 |	70.56 |	0.1 |	1.23 | <img src= ./type4_data/both_pretrained_what/lr_0.1/decision_boundary.png width="450">   |
| 1 | 68.66 |	31.33 |	26.16 |	72.63 |	0.3 |	0.9 | <img src= ./type4_data/both_pretrained_what/lr_1/decision_boundary.png width="450">   |
| 10 | 92.56 | 7.43 |	21.73 |	76.33 |0.13 | 	1.8 | <img src= ./type4_data/both_pretrained_what/lr_10/decision_boundary.png width="450">   |



### Learning attention weights for every data point blob data


#### Table C1: Simultaneous Model Performance (in percentage)
| \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| Train | -	 | -  |	99.9 |	0.1 |	0 |	0 | 




#### Table C2 : learning attention weights as well as what net(random)
LR for learning what net parameters is fixed 0.001

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 17.26	| 82.73 |	5.23	| 93.26 |	0.43 |	1.06 |
| 0.1 | 75.83 |	24.16 |	6.8 |	91.83 |	0.66 |	0.7 |
| 1 | 99.96 |	0.04	 | 12.96	 | 59.96 |	1.9 |	25.16 |
| 10 | 100 |	0	 | 12.16	| 52.7 |	2.36 |	32.76 | 



#### Now we are fixing the what net with final weights of simultaneous trained what net

#### Table C3: Fixed what net learning only attention weights for each data point
| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 15.4 |	84.6	| 21	 | 76.23 |	0.36 |	2.4 |
| 0.1 | 28.5 |	71.5 |	24.06 |	74.66 |	0.3	| 0.96 |
| 1 | 57.13	| 42.86 |	23.4 |	74.96 |	0 |	1.63 |
| 10  | 67.03 |	32.96	 | 19.9 |	75 |	0	 |5.1 |

#### Table C4: Fixed what net learning both attention weights and what net 

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   |
| 0.01 | 	15.96 | 84.03|	13.63	| 84.7 |	0.26	|  1.4 |
| 0.1 | 32.93 | 67.06	|21.06	| 77.16	| 0.2	| 1.56 |
| 1 | 89.86	| 10.13	| 29.23 | 63.83	| 0.2	 | 6.73 |
| 10 | 99.16	| 0.83	| 24.83	| 56.83	| 0.5	 | 17.83 |



### transformed gradient with Exponential Kernel type4 data 


#### Table D1 : learning attention weights as well as what net (random)
LR for learning what net parameters is fixed 0.001

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF | decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | --- |
| 0.01 | 24.16 |	75.83 |	25.53 |	21.50  |	17.066667 |	35.900000 | <img src= ./type4_data/exp_kernel/both_random_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1  |  100.0 |	0	|99.86 |	0	| 0.13 |	0 | <img src= ./type4_data/exp_kernel/both_random_what/lr_0.1/decision_boundary.png width="450"> |
| 1 | 99.26 |	0.73 |	66.83 |	32.40 |	0.067	| 0.70 | <img src= ./type4_data/exp_kernel/both_random_what/lr_1/decision_boundary.png width="450"> |
| 10 | 99.80 |	0.20  |	30.16 |	30.90| 	0.10	| 38.83 | <img src= ./type4_data/exp_kernel/both_random_what/lr_10/decision_boundary.png width="450"> |



#### Now we are fixing the what net with final weights of simultaneous trained what net

#### Table D2: Fixed what net learning only attention weights for each data point
| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |  decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | ---- |
| 0.01 | | <img src= ./type4_data/exp_kernel/only_attn_wts_pretrained_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1 | 	 | <img src= ./type4_data/exp_kernel/only_attn_wts_pretrained_what/lr_0.1/decision_boundary.png width="450">   |
| 1 |  | <img src= ./type4_data/exp_kernel/only_attn_wts_pretrained_what/lr_1/decision_boundary.png width="450">   |
| 10  | | <img src= ./type4_data/exp_kernel/only_attn_wts_pretrained_what/lr_10/decision_boundary.png width="450">   |

#### Table D3: Fixed what net learning both attention weights and what net 

| LR (for only attention wts) \ Analysis | argmax > 0.5 | argmax < 0.5 |  FTPT | FFPT | FTPF | FFPF |  decision boundary |
|  ----         | -------      |  --------    |  --   |  --  | --   | --   | ---- |
| 0.01 | 21.33 |	78.66 |	24.13 |	24.50 |	13.50 |	37.86	 | <img src= ./type4_data/exp_kernel/both_pretrained_what/lr_0.01/decision_boundary.png width="450">   |
| 0.1 | 92.03 | 7.96 |	87.93 |	10.53 |	0.63 |	0.90	 | <img src= ./type4_data/exp_kernel/both_pretrained_what/lr_0.1/decision_boundary.png width="450">   |
| 1 | 97.83 |	2.16 |	92.43 |	5.63 |	0.03 |	1.90 | <img src= ./type4_data/exp_kernel/both_pretrained_what/lr_1/decision_boundary.png width="450">   |
| 10 | 99.80 |	0.20 |	46.70 |	24.60 |	0 |	28.70 | <img src= ./type4_data/exp_kernel/both_pretrained_what/lr_10/decision_boundary.png width="450">   |


