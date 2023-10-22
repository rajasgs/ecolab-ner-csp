
'''
Created on 

@author: Raja CSP Raman

source:

    https://towardsdatascience.com/simple-transformers-named-entity-recognition-with-transformer-models-c04b9242a2a0
    
    Benchmark
    https://docs.google.com/spreadsheets/d/1F1FHgBmJ60FPrPPNZr8n5nTb7DorBc-tMGsOUppTH7E/

    https://docs.google.com/spreadsheets/d/1JOK1mFmOZb1S3sf-6VDSkqlxZhc31OcAAXYv51823FE/edit#gid=0

    https://towardsdatascience.com/simple-transformers-named-entity-recognition-with-transformer-models-c04b9242a2a0

    https://datascience.stackexchange.com/questions/92630/save-and-load-simple-transformer-model
'''

import os
# from nerInference import NERInference
from simpletransformers.ner import NERModel, NERArgs
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# Local
import constants as con

def train_and_save():

    data = pd.read_csv(con.ADDRESS_INPUT_BERT_CSV_PATH,encoding = "latin1" )
    data.rename(
        columns = {
            "Sentence#" : "sentence_id", 
            "Word"      : "words", 
            "Tag"       : "labels"
        }, 
        inplace = True
    )
    data["labels"] = data["labels"].str.upper()

    label = data["labels"].unique().tolist()

    args                        = NERArgs()
    args.num_train_epochs       = 3
    args.learning_rate          = 1e-4
    earning_rate                = 1e-4
    args.overwrite_output_dir   = True
    args.train_batch_size       = 16
    args.eval_batch_size        = 16

    model = NERModel('bert', 'bert-base-cased',labels = label, args = args, use_cuda = False)

    X = data[["sentence_id","words"]]
    Y = data["labels"]

    x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size =0.2)

    #building up train data and test data
    train_data  = pd.DataFrame({"sentence_id":x_train["sentence_id"],"words":x_train["words"],"labels":y_train})
    test_data   = pd.DataFrame({"sentence_id":x_test["sentence_id"],"words":x_test["words"],"labels":y_test})

    model.train_model(
        train_data,
        eval_data       = test_data,
        acc             = accuracy_score,
        # output_dir      = 'nermodel'
    )

def load_and_predict():
    
    model = NERModel('bert', 'outputs/', use_cuda = False)

    prediction, model_output = model.predict(["130-300 Spadina Road"])

    print(prediction)

def startpy():
    
    # prediction, model_output = model.predict(["254 Spadina Road"])
    # print(prediction)

    train_and_save()

    # load_and_predict()

    print("Training Done")

if __name__ == '__main__':
    startpy()