#Hope Crisafi
#Lab 7
#5/11/21
#Knut Tyler Olson

#NJW 8/10

import urllib.request

#Problem 1

fileName = 'labWk7.txt'

myFile = open(fileName,'w')

#NJW Do we need this variable?
entry = 0

for num in range(10):
    num = input('enter a number: ')
    myFile.write(num + '\n')

myFile.close()



#Part 2

myFile = open(fileName, 'r')

data = myFile.read()
print('data is', data)

#NJW This code crashes! (-2)
#NJW BECAUSE you SHOULD have data.split() below
#NJW I've commented it out so that the rest runs

#NJW Your code:
#listA = data.split

#NJW My fix:
listA = data.split()

listB = []

for num in listA:
    number = int(num)
    listB.append(number)

print(listA)
print(listB)

#Part 3

print('the min value is: ',(min(listB)))
print('the max value is: ',(max(listB)))
print('the average value is: ',(sum(listB)/len(listB)))

#NJW myFileList NOT defined.
#print(myFileList)


myFile.close()


#Part 4

parasitesFile = open('parasites.txt','r')
data = parasitesFile.read()
print(data)

subsequence = input('enter a subsequence: ')
count = 0
subsequenceLength = len(subsequence)

index = data.find(subsequence)

if index != -1:
    print('found at index: ',index)
else:
    print('not found')



greaterThanSymbol = data.rfind('>',0,index)
#start search at 0, end at input index

newLineFind = data.find('\n',greaterThanSymbol)
#look forwards for \n

print(data[greaterThanSymbol:newLineFind])


#Part 5

webName = 'http://cs.union.edu/CSDEPT/staff/'

connection = urllib.request.urlopen(webName)
data = str(connection.read())

startEmail = data.find('mailto:')
endEmail = data.find('.edu', startEmail)
fullEmail = data[startEmail + 7: endEmail + 4]

print('the first email is: ',fullEmail)


while startEmail != -1:
    startEmail = data.find('mailto:',startEmail + 1)
    endEmail = data.find('edu', startEmail)
    fullEmail = data[startEmail + 7:endEmail + 3]
    print('email is: ', fullEmail)

connection.close()



#if input found
#find method, search document for input
#locate the closest > above it
#print from index 1 to '\n' on that line
#convert sentence into a list
#find method 
