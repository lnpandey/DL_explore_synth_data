### averaging at last layer

#### FG 012
Base Models - 6 layer CNN Network

#### Fg vs Bg Classification

Train Accuracy - 99

Test Accuarcy  - 90
#### Fg1 vs FG2 vs Fg3 classification
Train Accuracy - 99

Test Accuracy - 82

| | Focus init | Classification init | trained | train accuracy | test accuracy |
| - | ---------  | ------------------- | ------- | -------------  | ------------  |
|1| random | random | - | 33 |  32 |
|2| random | random | both | 99 | 95 |
|3| random | random | classify | 93 | 41 |
|4| random | random | focus    | 33 | 32 |
|5| pretrained | random | - | 33  |  32 |
|6| pretrained | random | both | 99 | 97|
|7| pretrained | random | classify | 99 | 97 |
|8| pretrained | random | focus    | 33 | 33 |
|9| random     | pretrained | -    | 46 | 46 |
|10| random    | pretrained | both | 99 | 92 |
|11| random    | pretrained | classify |  95 | 46 |
|12| random    | pretrained | focus   | 99  | 87 |
|13| pretrained | pretrained | - | 55 | 55 |
|14| pretrained | pretrained | both | 99 | 97 |
|15| pretrained | pretrained | classify |99 | 97 |
|16| pretrained | pretrained | focus    | 34 | 34 |

#### FG 234

#### Fg vs Bg Classification

Train Accuracy - 99

Test Accuarcy  - 86

#### Fg1 vs FG2 vs Fg3 classification
Train Accuracy - 99

Test Accuracy - 


| | Focus init | Classification init | trained | train accuracy | test accuracy |
| - | ---------  | ------------------- | ------- | -------------  | ------------  |
|1| random | random | - | 33 |  32 |
|2| random | random | both |  99 | 88 |
|3| random | random | classify |  | |
|4| random | random | focus    |  |  |
|5| pretrained | random | - |   |   |
|6| pretrained | random | both |  | |
|7| pretrained | random | classify |  |  |
|8| pretrained | random | focus    |  |  |
|9| random     | pretrained | -    |  |  |
|10| random    | pretrained | both |  |  |
|11| random    | pretrained | classify |   |  |
|12| random    | pretrained | focus   |   |  |
|13| pretrained | pretrained | - |  |  |
|14| pretrained | pretrained | both |  | |
|15| pretrained | pretrained | classify | |  |
|16| pretrained | pretrained | focus    | |  |

