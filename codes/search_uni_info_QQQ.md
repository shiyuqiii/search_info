正则表达式re.findall的用法 用来提取关键字

<https://www.cnblogs.com/xieshengsen/p/6727064.html>

库nltk可以在提取信息时跳过一些词 **stopwords**
https://medium.com/@rqaiserr/how-to-convert-pdfs-into-searchable-key-words-with-python-85aab86c544f


how to extract keywords from pdfs and arrange using Python**使用了re.findall**

<https://towardsdatascience.com/how-to-extract-keywords-from-pdfs-and-arrange-in-order-of-their-weights-using-python-841556083341>

用pdfminner提取pdf信息

<https://www.jianshu.com/p/31939ee6f1c9>

弊端就是好想只能提取整个文本的信息 ，但是没有关系，我们可以提取整个文本的信息之后再用正则式提取

**apt-get install python-pip**还要安装个pip 连pip都没有。。。噗呲

解决乱码的问题
从一篇文章中提取出所有字符
**遗留问题：只截取第一页**

**step1**:解决's的问题. 
**step2**:解决 - 的问题：
1. 解决行内带有连字符的情况，因为不排除有的学校名带有连字符，所以行内带有连字符的视为一个单词

2. 行末带有连字符，连字符出现在小标题的行末和出现在正文的行末是不一样的，如果出现在正文行末，后面会有一个换行，出现在小标题行末会有两个换行。所以将出现在行末的连字符以及后面的换行都删去，前后单词连接。

**step3**:现在将七千多个学校和文章提取词做比对

3. 先将一个学校与一篇文章做比对 done

4. 再将所有学校与一篇文章做比较 

**step4**：（用到了函数$difflib.SequenceMatcher$）用学校的名字与文章中的University上下文做顺序匹配，计算匹配度，增加了$Institute $的检索
已经发现的几个问题：

1. ![4EEABD9B-4001-4F2C-AA4F-856E45D7E0E7](/Users/yuqishi/Library/Containers/com.tencent.qq/Data/Library/Application Support/QQ/Users/1797571490/QQ/Temp.db/4EEABD9B-4001-4F2C-AA4F-856E45D7E0E7.png) 

结果匹配到：Stevenson University（数据库确实有这个学校的）![DAD7958A-2824-44EB-8986-AA96BF8468D1](/Users/yuqishi/Library/Containers/com.tencent.qq/Data/Library/Application Support/QQ/Users/1797571490/QQ/Temp.db/DAD7958A-2824-44EB-8986-AA96BF8468D1.png) 

这个我暂时想不到解决方法



3. 也是问题比较大的一点：

![DED6C446-80F5-4AE5-9BE8-EC914B42218B](/Users/yuqishi/Library/Containers/com.tencent.qq/Data/Library/Application Support/QQ/Users/1797571490/QQ/Temp.db/DED6C446-80F5-4AE5-9BE8-EC914B42218B.png) 

匹配到了好几个学校：

$Georgia\quad Institute \quad of \quad Technology$
$School \quad of \quad Electrical \quad Engineering$
$School \quad of \quad Technology$ 

介个问题解决啦：找匹配到的最长连续单词的个数是否等于学校的单词个数，若等即可

4. 又出现个问题：正文里也有出现学校的 也会匹配出来



6. 是个问题的问题![image-20190605004158207](/Users/yuqishi/Library/Application Support/typora-user-images/image-20190605004158207.png) 

这种没能匹配出来，因为the是小写，数据库里的学校The是大写

大小写问题解决，全部转化成小写匹配

7. 最后一个问题：

![image-20190605011348715](/Users/yuqishi/Library/Application Support/typora-user-images/image-20190605011348715.png) 

应该很明显了，不过存储的时候去重应该就可以了

8. 真是不得不服 问题再+1 

![image-20190605013142233](/Users/yuqishi/Library/Application Support/typora-user-images/image-20190605013142233.png)

9. 没有的学校



![image-20190605094025871](/Users/yuqishi/Library/Application Support/typora-user-images/image-20190605094025871.png) 1901.00413



​![2F13BCF8-E547-4558-91DC-D27A41712A1C](/Users/yuqishi/Library/Containers/com.tencent.qq/Data/Library/Application%20Support/QQ/Users/1797571490/QQ/Temp.db/2F13BCF8-E547-4558-91DC-D27A41712A1C.png) 

第二个学校没有

![80A0EF19-13B3-43DA-B5BD-D508AB03F410](/Users/yuqishi/Library/Containers/com.tencent.qq/Data/Library/Application%20Support/QQ/Users/1797571490/QQ/Temp.db/80A0EF19-13B3-43DA-B5BD-D508AB03F410.png) 



