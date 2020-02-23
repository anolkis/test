
import requests
import math

f = open("result.txt", 'w')
f.write('{:^5}{:^5}{:^5}{:^5}{:^5}{:^5}{:^8}{:^8}{:^8}\n'.format('x1','y1',
'x2','y2','x3','y3','api_r','res', 'TEST'))

url = 'http://localhost:7080/api/area-triangle/'

myobj1 = {"x1":1, "y1":1, "x2":-2, "y2":4, "x3":-2, "y3":-2}
myobj2 = {"x1":0, "y1":0, "x2":0, "y2":1, "x3":1, "y3":0}
myobj3 = {"x1":3.4, "y1":1, "x2":-2, "y2":4, "x3":-2, "y3":-2}
myobj4 = {"x1":0, "y1":0, "x2":0, "y2":0, "x3":0, "y3":0}
myobj5 = {"x1":-1.1, "y1":-2, "x2":-1, "y2":-1, "x3":0, "y3":-1}
myobj6 = {"x1":-10, "y1":-100, "x2":10, "y2":100, "x3":5, "y3":5}

list_of_obj = (myobj1, myobj2, myobj3, myobj4, myobj5, myobj6)
test_res = '-'

for obj in list_of_obj:

	resp = requests.post(url, json=obj)
	api_r = float(resp.content)

	#print("%.1f" %api_r)
	A11 = obj["x1"]-obj["x3"]
	A12 = obj["y1"]-obj["y3"]
	A21 = obj["x2"]-obj["x3"]
	A22 = obj["y2"]-obj["y3"]

	res = 0.5*math.fabs(A11*A22 - A12*A21)

	#print("%.1f" %res)

	if api_r == res:
		test_res = 'pass'
	else:
		test_res = 'FAIL'

	f.write('{:^5}{:^5}{:^5}{:^5}{:^5}{:^5}{:^8}{:^8.1f}{:^8}\n'.format(obj["x1"],
	obj["y1"],obj["x2"],obj["y2"],obj["x3"],obj["y3"],api_r,res,test_res))

f.close()