fruits = ['apple', 'mango', 'jackfruit', 'pipeapple', 'barry']

def list_generator(data_list, list_type='ul'):
    
    list_typ = [f'<{list_type}>']

    for data in data_list:
        list_typ.append(f'<li>{data}</li>')

    list_typ.append(f'</{list_type}>')

    new_list = ''.join(list_typ)
    return new_list

my_list = list_generator(fruits, list_type='ol')
print(my_list)