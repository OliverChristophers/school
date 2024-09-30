def double(n):
    return 2 * n
def triple(n):
    return 3 * n
def quadruple(n):
    return double(n) + double(n)
def funky(n, m):
    return triple(n) + quadruple(m)

#testfall
a = 3
b = 14
double(a)        
double(b)  
    
triple(a)    
triple(b)  
    
quadruple(a) 
quadruple(b)   

funky(a, b)   
funky(b, b)