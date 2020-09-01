# Name: Quinten Cabo
# Student number: u789241

from os.path import isfile


def occupied(registry, day):
    if not isfile(registry):
        return -1
    else:
        number_of_guest = 0
        for guest in open(registry, 'r').readlines():
            guest = guest.strip().split(',')
            arrive = int(guest[1])
            leave = arrive + int(guest[2])
            if int(arrive <= day < leave):
                number_of_guest += 1
    return number_of_guest


def main():
    print(occupied("Registry1.txt", 10))  # 2
    print(occupied("Registry1.txt", 12))  # 3
    print(occupied("Registry1.txt", 19))  # 0
    print(occupied("Registry2.txt", 9))  # 6
    print(occupied("Registry2.txt", 0))  # 3
    print(occupied("Not_exist.txt", 9))  # -1


if __name__ == "__main__":
    main()
