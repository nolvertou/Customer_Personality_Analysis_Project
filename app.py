# import main Flask class and request object
from flask import Flask, request, render_template
import pandas as pd
import pickle
from sklearn import svm
from forms import SignUpForm
from forms import CustomerDataForm
from flask_bootstrap import Bootstrap5

data_type_dict = {
        'ID': 'int',
        'Year_Birth': 'int',
        'Education': 'int',
        'Marital_Status': 'int',
        'Income': 'float',
        'Kidhome': 'int',
        'Teenhome': 'int',
        'Recency': 'int',
        'MntWines': 'int',
        'MntFruits': 'int',
        'MntMeatProducts': 'int',
        'MntFishProducts': 'int',
        'MntSweetProducts': 'int',
        'MntGoldProds': 'int',
        'NumDealsPurchases': 'int',
        'NumWebPurchases': 'int',
        'NumCatalogPurchases': 'int',
        'NumStorePurchases': 'int',
        'NumWebVisitsMonth': 'int',
        'AcceptedCmp3': 'int',
        'AcceptedCmp4': 'int',
        'AcceptedCmp5': 'int',
        'AcceptedCmp1': 'int',
        'AcceptedCmp2': 'int',
        'Complain': 'int',
        'Z_CostContact': 'int',
        'Z_Revenue': 'int',
        'Response': 'int',
        'Customer_age': 'float'
    }


# create the Flask app
app = Flask(__name__)

# Secret Key
app.config['SECRET_KEY'] = 'thecodex'

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/query-example')
def query_example():
    # data_type_dict = {'Year_Birth': 'int', 'Education': 'str', 'Income': 'float'}
    # data_dict = {'Year_Birth': [], 'Education': [], 'Income': []}

    data_type_dict = {
        'ID': 'int',
        'Year_Birth': 'int',
        'Education': 'int',
        'Marital_Status': 'int',
        'Income': 'float',
        'Kidhome': 'int',
        'Teenhome': 'int',
        'Recency': 'int',
        'MntWines': 'int',
        'MntFruits': 'int',
        'MntMeatProducts': 'int',
        'MntFishProducts': 'int',
        'MntSweetProducts': 'int',
        'MntGoldProds': 'int',
        'NumDealsPurchases': 'int',
        'NumWebPurchases': 'int',
        'NumCatalogPurchases': 'int',
        'NumStorePurchases': 'int',
        'NumWebVisitsMonth': 'int',
        'AcceptedCmp3': 'int',
        'AcceptedCmp4': 'int',
        'AcceptedCmp5': 'int',
        'AcceptedCmp1': 'int',
        'AcceptedCmp2': 'int',
        'Complain': 'int',
        'Z_CostContact': 'int',
        'Z_Revenue': 'int',
        'Response': 'int',
        'Customer_age': 'float'
    }

    # data_type_dict = {'Year_Birth': int, 'Education' : str}
    data_dict = {
        'ID': [],
        'Year_Birth': [],
        'Education': [] ,
        'Marital_Status': [],
        'Income': [],
        'Kidhome': [],
        'Teenhome': [],
        'Recency': [],
        'MntWines': [],
        'MntFruits': [],
        'MntMeatProducts': [],
        'MntFishProducts': [],
        'MntSweetProducts': [],
        'MntGoldProds': [],
        'NumDealsPurchases': [],
        'NumWebPurchases': [],
        'NumCatalogPurchases': [],
        'NumStorePurchases': [],
        'NumWebVisitsMonth': [],
        'AcceptedCmp3': [],
        'AcceptedCmp4': [],
        'AcceptedCmp5': [],
        'AcceptedCmp1': [],
        'AcceptedCmp2': [],
        'Complain': [],
        'Z_CostContact': [],
        'Z_Revenue': [],
        'Response': [],
        'Customer_age': []
    }

    # Getting values from URL by GET Method
    for var in data_type_dict:

        # Getting the value
        value = request.args.get(var)
        if(value == None):
            value = 0

        # Giving format to the value
        if (data_type_dict[var] == 'str'):
            # print(data_type_dict[var])
            data_dict[var].append(str(value))
        elif (data_type_dict[var] == 'int'):
            # print(data_type_dict[var])
            data_dict[var].append(int(value))

        elif (data_type_dict[var] == 'float'):
            # print(data_type_dict[var])
            data_dict[var].append(float(value))




    # for var in data_dict:
    #     get_value = request.args.get(var)
    #     data_dict[var].append(int(get_value))

    # Assigning data_dict values to a dataframe
    df = pd.DataFrame.from_dict(data_dict)



    # Displaying data_dict into the Terminal for Debugging
    # print("data_dict = ",data_dict)
    # print("dataframe = ",df)
    # print(df.info())

    # Opening the model
    # Read the columnlist of dataframe
    with open('customer_personality_svm_model.pkl', 'rb') as fp:
        rd_svm_model = pickle.load(fp)

    # Read colnames_numerics_only
    with open('colnames_numerics_only', 'rb') as fp:
        colnames_numerics_only_read = pickle.load(fp)

    print(df[colnames_numerics_only_read])


    predicted_label = rd_svm_model.predict(df[colnames_numerics_only_read])
    print("Predicted label", predicted_label)

    return '''<h1>Dataframe Values</h1> <br> {}'''.format(data_dict)

