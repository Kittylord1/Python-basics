def mul_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list

#print(mul_by2([2, 4, 6]))

#MAP

my_list = [2, 4, 5, 6]
my_list2 = [3,7,8,9]
def mul_by2(item):

     return item * 2


print(list(map(mul_by2, my_list)))



#FILTER

def only_odd(item):

     return item % 2 != 0


print(list(filter(only_odd, my_list)))

#ZIP

new_list = (list(zip(my_list,my_list2)))
print(new_list)

#Lambda function

print(list(map(lambda item : item * 2, my_list)))

new_list2 = [(2,4),(3,6),(3,56),(3,5)]

print(list(map(lambda item: item**2,my_list)))
new_list2.sort(key = lambda x: x[1])
print(new_list2)

#List Comprehensions

list1 = [char for char in 'HELLO']
print(list1)

list2 = [num for num in range (0,100)]
print(list2)

list3 = [num*2 for num in range(0,100)]
print(list3)

list4 = [num*2 for num in range(0,100) if num*2 != 0 ]
print(list4)

#Dictionary Comprehension

dict1 = {'a':2,'b':5,'c':7}
list5 = {k:v**2 for k,v in dict1.items() if v%2==0 }
print(list5)