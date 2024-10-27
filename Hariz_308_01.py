import math
import time
import tracemalloc

# Function to check primes using the Sieve of Eratosthenes
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime

# Function to calculate Fibonacci numbers and count non-primes up to the 10^6 limit
def count_non_prime_fibonacci_in_range(n, m):
    # Precompute primes up to 10^6
    max_limit = 10**6
    prime_check = sieve_of_eratosthenes(max_limit)
    
    # Initialize Fibonacci numbers
    a, b = 0, 1
    non_prime_count = 0
    current_position = 2  # Fibonacci position (since a=0 and b=1 are already initialized)
    
    # Iterate through Fibonacci numbers, but stop once Fibonacci exceeds max_limit
    while b <= max_limit and current_position <= m:
        if current_position >= n:
            # Check if the Fibonacci number is non-prime
            if not prime_check[b]:
                non_prime_count += 1
        
        # Move to the next Fibonacci number
        a, b = b, a + b
        current_position += 1
    
    return non_prime_count

# Input with user prompts
print("Masukkan dua bilangan bulat n dan m (0 ≤ n ≤ m ≤ 10^6):")
n, m = map(int, input("Input n dan m (dipisahkan dengan spasi): ").split())

# Start measuring execution time
start_time = time.time()

# Output the count of non-prime Fibonacci numbers in the range
result = count_non_prime_fibonacci_in_range(n, m)
print(f"Jumlah bilangan Fibonacci non-prime dari posisi {n} hingga {m}: {result}")

# Measure execution time
execution_time = time.time() - start_time
print(f"Waktu eksekusi: {execution_time:.4f} detik")

# Start measuring memory usage
tracemalloc.start()

# Calculate and display memory usage after the main computation
current, peak = tracemalloc.get_traced_memory()
print(f"Penggunaan memori saat ini: {current / 10**6:.4f} MB; Penggunaan memori puncak: {peak / 10**6:.4f} MB")

# Stop tracing memory
tracemalloc.stop()
