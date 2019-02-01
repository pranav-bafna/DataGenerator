from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine('postgresql://data:gen123@10.20.202.43:5432/datagen')
connection = engine.connect()
table_names = engine.table_names()
#truncate_query = text("DROP TABLE "+table_name)
#connection.execution_options(autocommit=True).execute(truncate_query)


for table in table_names:
	path = "/elastic_search_test/Tables data/" + table + ".csv"
	print path 
	data_q = text("select * from "+table)
	data = connection.execute(data_q).fetchall()
	headers = connection.execute(data_q).keys()
	df = pd.DataFrame(data,columns = headers)
	df.to_csv(path, index = False, encoding = 'utf-8')

