weight = float(input("Weight: "))
unite = input("enter lbs for pounds and kg for killograms: ")

if unite.lower() == "l":
    pound = weight * 0.45
    print(f"your weight is {pound} kg")
elif unite.lower() == "kg":
    killogram = weight / 0.45
    print(f"your weight is {killogram} lbs")
else:
    print("something went to wrong")