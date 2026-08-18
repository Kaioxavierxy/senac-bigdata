def fibonaci(): 
    list = [1]
    number1 = 1
    for i in range(10):
      if(len(list) > 1):
        listLenght = len(list)
        lastNumber = list[listLenght - 1]
        listLenght2 = list[listLenght - 2]
        NumbersSum = lastNumber + listLenght2
        list.append(NumbersSum)
      else:
        list.append(number1)
    
    print(list)

fibonaci()