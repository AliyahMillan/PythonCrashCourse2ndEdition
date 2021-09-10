"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
8 September 2021
"""
#Done with help with Professor Graham
MAX_PRIMES = 1000
primes = list(x for x in range(2, MAX_PRIMES+1))
for current_prime in primes:
  for prime_multiple in range(current_prime*2, MAX_PRIMES*2, current_prime):

    #print(prime_multiple)
    if prime_multiple in primes:
      primes.remove(prime_multiple)

print(primes)
print("Length: ",len(primes))
