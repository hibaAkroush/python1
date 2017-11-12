# import urllib.request
# import urllib.parse
# import re

# url = "http://www.purplemath.com/modules/grphquad.htm"
# htmlFile = urllib.request.urlopen(url)
# respData = htmlFile.read()
# title = re.findall(r'<title>(.*?)</title>', str(respData))
# imgSoursre = re.findall(r'<img src="//www.(.*?)', str(respData)) 
# description = re.findall(r'name="description" content=(.*?)', str(respData)) 
# print(title,imgSoursre,description)
# <p class="text">
import urllib2
import re

# url = "http://www.purplemath.com/modules/grphquad.htm"
# req = urllib2.Request(url)
# response = urllib2.urlopen(req)
# the_page = response.read()
# title = re.findall(r'<title>(.*?)</title>', str(the_page))
# # description = re.findall(r'<p class="text">(.*?)</p>', str(the_page))
# img = re.findall(r'<img src=(.*?) ', str(the_page))


listOfTopics = []

urls =["http://www.purplemath.com/modules/grphquad.htm",
"http://www.purplemath.com/modules/absineq.htm",
"http://www.purplemath.com/modules/ineqquad.htm",
"http://www.purplemath.com/modules/numeric.htm",
"http://www.purplemath.com/modules/synthdiv.htm",
"http://www.purplemath.com/modules/factrthm.htm"]
i=0
while i<len(urls):
	x = {}
	req = urllib2.Request(urls[i])
	response = urllib2.urlopen(req)
	the_page = response.read()
	title = re.findall(r'<title>(.*?)</title>', str(the_page))
	img = re.findall(r'<img src="(.*?)"', str(the_page))
	url = urls[i]
	x.update({"img":img[12]})
	x.update({"title":title})
	x.update({"url":url})
	x.update({"id":i})
	listOfTopics.append(x)
	i+=1
print(listOfTopics)
# hrefs = re.findall(r'<a href=(.*?)</a>', str(respData))
# http://www.mathhelp.com/intermediate-algebra-help/?utm_campaign=purplemath&utm_source=_mh_cima&utm_medium=course
# values = {"utm_campaign":"purplemath",
# 		  "utm_source" : "_mh_cima",
# 		  "utm_medium" : "course"
# 		 }
# data = urllib.parse.urlencode(values)
# ,data
# print(respData)
# saveFile = open('algebraIntermediate.txt','w')
# saveFile.write(str(respData))
# saveFile.close()

# topics = hrefs[41: 100 ]

# for eachTopic in topics:
# 	title = eachTopic.split(">")
# 	print(title[1])
# /usr/local/opt/openssl/bin:$PATH

def Articles():
	articles = listOfTopics
	return articles
