#Telephone Digit Converter

#Password validation loop
password = ""
while password != "phone":
    password = input("Enter the password: ")

#Get valid number of letters (between 1 and 10)
max_letters = 0
while max_letters <= 0 or max_letters > 10:
    max_letters = int(input("Enter the maximum number of letters (1–10): "))
    if max_letters <= 0 or max_letters > 10:
        print("Invalid number. Please enter a number between 1 and 10.")

#Initialize counters
count = 0
valid_count = 0
invalid_count = 0

#Loop to get and process each letter
while count < max_letters:
    letter = input("Enter a letter: ")

    if letter == "A" or letter == "B" or letter == "C":
        print("Digit: 2")
        valid_count += 1
    elif letter == "D" or letter == "E" or letter == "F":
        print("Digit: 3")
        valid_count += 1
    elif letter == "G" or letter == "H" or letter == "I":
        print("Digit: 4")
        valid_count += 1
    elif letter == "J" or letter == "K" or letter == "L":
        print("Digit: 5")
        valid_count += 1
    elif letter == "M" or letter == "N" or letter == "O":
        print("Digit: 6")
        valid_count += 1
    elif letter == "P" or letter == "Q" or letter == "R" or letter == "S":
        print("Digit: 7")
        valid_count += 1
    elif letter == "T" or letter == "U" or letter == "V":
        print("Digit: 8")
        valid_count += 1
    elif letter == "W" or letter == "X" or letter == "Y" or letter == "Z":
        print("Digit: 9")
        valid_count += 1
    else:
        print("Invalid Character.")
        invalid_count += 1

    count += 1

#Final report
print("Total letters entered:", count)
print("Valid letters:", valid_count)
print("Invalid letters:", invalid_count)
