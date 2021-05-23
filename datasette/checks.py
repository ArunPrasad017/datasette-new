import os
from datetime import datetime


def fn_test(nums):
    print(os.getcwd())
    print(datetime.time())
    return sorted(nums)


def main():
    nums = [3, 4, 5, 9, 1, 2]
    fn_test(nums)


if __name__ == "__main__":
    main()
