import random as rand

n = rand.randint(1,100)

steps = 2
factors = []

#find all factors of n
for i in range (2,n+1):
  if n%i == 0:
    factors.append(i)
    steps += 1
print("all factors for " + str(n) + " are")
print(factors)

#find just prime factors of n
remove_list = []
for j in factors:
  for k in factors:
    if k > j:
      if k%j == 0:
        remove_list.append(k)
prime_factors = [x for x in factors if x not in remove_list]

#find powers of all prime factors of n
powers_factors = []
for p in prime_factors:
  e = 1
  z = p
  mod = n%z
  while mod == 0 and n >= z:
    e += 1
    z = p
    z = z ** e
    mod = n%z
  e = e - 1
  z = p
  z = z**e
  powers_factors.append(z)

  
print("prime factors for " + str(n) + " are")
print(prime_factors)
print("powers of prime factors are")
print(powers_factors)
