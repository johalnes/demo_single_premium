import datetime
import random
import numpy as np
import pandas as pd


def random_date(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

def create_data_file(N=1000,filename='policy_data.xlsx'):
    birth_days=np.array([ random_date(datetime.datetime(1960,1,1), datetime.datetime(1985,1,1)) for _ in range(N)])
    gender = np.array([random.choice(['M','F']) for _ in range(N)])
    interest_rate=np.array([random.choice([0.01,0.02,0.04]) for _ in range(N)])
    A6499 = np.array([random.randint(100,25000) for _ in range(N)])
    A6799 = np.array([random.randint(100,25000) for _ in range(N)])
    col_names = ['birth_day', 'gender', 'interest_rate', 'A6499', 'A6799']

    df=pd.DataFrame([birth_days, gender, interest_rate, A6499, A6799]).T
    df.columns=col_names
    df.to_excel(os.path.join(data_folder_raw,filename))

    return None



