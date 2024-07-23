immutable_var = (1, 2, "sun", True, [1, 2])
print(immutable_var)

immutable_var [0] = 10
immutable_var [3] = False
immutable_var [2] = "cloudy"
# обращение напрямую к самим элементам отсутствует, т.к.кортеж содержит ссылки на элементы,
# поэтому изменить значение элементов кортежа нельзя

mutable_list = [1, 5, 7, 'fun', False]   # см. Practical Task 5 part 2
mutable_list[1] = 2
mutable_list[2] = 'So'
mutable_list[4] = 'It`s'
mutable_list[3] = 10
mutable_list.append('rainy')
mutable_list.extend('now')
print(mutable_list)
