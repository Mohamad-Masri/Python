def read():
    count = 0
    with open("myfile.txt") as fp: 
        Lines = fp.readlines() 
    for line in Lines: 
        count += 1
        print(count, ".", line.strip())
        main()

def write():
    with open("myfile.txt", "w") as fp:
        TextToWrite = input("type a text to write : ")
        fp.writelines(TextToWrite)
        main()
        
def main():
    print("-----------------------------------")
    print("1. Read from file.")
    print("2. write inside a file")
    chose = int(input("chose a number : "))
    if chose == 1:
        read()
    else :
        write()

main()
