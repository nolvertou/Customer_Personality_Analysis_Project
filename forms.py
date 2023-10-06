from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, DateField, FloatField

print("test")

class SignUpForm(FlaskForm):
    username = StringField('Username', render_kw={"placeholder": "username"})
    password = StringField('Password')
    submit = SubmitField('Sign up')

class CustomerDataForm(FlaskForm):
    ID = IntegerField('ID',render_kw={"placeholder": "Enter ID", "value":1})
    Year_Birth = IntegerField('Year_Birth',render_kw={"placeholder": "Enter Year_Birth"})
    Education =  SelectField(choices=[('0', '2n Cycle'), ('1', 'Basic'), ('2', 'Graduation'), ('3', 'Master Education'), ('4', 'PhD'), ])
    Marital_Status = SelectField(choices=[('0', 'Absurd'), ('1', 'Alone'), ('2', 'Divorced'), ('3', 'Married'), ('4', 'Single'), ('5', 'Together'), ('6', 'Widow'), ('7', 'YOLO') ])
    Income = FloatField('Income', render_kw={"placeholder": "Enter Income"})
    Kidhome = IntegerField('Kidhome', render_kw={"placeholder": "Enter Kidhome"})
    Teenhome = IntegerField('Teenhome', render_kw={"placeholder": "Enter Teenhome"})
    Customer_age = FloatField('Customer_age', description="Add the time you have as a client (in years)")
    Recency = IntegerField('Recency', render_kw={"placeholder": "Enter Recency"})
    MntWines = IntegerField('MntWines', render_kw={"placeholder": "Enter MntWines"})
    MntFruits = IntegerField('MntFruits', render_kw={"placeholder": "Enter MntFruits"})
    MntMeatProducts = IntegerField('MntMeatProducts', render_kw={"placeholder": "Enter MntMeatProducts"})
    MntFishProducts = IntegerField('MntFishProducts', render_kw={"placeholder": "Enter MntFishProducts"})
    MntSweetProducts = IntegerField('MntSweetProducts', render_kw={"placeholder": "Enter MntSweetProducts"})
    MntGoldProds = IntegerField('MntGoldProds', render_kw={"placeholder": "Enter MntGoldProds"})
    NumDealsPurchases = IntegerField('NumDealsPurchases', render_kw={"placeholder": "Enter NumDealsPurchases"})
    NumWebPurchases = IntegerField('NumWebPurchases', render_kw={"placeholder": "Enter NumWebPurchases"})
    NumCatalogPurchases = IntegerField('NumCatalogPurchases', render_kw={"placeholder": "Enter NumCatalogPurchases"})
    NumStorePurchases = IntegerField('NumStorePurchases', render_kw={"placeholder": "Enter NumStorePurchases"})
    NumWebVisitsMonth = IntegerField('NumWebVisitsMonth', render_kw={"placeholder": "Enter NumWebVisitsMonth"})
    AcceptedCmp3 = IntegerField('AcceptedCmp3', render_kw={"placeholder": "Enter AcceptedCmp3"})
    AcceptedCmp4 = IntegerField('AcceptedCmp4', render_kw={"placeholder": "Enter AcceptedCmp4"})
    AcceptedCmp5 = IntegerField('AcceptedCmp5', render_kw={"placeholder": "Enter AcceptedCmp5"})
    AcceptedCmp1 = IntegerField('AcceptedCmp1', render_kw={"placeholder": "Enter AcceptedCmp1"})
    AcceptedCmp2 = IntegerField('AcceptedCmp2', render_kw={"placeholder": "Enter AcceptedCmp2"})
    Complain = IntegerField('Complain', render_kw={"placeholder": "Enter Complain"})
    Z_CostContact = IntegerField('Z_CostContact', render_kw={"placeholder": "Enter Z_CostContact"})
    Z_Revenue = IntegerField('Z_Revenue', render_kw={"placeholder": "Enter Z_Revenue"})
    Response = IntegerField('Response', render_kw={"placeholder": "Enter Response"})
    Customer_age = IntegerField('Customer_age', render_kw={"placeholder": "Enter username"})
    submit = SubmitField('Submit Customer Data')

