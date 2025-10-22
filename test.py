def isPrime(n):
   for i in range(2,n):
      if (n%i==0):
         return False
   return True

input = 54
output = input
while ( not isPrime(output)):
   output = output + 1

print("Next prime to ", input, "is", output, '.')
