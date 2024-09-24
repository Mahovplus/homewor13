def print_params(a = 1, b = 'sting', c = True):
    print(a, b, c)


print_params(c=[1,2,3])
values_list = [1, 'string', False]
values_dict = {"a" : 1, "b" : 'string', "c" : [1,2,3]}
print_params(*values_list)
print_params(**values_dict)
values_list2 = [2, True]
print_params(*values_list2, 42)

