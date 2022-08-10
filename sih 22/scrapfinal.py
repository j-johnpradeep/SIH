
import socket
import requests
import json
from bs4 import BeautifulSoup
import re

host="bbc.co.uk"
host_ip=socket.gethostbyname(host)
print("myip:"+host_ip)
ip_address=str(host_ip)
request_url = 'https://geolocation-db.com/jsonp/' + ip_address

response = requests.get(request_url)
result = response.content.decode()

result = result.split("(")[1].strip(")")

result  = json.loads(result)



def facebook():
    if fb is None:
        return "No Facebook Link Is Found"
    return fb['href']

def instagram():
    if insta is None:   
        return "No Instagram Link Is Found"
    return insta['href']
       
def twitter():
    if twt is None:
        return "No Twitter Link Is Found"
    return twt['href']

def youtube():
    if y is None:
        return "No Youtube Link Is Found"
    return y['href']

  

headers={'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
url=f'https://www.hindutamil.in/'
r=requests.get(url,headers)
soup=BeautifulSoup(r.content,'html.parser')
title=soup.find("title").text
fb= soup.find('a', {'href': re.compile("https?://(www\\.)?facebook\\.com/[^(share)]?(\\w+\\.?)+")})
insta= soup.find('a', {'href': re.compile("https?://(www\\.)?instagram\\.com/[^(share)]?(\\w+\\.?)+")})
twt= soup.find('a', {'href': re.compile("https?://(www\\.)?twitter\\.com/[^(share)]?(\\w+\\.?)+")})
y=soup.find('a', {'href': re.compile("https?://(www\\.)?youtube\\.com/[^(share)]?(\\w+\\.?)+")})      
fab=facebook()
i=instagram()
t=twitter()
y=youtube()

with open("text_output.txt","w") as f:
        print(result['country_name'],file=f)
        print("TITLE:",file=f)
        print(title,file=f)
        print("LINKS:\n",file=f)
        print(fab,file=f)
        print(i,file=f)
        print(t,file=f)
        print(y,file=f)
        

