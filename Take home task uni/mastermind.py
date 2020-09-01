# Name: Quinten Cabo
# Student number: u789241

def mastermind(secret, trial):
    x, o = '', ''
    for s, t in zip(secret, trial):
        if t == s:
            x += "X"
        elif t in secret:
            o += "O"
    return x + o


def main():
    print(mastermind("1234", "4321"))  # OOOO
    print(mastermind("1234", "5678"))  #
    print(mastermind("1234", "3524"))  # XOO
    print(mastermind("1234", "7254"))  # XX


if __name__ == "__main__":
    main()
