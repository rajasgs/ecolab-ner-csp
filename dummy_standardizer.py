
'''
Created on 

@author: Raja CSP Raman

source:
    
'''

def read_file(filepath):

    with open(filepath) as f:
        return f.readlines()

def standardize_local_single(address):

    new_address = address.lower()

    return new_address

def standardize_local_multiple(filepath):

    lines = read_file(filepath)

    for line in lines:
        line = line.strip()
        # print(f'line.length: {len(line)}')
        if(len(line) == 0):
            continue
        result = standardize_local_single(line)

        print(f'{result}')

        # print(f'-' * 80)

def startpy():
    standardize_local_multiple('sample_address.txt')
    

if __name__ == '__main__':
    startpy()


'''
python local_standardizer.py
'''