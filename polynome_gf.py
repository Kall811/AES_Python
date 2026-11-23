
def degre(A):
    n=len(A)-1
    while n>=0:
        if A[n]!=0:
            return n
        n-=1
    return (-1)

def div_eucl_gf(A,B):
    R=A.copy()
    Q=[0 for k in range(len(A))]
    p=degre(B)
    n=degre(R)
    while n>=p:
        Q[n-p] ^= 1
        for l in range(len(B)):
            R[n-p+l] ^= B[l]
        n=degre(R)
    return (Q,R)

def produit(A,B):
    n=degre(A)
    p=degre(B)
    if n==(-1) or p==(-1):
        return [0 for k in range(8)]
    degre_sortie=n+p 
    sortie=[0 for k in range(degre_sortie+1)]
    for k in range(n+1):
        for l in range(p+1):
            sortie[k+l] ^= A[k]*B[l]
    return sortie

def conversion_gf(a):
    sortie=[0 for k in range(8)]
    n=7
    p=2**7
    while a!=0:
        b=a//p
        sortie[n]=b
        a -= b*p
        n-=1
        p//=2
    return sortie 

def conversion_int(A):
    return sum([A[k]*(2**k) for k in range(8) if k<len(A)])

def reformatation(A):
    return [A[k] for k in range(8) if k<len(A)]

def produit_gf(a,b):
    A=conversion_gf(a)
    B=conversion_gf(b)
    C=produit(A,B)
    M=[1,1,0,1,1,0,0,0,1]
    _,R=div_eucl_gf(C,M)
    S=reformatation(R)
    s=conversion_int(S)
    return s


