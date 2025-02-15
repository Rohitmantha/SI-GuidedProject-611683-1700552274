# Smart Lender 
###  Applicant Credibility Prediction For Loan Approval
SI-GuidedProject-611683-1700552274 - Smart-Lender Loan Prediction

## Overview


The credit system plays a significant role in a country's economy and financial health, particularly in banks' credit risk evaluation processes, which are critical globally. One of the key challenges is assessing the risk involved in loan approvals, especially predicting loan defaulters.

**Credit risk evaluation** is vital for minimizing the loss from non-performing assets and ensuring efficient loan recovery. This leads to better financial outcomes for banks. However, predicting credit defaulters remains a complex task.

Machine Learning (ML) offers promising solutions to automate and enhance these prediction processes. By training models with historical data, banks can assess the credibility of applicants more accurately, leading to smarter decision-making. In this project, we will use several classification algorithms for predicting loan approval, including:
- **Decision Tree**
- **Random Forest**
- **K-Nearest Neighbors (KNN)**
- **XGBoost**

The best-performing model will be selected after training and testing the dataset. The trained model will then be saved in `.pkl` format. Integration with **Flask** will be implemented for web deployment.
## Features

- **🌐 Web Interface**: The `Web Interface` directory contains the code for the Flask web application. Users can interact with the trained model through this interface.

- **🧠 Model Development**: The `loan_prediction.ipynb` notebook in the model-building directory includes the code for developing and training the model. It provides detailed explanations of the model architecture and training process.

- **📊 Dataset**: The `loan_prediction.csv` file in the model-building directory contains the dataset used for training and testing the model. Ensure that you have the necessary permissions and rights to use and distribute the dataset.  
  The dataset is also available on Kaggle and can be accessed via an API: [Data Set](https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset)  

## Getting Started

### 🛠️ Prerequisites

- Python 3.x  
- Install dependencies like: Flask, Numpy, image, Keras, TensorFlow  

### 🚀 Running the Web Interface

1. Navigate to the `webapp-building` directory in the `Project Development Phase`.

2. Run the Flask application using the following command in the terminal at the same directory:  

   ```bash
   python app.py
    ```
    The web interface will be accessible at [http://localhost:5000](http://localhost:5000) on your local host. You can also access the web app on other devices on the same network by using the actual IP provided below the localhost.

## Project Team Information

##### **Team ID:** Team-592603
### Team Members:

- **👨‍💼 Team Leader:**
  - **Name:** Naga Vijay Rohit Mantha

- **👩‍💻 Team Member:**
  - **Name:** Bavana Durga Praneeth

- **👨‍💻 Team Member:**
  - **Name:** Shiva Sannidh Boosi

- **👨‍💻 Team Member:**
  - **Name:** N Devi Dhanush


