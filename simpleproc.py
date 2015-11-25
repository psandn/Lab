import csv
import matplotlib.pyplot as plt

new_liste = []
calc_liste = []

with open('testsimple.csv', newline='') as f:
    data = csv.reader(f)
    for item in data:
        for row in item:
            new_liste.append(float(row))  #here we build the list and converts the strings to floats


for nitem in new_liste:
    nitem = nitem / 2  #here we do some calculations, but the are not saved to the list
    print(nitem)
    
print (calc_liste)
for citem in new_liste:
    calc_liste.append(citem * 3)  #we are adding calculations to a new list
print (calc_liste)


plt.plot(calc_liste)
plt.plot(new_liste)
#plt.ylabel('some numbers')
plt.show()    
