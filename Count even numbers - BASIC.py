# method 1

count = 0
for i in range(1,10,2):
    if i!=9:
        count = count + 1
        print(i+1)
    else:
        print(f"We have {count} numbers")

# method 2

count = 0
for i in range(1, 10):
    if i != 10:
        if i % 2 == 0:
            count = count + 1 
            print(i)
        else:
            continue

print(f"we have {count} numbers")