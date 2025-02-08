def sqrt2(x, debug = False):
	s=1.0
	tol = 1.0e-14
	kmax = 100
	for k in range(kmax):
		if debug:
			print(f"At iteration {k}, the value of s = {s:20.15f}")
		s0 = s
		s=0.5*(s+x/s)
		delta_s = s - s0
		if(abs(delta_s/x)  < tol):
			break
	if debug:
		print(f"finally the value of s={s:16.15f}")
		
	return s
	

