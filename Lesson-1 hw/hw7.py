salary=input('Enter ur salary: ')
credit=input('Enter ur credit payment: ')
utilities=input('Enter ur utilities: ')
remains=int(salary)-(int(utilities)+int(credit))
print(f'Ur remain is: {remains}')