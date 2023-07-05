from time import sleep
import ray

ray.init()

sleep(10)

@ray.remote
def cube(n):
    return n * n * n

@ray.remote
def factorial(n):
    tmp = 1
    
    for i in range(1, n):
        tmp *= i

    return tmp

futures = [factorial.remote(i) for i in range(20, 50)]

print(ray.get(futures))