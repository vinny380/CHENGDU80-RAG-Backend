import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from preprocessing.policy_feature_func import create_policy_features
import pandas as pd
from agents.embed import embed
import ast


av_data_path = 'CD80_dataset/CD80_dataset/Human-Driving and AV Crash Data/Self-Driving Crash Datasets/SGO-2021-01_Incident_Reports_ADAS.csv'
user_data_path = 'CD80_dataset/CD80_dataset/Insurance Claims Data/insurance_claims.csv'


df = create_policy_features(av_path=av_data_path, user_path=user_data_path, number_of_rows=50)


def pre_process_df(df: pd.DataFrame) -> pd.DataFrame:
    list_of_data_dict = []
    for index in range(df.shape[0]):
        row_dict = df.iloc[index].to_dict()
        list_of_data_dict.append(row_dict)
    return list_of_data_dict


def true_false_for_column_group(data: dict, columns: list[str]) -> str:
    text = ''
    for column in columns:
        if data[column] == 1:
            text += column + ', '
        else:
            continue
    return text


def documents_to_dict(data: list[dict]) -> list[dict]:
    new_dict_list = []
    for element in data:
        new_dict = {
            'auto_make' : element["Make"],
            'auto_model' : element["Model"],
            'auto_year' : element["auto_year"],
            'age' : element["age"],
            'sex' : element["insured_sex"],
            'education_level' : element["insured_education_level"],
            'relationship' : element["insured_relationship"],
            'previous_accidents' : {
                'injuries' : true_false_for_column_group(element, ['No Injuries Reported', 'Minor', 'Moderate', 'Serious', 'Fatality']),
                'crash_speed' : element["SV Precrash Speed (MPH)"],
                'conditions' : true_false_for_column_group(element, ['high light', 'low light', 'medium light', 'weather_is_clear', 'weather_is_snow', 'weather_is_cloudy', 'weather_is_fog', 'weather_is_rain', 'weather_is_severe_wind', ]),
            }
        }
        new_dict_list.append(new_dict)
    return new_dict_list


def embed_pipeline(documents: list[dict]):
    new_list_of_dicts = []
    for document in documents:
        try:
            string_document = str(document)
            vector_embedding = embed(string_document)
            dictionary = ast.literal_eval(string_document)
            dictionary["embedding"] = vector_embedding
            new_list_of_dicts.append(dictionary)
        except:
            continue
    return new_list_of_dicts


list_of_data_dict = pre_process_df(df)
preprocessed_dicts = documents_to_dict(list_of_data_dict)
x = embed_pipeline(preprocessed_dicts)