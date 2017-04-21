from sympy.abc import D,g,m,n,r,x,B,s,z
from sympy import simplify
from sympy import tanh

# D=D
#D_0 = B
#s - sigma_1
#z= sigma_2
#g=g_1
#x=x
#m=m*
#n=m_1
#r=m*_0


D_expr_1 = B - s (g/x - n)*(0.5*D)*(1-(tanh((n-m)/D))**2)

m_expr_1 = r - z (g/x - n)*((n-m)/(0.5*D**2))*(1-(tanh((n-m)/D))**2)

m_expr_2 = r - z (g/x - n)*((n-m)/(0.5*D_expr_1**2))*(1-(tanh((n-m)/D_expr_1))**2)
print simplify(m_expr_2)
