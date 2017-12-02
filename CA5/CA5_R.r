
# CA5: R Calculator - 10357791 Alex Brown

# 1.Addition
addition <- function(numb1, numb2) {
  return(numb1 + numb2)
}

#Test Addition

addition(4,5)
addition(45,2)
addition(45,-6)

#2.Subtraction
subtraction <- function(numb1, numb2) {
  return(numb1 - numb2)
}

#Test Subtraction 
subtraction(6,7)
subtraction(23,56)
subtraction(34,-78)

#3.Division

division <- function(numb1, numb2){
  return(numb1 / numb2)
}

#Test Division 
division(34,2)
division(45,9)
division(6,-2)

#4.Multiplication
multiply <- function(numb1, numb2){
  return(numb1 * numb2)
}

#Test Multiplication
multiply(9,4)
multiply(45,2)
multiply(2,-2)

#5.Cube
cube <- function(numb1){
  return(numb1 ** 3)
}

#Test Cube
cube(4)
cube(12)
cube(8)

#6.Remainder
remainder <- function(num1, num2){
  return(num1 %% num2)
}


#.Test Remainder 
remainder(3, 7)
remainder(5, 7)
remainder(3, 11)

#7.Exponential

exponential <- function(numb1, numb2){
  return(numb1 ** numb2)}

#Test Exponential 
exponential(4, 7)
exponential(9, 4)
exponential(13, 45)

#8.Permutations
perm = function(n, x) {
  factorial(n) / factorial(n-x)
}

#Test Permutations
perm (34, 8)
perm (7, 9)

#9.Cube Root
cube_root <- function(numb1, numb2){
  return(numb1 ** 1. /3)
}

#Test Cube Root 
cube_root(4, 9)

#10.Square Root
sqrt_func <- function(numb1){
  return(sqrt(numb1))
}

#Test Square Root C
sqrt_func(4)
sqrt_func(5)
sqrt_func(8)



#Test Permutations
perm (16, 24)
perm (11, 5)