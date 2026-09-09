#PGR107
#Kandidatnr: 100
#Question 4


def isPalidrome():
    while True:
        user_input = input("Enter a string to check if it's a palidrome: ")
        user_input_clean = ''.join(char.lower() for char in user_input if char.isalpha())

        if not user_input_clean:
            print("You entered an empty or invalid string. Please enter a valid word or sentence.")
            continue
    
        if user_input_clean == user_input_clean[::-1]:
            print(f"{user_input_clean} is a palidrome.")
        else:
            print(f"{user_input_clean} is not a palidrome.")
        break

isPalidrome()
    