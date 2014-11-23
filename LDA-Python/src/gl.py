#coding=utf-8

import os;
import sys;

error_info='''lda setting file error, please set the parameters as the following format:
            TOPIC_COUNT:XXX
            ALPHA:XXX
            BETA:XXX'''

ldaset=open('F:\Git\Data-Mining-and-Machine-Learning\LDA-Python\src\SETTING','r').readlines();

if len(ldaset) != 3:
    print error_info;
    sys.exit();


if ldaset[0].startswith('TOPIC_COUNT:'):
    tc=int(ldaset[0].replace('TOPIC_COUNT:',''));
else:
    print error_info;
    sys.exit();


if ldaset[1].startswith('ALPHA:'):
    alpha=float(ldaset[1].replace('ALPHA:',''));
else:
    print error_info;
    sys.exit();
    
if ldaset[2].startswith('BETA:'):
    beta=float(ldaset[2].replace('BETA:',''));
else:
    print error_info;
    sys.exit();
    
