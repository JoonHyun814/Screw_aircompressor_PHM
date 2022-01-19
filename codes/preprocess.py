import numpy as np
import pandas as pd


def slice_window(data: np.ndarray,sequence_num: int,step: int) -> np.ndarray:
    """긴 시계열 데이터를 정해진 간격으로 정해진 길이의 sequence data로 바꾸어 줍니다.

    Args:
        data (np.ndarray): 초기의 긴 시계열 데이터
        sequence_num (int): window 크기
        step (int): window 간 sequence 간격

    Returns:
        (np.ndarray): 일정한 크기의 여러 개의 window 모음
    """    
    X_train = [data[i:i+sequence_num] for i in range(0,len(data)-sequence_num,step)]
    return np.array(X_train)


def normalization(data: pd.DataFrame , param_dict: dict) -> pd.DataFrame:
    """범위를 0~1로 만들어주는 함수

    Args:
        data (pd.DataFrame): 원본 data
        param_dict (dict): normalization할 "feature_name": (max,min)

    Returns: normalization된 data
        pd.DataFrame:
    """    
    for k,v in param_dict.items():
        data[k] = (data[k] - v[1])/(v[0]-v[1])
    return data