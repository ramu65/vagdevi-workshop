x=[30,20,40,20,60,80,30,20,40]

x.sort()

i = 1

y=x

while True:

    if i==len(y):

         break

    elif y[i-1]==y[i]:

        x.pop(i-1)

    else:
    
        i+=2

print(printing the line at x)
print(prnting te next line to x)
print(prnting the next line to yy)
print(prnting the next line to xx)