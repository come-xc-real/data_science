import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://eastmoney_db:5ncafabJBn8HydfP@47.109.54.146/eastmoney_db')
df = pd.read_sql('SELECT * FROM stock_report', engine)
df.to_csv('东方财富网个人股票报告数据.csv', index=False)
