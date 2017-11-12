# import urllib.request
# import urllib.parse
# import re
# # http://www.mathhelp.com/intermediate-algebra-help/?utm_campaign=purplemath&utm_source=_mh_cima&utm_medium=course

# url = "http://www.mathhelp.com/intermediate-algebra-help/"
# values = {"utm_campaign":"purplemath",
# 		  "utm_source" : "_mh_cima",
# 		  "utm_medium" : "course"
# 		 }
# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8')
# req = urllib.request.Request(url,data)
# resp = urllib.request.urlopen(req)
# respData = resp.read()
# # print(respData)
# # saveFile = open('algebraIntermediate.txt','w')
# # saveFile.write(str(respData))
# # saveFile.close()
# hrefs = re.findall(r'<a href=(.*?)</a>', str(respData))
# topics = hrefs[41: 100 ]

# for eachTopic in topics:
# 	title = eachTopic.split(">")
# 	print(title[1])
# # /usr/local/opt/openssl/bin:$PATH