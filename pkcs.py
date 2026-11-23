
def padding(b):
    n=len(b)
    N=16 - n%16
    a=bytes([N]*N)
    return b+a 

def unpadding(b):
    n=len(b)
    K=b[n-1]
    return b[:n-K]
