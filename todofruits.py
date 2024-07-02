#Ask user to enter number of fruits and display all fruits.
fruits= []
total_fruit=int(input("Enter total no of fruits: "))
for i in range(1,total_fruit+1):
    fruit=input(f"Enter fruit{i}: ")
    fruits.append(fruit)
print("\n...\n")
print("All fruits are: ")   

#Display all results
for fruit in fruits:
    print(fruit)