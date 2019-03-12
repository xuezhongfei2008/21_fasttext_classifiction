#encoding:utf-8
import jieba
import os
import pandas as pd
import csv
import re
jieba.load_userdict('./data/finWordDict.txt')

#保留汉字字符
def Extract_Chinese(doc):
    pattern = '[^\u4e00-\u9fa5]+'
    return re.compile(pattern).sub('', doc.__str__())

#添加机器人知识库数据
def load_RobotKnowledge(path):
    #添加机器人知识库数据
    df=pd.read_excel(path,sheet_name=0,ignore_index=False)
    df['question1']=df['标准问题(必填)']+df['相似问题']
    print(df['question1'])
    # parent_teacher_data['address'] = parent_teacher_data['country'] + parent_teacher_data['province'] + parent_teacher_data['city'] + parent_teacher_data['county']
    # df['question']=df['标准问题(必填)'].apply(Extract_Chinese)
    df['question']=df['question1'].apply(Extract_Chinese)
    df['label']=df['分类名称']
    df[['label','question']].to_csv("./data/question_all_text.txt", sep="\t",mode='w',header=False, index=False,encoding='utf-8')

def get_stop_words():
    stop_words=[]
    with open('./data/stop_words.txt','r',encoding="utf-8") as f:
        line=f.readline()
        while line:
            stop_words.append(line[:-1])
            line=f.readline()
    return stop_words

def make_traindata(input_path):
    ftrain = open("./data/train1600.txt","w",encoding='utf-8')
    # ftest = open("./data/test1600.txt","w",encoding='utf-8')
    all_doc_list=[]
    question_list=[]
    with open(input_path,'r',encoding='utf-8') as f:
        line=f.readline()
        # print("line",line)
        while line:
            # print("line", line)
            if(len(line))>0:
                # print(line)
                # print(type(line))
                label=line.split(sep='\t')[0]
                # question_list=jieba.cut(line.split(sep='\t')[1].replace('\t','').replace('\n',''))
                question_list = jieba.cut(line.split(sep='\t')[1].replace('\n', ''))
                # raw_word=' '.join(question_list)+'\t__label__'+label+'\n'
                # raw_word = ' '.join([word for word in question_list if word not in get_stop_words()]) + '\t__label__' + label + '\n'
                raw_word = ' '.join([word for word in question_list]) + '\t__label__' + label + '\n'
                # print(raw_word)
                ftrain.write(raw_word)
                # ftest.write(raw_word)
            line=f.readline()
    ftrain.close()
    # ftest.close()

if __name__=='__main__':
    # load_RobotKnowledge('../original_data/机器人知识库-2.23.xlsx')
    input_path='/opt/gongxf/python3_pj/Robot/CNN_Classification/CNN_model/train1.txt'
    #input_path='./data/question_all_text.txt'
    make_traindata(input_path)