@app.route('/form-example')
def form_example():
    return 'Form Data Example'

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if(form.is_submitted()):
        result = request.form
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['GET', 'POST'])
def classify_customer():
    data_dict = {}

    form = CustomerDataForm()
    if (form.is_submitted()):
        data_inm_dict = request.form

        # print(data_inm_dict)

        for element in data_inm_dict:
            # print(element)

            if (element == 'csrf_token' or element == 'submit'):
                continue
            else:
                print(element, "= ", data_inm_dict[element])

            if data_inm_dict[element] == '':
                data_dict[element] = [0]
            else:
                data_dict[element] = [int(data_inm_dict[element])]

        print(data_dict)

        df = pd.DataFrame.from_dict(data_dict)

        print(df)

        # Opening the model
        # Read the columnlist of dataframe
        with open('customer_personality_svm_model.pkl', 'rb') as fp:
            rd_svm_model = pickle.load(fp)

        # Read colnames_numerics_only
        with open('colnames_numerics_only', 'rb') as fp:
            colnames_numerics_only_read = pickle.load(fp)

        print(colnames_numerics_only_read)
        print(df[colnames_numerics_only_read])

        predicted_label = rd_svm_model.predict(df[colnames_numerics_only_read])
        print("Predicted label", predicted_label)

        # return '''<h1>Dataframe Values</h1> <br> {}'''.format(data_dict)


        # df = pd.DataFrame.from_dict
        # print(df.info())

        # Getting values from URL by GET Method
        # for var in data_type_dict:

        #
        #     # Getting the value
        #     value = data_dict[var]
        #     if (value == None):
        #         value = 0
        #
        #     # Giving format to the value
        #     if (data_type_dict[var] == 'str'):
        #         # print(data_type_dict[var])
        #         data_dict[var].append(str(value))
        #     elif (data_type_dict[var] == 'int'):
        #         # print(data_type_dict[var])
        #         data_dict[var].append(int(value))
        #
        #     elif (data_type_dict[var] == 'float'):
        #         # print(data_type_dict[var])
        #         data_dict[var].append(float(value))
        #
        # # for var in data_dict:
        # #     get_value = request.args.get(var)
        # #     data_dict[var].append(int(get_value))
        #
        # # Assigning data_dict values to a dataframe
        # df = pd.DataFrame.from_dict(data_dict)

        return render_template('results.html', result=data_dict, label = predicted_label)

    return render_template('classify.html', form=form)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)