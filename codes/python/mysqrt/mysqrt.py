x=1000000.0
s=1.0
tol = 1.0e-14
kmax = 100
for k in range(kmax):
    print(f"At iteration {k}, the value of s = {s}")
    s0 = s
    s=0.5*(s+x/s)
    delta_s = s - s0
    if(abs(delta_s/x)  < tol):
        break
print(f"finally the value of s={s}")


