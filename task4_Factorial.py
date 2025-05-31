# Creating a function
def factorial(n):
  if n==0:
    return 1
  else:
    return n*factorial(n-1)
  
# test of factorial
print (f"factorial of 5 is {factorial(5)}")
print (f"factorial of 10 is {factorial(10)}")
print (f"factorial of 15 is {factorial(15)}")
print (f"factorial of 50 is {factorial(50)}")