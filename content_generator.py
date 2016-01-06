# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 10:41:51 2016

@author: hehe
"""
import urllib
import urllib2
import mechanize
from bs4 import BeautifulSoup
from readability.readability import Document
import random
import json
import sys


def get_login_info(file='config.json'):
    try:
        config = json.load(open(file, 'rb'))
        return config
    except:
        print "loading config file error"
        return None
        
def baidu_translate(ApiKey, src, from_lang, to_lang):
    url = "http://openapi.baidu.com/public/2.0/bmt/translate?client_id="+ApiKey+"&%s"
    params = {'from': from_lang,
              'to': to_lang,
              'q': src.encode('utf8')
             }
    query = urllib.urlencode(params)
    try:
        req = urllib2.Request(url%query)
        con = urllib2.urlopen(req).read()
    except Exception, e:
        raise e
    else:    
        decoded = json.loads(con)
        result = []       
        for item in decoded['trans_result']:
            result.append(item['dst'])
        return '\n'.join(result)
        
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

def changeLiterally(cn_str):
    eng_article = baidu_translate(cn_str,'zh', 'en')
    zh_article_back = baidu_translate(eng_article,'en', 'zh')
    return zh_article_back
   
def main():  
    url = sys.argv[1]
    #url = 'http://jandan.net/2016/01/04/safe-sex-education.html'
    config = get_login_info()
    apikey = config['apikey']
    
    html_text = getHtml(url)
    doc = Document(html_text)
    readable_article = doc.summary()
    readable_title = doc.short_title()
    soup = BeautifulSoup(readable_article)
    final_article = soup.text
    print "原文:"
    print final_article
    eng_article = baidu_translate(apikey, final_article, 'zh', 'en')
    print "英文:"
    print eng_article
    zh_article_back = baidu_translate(apikey, eng_article, 'en', 'zh')
    print "中文:"
    print zh_article_back

if __name__ == "__main__":
    main()    