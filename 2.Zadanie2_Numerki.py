import matplotlib.pyplot as plt
numbers = []

user_input = input("Podaj dowolną liczbę: ")

while user_input.isalpha()==False:
    
    user_input = input("Podaj dowolną liczbę: ")
    
    if user_input.isalpha() and user_input=="exit":
        for i in numbers:
            print(i)
        if len(numbers)>3:
            xAxis=list(range(len(numbers)))
            plt.bar(xAxis, numbers )
            plt.xticks(xAxis)
            plt.yticks(numbers)
            plt.show()
        break
    
    elif user_input.isalpha() and user_input!="exit":
        print("Podałeś {} liczb. Dalej się nie bawię".format(str(len(numbers))))
        break
    
    else:      
        numbers.append(float(user_input))
    
