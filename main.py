from mat.raymatrix import RayMatrix
import ray


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
        [4, 5, 7],
        [5, 3, 2],
        [9, 4, 6],
        [1, 3, 8]])
    
    
    results = ray.get(A.rank())
    print(results)

    ray.shutdown()

if __name__ == "__main__":
    main()

