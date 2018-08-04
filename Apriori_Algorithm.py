
import numpy as np
import h5py
import matplotlib.pyplot as plt

import itertools



TR=np.array([[1,2,5],[2,4],[2,3],[1,2,4],[1,3],[2,3],[1,3],[1,2,3,5],[1,2,3]])
support_count=2;

def combn(A,n):
    lst=[];
    for comb in itertools.combinations(A,n):
        lst.append(list(comb));
    return lst;

def cntocc(TR,ss): #Count occarance of set ss in Transaction TR
    lent=TR.shape[0];
    cnt=0;
    for i in range(lent):
        if set(ss)<=set(TR[i]):
            cnt=cnt+1;
    return cnt;

def iscomp(buffer,st):
    decomb=combn(st,len(st)-1);
    for i in range(len(buffer)):
        buffer[i].sort();
    for i in range(len(decomb)):
        decomb[i].sort();
        if decomb[i] not in buffer:
            return False;
    return True;

def has_infreq_subset(c,lk_1):
    sk=combn(c,len(c)-1);
    for x in sk:
        if x not in lk_1:
            return True;
    return False;

def join(j,jj):
    t=j.copy();
    t.append(jj[len(jj)-1])
    t.sort();
    return t;

def apriori_gen(lk_1):
    CK=[];
    len1=len(lk_1);
    for i in range( len1 ):
        l1=lk_1[i];
        for j in range( i+1,len1 ):
            if i!=j:
                l2=lk_1[j];
                if l1[0:len(l1)-1]==l2[0:len(l2)-1]:
                    c=join(l1,l2);
                    if has_infreq_subset(c,lk_1)==False:
                        CK.append(c);
    return CK;             
    
def freq_gen(CK,TR):
    LK=[];cnt=[];
    for x in CK:
        cn=cntocc(TR,x);
        if cn>=support_count:
            LK.append(x);
            cnt.append(cn);
    return LK,cnt;      

def apriori(TR):
    items=[];
    imap=[];
    for i in range(TR.shape[0]):
        for j in TR[i]:
            if j not in items:
                items.append(j);
    
    items.sort();
    buffer=[];
    for i in range(len(items)):
        buffer.append([items[i]]);
    
    count=[];
    for i in range(len(buffer)):
        ty=cntocc(TR,buffer[i]);
        count.append(ty);
    
    newbuffer=[];
    newcount=[];
    for i in range(len(buffer)):
        if count[i]>=support_count:
            newbuffer.append(buffer[i]);
            newcount.append(count[i]);
    buffer=newbuffer.copy();
    count=newcount.copy();  
    while 1:
        
        CK=apriori_gen(buffer);
        LK,cc=freq_gen(CK,TR);
        if len(LK)==0:
            break;
        buffer=LK.copy();
        count=cc.copy();
    return buffer,count;
                    
        
def conf_rule_gen(TR,buffer,confidence):
    Tlen=len(TR);
    for x in buffer:
        for i in range(1,len(x)):
            CS=combn(x,i);
            for y in CS:
                z=set(x)-set(y);
                uni=set(y)|set(z);
                
                conf=cntocc(TR,uni)/cntocc(TR,y);
                if conf>=confidence:
                    print(y,"->",list(z),"=",conf);
    

bf,cnt=apriori(TR)  
conf_rule_gen(TR,bf,.8)
