

import numpy as np

def nonlin(x, deriv=False):
    if(deriv==True):
        return (x*(1-x))
    
    return 1/(1+np.exp(-x))

X = np.array([[0,0,1],  
            [0,1,1],
            [1,0,1],
            [1,1,1]])

y = np.array([[0],
             [1],
             [1],
             [0]])


np.random.seed(1)

syn0 = 2*np.random.random((3,4)) - 1  
syn1 = 2*np.random.random((4,1)) - 1  

for j in xrange(60000):  
    
    # Calculate forward through the network.
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
    
    # Back propagation of errors using the chain rule. 
    l2_error = y - l2
    if(j % 10000) == 0:   # Only print the error every 10000 steps, to save time and limit the amount of output. 
        print "Error: " + str(np.mean(np.abs(l2_error)))
        
    l2_delta = l2_error*nonlin(l2, deriv=True)
    
    l1_error = l2_delta.dot(syn1.T)
    
    l1_delta = l1_error * nonlin(l1,deriv=True)
    
    #update weights (no learning rate term)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)
    
print "Output after training"
print l2
    
    


# See how the final output closely approximates the true output [0, 1, 1, 0]. If you increase the number of interations in the training loop (currently 60000), the final output will be even closer. 

# In[8]:

#get_ipython().run_cell_magic(u'HTML', u'', u'<iframe width="560" height="315" src="https://www.youtube.com/embed/h3l4qz76JhQ" frameborder="0" allowfullscreen></iframe>')


# In[ ]:
