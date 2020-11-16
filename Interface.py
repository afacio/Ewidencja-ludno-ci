import Container
import Function
import Tree
import Pesel
import os

class Interface():
    def __init__(self):
        self._MENU = "\nAvailable commands:" \
                     "\n1 - add new person\n2 - delete person\n3 - find person" \
                     "\n4 - show all content" \
                     "\n5 - del all data file\n6 - exit\n"
        self._filename = "PESEL_storage.txt"
        self._program_path = os.getcwd()
        self._home_path = os.path.join(self._program_path, "main container")
        self._current_path = self._home_path

        if not os.path.isdir(self._home_path):
            print("main file doesn't exist")
            Container.create_ft2("main container")
            f = open(self._filename, "w")
            f.close()
        else:
            print("main file is exists")
            if len(os.listdir('./main container')):
                print("main file isn't empty")
            else:
                print("main file is empty")
                f = open(self._filename, "w")
                f.close()

        os.chdir(self._home_path)

    def choice(self):
        program = True
        while (program):
            choice = input(self._MENU)

            if choice == '1':
                pesel = Pesel.add_pesel()
                if pesel:
                    self._current_path = Container.create_ft1(self._current_path, "name")
                    self._current_path = Container.create_ft1(self._current_path, "surname")
                    Container.create_ft2(pesel)
                    os.chdir(self._home_path)
                    self._current_path = self._home_path

            elif choice == '2':
                person = Function.find_person(self._current_path)
                if person:
                    name = person[0]
                    surname = person[1]
                    pesel = person[2]
                    self._current_path = os.path.join(self._current_path, name, surname)
                    if Function.answer("Do You want delete your person? [y/n]"):
                        os.chdir(self._home_path)
                        with open("../" + self._filename, "r") as f:
                            lines = f.readlines()
                        with open("../" + self._filename, "w") as f:
                            for line in lines:
                                if line.strip("\n") != pesel:
                                    f.write(line)
                            f.close()

                        os.chdir(self._current_path)
                        os.path.join(self._current_path, pesel)
                        Container.remove_item(os.path.join(self._current_path, pesel))
                        self._current_path = os.path.normpath(os.getcwd() + os.sep + os.pardir)
                        os.chdir(self._current_path)
                        if len(os.listdir(os.path.join(self._current_path, surname))) == 0:
                            Container.remove_item(os.path.join(self._current_path, surname))
                            self._current_path = os.path.normpath(os.getcwd() + os.sep + os.pardir)
                            os.chdir(self._current_path)
                            if len(os.listdir(os.path.join(self._current_path, name))) == 0:
                                Container.remove_item(os.path.join(self._current_path, name))

            elif choice == '3':
                person = Function.find_person(self._current_path)
                if person:
                    name = person[0]
                    surname = person[1]
                    pesel = person[2]
                    print("\nSearch process  - success")
                    print(name + " " + surname + ": " + pesel + " | EXIST ")
                    os.chdir(self._home_path)
                    self._current_path = self._home_path

            elif choice == '4':
                paths = Tree.DisplayablePath.make_tree(self._home_path)
                for path in paths:
                    print(path.displayable())

            elif choice == '5':
                if Function.answer("Do You want delete your data? [y/n]"):
                    os.chdir(self._program_path)
                    if Function.file_exists_ft2(self._program_path, self._filename):
                        os.remove(self._filename)
                    Container.remove_item(self._home_path)
                    program = False

            elif choice == '6':
                if Function.answer("Do You want close program? [y/n]"):
                    program = False

            else:
                print("Unknown command: " + choice)

