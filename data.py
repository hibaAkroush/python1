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
# urls = []

# mainurl = "http://www.mathhelp.com/intermediate-algebra-help/?utm_campaign=purplemath&utm_source=_mh_cima&utm_medium=course"
# req = urllib2.Request(mainurl)
# response = urllib2.urlopen(req)
# the_page = response.read()
# urls = re.findall(r'/how_to/(.*?)">', str(the_page))
# j=0
# while j<len(urls):
# 	temp = urls[j]
# 	urls[j] = "http://www.mathhelp.com/how_to/"+urls[j]
# 	j+=1
# print(urls)

# listOfTopics = []

# i=0
# while i<len(urls):
# 	x = {}
# 	req = urllib2.Request(urls[i])
# 	response = urllib2.urlopen(req)
# 	the_page = response.read()
# 	title = re.findall(r'<title>(.*?)</title>', str(the_page))
# 	img = re.findall(r'<img src="(.*?)"', str(the_page))
# 	content = re.findall(r'</h1><p>(.*?)</p>', str(the_page))
# 	url = urls[i]
# 	x.update({"img":img[1]})
# 	x.update({"title":title})
# 	x.update({"url":url})
# 	x.update({"id":i})
# 	x.update({"content":content})
# 	listOfTopics.append(x)
# 	i+=1
# def Articles():
# 	articles = listOfTopics
# 	return articles
# urls =["http://www.purplemath.com/modules/grphquad.htm",
# "http://www.purplemath.com/modules/absineq.htm",
# "http://www.purplemath.com/modules/ineqquad.htm",
# "http://www.purplemath.com/modules/numeric.htm",
# "http://www.purplemath.com/modules/synthdiv.htm",
# "http://www.purplemath.com/modules/factrthm.htm"]
# print(listOfTopics)
# hrefs = re.findall(r'<a href=(.*?)</a>', str(respData))
# urlex = "http://www.mathhelp.com/intermediate-algebra-help/?utm_campaign=purplemath&utm_source=_mh_cima&utm_medium=course"
# values = {"utm_campaign":"purplemath",
# 		  "utm_source" : "_mh_cima",
# 		  "utm_medium" : "course"
# 		 }
# req2 = urllib2.Request(urlex)
# response2 = urllib2.urlopen(req2)
# the_page2 = response2.read()
# # data = urllib.urlencode(values)

# content = re.findall(regex, the_page2)
# print(content)
# print(respData)
# saveFile = open('algebraIntermediate.txt','w')
# saveFile.write(str(respData))
# saveFile.close()

# topics = hrefs[41: 100 ]

# for eachTopic in topics:
# 	title = eachTopic.split(">")
# 	print(title[1])
# /usr/local/opt/openssl/bin:$PATH


