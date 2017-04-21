import numpy as np


# generate a grid with a bias
def grid_gen(n_pairs,grid_length,bias):
    m_g_pairs = np.zeros(shape=(2,n_pairs))

    for j in range(0,n_pairs): #n_pairs is the number of time pairs
        N = grid_length**2
        x = bias
        m = float(np.random.randint(N/10,size=1)) #arbatry N/n to ensure m/N is small


        s=np.random.choice([0,1],size=(N,),p=[(1-m/N),m/N]) # make grid with s_i= 1 with prob m/N
        #print m,np.sum(s)
        s_1=np.squeeze(np.zeros(shape=(1,N)))


        for i in range(0,N,1):
            if s[i,]==1:
                s_1[i,] = np.random.choice([0,1],p=[(1-x),x])  # s_i detected correctly with prob m_M_pairs[1,i] to give s^1 the underdetected version of s
            else:
                s_1[i,]=0

        g=np.sum(s_1)

        m_g_pairs[0,j]=float(m)
        m_g_pairs[1,j]=float(g)

    return m_g_pairs
