


FILEPATH = "address_multi.txt"
import predict_single as pres
import standardize_address as stad


def get_address_lines():

    read_object = open(FILEPATH, "r")
    values_list = read_object.readlines()

    return values_list

def startpy():

    import sys

    model_path = sys.argv[1]

    adds_list = get_address_lines()

    for c_address in adds_list:
        print(f'address: {c_address}')  

        cleaned_address = stad.standardize_single_address(c_address)

        print(f'cleaned: {cleaned_address}')
        result = pres.test_single(cleaned_address, model_path)
        pres.print_addres_dict(result)

        print('-' * 20)


if __name__ == '__main__':
    
    startpy()

    # test_java_class()



    pass
'''
How to run?

python predict_multiple.py /home/rajaraman/datasets/ecolab-ner-archive/ecolab_address_20240313_3.model.ser.gz
'''