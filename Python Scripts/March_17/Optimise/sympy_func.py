from grid import grid_gen
import numpy as np

pairs = np.array(grid_gen(100,30,0.5))

def ML_deriv(m_g_pairs):
        from sympy import tanh,log,exp
        from sympy.abc import m,M,D,g
        import sympy.utilities.lambdify
        from sympy import factorial
        from sympy import diff

        #print dir(sympy.functions.combinatorial)
        #Python differentiation==========================================================================

        #expr = log(exp(-(0.5+(0.5)*tanh(((m-M)/D)))*m)*(((0.5+(0.5)*tanh(((m-M)/D)))*m)**g))
        expr = -(0.5+(0.5)*tanh((m-M)/D))*m*log(((0.5+(0.5)*tanh((m-M)/D))*m)**g)
        #log(exp(-(0.5+(0.5)*tanh((m-M)/D))*m)*(((0.5+(0.5)*tanh(((m-M)/D)))*m)**g))

        print diff(expr,D)
        print diff(expr,M)


ML_deriv(pairs)
