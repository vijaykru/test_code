import re
def normalizedData(string):
    list_data = []
    for data in string.split(' '):
        data = re.sub('\.\.+', ' ', data) 
        #data = re.sub('\.', '', data)
        data = re.sub(' ', '', data)
        data = re.sub('\//+', '/', data)
        list_data.append(data)
    return " ".join(list_data)
    

string = "folder1/folder2/../folder3/../../foldern/.././folder8/..../"
print(normalizedData(string))

string = "hello...hello..what...you.doing../best/../of/./luck"
print(normalizedData(string))


string = "hello...hello..what...you.doing../best/../of/./luck   how are you ../buddy/."
print(normalizedData(string))


string = "hello...hello..what.you.doing../best/../of/./luck./buddy/."
print(normalizedData(string))