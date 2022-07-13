# Fibonacci Series
def fibonacci_seq(number):
   if number <= 1:
       return number
   else:
       return(fibonacci_seq(number-1) + fibonacci_seq(number-2))