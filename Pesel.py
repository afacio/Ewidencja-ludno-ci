def add_pesel():
    f = open("../PESEL_storage.txt", "r")
    while(True):
        answer = input("Enter person pesel number")
        try:
            pesel = int(answer)
            for line in f:
                if answer in line:
                    print("Person of this pesel exist !")
                    f.close()
                    return False
            f = open('../PESEL_storage.txt', 'a')
            f.write(answer + "\n")
            f.close()
            return answer
        except ValueError:
            print("Enter a value of type int")