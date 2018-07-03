#-*- coding:utf-8 -*-

#从递增数组中找出和为S的任意两个数
#昨天讨论的通过从数组两端向中间收缩的逻辑，在以下数据中会有bug

data = [1,4,5,35,37,38]
sum = 40
#expect: 5,35

data = [1,4,5,33,36,37,38,45,48]
sum=40
#expect: 4,36

#重新整理了一下思路，用以下方式可以O(n)实现
def find(data,length,sum):
    #存放差值的集合
    diffSet = set()
    for i in range(length):
        diff = sum - data[i]
        #由于是递增数组，当遍历到当前元素已经存在于diffSet时，可知有对应差值
        if data[i] in diffSet:
            return diff , data[i]
        diffSet.add(diff)

print(find(data,len(data),sum))
