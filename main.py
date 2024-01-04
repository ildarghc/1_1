immutable_var = (1, 0.5, 'i')
print(immutable_var)
# Значения элементов кортежа нельзя изменить по определению, т.к. кортеж предполагает список, который нельзя изменить
mutable_list = [1, 0.5, 'i']
mutable_list.append('mutator')
print(mutable_list)
