# Chinese keyword recommendation for search engine

A keyword recommendation model build with LDA and RNN

The model recommend relevant keywords according to your input word, and since the model is trained with news data, it is applicable to online news website.


# Overview

  - Input some keyword and the model will recommend some relevant keyword
  - The model is trained with Chinese news data, so it's applicable to search engine of  online news website


You can also:
  - Customize your model by tuning the parameter in config.json or use your own news data



# model
### 1. preprocessing
Although the stopwords are filtered out in advance, but there are still a lot of common words don't contribute to the training , even interfere it.
So a word_filter is designed to improve the model performance, and filter out words whose document frequency is too high or low.
The threshold of document frequency filter could be tuned in config.
> document frequency -- the number of document which the word appears


### 2. LDA
LDA is used to infer the relationship between words.
We use LDA to estimate P(z | w) , and then use it as word embedding.

> P( z | w ) -- probability of word w belongs to topic z

More detail about LDA please refer to 

* [Finding scientific topics](https://www.pnas.org/content/pnas/101/suppl_1/5228.full.pdf?__=) - TL Griffiths, M Steyvers


### 3. RNN
Another algorithm use to infer the relationship between words.
We use a LSTM , single-layer Recurrent Neural Network.


### 4. LDA vs RNN
By using LDA and RNN in the same time, the model can get more diverse recommendation results. And we choose LDA and RNN, because they train the model in different way, Bag of Words (LDA) and N-Gram (RNN). And the result differs in the way in below.

```sh
INPUT : 川普 (Trump) 
```
```sh
LDA results : 
[ "中國" (China),   "美國"(U.S.A.),  "日本"(Japan), "北韓"(North Korea)]
```
```sh
RNN results :
 [ "杜特蒂" ( president of Philippines ), "icbm"(intercontinental ballistic missile),  
 "文在寅" (president of Korea) , "普丁"(Putin, president of Russia) ]
```
LDA learn more "international news characteristic" from "Trump", because it read the news like it's a bag of word.
On the other hand, RNN learn more "person name" and "president" characteristic from "Trump".
Therefore,  combining the results of 2 algorithm, the model can get more diverse recommendation results.


# Demo


Download [data](https://drive.google.com/file/d/18GjVFEcBdu_JBA_Yf9dyTc4wlwG2RTbd/view?usp=sharing) and put in folder "data"

Download [pre-trained RNN](https://drive.google.com/file/d/1wqj1-ZAxq12TpyqRs6ZKIvTdOFkZ6FgK/view?usp=sharing) and put in folder "RNN/saved_model/"

then


```sh
--mode train(train a new model) / recommend (recommend with saved model)
--model LDA / RNN (choose a model RNN or LDA)
--word (input your word here)
```
               
#### 1. recommend with saved model


```sh
$ python3 main.py --mode recommend --model LDA --word (input your word here)
```


#### 2. train a new model

```sh
$ python3 main.py --mode train --model LDA 
```


# Customize 
#### 1. parameter tuning
change the patameter in config.json

#### 2. train with your news data
Put your Chinese news data in folder "data"
see example in /data/news_data.json
