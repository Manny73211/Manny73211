num1 = input ("first number: ")
num2 = input ("second number: ")
print("""
modes:
1: addition
2: subtraction
3: multiplication
""")
mode = input ("what is the mode: ")

if mode=="1":
    ans = int(num1) + int(num2)
    print ("answer: {0}" .format (str(ans)))

elif mode=="2":
    ans = int(num1) - int(num2)
    print ("answer: {0}" .format (str(ans)))

elif mode=="3":
    ans = int(num1) * int(num2)
    print ("answer: {0}" .format (str(ans)))

else:
    print ("not a valid mode.")