import os

directory = './art/school'
extension = '.jpeg'
def print_as_array():
    print('[')
    for filename in os.listdir(directory):
        fullPath = os.path.join(directory, filename)
        if os.path.isfile(fullPath):
            print('"' + filename + '",')
    print(']')

def print_nums():
    print('[')
    i = 1
    for filename in os.listdir(directory):
        print('"' + str(i) + extension + '",')
        i = i + 1
    print(']')

def rename_as_numbers():
    i = 1
    for filename in os.listdir(directory):
        newName = directory + '/' + str(i) + extension
        # if already exists, skip it
        while os.path.isfile(newName):
            print('warn ' + newName)
            i = i + 1
            newName = directory + '/' + str(i) + extension
        
        fullPath = directory + '/' + filename

        if os.path.isfile(fullPath):
            os.rename(fullPath, newName)  
        i = i + 1

#print_as_array()
#print_nums()
rename_as_numbers()
# rename files