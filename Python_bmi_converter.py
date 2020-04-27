import decimal


weight = decimal.Decimal(input("Enter your weight in KG: "))
height = decimal.Decimal(input("Enter your height in meter: "))
bmi = weight / (height * height)
print("Your bmi is {the_bmi:1.4}".format(the_bmi=bmi))

if bmi <= 18.3:
    print("Bmi condition: [Too low] :(")

elif bmi <= 24.9:
    print("Bmi condition: [Healthy] :D")

elif bmi <= 25.9:
    print("Bmi condition: [just a little Overweight/kinda healthy] :)")

elif bmi <= 30 or bmi >= 30:
    print("Bmi condition: [warning! Too much overweight] :(")
