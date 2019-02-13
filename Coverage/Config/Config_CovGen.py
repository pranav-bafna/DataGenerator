cov_id_prefix = "COV01-1"
id_length = 6
cov_probability = [0.5,0.5]

Coverage_limits = [
    "$15k/30k/10k",
    "$25k/50k/10k",
    "$50k/100k/10k",
    "$50k/100k/15k",
    "$100k/300k/10k",
    "$100k/300k/15k",
    "$100k/300k/25k"]

cl_headers = ["coverage_id", "coverage", "coverage_limit"]
coverage_names = ["BI", "PD", "Uninsured", "Underinsured", "Medical Payments"]
cl_table_name = 'coverage_limit'


c_headers = ["coverage_id", "coverage_name", "vin", "policy_number", "coverage_status", "record_start_date", "record_end_date", "record_update_date"]
c_table_name = 'coverage'

connection_string = 'postgresql://data:gen123@10.20.202.43:5432/datagen'