![image-20190605094229975](/Users/yuqishi/Library/Application Support/typora-user-images/image-20190605094229975.png) 1903.00087 

####使用1.2版本之后遇到的问题
**下列咩有检索出来的test中的论文名称及原因**
1901.00600	Chinese Academy of Sciences，数据库中有the
1901.00520	CuraCloud ，我在数据库中也没找着

1901.00686		![屏幕快照 2019-06-11 10.46.48](/Users/yuqishi/Desktop/屏幕快照 2019-06-11 10.46.48.png) 

不知道是什么学校 咩检索出来，应该得改单词匹配的那个函数吧，容错性不够，不过就算这个单词与university成功匹配，因为数据库中的大学是 19339 University of Hamburg，我没有做去介词的操作，因此按照当前算法也是没有办法找出来的

1901.00488	Chinese Academy of Sciences，数据库中有the

1901.00097	同上

1901.00534	![image-20190611105602401](/Users/yuqishi/Library/Application Support/typora-user-images/image-20190611105602401.png) 
百密一疏，又是一个没找到的学校

1901.00054.pdf	Chinese Academy of Sciences，数据库中有the

1901.00643.pdf	要了命了 这个是真真正正咩检测出来的学校 National University of Singapore
我一会整理完看一下原因，解决，因为University单词太靠前，倒是University关键词列表为空

1901.00363	Baidu Inc这种数据库没有，我的算法里也没有写找公司的部分
1901.00366	Sensetime research理由同上
1901.00680	UCLA stanford UIUC 缩写没有找出

解决大学重复输出的问题
将pdf和对应的大学写入json

####evaluate 

![屏幕快照 2019-06-13 10.05.23](/Users/yuqishi/Desktop/屏幕快照 2019-06-13 10.05.23.png) 

![屏幕快照 2019-06-13 10.05.32](/Users/yuqishi/Desktop/屏幕快照 2019-06-13 10.05.32.png) 



#####1901.00001 0.0 0.0
in ground_truth `["\"National Technical University of Ukraine, \"Igor Sikorsky Kyiv Polytechnic Institute\""]` 
in extract_university  `["National Technical University"]`

1. 

#####1901.00003 0.2 0.5
`["Carnegie Mellon University", "Uber Advanced Technologies Group"]`

`["Carnegie Mellon University", "Princeton University", "Stanford University", "Toyota Technological Institute at Chicago", "Toyota Technological Institute"]`

1. 数据库中没有Uber Advanced Technologies Group
2. 准确率低的原因是将refenrence中的学校也检索出来了

#####1901.00027 1.0 0.5
`["Nanyang Technological University", "Hebrew University of Jerusalem"]`

`["Nanyang Technological University"]`

1. 数据库中咩有Hebrew University of Jerusalem

#####1901.00039 0.6666666666666666 0.6666666666666666
`["University of Adelaide", " Southeast University", "Sichuan University"]`
`["Sichuan University", "Southeast University", "The University of Adelaide"]`
1. 按理说evaluate的算法是去掉冠词比对的，所以这个我不太清楚为什么没匹配上

#####1901.00040 0.0 0.0
`["queen university", "harvard medical school", "massachusetts institute of technology", "the university of tokyo", "university of british"]`
`["The University of Tokyo"]`

1. 除了massachusetts institute of technology 在数据库中有
2. massachusetts institute of technology问题出现的原因是在提取university上下文时

![屏幕快照 2019-06-13 10.45.26](/Users/yuqishi/Desktop/屏幕快照 2019-06-13 10.45.26.png) 

![image-20190613104605176](/Users/yuqishi/Library/Application Support/typora-user-images/image-20190613104605176.png) 

这个提取的问题尚且不知道出现在哪儿，为什么出现了跨行提取


#####1901.00049 0.5 0.2
`["university of southern california", "usc institute for creative technologies", "university of southern california", "Snap Inc", "Pinscreen"]`
`["University of Southern California", "Waseda University"]`
1. usc institute for creative technologies 数据库没有
2. university of southern california 在ground_truth里面重复标记了，不过好像咩影响召回率 忽略吧
3. Snap Inc 我的算法没有查找公司的部分
4. Pinscreen数据库没有
5. Waseda University在ground_truth中漏标记了，原文是有的

#####1901.00054 1.0 0.5
`["university of chinese academy of sciences", "institute of software, chinese academy of sciences"]`
`["University of Chinese Academy of Sciences"]`
1. 重复标记了哈
2. 