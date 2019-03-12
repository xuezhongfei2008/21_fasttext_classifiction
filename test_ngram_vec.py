#encoding:utf-8
from nltk.util import ngrams

a = ['我', '是', '中', '国', '人']
b = ngrams(a, 3)
for i in b:
    print("".join(tuple(i)))


# def getNgrams(input, n,list):
#     input =input.strip()
#     output = {} # 构造字典
#     for i in range(len(input)-n+1):
#         ngramTemp = " ".join(input[i:i+n])#.encode('utf-8')
#         list.append(ngramTemp)
#
# for d in sent_set:
#     print("d", d)
#     getNgrams(d, 2, two_grarm_list)  # 2-grarm
#
# fre2 = nltk.FreqDist(two_grarm_list)  # 计算频数分布情况
# fre2 = sorted(fre2.items(), key=operator.itemgetter(1), reverse=True)  # =True 降序排列


