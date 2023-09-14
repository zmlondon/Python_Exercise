import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
#input name string split function
names = names_string.split(", ")

num_person = len(names)
random_choice = random.randint(0, num_person - 1)
person_pay_bill = names[random_choice]
print(f"{person_pay_bill}")