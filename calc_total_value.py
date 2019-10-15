import numpy as np

def calc_total_value(cash_history, asset_value_history_dic,step):
    total_asset_value = 0
    for stock in  asset_value_history_dic.keys():
        total_asset_value  += asset_value_history_dic[stock][step]
    
    total_value = cash_history[step] + total_asset_value

    return total_value