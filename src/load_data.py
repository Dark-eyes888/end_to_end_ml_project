# get data and load in data/raw file 
import os
import argparse
from get_data import get_data,read_params

def load_and_save(config_path):
    config= read_params(config_path)
    df=get_data(config_path)
    cols=[cols.replace("  ","_") for cols in df.columns]
    raw_path= config['load_data']['raw_dataset_csv']
    df.to_csv(raw_path,sep=',',index=False,header=cols)
  

if __name__ == '__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--config',default='params.yaml')
    param_args=args.parse_args()
    load_and_save(param_args.config)