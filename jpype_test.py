'''
Created on 

@author: Raja CSP Raman

source:
    https://pypi.org/project/JPype1/1.4.0/

    https://jpype.readthedocs.io/en/latest/install.html
'''


# from jpype import *
import jpype


def test_1():

    startJVM("-ea", classpath=["/home/rajaraman/rprojects/ecolab-ner-csp/"])
    SampleClass = JClass("SampleClass")

    print(SampleClass.square(4))

def test_2():

    jvm_dir = "/home/rajaraman/rprojects/ecolab-ner-csp/"
    jpype.startJVM(classpath = ['jars/*', "/home/rajaraman/rprojects/ecolab-ner-csp/"])

    SampleClass = jpype.JClass("SimplePredictNER")

    print(SampleClass.getTokens("254 Spadina Road"))
    print(SampleClass.getTokens("255 Spadina Road"))

def startpy():

    test_2()

if __name__ == '__main__':
    startpy()