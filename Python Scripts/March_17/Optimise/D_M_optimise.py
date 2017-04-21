import numpy as np
import grid
from scipy.optimize import minimize
from scipy.special import factorial
import math

m_g_pairs = grid.grid_gen(100,30,0.5)
#param[0] = m*,param[1]=D
#print m_g_pairs
def deriv_M(param):
    return (np.sum(-((m_g_pairs[:,1]/(0.5+0.5*np.tanh((m_g_pairs[:,0]-param[0])/param[1])))-m_g_pairs[:,0])*(0.5*(m_g_pairs[:,0]-param[0])/param[1])*(1-np.tanh((m_g_pairs[:,0]-param[0])/param[1])**2)))-(param[0]-100)/5
    #np.sum(0.5*m_g_pairs[:,0]*(-np.tanh((-param[0]+ m_g_pairs[:,1])/param[1])**2 + 1)/(param[1]*(-0.5*np.tanh((-param[0]+ m_g_pairs[:,1])/param[1]) - 0.5)) + 0.5*m_g_pairs[:,1]*(-np.tanh((-param[0]+ m_g_pairs[:,1])/param[1])**2 + 1)/param[1])

def deriv_D(param):
    return np.sum(-((m_g_pairs[:,1]/(0.5+0.5*np.tanh((m_g_pairs[:,0]-param[0])/param[1])))-m_g_pairs[:,0])*(0.5*(1/param[1]))*(1-np.tanh((m_g_pairs[:,0]-param[0])/param[1])**2))-(param[1]-10)/2
        #np.sum(-((param[1]/(-0.5*np.tanh((-param[0]+ m_g_pairs[:,1])/param[1])))-m_g_pairs[:,0])*(0.5*param[1])*(1-np.tanh((-param[0]+ m_g_pairs[:,1])/param[1])**2))
def M0_D0_test():
    for i in ([500,10],[250,10],[1,10],[1,25],[1,50]):
        result1 = minimize(deriv_M, i,bounds=((1,1000),(1,1000)),method='SLSQP')
        #result2 = minimize(deriv_D, i,bounds=((0,1000),(0,1000)))
        print "fun:", result1.fun ,"   x:" ,result1.x
        print "fun:", result2.fun ,"   x:" ,result2.x


#result = minimize(deriv_M, [10,50], bounds=((1,1000),(1,1000)))

def dM_eval():
    func_dM = []
    for i in M_range:
        for j in D_range:
            param=[i,j]
            if math.isnan(deriv_D(param)):
                print 'YO', param,
            else:
                dM = param + [deriv_D(param)]
                func_dM.append(dM)

    #func_dM=zip(*[iter(func_dM)]*100)
    func_dM= np.array(func_dM)
    return func_dM

M_range=range(0,100)
D_range=range(1,101)
result = dM_eval()
print result.shape

def plot_3d():
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.scatter(result[:,0],result[:,1],result[:,2])

    ax.set_xlabel('m*')
    ax.set_ylabel('D')
    ax.set_zlabel('function')
    plt.show()

plot_3d()

def eval_func():
    for i in range (0,200):
        for j in range (0,200):
            param = [M_func_dM[i,0],M_func_dM[0,j]]
            if param[0]== m_g_pairs.any():
                pass
            else:
                M_func_dM[i,j]=deriv_M(param)

#result = eval_func()
#print result
"""
#optimising the log likely hood this is finding the roots of the log likelihood, what we want is to minimise dlog-like/dD and dlog-like/dm*
def log_like(param):
    return -np.sum(np.log(np.exp(-(1+np.tanh((m_g_pairs[:,0]-param[0])/param[1])))*((1+np.tanh((m_g_pairs[:,0]-param[0])/param[1])*m_g_pairs[:,0])**(m_g_pairs[:,1]))/(factorial(m_g_pairs[:,1]))))




result = optimize.minimize(log_like, [10,10], bounds=((0,1000),(0,1000)))
print dir(result)
print type(result.x)
"""
