# %%
import pandas as pd

# %%
data = pd.read_csv('Insurance Claims Data/insurance_claims.csv')

# %%
data['incident_type'].value_counts()

# %%
data.info()

# %%
feature_list = [0,1,10,11,14,37]

# %%
data_features = pd.DataFrame()
for i in feature_list:
    data_features[data.columns[i]] = data[data.columns[i]]

# %%
data_features

# %%
data_features['insured_education_level'].value_counts()

# %%
education_mapping = {
    'High School': 1,
    'Associate': 2,
    'College': 2,
    'JD': 3,
    'MD': 3,
    'Masters': 3,
    'PhD': 3
}

# Apply the mapping to the column
data_features['insured_education_level_category'] = data_features['insured_education_level'].map(education_mapping)


# %%
data_features['insured_relationship'].value_counts()

# %%
relationship_mapping = {
    'unmarried' : 1,
    'other-relative' : 1,
    'not-in-family' : 1,
    'husband' : 2,
    'wife' : 2,
    'own-child' : 3
}

data_features['insured_relationship_category'] = data_features['insured_relationship'].map(relationship_mapping)

# %%
data_features['sex_encoded'] = data_features['insured_sex'].apply(lambda x: 1 if x == 'MALE' else 2)

# %%
data_features

# %%
# data_features.to_csv('user_profile.csv', index=False)

# %%
# data_features.drop(columns=['insured_education_level', 'insured_relationship', 'insured_sex'], inplace=True)


