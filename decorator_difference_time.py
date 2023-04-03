from time import time


def decorator(func):
    def wrapper(*args, **kwargs):
        time_start = time()
        difference = func(*args, **kwargs)
        print(time() - time_start)

        return difference

    return wrapper


@decorator
def main():
    return


main()
