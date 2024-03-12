



'''
Created on 

@author: Raja CSP Raman

source:
    
'''

import os
from pathlib import Path
#import stanza
import re
#form typing import List
import subprocess
#from stanza.server import CoreNLPClient

# Local
from constants import (CORE_NLP_TRAINING_FILEPATH, CORE_NLP_TESTING_FILEPATH, CORE_NLP_MODELNAME, NER_MODEL_FOLDER_BASE)

'''
Below line, installs the stanfordCore NLP JARS. As it is already installed separately, commenting out the line.
'''
#stanza.install_corenlp()


# CORENLP_HOME is set to the directory where StanfordCore jars have been extracted to
core_nlp_path = os.getenv('CORENLP_HOME')

#core_nlp_path = os.getenv('CORENLP_HOME',str(Path.home() / 'stanza_corenlp')) # When StanfordCore jars are installed through stanza, this line can be used to get the path of the jars

#classpath = [str(file_name) for file_name in Path(core_nlp_path).iterdir()
#                if "stanford-corenlp" in str(file_name.name) ][0]

#classpath = "/home/ashish/corenlp/stanford-corenlp-4.5.2/*"
classpath = "jars/*"
print('The classpath is: ',classpath)

def ner_prop_str(train_files: list, test_files: list, output: str) -> str:
    train_fils_str = ",".join(train_files)
    test_files_str = ",".join(test_files)

    # Original
    # return f"""
    # trainFileList = {train_fils_str}
    # testFiles = {test_files_str}
    # serializeTo = {output}
    # map = word=0,answer=1

    # useClassFeature = true
    # useWord=true
    # useNGrams=true
    # noMidNGrams=false
    # maxNGramLeng=6
    # usePrev=true
    # useNext=true
    # useSequences=true
    # usePrevSequences=true
    # maxLeft=4
    # useTypeSeqs=true
    # useTypeSeqs2=true
    # useTypeySequences=true
    # wordShape=chris2useLC
    # useDisjunctive=true 
    # """

    # Experiment
    return f"""
    trainFileList = {train_fils_str}
    testFiles = {test_files_str}
    serializeTo = {output}
    map = word=0,answer=1

    useClassFeature = true
    useWord=true
    useNGrams=true
    noMidNGrams=false
    maxNGramLeng=6
    usePrev=true
    useNext=true
    useSequences=true
    usePrevSequences=true
    maxLeft=4
    useTypeSeqs=true
    useTypeSeqs2=true
    useTypeySequences=true
    wordShape=chris1
    useDisjunctive=true 
    """


def write_ner_prop_file(ner_prop_file:str, train_files: list,test_files: list, output_file)-> None:
    with open(ner_prop_file, 'wt') as f:
        props = ner_prop_str(train_files, test_files, output_file)
        f.write(props)

def cleanfile(filename):

    with open(filename,'w') as file:
        pass

def write2file(file, content):

    print(f'inside write2file')
    print(content)

    with open(file, 'a') as filetowrite:
        filetowrite.write(content)

def train_model(model_name: str, train_files: list, test_files: list, print_report: bool, classpath: str ):

    output_filepath     = 'ner_output.txt'

    cleanfile(output_filepath)
    
    model_file        = os.path.join(NER_MODEL_FOLDER_BASE, f'{model_name}.model.ser.gz') 
    ner_prop_filename = os.path.join(NER_MODEL_FOLDER_BASE, f'{model_name}.model.props') 

    write_ner_prop_file(ner_prop_filename, train_files, test_files, model_file)

    with open("ner_classification.txt", 'w') as f:
        result = subprocess.run(
            [
                'java',
                '-Xmx1g',
                '-cp', 
                classpath,
                'edu.stanford.nlp.ie.crf.CRFClassifier',
                '-prop', 
                ner_prop_filename,
                # 'capture_output=True',
                # '>',
                # 'neroutput.txt',
                # '2>&1'
            ], 
            stdout = f
        )
    
    ''',
                capture_output=True,
                check=True'''
    
    if print_report:
        print(*result.stderr.decode('utf-8').split('\n')[-11:], sep='\n')

        print(f'trap234')
        write2file(output_filepath, result.stderr.decode('utf-8'))

    # print("done1")
    return model_file


def annotate_ner(ner_model_file:str, texts, tokenize_whitespace=True):

    properties = {
        "ner.model": ner_model_file,
        "tokenize.whitespace":tokenize_whitespace,
        "ner.applyNumericClassifiers": False
    }

    annotated = []

    '''
    with CoreNLPClient( 
        annotators = ['tokenize', 'ssplit', 'ner'],
        properties = properties,
        timeout = 10000,
        be_quiet = True,
        memory = '1G'
    ) as client:
        for text in texts:
            annotated.append(client.annotate(text))
    '''
    
    return annotated



def extract_ner_data(annotation):
    tokens = [token for sentence in annotation.sentence
                    for token in sentence.token]
    return {'tokens': [t.word for t in tokens],
            'ner': [t.coarseNER for t in tokens]}


def ner_extract(ner_model_file: str,
                texts,
                tokenize_whitespace = True):
    annotations = annotate_ner(ner_model_file, texts, tokenize_whitespace)
    return [extract_ner_data(ann) for ann in annotations]

def startpy():

    #train_model("ecolab_address_NER", ["coreNLP_training_dataset.txt"], ["stanford_training_datatset.txt"], True, classpath)
    # train_model("ecolab_address_ner_model_csp", ["Ecolab_Address_Training.txt"], ["Ecolab_Address_Test_2.txt"], True, classpath)
    # train_model("ecolab_address_20230720", ["Ecolab_Address_Training_Ver1.txt"], ["Ecolab_Address_Testing_Ver1.txt"], True, classpath)

    # train_model(
    #     "ecolab_address_20231018_3", 
    #     ["Ecolab_Address_Training_Pattern1_2023_08_28_4.txt"], 
    #     ["Ecolab_Address_Testing_Pattern1_2023_08_28_4.txt"], 
    #     True, 
    #     classpath
    # )

    train_model(
        model_name      = CORE_NLP_MODELNAME, 
        train_files     = [CORE_NLP_TRAINING_FILEPATH], 
        test_files      = [CORE_NLP_TESTING_FILEPATH], 
        print_report    = False, 
        classpath       = classpath
    )

    #result = ner_extract("/home/ashish/Documents/NER/ecolab_address_NER.model.ser.gz", ["2 The Square", "188 Belmont Road", "Deltaweg 76"], True)

    #print(result)
    pass
    

if __name__ == '__main__':
    startpy()


'''
How to run?

python ner.py

sample output:
https://gist.github.com/rajasgs/19ea4b6c834cdff53691812d08d272d8
'''

# Compiling the Java file
# javac -cp "/home/ashish/corenlp/stanford-corenlp-4.5.2/*" PredictNER.java

# Running the class
# java -cp "/home/ashish/corenlp/stanford-corenlp-4.5.2/*:." PredictNER