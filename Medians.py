'''  Preconditions:  X and Y are sorted Python lists of integers values, and
       their lengths are both equal to 2^k+1 for some k >= 0.  
     Postcondition:  the two medians of X+Y have been returned as a 
       python List of size two.
'''
def medians(X,Y):
   lastIndex = len(X) - 1
   return mediansAux(X, 0, lastIndex, Y, 0, lastIndex)

'''  Preconditions:  j1-i1+1 = j2-i2+1 = 2^k+1 for some k >= 0, and
        X[i1:j1+1] and Y[i2:j2+1] are sorted lists of integers.
     Postcondition:  the two medians of X[i1:j1+1] + Y[i2:j2+1]  have
        been returned as a Python list of length two.
     Fill in the recursive procedure.  To get credit, your running time must 
        be o(n) where n = j1-i1+1
'''
def mediansAux(X, i1, j1, Y, i2, j2):
    if ((j1 - i1) == 1) and ((j2 - i2) == 1):
        # Number of elements in base case is 2^0+1=2, get median manually
        if (X[j1] <= Y[i2]):
            # All entries in X[i1:j1] is no bigger than entries in Y[i2:j2]
            return [X[j1], Y[i2]]
        if (X[i1] >= Y[j2]):
            # All entries in X[i1:j1] is no smaller than entries in Y[i2:j2]
            return [Y[j2], X[i1]]
        # Else we compare X[i1] and Y[i2], X[j1] and Y[j2] to get the medians
        if (X[i1] <= Y[i2]):
            first_median = Y[i2]
        else:
            first_median = X[i1]
        if (X[j1] <= Y[j2]):
            second_median = X[j1]
        else:
            second_median = Y[j2]
        return [first_median, second_median]
    Xmid = (i1 + j1)/2
    Ymid = (i2 + j2)/2
    if (X[Xmid] == Y[Ymid]):
        # median of X is the same as median of Y, those are medians X+Y
        return [X[Xmid], Y[Ymid]]
    if (X[Xmid] > Y[Ymid]):
        # median of X is higher than median of Y, remove latter part of X and former part of Y
        return mediansAux(X, i1, (i1+j1)/2, Y, (i2+j2)/2, j2);
    else:
        # median of X is lower than medain of Y, remove the former part of X and latter part of Y
        return mediansAux(X, (i1+j1)/2, j1, Y, i2, (i2+j2)/2);
