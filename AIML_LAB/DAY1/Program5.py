import time
def fibonacci(n):
    if(n==0 or n==1):
        return n
    else:
        return (fibonacci(n-2)+fibonacci(n-1))
n=int(input("Enter the value of n: "))
start_time= time.perf_counter()
if n == 0:
    fib_value = 0
elif n == 1:
    fib_value = 1
else:
    a, b = 0, 1
    for i in range(2, n+1):  # start from 2
        fib_value = a + b
        a = b
        b = fib_value
print(f"Final value by iterative approach: {fib_value}")
end_time = time.perf_counter()
execution_time= end_time - start_time
print(f"Execution time for iterative approach: {execution_time}")
start_time = time.perf_counter()
fib_value=fibonacci(n)
print(f"Final value by recursive approach: {fib_value}")
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time for recursive approach: {execution_time}")
