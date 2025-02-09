
def test1():
	
	from numpy import sqrt
	from mysqrt import sqrt2
	
	xvalues = [2,100,10000,0.00001,1e+8,0]
	small = 1e-14
	for x in xvalues:
		s = sqrt2(x)
		s_numpy = sqrt(x)
		if x == 0:
			if s == 0:
				print(f"for x = {x}, s = {s} and s_numpy = {s_numpy}")
				continue
			else:
				print("Test failed for x=0")
		print(f"for x = {x}, s = {s} and s_numpy = {s_numpy}")
		assert abs((s-s_numpy)/x) < small,f" square root disagrees with numpy square root for x ={x}"
	

def test2():
	
	from numpy import sqrt
	from mysqrt import sqrt2
	
	xvalues = [80, 3]
	small = 1e-14
	for x in xvalues:
		s = sqrt2(x)
		s_numpy = sqrt(x)
		if x == 0:
			if s == 0:
				print(f"for x = {x}, s = {s} and s_numpy = {s_numpy}")
				continue
			else:
				print("Test failed for x=0")
		print(f"for x = {x}, s = {s} and s_numpy = {s_numpy}")
		assert abs((s-s_numpy)/x) < small,f" square root disagrees with numpy square root for x ={x}"
