##网页关键词提取
###需要
jieba

mechanize
###使用
```shell
python web_key_words.py http://jandan.net/2015/12/22/10-celebs.html
```
###输出
```
博士 博士学位 大学 JB amy Amy 数学 教授 出演 乐队 说 职业 美国 硕士 研究 明星 拿到 形象 学历 含蓄 医学博士 魅力 高 面带微笑 重返
```
##网页内容更改
翻译成英文再翻译回来.需要申请百度APIKEY.

[http://developer.baidu.com/wiki/index.php?title=%E5%B8%AE%E5%8A%A9%E6%96%87%E6%A1%A3%E9%A6%96%E9%A1%B5/%E7%99%BE%E5%BA%A6%E7%BF%BB%E8%AF%91API](http://developer.baidu.com/wiki/index.php?title=%E5%B8%AE%E5%8A%A9%E6%96%87%E6%A1%A3%E9%A6%96%E9%A1%B5/%E7%99%BE%E5%BA%A6%E7%BF%BB%E8%AF%91API)
###使用
修改config.json,填入apikey.
```shell
python content_generator.py http://jandan.net/2015/12/22/10-celebs.html
```
###输出
```
原文:
Justin Bieber与Selena Gomez
衣着华丽、充满魅力、面带微笑，非常含蓄，学历不高，这就是演艺明星在公众眼中的形象
英文:
Bieber Justin and Gomez Selena
Dress gorgeous, full of charm, with a smile, very subtle, education is not high,
中文:
比伯贾斯廷和戈麦斯Selena
衣着华丽，充满魅力，带着微笑，非常微妙，学历不高，这是一个形象的表演艺术明星在公
```
