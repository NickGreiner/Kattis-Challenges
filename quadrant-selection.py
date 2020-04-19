coordinateX = int(input())
coordinateY = int(input())

if coordinateX > 0 and coordinateY > 0:
    print(1)

elif coordinateX < 0 and coordinateY > 0:
    print(2)

elif coordinateX < 0 and coordinateY < 0:
    print(3)

elif coordinateX > 0 and coordinateY < 0:
    print(4)

else:
    print("Error")
