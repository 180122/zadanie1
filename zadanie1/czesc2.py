'''
Created on 27 wrz 2016

@author: student
'''
def second_part(data):
    with open(data['file_name'], 'w') as f:
        f.write('Hello world!')
        print(data['poprawny'])