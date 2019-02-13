from datetime import datetime

claim_primary_exposure_file = "../input/claim_primary_exposure.csv"
group_type_file = "../input/group_type.txt"
resolution_claim_file = "../input/Resolution_claims.txt"

reported_days = 5

no_of_exp = 1000

exp_headers = ["exposure_id","exp_createdate","exp_claim_id","exp_lossparty","exp_coverage_id","exp_incident_id","exp_vehicle_id","exp_group","exp_type","exp_closedate","exp_status","exp_resolution"]
claim_headers = ["claim_id","claim_claimnumber", "policy_number", "incident_id", "claim_lossdate", "claim_reporteddate", "claim_status", "claim_closedate", "claim_losstype", "claim_lob", "claim_severity", "claim_loss_add_state","claim_glass_ind","claim_primary_group","claim_primary_adjuster_id","claim_litigation_ind","claim_subrogation_status","claim_salvage_status","claim_litigation_status","claim_fatalities","claim_large_loss","claim_coverage_in_question","claim_siu_status","claim_siu_score","claim_resolution"]

# datetime in the format of year, month, date
claim_start_date = datetime(2018,1,1)
claim_end_date = datetime(2019,1,31)

exp_start_date = datetime(2018,10,1)
exp_end_date = datetime(2018,12,31)

claim_table_name = "cc_claims"
exp_table_name = "exposure"

exp_status_within_dates = {"Open":0.8, "Closed":0.2}
exp_status_outside_dates = {"Open":0.2, "Closed":0.8}
exp_close_date = datetime(2019,2,5)

claim_siu_status = {"Assigned":0.1, "Unassigned":0.9}
claim_litigation_status = {"Open":0.6, "Close":0.4}

exp_lossparty_stutus = {"Insured":0.65, "Thirdparty":0.35}

litigation_ind = {"Y":0.1, "":0.9}

fatalities = {"Y":0.6, "":0.4}

large_loss = {"Y":0.6, "":0.4}

coverage_in_quest = {"Y":0.6, "":0.4}

min_glass_close_days = 15
max_glass_close_days = 20

min_other_close_days = 35
max_other_close_days = 40

min_siu_score = 1

max_siu_score = 10

pivot_claims_for_exp_file = "../output/pivot_claims_for_exp_5.csv"

connection_string = 'postgresql://data:gen123@10.20.202.43:5432/datagen'