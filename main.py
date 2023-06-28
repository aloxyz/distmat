from mat.raymatrix import RayMatrix
import ray
import random


# def main():
#     counters = [rm.ParallelMatrix.remote([
#         [4, 5, 7],
#         [5, 3, 2],
#         [9, 4, 6],
#         [1, 3, 8]
#     ]) for i in range(4)]

#     futures = [c.range.remote() for c in counters]
#     print(ray.get(futures))


def main():
    ray.init()
    A = RayMatrix([
        [1, 2, 3],
        [4, 5, 7],
        [5, 3, 2],
        [9, 5, 6],
        [1, 3, 8]])
    
    B = RayMatrix([[random.randint(0, 9) for _ in range(9)] for _ in range(8)])

    print(B.rank())

    ray.shutdown()

if __name__ == "__main__":
    main()

