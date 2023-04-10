from math import sinh, exp, e, pi
x = 2*pi
r1 = sinh(x)
r2 = 0.5*(exp(x) - exp(-x))
r3 = 0.5*(e**x - e**(-x))
print("Nilai r1=\n", r1)
print("Nilai r2=\n", r2)
print("Nilai r2=\n", r3) 

#output dari program ini adalah
# Nilai r1=
#  267.74489404101644
# Nilai r2=
#  267.74489404101644
# Nilai r2=
#  267.7448940410163
