#coding=utf-8

from __future__ import division;

import gl;  #global variances
import handle_collection;
import random;


Z=list();   #Z[d][l] represent the topic of l-th word in d-th document  
M=list();   #M[d][t] represent the count of assignment for t-th topic in d-th document
N=list();   #N[t][v] represent the count of assignment of t-th topic for v-th word
            #in vocab in the whole document collections   
SUM=list(); #store the sum of one topic over the whole vocabulary.


def init():
    #init M
    global M;
    for i in range(handle_collection.document_cnt):
        M.append([]);
        for j in range(gl.tc):
            M[i].append(0);
    
    #init N
    global N;
    for i in range(gl.tc):
        N.append([]);
        SUM.append(0);
        for j in range(len(handle_collection.vocab)):
            N[i].append(0);
    
    #init Z
    global Z;
    for i in range(handle_collection.document_cnt):
        Z.append([]);
        for j in range(len(handle_collection.word_in_doc[i])):
            #assign a random topic to the j-th word in doc d;
            Z[i].append(random.randint(0,gl.tc-1));
            t=Z[i][j];
            v=handle_collection.word_in_doc[i][j];
            #increase the value of M
            M[i][t]+=1;
            #increase the value of N
            N[t][v]+=1;
            #increase sum
            SUM[t]+=1;

def determin_the_modified_topic(d,l):
    rst=-1;
    probability=-1;
    v=handle_collection.word_in_doc[d][l];
    for t in range(gl.tc):
        tmp=(M[d][t]+gl.alpha)*(N[t][v]+gl.beta)/(SUM[t]+len(handle_collection.vocab)*gl.beta);
        #print tmp;
        if tmp>probability:
            probability=tmp;
            rst=t;
    return rst;
    
def one_wheel_of_gibbs(i):
    print 'gibbs sampling step %d...'%i;
    for d in range(handle_collection.document_cnt):
        for l in range(len(handle_collection.word_in_doc[d])):
            t=Z[d][l];
            v=handle_collection.word_in_doc[d][l];
            M[d][t]-=1;
            N[t][v]-=1;
            SUM[t]-=1;
            newt=determin_the_modified_topic(d,l);
            Z[d][l]=newt;
            M[d][newt]+=1;
            N[newt][v]+=1;
            SUM[newt]+=1;

def print_vocab_distribution_for_one_topic():
    print 'print vocabulary distribution...';
    filename='.\\..\\data\\'+'vocab_distri.txt';
    fobj=open(filename,'w');
    for t in range(gl.tc):
        for v in range( len(handle_collection.vocab) ):
            fobj.write('%.8f\t'%((N[t][v]+gl.beta)/(SUM[t]+len(handle_collection.vocab)*gl.beta)));
        fobj.write('\n');
    fobj.close();
        
def print_topic_distribution_for_one_document():
    print 'print topic distribution...'
    filename='.\\..\\data\\'+'topic_distri.txt';
    fobj=open(filename,'w');
    for d in range(handle_collection.document_cnt):
        tsum=0.0;
        for t in range(gl.tc):
            tsum+=M[d][t];
        for t in range(gl.tc):
            fobj.write('%.8f\t'%((M[d][t]+gl.alpha)/(tsum+gl.tc*gl.alpha)));
        fobj.write('\n');
    fobj.close();
        
def gibbs_sampling():
    print 'start gibbs sampling...'
    for i in range(1000):
        one_wheel_of_gibbs(i+1);
    print_vocab_distribution_for_one_topic();
    print_topic_distribution_for_one_document();
    
def lda():
    #process the document collections,and store necessary information in global variances.
    handle_collection.handle_collections('.\\..\\data\\','collection.txt');
    
    #initialize Z,M,N
    init();
    gibbs_sampling();
    

if __name__ == '__main__':
    print 'start lda...';
    lda();
    print 'lda over.'
    