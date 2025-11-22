import random 
# my_list = ['a','b','c','d','e','f','g','h']
# one_data = random.choice(my_list)
# print(one_data)

s1 = ['This is Awal.','I am Awal.', 'My name is Awal.', 'Here is Awal.']
s2 = ['I am from Dhaka.','I live in Dhaka.', 'Dhaka is my residential area.','Dhaka is my hometown.']
s3 = ['I am a web developer.','I do web development.','I am a Python developer.','I am a professional web developer.']

#paragraph = f'{random.choice(s1)} {random.choice(s2)} {random.choice(s3)} '
#paragraph = random.choice(s1) + ' ' + random.choice(s2) + ' ' + random.choice(s3)
paragraph = ' '.join([random.choice(s1), random.choice(s2), random.choice(s3)])
print(paragraph)

