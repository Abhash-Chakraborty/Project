import pickle
from datetime import datetime
import subprocess


def readlendbook():
    w = []
    with open("assets\\files\\lendbook.dat", "rb") as k:
        try:
            l = []
            while True:
                z = pickle.load(k)
                l.append(z)
                w = l
        except EOFError:
            pass
    return w


def suggestion():
    w = []
    with open("assets\\files\\Suggestion.dat", "rb") as k:
        try:
            l = []
            while True:
                z = pickle.load(k)
                l.append(z)
                w = l
        except EOFError:
            pass
    return w


def lendbookdet():
    w = []
    with open("assets\\files\\lendbookdet.dat", "rb") as k:
        try:
            l = []
            while True:
                z = pickle.load(k)
                l.append(z)
                w = l
        except EOFError:
            pass
    return w


def libbookdet():
    w = []
    with open("assets\\files\\libbookdet.dat", "rb") as k:
        try:
            l = []
            while True:
                z = pickle.load(k)
                l.append(z)
                w = l
        except EOFError:
            pass
    return w


def readbookdet():
    w = []
    with open("assets\\files\\readbookdet.dat", "rb") as k:
        try:
            l = []
            while True:
                z = pickle.load(k)
                l.append(z)
                w = l
        except EOFError:
            pass
    return w


def readbook():
    name = "Abhash Chakraborty"
    phone = 9632587415
    date = str(datetime.now())
    bookid = input("Enter Book Id: ")
    s = 0
    with open("assets\\files\\booklist.dat", "rb") as f:
        try:
            while True:
                k = pickle.load(f)
                if k[0] == bookid and k[5] == "Yes":
                    subprocess.Popen([f"assets\\books\\{bookid}.pdf"], shell=True)
                    l = [k[0], k[1], k[2], name, phone, date[0:10], date[11:19]]
                    with open("assets\\files\\readbookdet.dat", "ab") as t:
                        pickle.dump(l, t)
                    s += 1
        except EOFError:
            if s == 0:
                print("No book found")
