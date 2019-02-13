headers = ["incident_id", "incident_vin", "is_the_vehicle_driveable", "driver", "inc_desc"]
lower_limit = 10
upper_limit = 20
inc_des_path = "../Input/inc_sample_desc.csv"
table_name = "incident_il"
connection_string = 'postgresql://data:gen123@10.20.202.43:5432/datagen'
vehicle_driveable_flag = {"Y":0.8, "":0.2}