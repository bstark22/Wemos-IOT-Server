
## Testing to see that values are returned correctly: (0,0.04)(1,null)(1,0.04)(1,null)(0,null)
import requests
IP='192.168.1.xx'
val='1'
ConnectStatus=0
r=requests.get('http://'+IP+'/run/'+val)
print(r.text)

r=requests.get('http://'+IP+'/gpio/'+val)
print(r.text)

r=requests.get('http://'+IP+'/run/'+val)
print(r.text)

val='0'
r=requests.get('http://'+IP+'/run/'+val)
print(r.text)

r=requests.get('http://'+IP+'/gpio/'+val)
print(r.text)

