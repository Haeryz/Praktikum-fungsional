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

# Function to calculate Fibonacci numbers and count even Fibonacci numbers in a given range
def count_even_fibonacci_in_range(n, m):
    # Precompute primes up to 10^6 (can also just check for evenness directly)
    max_limit = 10**6
    prime_check = sieve_of_eratosthenes(max_limit)
    
    # Initialize Fibonacci numbers
    a, b = 0, 1
    even_count = 0
    current_position = 0  # Fibonacci position
    
    # Iterate through Fibonacci numbers until the maximum position
    while current_position <= m:
        # Check if the Fibonacci number is even
        if b % 2 == 0 and current_position >= n:
            even_count += 1
        
        # Move to the next Fibonacci number
        a, b = b, a + b
        current_position += 1
        
        # Stop if we exceed max_limit
        if b > max_limit:
            break
    
    return even_count

# Input with user prompts
print("Masukkan dua bilangan bulat n dan m (0 ≤ n ≤ m ≤ 10^6):")
n, m = map(int, input("Input n dan m (dipisahkan dengan spasi): ").split())

# Start measuring execution time
start_time = time.time()

# Output the count of even Fibonacci numbers in the range
result = count_even_fibonacci_in_range(n, m)
print(f"Jumlah bilangan Fibonacci genap dari posisi {n} hingga {m}: {result}")

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
