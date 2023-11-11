from flask import Blueprint, render_template, request

import joblib

views = Blueprint('views', __name__)

# Load the model
svm = joblib.load('svm_model.pkl')

# Load the scaler
scaler = joblib.load('scaler.pkl')

@views.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        fields = [
            'radius_mean', 'radius_worst', 'radius_se',
            'texture_mean', 'texture_worst', 'texture_se',
            'perimeter_mean', 'perimeter_worst', 'perimeter_se',
            'area_mean', 'area_worst', 'area_se',
            'smoothness_mean', 'smoothness_worst', 'smoothness_se',
            'compactness_mean', 'compactness_worst', 'compactness_se',
            'concavity_mean', 'concavity_worst', 'concavity_se',
            'concave_points_mean', 'concave_points_worst', 'concave_points_se',
            'symmetry_mean', 'symmetry_worst', 'symmetry_se',
            'fractal_dimension_mean', 'fractal_dimension_worst', 'fractal_dimension_se'
        ]

        #  Check if all the fields are filled
        for field in fields:
            if request.form[field] == '':
                return render_template('index.html', error="Please fill all the fields")
       
        # Get the data from the form
        input_data = []
        for field in fields:
            input_data.append(float(request.form[field]))
       
        # Scale the data
        input_data = scaler.transform([input_data])

        # Make the prediction
        prediction = svm.predict(input_data)

        # Return the result
        if prediction[0] == 1:
            result = "Malignant"
        else:
            result = "Benign"

        return render_template('index.html', result=result)
    
    return render_template('index.html')