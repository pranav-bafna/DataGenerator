Coverage_limits = [
    "$15k/30k/10k",
    "$25k/50k/10k",
    "$50k/100k/10k",
    "$50k/100k/15k",
    "$100k/300k/10k",
    "$100k/300k/15k",
    "$100k/300k/25k"]

#cl_file_path = '../Input/coverage_limit.csv'
cl_headers = ["coverage_id", "coverage", "coverage_limit"]
coverage_names = ["BI", "PD", "Uninsured", "Underinsured", "Medical Payments"]
cl_table_name = 'coverage_limit'

#cl_file_path = '../Output/Coverage_limits.csv'
c_headers = ["coverage_id", "coverage_name", "vin", "policy_number", "record_start_date", "record_end_date", "record_update_date"]
#VIN_data_path = '/elastic_search_test/Unique_VIN_Data.csv'
#policy_data_path = '/elastic_search_test/policy_data.csv'
c_table_name = 'coverage'