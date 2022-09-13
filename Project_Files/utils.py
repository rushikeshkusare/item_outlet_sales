import pandas as pd
import numpy as np
import config
import json
import pickle
import re

class SalesPrediction() :

    def __init__(self, item_weight,  item_visibility, item_mrp, outlet_establishment_year, outlet_size, outlet_location_type, item_fat_content, item_type, outlet_type) :
        self.item_weight = item_weight
        self.item_visibility = item_visibility
        self.item_mrp = item_mrp
        self.outlet_establishment_year = outlet_establishment_year
        self.outlet_size = outlet_size
        self.outlet_location_type = outlet_location_type
        self.item_fat_content = 'Item_Fat_Content_' + item_fat_content
        self.item_type = 'Item_Type_' + item_type
        self.outlet_type = 'Outlet_Type_' + outlet_type

    def get_model(self) :

        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, 'r') as f:
            self.json_data = json.load(f)

    def get_prediction(self) :
        
        self.get_model()
        
        item_fat_index = self.json_data['Columns'].index(self.item_fat_content)
        item_type_index = self.json_data['Columns'].index(self.item_type)
        outlet_type_index = self.json_data['Columns'].index(self.outlet_type)

        test_array = np.zeros(len(self.json_data['Columns']))
        test_array[0] = self.item_weight
        test_array[1] = self.item_visibility
        test_array[2] = self.item_mrp
        test_array[3] = self.json_data['Outlet_Establishment_Year'][self.outlet_establishment_year]
        test_array[4] = self.json_data['Outlet_Size'][self.outlet_size]
        test_array[5] = self.json_data['Outlet_Location_Type'][self.outlet_location_type]
        test_array[item_fat_index] = 1
        test_array[item_type_index] = 1
        test_array[outlet_type_index] = 1

        predicted_sales = np.around(self.model.predict([test_array]), 2)[0]

        return predicted_sales