# Name: Quinten Cabo
# Student number: u789241


def stopwatch(wlist):
    if len(wlist) == 1:
        return int(wlist[0])
    else:
        wlist.append(lcm(wlist[0], wlist[1]))
        wlist = wlist[2:]
        return stopwatch(wlist)


def hcf(x, y):
    x, y = min(x, y), max(x, y)
    if y % x == 0:
        return x
    else:
        return hcf(y % x, x)


def lcm(x, y):
    return x * y / hcf(x, y)


def main():
    print(stopwatch([10]))  # 10
    print(stopwatch([10, 12, 15]))  # 60
    print(stopwatch([15, 12, 10]))  # 60
    print(stopwatch([15, 12, 10, 6, 24, 40]))  # 120
    print(stopwatch([19, 37, 101, 7, 23]))  # 11431483


if __name__ == "__main__":
    main()
