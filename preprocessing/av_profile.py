# %%
import pandas as pd

# %%
data = pd.read_csv('Human-Driving and AV Crash Data/Self-Driving Crash Datasets/SGO-2021-01_Incident_Reports_ADAS.csv')

# %%
data = data[data['Driver / Operator Type'] == 'Consumer']

# %%
data.info

# %%
data.iloc[:, 10:]

# %%
data.columns

# %%
feature_list = [10, 11, 38, 67, 71, 72, 73, 74, 75, 76, 77, 84, 98, 66, 69, 102, 85, 99, 82]

# %%
data_features = pd.DataFrame()
for i in feature_list:
    data_features[data.columns[i]] = data[data.columns[i]]

# %%
data_features.info()

# %%
data_features.columns

# %%
'''
weather_conditions = {
    'Weather - Clear': 'Clear',
    'Weather - Snow': 'Snow',
    'Weather - Cloudy': 'Cloudy',
    'Weather - Fog/Smoke': 'Fog/Smoke',
    'Weather - Rain': 'Rain',
    'Weather - Severe Wind': 'Severe Wind'
}

# Apply a lambda function to create the new column
data_features['Weather Conditions'] = data_features.apply(
    lambda row: [condition for col, condition in weather_conditions.items() if row[col] == 'Y'],
    axis=1
)
drop_list = ['Weather - Clear','Weather - Snow','Weather - Cloudy','Weather - Fog/Smoke','Weather - Rain','Weather - Severe Wind']
data_features.drop(columns=drop_list, inplace=True)
'''

# %%
data_features['weather_is_clear'] = data_features['Weather - Clear'].apply(lambda x: 1 if x == 'Y' else 0)
data_features['weather_is_snow'] = data_features['Weather - Snow'].apply(lambda x: 1 if x == 'Y' else 0)
data_features['weather_is_cloudy'] = data_features['Weather - Cloudy'].apply(lambda x: 1 if x == 'Y' else 0)
data_features['weather_is_fog'] = data_features['Weather - Fog/Smoke'].apply(lambda x: 1 if x == 'Y' else 0)
data_features['weather_is_rain'] = data_features['Weather - Rain'].apply(lambda x: 1 if x == 'Y' else 0)
data_features['weather_is_severe_wind'] = data_features['Weather - Severe Wind'].apply(lambda x: 1 if x == 'Y' else 0)

drop_list = ['Weather - Clear','Weather - Snow','Weather - Cloudy','Weather - Fog/Smoke','Weather - Rain','Weather - Severe Wind']
data_features.drop(columns=drop_list, inplace=True)

# %%
data_features

# %%
data_features = data_features[data_features['Highest Injury Severity Alleged'] != 'Unknown']
# data_features = data_features[data_features['SV Pre-Crash Movement'] != 'Unknown']
# data_features = data_features[data_features['SV Pre-Crash Movement'] != 'Other, see Narrative']
data_features = data_features[data_features['Lighting'] != 'Unknown']
data_features = data_features[data_features['Lighting'] != 'Other, see Narrative']
data_features = data_features[data_features['SV Precrash Speed (MPH)'] != 'Unknown']

# %%
data_features['Highest Injury Severity Alleged'].value_counts()

# %%
severity_mapping = {
    'No Injuries Reported': 1,
    'Minor': 2,
    'Moderate': 3,
    'Serious': 4,
    'Fatality': 5
}

# Apply the mapping to create a new column
data_features['Injury_Severity_Category'] = data_features['Highest Injury Severity Alleged'].map(severity_mapping)

# %%
data_features['Lighting'].value_counts()

# %%
lighting_mapping = {
    'Daylight' : 1,
    'Dark - Lighted' : 2,
    'Dark - Not Lighted' : 3,
    'Dark - Unknown Lighting' : 3,
    'Dawn / Dusk' : 2
}

data_features['lighting_category'] = data_features['Lighting'].map(lighting_mapping)

# %%
data_features

# %%
import numpy as np

# %%
# liability is fabricated
data_features['liability'] = np.random.randint(2, 5, size=len(data_features)) // 2


# %%
data_features

# %%
severity_counts = data_features.groupby(['Make', 'Model', 'Injury_Severity_Category']).size().unstack(fill_value=0)
#severity_ratios = severity_counts.div(severity_counts.sum(axis=1), axis=0)

severity_counts.reset_index(inplace=True)
severity_counts.columns = ['Make', 
                           'Model',
                           'No Injuries Reported',
                           'Minor',
                           'Moderate',
                           'Serious',
                           'Fatality']
#severity_ratios
severity_counts

# %%
avg_speed_df = data_features.groupby(["Make", "Model"], as_index=False)["SV Precrash Speed (MPH)"].mean()
avg_speed_df

# %%
lighting_counts = data_features.groupby(['Make', 'Model', 'lighting_category']).size().unstack(fill_value=0)
# lighting_ratios = lighting_counts.div(severity_counts.sum(axis=1), axis=0)

lighting_counts.reset_index(inplace=True)
lighting_counts.columns = ['Make', 
                           'Model',
                           'high light',
                           'medium light',
                           'low light'
                           ]
                           
lighting_counts

# %%
weather_counts = data_features.groupby(['Make', 'Model', 
                                        'weather_is_clear', 
                                        'weather_is_snow', 
                                        'weather_is_cloudy', 
                                        'weather_is_fog',
                                        'weather_is_rain',
                                        'weather_is_severe_wind'
                                        ]).size().unstack(fill_value=0)

weather_counts.reset_index(inplace=True)
weather_counts.columns = ['Make', 'Model', 
                            'weather_is_clear', 
                            'weather_is_snow', 
                            'weather_is_cloudy', 
                            'weather_is_fog',
                            'weather_is_rain',
                            'weather_is_severe_wind'
                            ]
                           
weather_counts

# %%
liability_counts = data_features.groupby(['Make', 'Model', 'liability']).size().unstack(fill_value=0)

liability_counts.reset_index(inplace=True)
liability_counts.columns = ['Make', 'Model', 
                            'Subject Vehicle Liability', 
                            'Other Vehicle Liability'
                            ]
                           
liability_counts

# %%
model_stats = pd.merge(severity_counts, avg_speed_df, on=['Make', 'Model'])
model_stats = pd.merge(model_stats, lighting_counts, on=['Make', 'Model'])
model_stats = pd.merge(model_stats, weather_counts, on=['Make', 'Model'])
model_stats = pd.merge(model_stats, liability_counts, on=['Make', 'Model'])
# model_stats.drop(columns=['index'], inplace=True)
model_stats = model_stats.drop_duplicates(subset=['Model'], keep='first')  # 'column_name' is the name of your column
model_stats.reset_index(drop=True, inplace=True)
model_stats

# %%
# model_stats.to_csv('model_stats.csv', index=False)


