#encoding:utf-8
import jieba
import os
import fasttext
from gensim.models import FastText
from Make_TrainData import *

Inputdata_Path = './data/train1600.txt'
test_path='./data/test1600.txt'

def build_classification(Inputdata_Path):
    print("开始训练模型：....")
    # wordvec=fasttext.skipgram(Inputdata_Path,'./model_skipgram/model',lr=0.01,dim=200,ws=5,epoch=10,min_count=1,neg=5,word_ngrams=5)
    # print(wordvec.words)          #获取词汇表
    # print(wordvec['任性贷'])   #获取词向量
    # print(wordvec.cosine_similarity('任性付','任性贷'))  #相似性
    classifier = fasttext.supervised(Inputdata_Path, "./Model/Q_fasttext.model", label_prefix="__label__",lr=0.1,dim=200,bucket=500000)
    print("训练完成。")

def test_classification_model(text):
    test_text=[]
    classifier = fasttext.load_model('./Model/Q_fasttext.model.bin', label_prefix='__label__')
    # print(classifier)
    # text_list=list(jieba.cut(Extract_Chinese(text.replace('\t','').replace('\n',''))))
    # # test_text.append(' '.join([word for word in text_list if word not in get_stop_words()]))
    # test_text.append(' '.join([word for word in text_list ]))
    # print(test_text)
    # pre_label=classifier.predict(test_text)
    # print(pre_label)
    # return pre_label
    result = classifier.test(test_path)
    print("precision:",result.precision)
    print("recall:",result.recall)

    # labels_right = []
    # texts = []
    # with open("news_fasttext_test.txt",encoding='utf-8') as fr:
    #     for line in fr:
    #         line = line.rstrip()
    #         labels_right.append(line.split("\t")[1].replace("__label__", ""))
    #         texts.append(line.split("\t")[0])
    #     print("texts：",texts)
    #     print("labels_right：",labels_right)
    # labels_predict = [e[0] for e in classifier.predict(texts)]  # 预测输出结果为二维形式
    # print("labels_predict：",labels_predict)
    # text_labels = list(set(labels_right))
    # text_predict_labels = list(set(labels_predict))
    # print("text_predict_labels:",text_predict_labels)
    # print("text_labels",text_labels)


if __name__=='__main__':
    # make_data()

    # build_classification(Inputdata_Path)
    text="我是使用微信支付"
    test_classification_model(text)

