'''
Optimized Prime Filer
'''

import math

def is_prime(n: int) -> bool:
    """
    Checks if a number is prime using the optimized O(sqrt(n)) approach.
    """
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime
    if n % 2 == 0:
        return False # Eliminate other even numbers early
        
    # We only need to check up to the square root of n
    # Any factor larger than the square root would have a corresponding 
    # factor smaller than the square root.
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2): # Check odd numbers only
        if n % i == 0:
            return False
    return True

def filter_primes(numbers: list[int]) -> list[int]:
    """
    Filters a list of integers and returns only the prime numbers.
    """
    return [num for num in numbers if is_prime(num)]

if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 13, 15, 17, 20, 23, 25, 29]
    
    primes = filter_primes(test_list)
    
    print(f"Original List: {test_list}")
    print(f"Prime Numbers: {primes}")