import os 
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import dill
import pickle
from sklearn.metrics import r2_score
def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as ex:
        raise CustomeException(ex,sys)

def evaluate_model(X_train,y_train,X_test,y_test,models,param):
    report = {}
    try:
        for model_name, model in models.items():
            try:
                model.fit(X_train, y_train)  # Train model

                # Predict on training and test data
                y_train_pred = model.predict(X_train)
                y_test_pred = model.predict(X_test)

                # Calculate R-squared scores (assuming you want both, even though they're calculated the same here)
                train_model_score = r2_score(y_train, y_train_pred)
                test_model_score = r2_score(y_test, y_test_pred)

                # Use the model name as the key for the report
                report[model_name] = test_model_score

            except Exception as e:
                raise CustomException(e, sys)  # Ensure CustomException can handle these arguments correctly

        return report

    except Exception as e:
        raise CustomException(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)