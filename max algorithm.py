ints = []
f = int(input("number of intergers: "))
bools = []
for t in range(f):
    bools.append(False)
while len(ints)<f:
    ints.append(int(input("input numbers until you stop seeing this message: ")))

while all(bools)!=True:
    for i in range(len(ints)):
        if i == 0:
            if ints[i] == ints[i+1]:
                bools[i]=True
            else:
                bools[i]=False
                if ints[i]<ints[i+1]:
                    ints[i] = ints[i]+1
        elif i < (len(ints)-2):
            if ints[i] == ints[i+1]:
                if ints[i] == ints[i-1]:
                    bools[i]=True
                elif ints[i]<ints[i-1] or ints[i]<ints[i+1]:
                    bools[i]=False
                    ints[i] = ints[i]+1
                else:
                    bools[i]=False
            elif ints[i]<ints[i-1] or ints[i]<ints[i+1]:
                bools[i]=False
                ints[i] = ints[i]+1
            else:
                bools[i]=True
        else:
            if ints[i]==ints[i-1]:
                bools[i]=True
            elif ints[i]<ints[i-1]:
                bools[i]=False
                ints[i] = ints[i]+1
    print(ints)
print("done")
