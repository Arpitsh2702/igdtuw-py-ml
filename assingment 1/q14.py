#Write a program that reads multiple lines of input from the user until the enter an empty line, then prints all the lines.
def main():
    lines =  []
    print("enetr your lines of text(press enetr to finish):")
    while True :
        line = input()
        if line =="":
            break
        lines.append(line)

    print("\n you entered/:")
    for line in lines:
        print(line)

if __name__=="__main__":
    main()       

    
