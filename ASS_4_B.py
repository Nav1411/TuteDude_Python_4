def main():
    user_input = input("Enter some text: ")

    with open("output.txt", "a") as file:
        file.write(user_input + "\n")  

    additional_data= input("Enter the additional data to append.")
    
    with open("output.txt", "a") as file:
        file.write(additional_data  + "\n")

   
    with open("output.txt", "r") as file:
        content = file.read()
        print("Final content:", content)

if __name__ == "__main__":
    main()