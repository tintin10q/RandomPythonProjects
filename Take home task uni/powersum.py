# Name: Quinten Cabo
# Student number: u789241


def powersum(n):
    if n < 0:
        return -1
    return_value = 0
    for i in range(n + 1):
        return_value += 2 ** i
    return return_value


def main():
    print(powersum(3))
    print(powersum(0))
    print(powersum(-3))


if __name__ == "__main__":
    main()
