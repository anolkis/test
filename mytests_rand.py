
import requests
import math
import random

f = open("result_rand.txt", 'w')
f.write('{:>8}{:>8}{:>8}{:>8}{:>8}{:>8}{:>8}{:>8}{:>8}\n'.format('x1','y1',
'x2','y2','x3','y3','api_r','res', 'TEST'))

url = 'http://localhost:7080/api/area-triangle/'

obj = {"x1":0, "y1":0, "x2":0, "y2":0, "x3":0, "y3":0}

test_res = '-'

for test in range (1, 100):

	dots = []

	for i in range(0, 6):

		tmp = float('{:.1f}'.format(random.randint(-100, 100)/random.randint(1, 10)))
		dots.append(tmp)
		print(dots[i])

	i=0
	for key in obj:
		obj[key] = dots[i]
		i = i + 1 
	
	print(obj)


	resp = requests.post(url, json=obj)
	api_r = float(resp.content)

	print("Api_res %.1f" %api_r)
	A11 = obj["x1"]-obj["x3"]
	A12 = obj["y1"]-obj["y3"]
	A21 = obj["x2"]-obj["x3"]
	A22 = obj["y2"]-obj["y3"]

	res = 0.5*math.fabs(A11*A22 - A12*A21)

	print("result %.1f" %res)

	if api_r == res:
		test_res = 'pass'
	else:
		test_res = 'FAIL'

		f.write('{:>8}{:>8}{:>8}{:>8}{:>8}{:>8}{:>8}{:>8.1f}{:>8}\n'.format(obj["x1"],
		obj["y1"],obj["x2"],obj["y2"],obj["x3"],obj["y3"],api_r,res,test_res))

f.close()