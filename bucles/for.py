for i in [2,1,5]:
    print(i)


smallest = None
print("Before:", smallest)
for itervar in [9, 41, 12, 3, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        #break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)