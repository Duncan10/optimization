def numEval(f, x, A, eps):
    """
    f: argument function
    x: input vector
    eps: scalar
    A: matrix
    """
    #allocate space for gradient
    n = x.shape
    grad = np.zeros(n)
    #only test for map function to be removed
    grad_out = np.zeros(n)
    #precompute matrices
    eps_m = np.eye(len(grad))*eps
    x_ = np.matmul(A,x)
    eps_M = np.matmul(A, eps_m)

    
  
    #TODO: every time matmul makes no sense !!
    for i in range(0, len(x)):
        #TODO: every time matmul makes no sense !!
        #first function somehow more precise, why?
        #grad[i]=(f(np.matmul(A,(x+eps_m[i,])))-f(np.matmul(A,(x-eps_m[i,]))))/(2*eps)
        grad_out[i] = (f(x_ + eps_M[:,i]) - f(x_ - eps_M[:,i]))/(2*eps)
    #print("originial grad reference:", grad)


    return grad_out