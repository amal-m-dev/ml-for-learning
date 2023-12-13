import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def load_saved_artifacts():
    print('Loading artifacts..')
    global __locations
    global __data_columns
    global __model

    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open("./artifacts/blr_home_prices_model.pickle",'rb') as f:
        __model = pickle.load(f)

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2) 

def get_location_names():
    return __locations



if __name__ == '__main__':
    print('starting util')
    load_saved_artifacts()
    # print(get_estimated_price('1st block jayanagar', 1000, 2, 2))
    # print(get_estimated_price('1st phase jp nagar', 1000, 2, 2))
    # print(get_estimated_price('btm layout', 1000, 2, 2))

    # print(get_estimated_price('Kalhalli', 1000, 2, 2)) #other location
    # print(get_estimated_price('Ejipura', 1000, 2, 2))
    # # print(get_loc_names())