#!/usr/bin/env python
#_*_coding:utf-8_*_
#统计日志里面的各字段，根据相关字段进行微调即可使用
import sys
#from collections import Counter

accessfile=file("/root/python_su/izcat.com/access1.log",'rb')


a=accessfile.read().splitlines()
b=(i for i in a)
L=[]
k={}
for i in b:
 #print i
 n=i.split()
 try:
  m=[j for j in n]
 #m[0]表示第一个字段，依次类推
  L.append(m[0])
 except  IndexError:
  break
for i in L:
#此处k[i]中的i根据要求可能要在int进行类型转换
 k[i]=L.count(i)
print k
