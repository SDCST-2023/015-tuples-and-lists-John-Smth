#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
print("People:Gary, Barry, Terry, Mary, Jerry, Cranberry")
print("Gary, Barry, Terry, Mary, Jerry, Cranberry")
people = ["Gary", "Barry", "Terry", "Mary", "Jerry", "Cranberry"]

FW = input("Enter The Disliked Individual Please:")
DW = input("Enter Your favourite person:")

if FW in people:
    Num = people.index(FW)
    people.insert(Num,DW)
    people.remove(FW)
    print(people)
    
