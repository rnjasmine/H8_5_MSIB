# recursive function (function yang memanggil dirinya sendiri)
def fact(n):
    return 1 if n == 1 else n * fact(n - 1)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:   # jika argumen > 1
        print(sys.argv[0])
        print(fact(int(sys.argv[1])))   