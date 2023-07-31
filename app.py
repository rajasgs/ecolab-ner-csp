'''
Source:

Author: Raja CSP

    UI
    https://github.com/tactlabs/smalltics-flask/blob/master/templates/index.html
'''
from flask import Flask, render_template, request, redirect, url_for
import random
import json
import pandas as pd

app  = Flask(__name__)
PORT = 3012

N_ENTRIES = 3

GROCERY_PATH    = 'grocery_unique.csv'
GROCERY_TRACK   = 'grocery_training_new.txt'
GROCERY_OUTPUT  = 'grocery_track.json'
SS              = 'grocery_training_new.txt'

def read_address():

    df = pd.read_csv(GROCERY_PATH)
    # print(df.loc[:,"Orders"])

    last_address_index = 0

    with open(GROCERY_OUTPUT, 'r') as openfile:
 
    # Reading from json file

        json_object = json.load(openfile)
        

        last_address_index = json_object['last_entry']
    
    addresses = []


    df = df.iloc[last_address_index:last_address_index+N_ENTRIES]

    for index,row in df.iterrows():
        # print(row['ADDRESS'])
        addresses.append(str(row['Orders']))

    return addresses
    
def dump_to_file(data):
    with open(SS, 'a') as f:

        for entry in data:
            for line in entry:
                text = line[0]+"    "+line[1]
                text = line[0]+"    "+line[1]

                f.write(text)
                f.write('\n')
            f.write('\n')


        # Serializing json
    
    with open(GROCERY_OUTPUT, 'r') as openfile:
 
    # Reading from json file

        json_object = json.load(openfile)
        last_address_index = json_object['last_entry']
        
    json_object = json.dumps({"last_entry" : last_address_index+N_ENTRIES }, indent=4)
    
    # Writing to sample.json
    with open(GROCERY_OUTPUT, "w") as outfile2:
        outfile2.write(json_object)

    # print(df.to_string())  
    return 0

    
@app.route("/", methods=["GET","POST"])
def startpy():

    # result = {
    #     "Greetings" : "P.S. I am here",
    #     "random_number" : random.randint(20, 100)
    # }

    # return result

    addresses = read_address()

    split_address = []

    for one in addresses:
        split_address.append(one.split())
    


    return render_template('index.html', result = split_address)


@app.route('/address_submit', methods=["POST"])
def address_form_submit():

    # return request.files
    
    data = []
    # data = []


    for i in range(4):
        add_src= request.values.getlist("src"+str(i+1))
        add_temp= request.values.getlist("add"+str(i+1))

        temp = []

        print(add_src)
        for n in range(len(add_temp)):
            temp.append([add_src[n],add_temp[n]])
            print([add_src[n],add_temp[n]])
        data.append(temp)

    print(data)

    dump_to_file(data)

    return redirect(url_for('startpy'))


if __name__ == "__main__":
    app.run(
        debug   = True,
        host    = "0.0.0.0",
        port    = PORT
    )