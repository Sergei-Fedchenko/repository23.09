#1
# one={2,4,6,8,10,12,14,16,18,20}
# two={1,3,5,7,9,11,13,15,17,19}
# print(one)
# print(two)
#2
# my_one={2,4,6,8,10,12,14,16,18,20}
# my_two={1,3,5,7,9,11,13,15,17,19}
# my_three=my_one | my_two
# print(my_three)
#3
# my_one={1,2,3,4,5,6,7,8,9,10}
# my_two={5,6,7,8,9,10,11,12,13,14,15}
# my_three=my_one.intersection(my_two)
# print(my_three)
#4
# my_one={1,2,3,4,5,6,7,8,9,10}
# my_two={5,6,7,8,9,10,11,12,13,14,15}
# my_three=my_one.difference(my_two)
# print(my_three)
#5
# my_one={1,2,3,4,5,6,7,8,9,10}
# my_two={5,6,7,8,9,10,11,12,13,14,15}
# my_three=my_one.symmetric_difference(my_two)
# print(my_three)
#6
# set_list = {1,2,3,4,5,6,7,8,9,10}
# def set_function():
#     while True:
#         a = int(input("Ведите число"))
#         if a is 0:
#             print('Exit')
#             break
#         if a in set_list:
#             print('Число уже есть')
#         else:
#             print(len(set_list))
#             print('Такого числа нет')
# set_function()
#7
# set_1={1,2,3,4,5,6,7,8,9,10}
# set_1.discard(5)
# print(set_1)
#8
# set_list = [1,2,3,4,5,6,7,8,9,10]
# set_mnoj = set(set_list)
# set_bad =[11,12,13,14,15,16,17,18,19,20]
# set_salfetka=set(set_bad)
# def my_list():
#     set_tes = set_mnoj | set_salfetka
#     print(set_tes)
# my_list()

#9
# def my_list():
#     set_spicok =[1,2,2,3,3,3,4,4,4,4]
#     set_mnoj=set(set_spicok)
#     print(sorted(set(set_mnoj)))


# my_list()
#10
def my_list():
    set1={1,2,3,4,}
    set2={1,2,4,3,5,7}
    print(set1.issubset(set2))
my_list()
