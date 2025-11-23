History_file= "history.txt"
def show_history():
    file = open(History_file,"r")
    lines = file.readlines()
    if len(lines)==0:
        print("No History Found")

    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()
def clear_history():
    file = open(History_file,"w")
    file.close()
    print("History cleared")


def save_history(equation, result):
    file = open(History_file,"a")
    file.write(equation + "=" + str(result) + "\n")
    file.close()
def calculate(user_input):
    parts = user_input.split()
    if len(parts)!=3:
        print("Invalid Input. Use format: number operator number(2 + 4)")
        return
    num1 = int(parts[0])
    op = parts[1]
    num2 = int(parts[2])



    if op=="+":
        result=num1+num2
    elif op=="-":
        result=num1-num2
    elif op=="*":
        result=num1*num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2
    else:
        print("Invalid operator")
        return


    print("Result:", result)
    save_history(user_input, result)


def main():
    print("Welcome to a Simple Calculator(type history,clear,exit")
    while True:
        user_input = input("Type the equation:(+,-,*,/) or give command( history,exit,clear)")
        if user_input == "exit":
          print("Goodbye")
          break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)

main()
