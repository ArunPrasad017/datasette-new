import os


def fn_test(nums: list) -> list:
    print(os.getcwd())
    return sorted(nums)


def main() -> list:
    nums = [3, 4, 5, 9, 1, 2]
    return fn_test(nums)


if __name__ == "__main__":
    main()
