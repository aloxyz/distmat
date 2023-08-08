import ray

def run():
    ray.init()

    ray.shutdown()


if __name__ == "__main__":
    run()
