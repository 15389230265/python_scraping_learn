import requests
import webbrowser

param = {"wd": "莫烦Python"}  # 搜索的信息
r = requests.get('http://www.baidu.com/s', params=param)
print(r.url)
# webbrowser.open(r.url)

data = {'firstname': '浩翔', 'lastname': '梁'}
r = requests.post('http://pythonscraping.com/pages/files/processing.php', data=data)
print(r.text)

file = {'uploadFile': open('./pkq.jpg', 'rb')}
r = requests.post('http://pythonscraping.com/pages/files/processing2.php', files=file)
print(r.text)

payload = {'username': '梁浩翔', 'password': 'password'}
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())

# 网页404
# r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
# print(r.text)

#  在一次会话中, 我们的 cookies 信息都是相连通的, 它自动帮我们传递这些 cookies 信息
session = requests.Session()
payload = {'username': '梁浩翔', 'password': 'password'}
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())

r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(r.text)
