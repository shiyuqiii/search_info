# -*- coding: UTF-8 -*-
import PyPDF2
import textract

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#read pdf file
#write a for-loop to open many files
filename = 'Matrix Factorization Techniques.pdf'
pdfFileObj = open(filename, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

num_pages = pdfReader.numPages
count = 0
text = ""

# while 循环会读取每一页
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

if text != "":
   text = text
else:
   text = textract.process(fileurl, method='tesseract', language='eng')

#The word_tokenize() function will break our text phrases
#into individual words
tokens = word_tokenize(text)
#we'll create a new list which contains punctuation we wish to clean
punctuations = ['(',')',';',':','[',']',',']
#We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords
stop_words = stopwords.words('english')
#We create a list comprehension which only returns a list of words that are NOT IN stop_words and NOT IN punctuations.
keywords = [word for word in tokens if not word in stop_words and not word in punctuations]