#coding=utf-8

#print top 10 words in a topic according to vocab_distri.txt


path = '.\\..\\data\\';

allwords = [ each.strip() for each in open(path+'vocab.txt','r').readlines() ];

topics = [ each.strip() for each in  open(path+'vocab_distri.txt','r').readlines() ];

fobj = open(path+'top10_words_for_each_topic.txt','w');

stopword=set();

tmp=open(path+'stopword.txt','r').readlines();
for i in range(len(tmp)):
    tmp[i]=tmp[i].strip();
stopword = set(tmp);

for each in topics:
    one_topic = sorted( tuple( enumerate ( [ float(pro) for pro in each.split() ] ) ),
                        key=lambda x:x[1],reverse=True );
    print sum( [ float(pro) for pro in each.split() ] );
    cnt=0;
    for i in range(1000):
        if allwords[ one_topic[i][0] ] not in stopword:
            fobj.write(allwords[ one_topic[i][0] ]+' ');
            cnt+=1;
            if cnt==10:
                break;
    fobj.write('\n');
    
fobj.close();
