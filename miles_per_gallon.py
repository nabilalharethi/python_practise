#MPG = Miles driven / Gallons of gas used 

Distance = (input("Enter the distance driven: "))

Gallons = (input("Enter the amount of  gallons used: "))

MPG  = int (Distance) / int(Gallons)

print(f"A car traviling at {Distance} using  {Gallons}")
print(f"uses {MPG:.2f} per gallon ")
