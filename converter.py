




'''
Created on 

@author: Raja CSP Raman

source:
    
'''

import pandas as pd

SOURCE_FILEPATH         = 'temp.txt'
DESTINATION_FILEPATH    = 'one.csv'

def get_parts(content):

    content_parts = content.split()

    # print(len(content_parts))

    part_1 = content_parts[0].strip()
    part_2 = content_parts[1].strip()

    return part_1, part_2

def convert_format():

    line_counter = 0
    with open(SOURCE_FILEPATH) as filehandle:
        lines = filehandle.readlines()

    df = pd.DataFrame(columns=['Sentence#', 'Word', 'Tag'])
    

    for line in lines:
        
        if(len(line.strip()) == 0 ):
            print('empty line')
            line_counter += 1

            # if(line_counter > 5):
            #     break
            continue

        print(line_counter, line)

        part_1, part_2 = get_parts(line)
        # df = df.append({'Sentence#': line_counter, 'Word': part_1, 'Tag': part_2}, ignore_index = True)
        df.loc[len(df)] = [line_counter, part_1, part_2]

    df.to_csv('address_training_bert_1.csv', index=False)

    print(len(df))

def startpy():
    
    convert_format()

if __name__ == '__main__':
    startpy()