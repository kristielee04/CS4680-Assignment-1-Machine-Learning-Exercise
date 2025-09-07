# CS4680 Assignment 1 – Machine Learning Exercise

## Problem Identification
- **Problem:** Predict breast cancer based on the features of the cell nuclei.  
- **Target Variable:** Diagnosis is either Malignant or Benign  
- **10 Features:**  
  1. Radius  
  2. Texture  
  3. Perimeter  
  4. Area  
  5. Smoothness  
  6. Compactness  
  7. Concavity  
  8. Concave points  
  9. Symmetry  
  10. Fractal dimension  

---

## Data Collection
- **Dataset:** Wisconsin Breast Cancer Dataset  
- **Source:** https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
- **Size:** 569 instances × 30 features
- **Target Values:**  
  - `0` → Malignant  
  - `1` → Benign

---

## Model Development
For these models, only a portion of the dataset was used for training. The unseen portion of the dataset was used for testing.

1. **Classification Models**  
   Support Vector Machine (SVM) was used to classify whether the cells are malignant or benign.

2. **Regression Models**  
   Linear Regression and Polynomial Regression were used to predict a continuous tumor feature (`radius`) while using the other features as the predictor. 

---

## Model Evaluation

Based on this dataset, I believe the most beneficial approach is using it as a classification model for diagnosing breast cancer.

### Classification (SVM)
The model correctly classified all the diagnoses in the test dataset. Based on this, it can be believed that the model will be effective in diagnosing breast cancer based on the fetures of the cell nuclei.

### Regression (Linear vs. Polynomial)
Both models predicted the cell's nucleus radius quite well. However, based on the tested dataset, the Linear Regression model performed better in predicting the nucelus radius. The Polynomial Regression model also preedicted the radius closely, but the gap compared to the Linear model was far more significant. Thus, Linear Regression can be seen as more reliable in this case.

