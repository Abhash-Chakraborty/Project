import pickle
import datetime
import os


def returnlend(self, name, phone):
    with open("assets\\files\\lendbookdet.dat", "rb") as f:
        k = open("assets\\files\\lendbook.dat", "rb")
        s = 0
        c = 0
        name = name.upper()
        retbook = []
        book = []
        try:
            while True:
                l = pickle.load(f)
                if self == l[12]:
                    s += 1
                    try:
                        while True:
                            x = pickle.load(k)
                            if l[0] == x[0]:
                                c += 1
                                print(
                                    f"_________________________________________________________________________________"
                                    f"________________________________________________________________")
                                print(
                                    f"Book I.D.            Author                         "
                                    f"Book Name                                       ")
                                print(
                                    f"_________________________________________________________________________________"
                                    f"________________________________________________________________")
                                print(f"{x[0]}{' ' * (10 - len(x[0]))}           {x[2]}{' ' * (30 - len(l[2]))}{x[1]}")

                                print(
                                    f"_________________________________________________________________________________"
                                    f"________________________________________________________________")

                                print("Do you want to continue[y/n]?")
                                a = input()
                                if a == "y" or a == "Y":
                                    if l[0] == x[0]:
                                        retbook.append(x[0])
                                        retbook.append(x[1])
                                        retbook.append(x[2])
                                        retbook.append(x[3])
                                        retbook.append(x[4])
                                        retbook.append(x[5])
                                        retbook.append(name)
                                        retbook.append(l[7])
                                        retbook.append(phone)
                                        retbook.append(l[9])
                                        retbook.append(datetime.date.today())
                                        retbook.append('Return')
                                        retbook.append(l[12])
                                        with open("assets\\files\\lendbookdet.dat", "ab") as r:
                                            pickle.dump(retbook, r)
                                        s += 1
                                        if l[9] < datetime.date.today():
                                            print("You are late.")
                                        print("Operation Completed.\nThank you for visiting our library.")
                                else:
                                    book.append(x)
                    except EOFError:
                        pass



        except EOFError:
            if c==0:
                print("Book is already returned")
            if s == 0:
                print("No book is assigned with is reference number")
            with open("assets\\files\\temp.dat", "wb") as k:
                for i in book:
                    pickle.dump(i, k)
            os.remove("assets\\files\\lendbook.dat")
            os.rename("assets\\files\\temp.dat", "assets\\files\\lendbook.dat")


def lendrenew(self):
    with open("assets\\files\\lendbookdet.dat", "rb") as f:
        k = open("assets\\files\\lendbook.dat", "rb")
        s = 0
        c = 0
        retbook = []
        try:
            while True:
                l = pickle.load(f)
                if self == l[12]:
                    s += 1
                    try:
                        while True:
                            x = pickle.load(k)
                            if l[0] == x[0]:
                                c += 1
                                print(
                                    f"_________________________________________________________________________________"
                                    f"________________________________________________________________")
                                print(
                                    f"Book I.D.            Author                         "
                                    f"Book Name                                       ")
                                print(
                                    f"_________________________________________________________________________________"
                                    f"________________________________________________________________")
                                print(f"{x[0]}{' ' * (10 - len(x[0]))}           {x[2]}{' ' * (30 - len(l[2]))}{x[1]}")

                                print(
                                    f"_________________________________________________________________________________"
                                    f"________________________________________________________________")

                                print("Do you want to continue[y/n]?")
                                a = input()
                                if a == "y" or a == "Y":
                                    retbook.append(x[0])
                                    retbook.append(x[1])
                                    retbook.append(x[2])
                                    retbook.append(x[3])
                                    retbook.append(x[4])
                                    retbook.append(l[5])
                                    retbook.append(l[6])
                                    retbook.append(l[7])
                                    retbook.append(l[8])
                                    retbook.append(l[9])
                                    retbook.append(datetime.date.today() + datetime.timedelta(days=7))
                                    retbook.append('Renew')
                                    retbook.append(l[12])
                                    with open("assets\\files\\lendbookdet.dat", "ab") as r:
                                        pickle.dump(retbook, r)
                                    if l[9] < datetime.date.today():
                                        print("You are late.")
                                    print("Operation Completed")
                                    print(
                                        f"Please renew the book before {datetime.date.today() + datetime.timedelta(days=7)}. Your reference number is {l[12]}.")
                                else:
                                    break
                    except EOFError:
                        pass

                    if c == 0:
                        print("Book is already returned")
        except EOFError:
            if s == 0:
                print("No book is assigned with is reference number")
