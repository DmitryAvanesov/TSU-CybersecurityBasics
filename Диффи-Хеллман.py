q = 1357
g = 10

for a in range(1000):
  for b in range(1000):
    if g**a % q == 419 and g**b % q == 34 and g**(a * b) % q == 33:
      print(f'{a}, {b}')