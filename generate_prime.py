inpt = input('Enter a positive integer:')
try:
  val = int(inpt)

except:
  exit('Error in casting to integer.')

for i in range(2, val + 1):
  j = int(i / 2)
  is_prime = True
  for k in range(2, j + 1):
    if divmod(i, k)[1] == 0:
      # this is not prime
      is_prime = False
      break
  
  if is_prime :
    print(i)