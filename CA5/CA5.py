
# CA5: Python Calculator - 10357791 Alex Brown

import itertools

# 1. Addition
def addition(first, second):
    return map(lambda x, y: x+y, first, second)	

# 2. Subtraction
def subtraction(first, second):
    return map(lambda x, y: x-y, first, second)	

# 3. Division	
def division(first, second):
	return map(lambda x, y: x/float(y) if y!=0 else 'nan', first, second) 
   
        
# 4. Multiplication	
def multiplication(first, second):
	return map(lambda x, y: x*float(y) if y!=0 else 'nan', first, second) 
    

# 5. Cube
def cube(values):	
	return map(lambda x: x*x*x, values)
	
   
# 6. Remainder
def mod(values):	
	return map(lambda x: x%x, values)
	
# 7. Exponential    
def exponent(first, second):
    return map(lambda x, y: x**y, first, second)   

	   
# 8. Permutations
def permutation(a,k=0):
   if(k==len(a)):
      print a
   else:
      for i in xrange(k,len(a)):
         a[k],a[i] = a[i],a[k]
         permutation(a, k+1)
         a[k],a[i] = a[i],a[k]
   
# 9. Cube Root
def cubeR(values):	
	return map(lambda x : x ** 1/3, values) 
    
# 10. Square Root
def squareR(values):	
	return map(lambda x : x ** 0.5, values) 

   
    
   


        
#PRINT RESULT FOR CALLS HERE
print
print "***********************"
print "CALC TESTING RESULTS	"
print "***********************"
print
print "Addition result: ", addition([6, 4, 23, 15, 7], [5, 11, 45, 32, 28]) 
print  
print "Subtraction result: ",subtraction([10, 16, 1, 23, 6], [2, 5, 6, 3, 65])
print 
print "Division result: ",division([8, 30, 45],[4, 5, 9])
print  
print "Multiplication result: ",multiplication([6, 5, 7, 23, 160], [12, 34, 66, 8, 45])
print
print "Cube result: ",cube([4, 2, 100])
print
print "Remainder result: ",mod([14, 4, 22])
print
print "Exponent result: ",exponent([4, 12, 6], [4, 4, 6])
print
print "Permutation result: "
print permutation([2,4,5])
print
print "Cube Root result: ",cubeR ([4, 13, 45])
print
print "Square Root result: ",squareR([3, 5, 78])
print



	



