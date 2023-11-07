
'''

Created on 

@author: Raja CSP Raman

source:
    
'''

FILEPATH = 'metrics_input.txt'

dict_parts = {
    0 : 'entity',
    1 : 'p',
    2 : 'r',
    3 : 'f1',
    4 : 'tp',
    5 : 'fp',
    6 : 'fn'
}

def set_dict(r_dict, parts):

    for idx, val in enumerate(parts):
        r_dict[dict_parts[idx]] = val

    return r_dict

def startpy():

    with open(FILEPATH) as fp:
        for idx, line in enumerate(fp):

            if(idx == 0):
                continue

            line = line.replace('\n', '').strip()

            if(len(line) <= 0):
                continue

            # print(f'[{line}]')

            parts = line.split('\t')
            # print(len(parts))
            r_dict = {
                'entity' : 0,
                'p' : 1,
                'r' : 2,
                'f1' : 3,
                'tp' : 4,
                'fp' : 5,
                'fn' : 2
            }

            r_dict = set_dict(r_dict, parts)

            # print(line)

            print(r_dict)

    pass

if __name__ == '__main__':
    startpy()