'''
Created on 27 wrz 2016

@author: student
'''
def czesc1():
    data = {'file_name':'', 'poprawny':'', 'niepoprawny':''}
    data['file_name'] = raw_input("Podaj nazwe pliku")
    data['poprawny'] = raw_input("Podaj poprawny")
    data['niepoprawny'] = raw_input("Podaj niepoprawny")
    return data