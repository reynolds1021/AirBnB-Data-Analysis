
def areacalculator():
    _input_ = input("Enter the shape: ")
    area = 0 #Initialize area at 0 
    circumfrence = 0 #Initialize circumfrence 
    pi = 3.141592654
    if _input_ == "Square":
        side = int(input("Enter the value of side: "))
        area = area + (side ** 2)
    elif _input_ == "Circle":
        radius = int(input("Enter the value of radius: "))
        circumfrence = area + (2 * pi * radius)
    elif _input_ == "Rectangle":
        length = int(input("Enter the value of length: "))
        width = int(input("Enter the value of length: "))
        area = area + (length * width)
    elif _input_ == "Triangle":
        base = int(input("Enter the value of base: "))
        height = int(input("Enter the value of height: "))
        area = area +(0.5 * base * height)
    else:
        print ("Select a valid shape")
    print ("%.2f" % area)

areacalculator()
