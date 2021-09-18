import pickle
import random


def referenceno():
    with open("assets\\files\\lendbookdet.dat", "rb") as f:
        a = random.randint(10000000000, 99999999999)
        try:
            while True:
                l = pickle.load(f)
                if a == l[11]:
                    a += 1
                else:
                    pass
        except EOFError:
            return a


def bookid():
    with open("assets\\files\\booklist.dat", "rb") as f:
        a = random.randint(1000000, 9999999)
        try:
            while True:
                l = pickle.load(f)
                if f"#{a}" == l[0]:
                    a += 1
                else:
                    pass
        except EOFError:
            return f"#{a}"
