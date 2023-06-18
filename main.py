import sys

from controller import Controller

bigbrain = Controller()

def main():
    "-s" in sys.argv
    if len(sys.argv) > 1:
        if "-s" in sys.argv or "-S" in sys.argv:
            print(sys.argv)
            bigbrain.simulatieInterface()
    else:
        bigbrain.beginInterface()


if __name__ == "__main__":
    main()

