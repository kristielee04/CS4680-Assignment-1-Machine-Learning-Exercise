from sklearn import svm
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_breast_cancer

# 1. Problem Identification
# Problem: Predicting Breast Cancer
# Target Variable: Diagnosis is either malignant or benign
# 10 features are computed for each cell nucleus:
# radius, texture,perimeter, area, smoothness, compactness, concavity, concave points, symmetry, and fractal dimension

# 2. Data Collection
# Wisconson Breast Cancer Dataset imported from scikit-learn datasets
# Dataset size - 569 instances x 30 features

# Load dataset from scklearn.datasets
data = load_breast_cancer()

# 3. Model Development: 

# Classification Model to predict diagnosis
# Using a portion of data as the training set (mixture of malignant and benign diagnosis)
training_idx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60] 
input_data_classification = data.data[training_idx]
output_data_classification = data.target[training_idx]

model = svm.SVC()
model.fit(input_data_classification, output_data_classification)

# Testing different rows of the dataset, not used in training
test_idx = [20, 30, 70, 100, 200, 300]
predictions = model.predict(data.data[test_idx]) # Prediction on testing rows

# Comparison to actual diagnosis
print("Classification Models:")
for i, idx in enumerate(test_idx):
    prediction_label = data.target_names[predictions[i]]
    true_label = data.target_names[data.target[idx]]
    print(f"Sample {idx} - Predicted: {prediction_label} | Actual: {true_label}")


# Regression Model to predict a continous feature: radius of cell nucleus
# Using a portion of data as the training set so the other data can be used for testing
print("\nRegression Models:")
input_data_regression = data.data[training_idx, 1:] # all other features will be used as the predictor
output_data_regression = data.data[training_idx, 0] # radius will be used as the regression target

# model 1: linear model
model1 = linear_model.LinearRegression()
model1.fit(input_data_regression, output_data_regression)
res1 = model1.predict(data.data[test_idx, 1:])
# Comparison to actual radius values
print("\nModel 1: Linear Model")
for i, idx in enumerate(test_idx):
    true_value = data.data[test_idx, 0]
    print(f"Sample {idx} - Predicted: {res1} | Actual: {true_value}")


# model 2: polynomial model
model2 = make_pipeline(PolynomialFeatures(2), linear_model.LinearRegression())
model2.fit(input_data_regression, output_data_regression)
res2 = model2.predict(data.data[test_idx, 1:])
# Comparison to actual radius values
print("\nModel 2: Polynomial Model")
for i, idx in enumerate(test_idx):
    true_value = data.data[test_idx, 0]
    print(f"Sample {idx} - Predicted: {res2} | Actual: {true_value}")


# 4. Model Evaluation
# Classification Model:
# Based on the tested values, the classification model used had correctly predicted the diagnosises from using the trained dataset.

# Regression Models: Linear vs Polynomial Models
# Both models predicted the data quite well. However, from the tested dataset, the linear model was better at predicting the radius.