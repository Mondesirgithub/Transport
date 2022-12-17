import requests

def getLocation(ip , token):
   url = f'http://api.ipstack.com/{ip}?access_key={token}'

   headers = {'Content-Type':'application/json'}
   reponse = requests.get(url , headers)

   print('Request ,', reponse)
   print('******************************************')
   print(reponse.text)


getLocation('102.129.81.173','8410640576d52c3d373c98705c77b5dc')