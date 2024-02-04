import os
import sys
from dataclasses import dataclass
from catboost import CatBoostRegressor
# from sklearn.com import ColumnTransformer
# from sklearn.impute import SimpleImputer
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import OneHotEncoder,StandardScaler
from src.logging import logger

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
from src.exception import CustomeException
from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path("Artifacts","model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_traing(self,train_array,test_array,preprocessor_path):
        try:
            pass
            logging.info("splitting the train and test data ")
            X_train,y_train,X_test,y_test=(
                train_array[:,:,-1],
                train_array[:,-1]
            )
        except Exception as ex:
            pass
    
