import config
import re
from flask import Flask, jsonify, redirect, render_template, request, url_for
from Project_Files.utils import SalesPrediction

app = Flask(__name__)

################################################################################################
#######################################  Home API  #############################################
################################################################################################

@app.route('/')
def home_flask() :
    return render_template('index.html')

################################################################################################
######################################  Result API  ############################################
################################################################################################

@app.route('/prediction', methods = ['POST', 'GET'])
def get_prediction() :
    if request.method == 'POST' :
        item_weight = float(request.form['Item_Weight'])
        item_visibility = float(request.form['Item_Visibility'])
        item_mrp = float(request.form['Item_MRP'])
        outlet_establishment_year = request.form['Outlet_Establishment_Year']
        outlet_size = request.form['Outlet_Size']
        outlet_location_type = request.form['Outlet_Location_Type']
        item_fat_content = request.form['Item_Fat_Content']
        item_type = request.form['Item_Type']
        outlet_type = request.form['Outlet_Type']

        sales = SalesPrediction(item_weight,  item_visibility, item_mrp, outlet_establishment_year, outlet_size, outlet_location_type, item_fat_content, item_type, outlet_type)
        predicted_sales = sales.get_prediction()

        return render_template('output.html', result=predicted_sales)

    elif request.method == 'GET' :
        item_weight = float(request.args.get('Item_Weight'))
        item_visibility = float(request.args.get('Item_Visibility'))
        item_mrp = float(request.args.get('Item_MRP'))
        outlet_establishment_year = request.args.get('Outlet_Establishment_Year')
        outlet_size = request.args.get('Outlet_Size')
        outlet_location_type = request.args.get('Outlet_Location_Type')
        item_fat_content = request.args.get('Item_Fat_Content')
        item_type = request.args.get('Item_Type')
        outlet_type = request.args.get('Outlet_Type')

        sales = SalesPrediction(item_weight,  item_visibility, item_mrp, outlet_establishment_year, outlet_size, outlet_location_type, item_fat_content, item_type, outlet_type)
        predicted_sales = sales.get_prediction()

        return render_template('output.html', result=predicted_sales)


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port = config.PORT_NUMBER,debug=False)