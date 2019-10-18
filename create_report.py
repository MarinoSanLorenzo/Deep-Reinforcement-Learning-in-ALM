# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:20:11 2019

@author: msanl
"""
import pandas as pd

def createReport(env):
    
    df_stocks = pd.DataFrame.from_dict(env.stocks_history_dic)
    print(len(df_stocks))
    df_actions = pd.DataFrame.from_dict(env.action_history_dic).transpose()
    print(len(df_actions))
    df_total_value = pd.Series(env.total_value_history)
    print(len(df_total_value))
    df_nb_stocks = pd.DataFrame.from_dict(env.agent.asset_nbstock_history_dic)
    print(len(df_nb_stocks))
    df_vstocks = pd.DataFrame.from_dict(env.agent.asset_vstock_history_dic)
    print(len(df_vstocks ))
    df_asset_value = pd.DataFrame.from_dict(env.agent.asset_value_history_dic)
    print(len(df_asset_value))
    df_cash = pd.Series(env.agent.cash_history)
    print(len(df_cash))
    df_profit = pd.Series(env.agent.profit_history)
    print(len(df_profit ))
#    df = pd.concat([df_stocks,df_actions,df_total_value, df_nb_stocks, df_vstocks, df_asset_value, df_cash,  df_profit ])
#    
    return df        