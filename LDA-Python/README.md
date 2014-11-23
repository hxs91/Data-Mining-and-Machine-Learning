LDA实现记录

准备阶段：
数据：
collection.txt	文档集
stopword.txt 英文停用词
vocab.txt 一个英文词典，里边包含词的各种形式（第三人称单数，过去式，过去分词）

处理数据：
将每个文档数字化，具体采用如下的格式：
[M] [term_1]:[count] [term_2]:[count] ...  [term_N]:[count]
其中M代表该文档中含有M个不同的词，之后的term和count分别代表一个词以及该词在该文档中出现的次数，将整理之后的文档输出到collection.dat中。

备注：采用的是gibbs sampling方法，迭代1000轮，详细参照!2004_PNAS_Finding Scientific Topics这篇论文。

SETTING里可以设置参数，包括主题的个数，alpha和beta

