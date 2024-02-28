

from constants import *
import sys

def cleanfile(filename):

    with open(filename,'w') as file:
        pass

from pathlib import Path

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
        c_filename = 'patterns/' + cline
        my_file = Path(c_filename)
        if not my_file.is_file():
            print(f'{c_filename} is not available, so skipping')
            continue
        with open(c_filename) as f:
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
        c_filename = 'patterns/' + cline
        my_file = Path(c_filename)
        if not my_file.is_file():
            print(f'{c_filename} is not available, so skipping')
            continue
        with open(c_filename) as f:
            cfile_lines = f.read()

        with open(training_file, 'a') as filetowrite:
            filetowrite.write(cfile_lines)

            filetowrite.write('\n\n')


def print_filenames():

    for idx in range(1, 57):
        print(f"pattern{idx}-input-training.txt")

def startpy():

    # print_filenames()
    # return

    ctype = int(sys.argv[1])
    # 1 - training; 2 - testing

    testing_file    = CORE_NLP_TESTING_FILEPATH

    

    # print(f'training_file : {training_file}')

    if(ctype == 1):
        combine_training_files()
    elif(ctype == 2):
        combine_testing_files()
    else:
        print("Not matched")

if __name__ == '__main__':

    startpy()

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