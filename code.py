import matplotlib.pyplot as plt
import math

def prime(n):
    if n % 2 == 0:
        return False  # number is not prime
    iterations = int(math.sqrt(n)) + 1
    for i in range(3, iterations, 2):
        if n % i == 0:
            return False
    return True


primes = []
difference_between_primes = []
x = []
y = []
counter = 1
for i in range(3, 1000, 1):
    if prime(i):
        primes.append(i)
        x.append(i)
        difference_between_primes.append(counter)
        counter = 0
    else:
        counter += 1
print (difference_between_primes)
y = difference_between_primes
"""
for i in range(len(y)):
    x.append(i)
"""
# plotting points as a scatter plot
plt.scatter(x, y, label="", color="green", marker="*", s=30)

plt.ylabel('difference between the last prime and the prine itself')
plt.xlabel('numbers')
plt.title('difference between sequential primes')
plt.legend()

# function to show the plot
plt.show()
