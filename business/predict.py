



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
    model_version
):
    vas_singleton = vas.ValidatorSingleton.getInstance(model_version)

    result = vas_singleton.get_tokens(address)
    print(f'result : {result}')

    print(f'vas_singleton.model : {vas_singleton.model}')

    return result, vas_singleton.model