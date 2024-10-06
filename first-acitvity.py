my_tuple = (1,2,3)
print(my_tuple)

my_tuple = (1,"Hello", 3.4)
print(my_tuple)

my_tuple = ('Z','A' , 'R' ,'A')
print(my_tuple[0])
print(my_tuple[3])

n_tuple = ("mouse" , [8 ,4,6] , (1,2,3))
print(n_tuple[0][3])
print(n_tuple[1][1])


print("Sliced: " , my_tuple[1:4])

for letter in (my_tuple):
    print("Hello", letter)