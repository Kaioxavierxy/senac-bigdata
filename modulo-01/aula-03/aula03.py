## Logic and conditions
haveCnh = True 
beenDrinking = False

allowedToDrive = haveCnh and not beenDrinking
print("The result of test is:", allowedToDrive)

buss = True
train = True
comeToClass = buss or train
print("The result of test is:", comeToClass)

## if elif else
transport = input("What's your transport type")
rained = True

if rained and transport == "moto":
    result = "Deu ruim mano"
elif not rained and transport == "moto":
    result = "Tô seco ;)"
else: 
    result = "Tô seco ;)"

print(result)