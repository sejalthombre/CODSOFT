while True:
    choice= int(input("Enter a choice:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Mode\n6.Exit\n"))
    match choice:
        case 1:
            fn=int(input("enter the first number:"))
            sn=int(input("enter the second number:"))
            print("Addition =",fn+sn)
        case 2:
            fn=int(input("enter the first number:"))
            sn=int(input("enter the second number:"))
            print("Subtraction =",fn-sn)
        case 3:
            fn=int(input("enter the first number:"))
            sn=int(input("enter the second number:"))
            print("Multiplication =",fn*sn)
        case 4:
            fn=int(input("enter the first number:"))
            sn=int(input("enter the second number:"))
            print("Division =",fn/sn)
        case 5:
            fn=int(input("enter the first number:"))
            sn=int(input("enter the second number:"))
            print("Mode =",fn%sn)
        case 6:
            print("Exit")
            break
        case _:
            print("Invalid Input")
   
