# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:44:45 2017

@author: Lenovo-Y430p
"""
#深度优先搜索（k数和）
def kSumII( A, k, target):
        # write your code here
        cur=()
        temp=[]
        depthsearch(cur,target,k,temp,A,0,0)  
        print(temp)
        return temp

def depthsearch(cur,target,k,temp,A,sum1,index):
    #回溯法的特点在于找到出口，仔细检查出口方案
    if len(cur)==k and sum1==target:
        temp.append(cur)
        return
    if len(cur)>=k:
        return 
    if index==len(A):
        return 
    if sum1>=target:
        return 
    #对路径入栈
    #因为所有的的路径都是一个方向所以比较容易
    cur+=tuple([A[index]])
    depthsearch(cur,target,k,temp,A,sum1+A[index],index+1)
    #对检查过路径出栈
    cur=cur[:-1]
    depthsearch(cur,target,k,temp,A,sum1,index+1)
def main():
    
    A=[1,2,3,4]
    target=5
    k=2
    kSumII(A, k, target)
if __name__=='__main__':
    main()
    
        
        