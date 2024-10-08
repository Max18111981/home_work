# Добавьте к первому заданию возможность передавать
# границы диапазона для поиска всех простых чисел.


import time
from functools import wraps


def timer_decorator(func):
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"Finished in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer_decorator
def get_primes(start, end):
    primes = []
    for possiblePrime in range(start, end + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes


start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

primes = get_primes(start_range, end_range)
print("Prime numbers:", primes)