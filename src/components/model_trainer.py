import os
import sys
from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
# from sklearn.com import ColumnTransformer
# from sklearn.impute import SimpleImputer
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import OneHotEncoder,StandardScaler
from src.logger import logging

from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.exception import CustomException
from src.utils import save_object,evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_traing(self,train_array,test_array):
        try:
            pass
            logging.info("splitting the train and test data")
            X_train,y_train,X_test,y_test=(
                train_array[:,-1],
                train_array[:,-1],
                test_array[:,-1],
                test_array[:,-1]
            )
            models={
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Bradiant Bossting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "K-Neighbour Classifier": KNeighborsRegressor(),
                "XGB Classifier": XGBRegressor(),
                "Cat Boost Classfier":CatBoostRegressor(),
                "AdaBost classifier":AdaBoostRegressor()
            }
            logging.info(f"splitting the train and test data {X_train.shape}")
            X_train = X_train.reshape(-1, 1)
            X_test = X_test.reshape(-1, 1)
            logging.info(f"splitting the train and test data {X_train.shape}")
            model_report:dict=evaluate_model(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)

            best_model_score=max(sorted(model_report.values()))

            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model=models[best_model_name]

            if best_model_score<0.6:
                raise CustomeException("no best model found")
            
            logging.info(f"best model found on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model)
            predicted=best_model.predict(X_test)

            r2_square=r2_score(y_test,predicted)

            return r2_square


        except Exception as ex:
            raise CustomException(ex,sys) 
    
