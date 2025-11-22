#from htmlGenerator import html_converter

fruits = ['apple', 'mango', 'barry', 'pine apple', 'jackfruit']

# list_con = ['<ul>']
# for list in fruits:
#     list_con.append(html_converter('li', list))
# list_con.append('</ul>')

# new_list = ''.join(list_con)

# print(new_list)

def html_list(data_list, list_type='<ul>'):
    list_con = [f'<{list_type}>']
    for data in data_list:
        list_con.append(f'<li>{data}</li>')
    list_con.append(f'</{list_type}>')

    new_list = ''.join(list_con)
    return new_list

n = html_list(fruits)
print(n)