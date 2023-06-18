import sys

from controller import Controller

bigbrain = Controller()

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "s" or sys.argv[1] == "-S":
            bigbrain.simulatieInterface()
    else:
        bigbrain.beginInterface()


if __name__ == "__main__":
    main()

