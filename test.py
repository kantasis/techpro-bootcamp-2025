def isPrime(n):
   for i in range(2,n):
      if (n%i==0):
         return False
   return True

input_number = 57

temporary_number = input_number
while ( not isPrime(temporary_number)):
   for i in range(2,temporary_number):
      if (temporary_number % i == 0): 
         print("Prime factor: ", i)
         temporary_number = temporary_number // i 
         break
print("Prime factor: ", temporary_number)

