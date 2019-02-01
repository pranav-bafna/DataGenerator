expcar_file_path = "../Input/expcars_make_model.csv"
othercar_file_path = "../Input/othercars_make_model.csv"
#vehicle_data_path = "../Output/vehicle_data_1L.csv"
VIN_file_path = "../Input/Unique_VIN_Data_5m.csv"
headers = ["vin", "license_plate_no", "car_make", "car_model", "year", "price", "car_age", "mileage"]
num_records = 100000
string_length = 16
car_distribution = [0.08,0.92]
min_othercar_price = 35000
max_othercar_price = 70000
min_expcar_price = 65000
max_expcar_price = 99999
min_car_age = 1
max_car_age = 10
min_car_mileage = 8
max_car_mileage = 18
output_table_name = 'vehicle'