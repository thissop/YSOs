from itertools import permutations

#Get permutations of numbers
numbPerms = [''.join(p) for p in permutations('234')]

#Get Permutations of operators
operatorPerms1 = [''.join(p) for p in permutations('+-*/%')]

#Get three character operator strings from original 5P5 permutation. 
opPerms2 = []
for item in operatorPerms1:
    opPerms2.append(item[0:3])
    opPerms2.append(item[1:4])
    opPerms2.append(item[2:5])

#Get rid of duplicates, leving you with a 5P3 permutation set of operations
opPerms2 = list(set(opPerms2))

#create final commands, adds decimals for java to calculate them
finalcommands = []
for item in numbPerms:
    for elem in opPerms2:
        finalcommands.append(item[0]+'.0'+elem[0]+item[1]+'.0')
        finalcommands.append(item[0]+'.0'+elem[0]+item[1]+'.0'+elem[1]+item[2]+'.0')
#uses eval to find how many unique outputs...bru java doesn't have an evaulate
#string as literal function like python. 
results = []
for elem in finalcommands:
    results.append(round((eval(elem)),3))
results = list(set(results))

#Generates list of java commands
javacommands = []
for elem in finalcommands:
    elem = 'System.out.println("'+elem+'="+('+elem+'));'
    javacommands.append(elem)
#gets rid of duplicates
finalcommands = list(set(finalcommands))
javacommands = list(set(javacommands))
#print out operator permutations list and uniqueresults
def report():
    print('Number of unique expressions: '+str(len(finalcommands)))
    print('Unique expressions:\n',finalcommands)
    print('Number of unique results: '+str(len(results)))
    print('Unique results:\n',results)
#record java commands to text file 
def record():
    with open('/home/thaddaeus/FMU/compsci/javaCommands.txt','w') as f:
        for elem in javacommands:
            f.write(elem+'\n')
record()




