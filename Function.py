import os

def answer(text):
    while (True):
        answer = input(text)
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Unknown sign")

def file_exists_ft1(path, type):
    while(True):
        answer = input("Enter person " + type)
        try:
            dir = os.path.join(path, answer)
            if os.path.exists(dir):
                return answer
            else:
                return False
        except ValueError:
            print("ValueError")

def file_exists_ft2(path, name):
    while(True):
        dir = os.path.join(path, name)
        if os.path.exists(dir):
            return dir
        else:
            return False

def find_person(path):
    name = file_exists_ft1(path, "name")
    if not name:
        print("Person doesn't exist")
        return False
    else:
        path = os.path.join(path, name)
        os.chdir(path)

        surname = file_exists_ft1(path, "surname")
        if not surname:
            print("Person doesn't exist")
            return False
        else:
            path = os.path.join(path, surname)
            os.chdir(path)

            pesel = file_exists_ft1(path, "pesel")
            if not pesel:
                print("Person doesn't exist")
                return False
            else:
                person = list()
                person.append(name)
                person.append(surname)
                person.append(pesel)
                return person