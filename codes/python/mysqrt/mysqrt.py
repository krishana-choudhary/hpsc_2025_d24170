x=2.0
s=1.0
kmax = 10
for k in range(kmax):
    print(f"At iteration {k}, the value of s = {s}")
    s=0.5*(s+x/s)
print(f"finally the value of s={s}")


