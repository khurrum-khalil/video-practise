#list functions
lucky_numbers=[,4,8,5,2,3,4,8]
friends=['khurram','ali','khan','owesome','lol']
print(friends)

#extend function
friends.extend(lucky_number)
print(friends)

#adding elements
friends.apprnd('creed')
print(friends) #adding elements

#insert on any specific location
friends.insert(1, 'khalil')
print(friends)

#remove
friends.remove('khurram')
print(friends)

#pop
friends.pop()
print(friends) #remove the last element

#indexing
print(friends.index('ali'))

#count
print(friends.count('jim'))

#assencing order
friends.sort()
print(friends)

#reverse
lucky_numbers.reverse()
print(lucky_numbers)

#to clear list
friends.clear()
print(friends)
