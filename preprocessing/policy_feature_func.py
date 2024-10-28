from av_profile_func import create_av_profile
from user_profile_func import create_user_profile
import pandas as pd

def create_policy_features(av_path, user_path):
    '''
    takes in path for av data
    takes in path for user data

    returns a df of policy features including both av and user profile
    '''

    av_profile = create_av_profile(av_path)
    user_profile = create_user_profile(user_path)

    sample_av = av_profile.sample(n=50).reset_index(drop=True)
    sample_user = user_profile.sample(n=50).reset_index(drop=True)

    policy_sample = pd.concat([sample_av, sample_user], axis=1)

    return policy_sample