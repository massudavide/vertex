import random

# genera i coefficienti a,b,c
# input: h -> numero di funzioni da generare, length -> per determinare c
def get_coeffs(h,length):
    a_list = []
    b_list = []
    c = next_prime(length)
    # a_list = (random.sample(range(1, 256), h))
    # b_list = (random.sample(range(1, 256), h))
    a_list = (random.sample(range(1, c-1), h))
    b_list = (random.sample(range(1, c-1), h))
    coeffs = []
    coeffs.append(a_list)
    coeffs.append(b_list)
    coeffs.append(c)
    return (coeffs)

def is_prime(x):
    return all(x % i for i in range(2, x))

def next_prime(x):
    return min([a for a in range(x+1, 2*x) if is_prime(a)])
