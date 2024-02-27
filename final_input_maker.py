

from constants import *
import sys

def cleanfile(filename):

    with open(filename,'w') as file:
        pass

def combine_training_files():

    training_file   = CORE_NLP_TRAINING_FILEPATH
    # training_file = 'test.txt'

    soure_file = 'files2combine_training.txt'

    # clean the file first
    cleanfile(training_file)

    lines = None
    with open(soure_file) as f:
        lines = f.readlines()

    for cline in lines:
        print(cline)

        cline = cline.replace('\n', '').strip()

        cfile_lines = None
        with open('patterns/' + cline) as f:
            cfile_lines = f.read()

        with open(training_file, 'a') as filetowrite:
            filetowrite.write(cfile_lines)

            filetowrite.write('\n\n')

def combine_testing_files():

    training_file   = CORE_NLP_TESTING_FILEPATH
    # training_file = 'test.txt'

    soure_file = 'files2combine_testing.txt'

    # clean the file first
    cleanfile(training_file)

    lines = None
    with open(soure_file) as f:
        lines = f.readlines()

    for cline in lines:
        print(cline)

        cline = cline.replace('\n', '').strip()

        cfile_lines = None
        with open('patterns/' + cline) as f:
            cfile_lines = f.read()

        with open(training_file, 'a') as filetowrite:
            filetowrite.write(cfile_lines)

            filetowrite.write('\n\n')

def startpy(ctype):

    testing_file    = CORE_NLP_TESTING_FILEPATH

    # print(f'training_file : {training_file}')

    if(ctype == 1):
        combine_training_files()
    elif(ctype == 2):
        combine_testing_files()
    else:
        print("Not matched")

if __name__ == '__main__':

    ctype = int(sys.argv[1])
    # 1 - training; 2 - testing
    
    startpy(ctype)

    # test_split()

    # print(test_2())

    pass


'''
How to run?

# training
python final_input_maker.py 1

# testing
python final_input_maker.py 2
'''