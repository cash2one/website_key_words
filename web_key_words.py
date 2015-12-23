# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 13:57:15 2015

@author: hehe
"""
import random
import jieba
import mechanize
from bs4 import BeautifulSoup
import re
import sys

def getHtml(url):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    header = {'Accept': 'text/html,application/xhtml+xml,applicatiaaon/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    header['User-Agent'] = 'Mozilla/{0}.{1} \
        (X11; Linux x86_64) AppleWebKit/537.11 \
        (KHTML, like Gecko) Chrome/{2}.0.1271.64 \
        Safari/537.{3}'.format(random.randint(1,9), \
        random.randint(1,9), random.randint(10,30), \
        random.randint(1,20))    
    br.addheaders = header.items()        
    
    htmltext = br.open(url).read()    
    return htmltext

def getArticleFromHtml(htmltext):
    article_text = ""
    soup = BeautifulSoup(htmltext)
    for tag in soup.findAll('p'):
        try:
            article_text += tag.contents[0]
        except:
            continue
    return article_text
        
def getArticle(url):
    htmltext = getHtml(url)
    article_text = getArticleFromHtml(htmltext)        
    return article_text

def getKeyWords(text, stopwords, topk):
    word_dict = {}
    text = processLine(text)
    words = jieba.cut(text, cut_all=False)
    for word in words:
        if not word.isspace():
            if not word.isdigit():
                word_dict[word] = word_dict.get(word, 0) + 1
            
    for stopword in stopwords:
        if word_dict.get(stopword):
            word_dict.pop(stopword)
            
    word_freq = sorted(word_dict.items(), key=lambda (k,v):(v,k), reverse=True)
    most_word = word_freq[:25]
    return [item[0] for item in most_word]
    
def processLine(line):
    return re.sub("]-·[\s+\.\!\/_,$%^*(+\"\':]+|{}[：+——！，。？、~@#￥%……&*（）():\"=《]+".decode("utf8"),
                                           " ".decode("utf8"), line)
def loadStopWords(file='stop_words.txt'):
    with open(file, 'rb') as f:
        stop_words = f.read().decode('utf8')
        stop_words = stop_words.split()
    return stop_words

def printKeyWords(keywords):
    for keyword in keywords:
        print keyword,

#url = 'http://jandan.net/2015/12/23/justin-bieber-fan.html'
#url = 'http://news.sina.com.cn/c/sd/2015-12-23/doc-ifxmueaa3700748.shtml'      
url = sys.argv[1]
stop_words = loadStopWords()    
article_text = getArticle(url)        
key_words = getKeyWords(article_text, stop_words,topk=25)
printKeyWords(key_words)
