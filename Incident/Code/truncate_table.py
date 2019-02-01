from sqlalchemy import create_engine, text

def truncate(table_name):
	engine = create_engine('postgresql://data:gen123@10.20.202.43:5432/datagen')
	connection = engine.connect()
	truncate_query = text("DROP TABLE "+table_name)
	connection.execution_options(autocommit=True).execute(truncate_query)

#truncate(table_name)