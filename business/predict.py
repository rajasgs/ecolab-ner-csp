



# def predict(
#     c_address):

#     address_dict = get_tokens(singleton_predict, c_address)

#     print(f'address_dict : {address_dict}')

#     return address_dict

# Local import
# import constants.constants as c
import business.validator_single as vas

def classify_address(
    address,
    model_version = "v1"
):
    vas_singledon = vas.ValidatorSingleton.getInstance(model_version)

    result = vas_singledon.get_tokens(address)
    print(f'result : {result}')

    return result