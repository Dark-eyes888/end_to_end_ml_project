# read param 
# preprocess 
# return dataframe
import os
from re import L
import yaml
import pandas as pd
import numpy as np
import argparse



def read_params(config_path):
    with open(config_path) as f:
        config=yaml.safe_load(f)
    return config

def get_data(config_path):
    config= read_params(config_path)
    data_path=config["data_source"]["s3_source"]
    df= pd.read_csv(data_path,sep=',')
    return df

if __name__ == '__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--config',default='params.yaml')
    param_args=args.parse_args()
    data =get_data(param_args.config)

print(data)