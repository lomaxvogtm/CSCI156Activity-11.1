__author__ = 'Madeleine'


Cars = {'Toyota': ['Prius'], 'Ford': ['Focus'], 'Honda': ['Accord'], 'Subaru': ['Impreza'], 'Mazda': ['Mazda3']}


#2
print(Cars['Honda'])
print('\n')

#3
print(Cars.get('Toyota'))
print('\n')

#4
for car in Cars:
    print(car)
print('\n')

#5
for car in Cars:
    if car == "pie":
        print("I like pie.")
    else:
        print("Pie is not a car!")
