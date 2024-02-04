# purpose of the transformation is --feature engineering ,data cleaning,conver categorical feature into Numerical feature.
import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from src.exception import CustomeException
from src.logger import logging
from src.utils import save_object
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    
    def get_data_transformer_obj(self):  # to create a pkl file for converting cat feature into numerrical feature nothing but data transformation 
        try:
            numerical_features = ["reading_score", "writing_score"]
            categorical_features = ["gender",
            "race_ethnicity", 
            "parental_level_of_education", 
            "lunch", 
            "test_preparation_course"]
            num_pipleine=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scalar",StandardScaler(with_mean=False))
                ]
            )
            logging.info("Numerical coloumns standard scalling is completed  ")

            Cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scalar",StandardScaler(with_mean=False))
                ]
            )
            logging.info("Categorical coloumns encoding is completed ")

            preprocessor=ColumnTransformer(
                [("num_pipleine",num_pipleine,numerical_features),
                ("Cat_pipleline",Cat_pipeline,categorical_features)
                
                ]
            )
            return preprocessor

        except Exception as e:
            raise CustomeException(e,sys)

    def initiate_data_transformation(self,train_data_path,test_data_path):
        try:
            train_df=pd.read_csv(train_data_path)
            test_df=pd.read_csv(test_data_path)
            logging.info("Data reading is done")
            logging.info("obtaining pre-procesising object")
            preprocessor_obj=self.get_data_transformer_obj()
            target_Column=['math_score']
            numerical_features : ["reading_score", "writing_score"]

            input_feature_train_df=train_df.drop(columns=target_Column,axis=1)
            target_feature_train_df=train_df[target_Column]

            input_feature_test_df=test_df.drop(columns=target_Column,axis=1)
            target_feature_test_df=test_df[target_Column]

            logging.info("executing prepossing on train and test dataframe")

            input_feature_train_array=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_array=preprocessor_obj.transform(input_feature_test_df)

            train_arr=np.c_[input_feature_train_array,np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_array,np.array(target_feature_test_df)]

            logging.info("Saving preprocessing Objects")
            
            # saving the pikel file
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            )

            return(
                train_arr,test_arr,
                self.data_transformation_config.preprocessor_obj_file_path

            )

        except Exception as ex:
            raise CustomeException(ex,sys)