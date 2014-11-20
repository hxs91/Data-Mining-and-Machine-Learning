#coding=utf-8
'''
Created on 2014.11.20

@author: Administrator
'''

import os;

stopword=set(); #english stop word
vocab=dict();   #english dictionary
document_cnt=0; #count of document
all_cnt=dict(); #count the occurrence of a word in all documents
minimal_occurrence=5;   #one word should at least occur minimal_occurrence times in documents


#return a list of text
def convert(text):
    tmp=text.lower();   #convert to lower case
    rst=''
    for ch in tmp:
        if ch.isalpha():
            rst+=ch;
        else:
            ch=' ';
            rst+=ch;
    return rst.split(' ');

#formating one document
def one_document(text,filename,fobj):
    tlist=convert(text);
    rcd=dict();
    
    for each in tlist:
        if each not in stopword:
            if vocab.has_key(each):
                tmp=vocab[each];
                if rcd.has_key(tmp) and all_cnt[tmp]>=minimal_occurrence:
                    rcd[tmp]+=1;
                else:
                    rcd[tmp]=1;
    
    global document_cnt;
    
    if len(rcd)==0:
        return;
    
    document_cnt+=1;
    
    fobj.write('%d'%len(rcd));
    for key in rcd:
        fobj.write(' %d:%d'%(key,rcd[key]));
    
    fobj.write('\n');
    
    return rcd;

def get_allcnt(text):
    tlist=convert(text);
    for each in tlist:
        if each not in stopword:
            if vocab.has_key(each):
                tmp=vocab[each];
                if all_cnt.has_key(tmp):
                    all_cnt[tmp]+=1;
                else:
                    all_cnt[tmp]=1;

def handle_collections(path,name):
    format=path+'format.txt';
    
    if os.path.exists(format):
        print 'format.txt already exists, program will terminate'
        return;
    formatobj=open(format,'a');
    #initialize stop word and vocab 
    init(path);
    
    filename=path+name;
    lines=open(filename,'r').readlines();
    
    global document_cnt;
    
    #print filename;
    document_cnt=0;
    content='';
    flag = False;
    
    for eachLine in lines:
        if eachLine.strip() == '<TEXT>':
            flag=True;
            content='';
        elif eachLine.strip() == '</TEXT>':
            get_allcnt(content);
        elif flag:
            content+=eachLine;
            
    content='';
    flag = False;
    
    for eachLine in lines:
        if eachLine.strip() == '<TEXT>':
            flag=True;
            content='';
        elif eachLine.strip() == '</TEXT>':
            one_document(content,format,formatobj);
        elif flag:
            content+=eachLine;
    
    formatobj.close();
    print 'total %d document%s' % (document_cnt,'s' if document_cnt>1 else '');

def init(path):
    #read stop word
    tmp=open(path+'stopword.txt','r').readlines();
    for i in range(len(tmp)):
        tmp[i]=tmp[i].strip();
    stopword = set(tmp);
    tmp=open(path+'vocab.txt','r').readlines();
    for i in range(len(tmp)):
        vocab[tmp[i].strip()]=i+1;
        
    #print stopword
    #print len(vocab)
    #print vocab
        
if __name__ == "__main__":
    handle_collections('.\\..\\data\\','collection.txt');
    #init('.\\..\\data\\')