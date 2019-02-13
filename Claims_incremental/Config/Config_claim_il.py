from datetime import datetime

resolution_claim_file = "../Input/Resolution_claims.txt"
claim_primary_exposure_file = "../Input/claim_primary_exposure.csv"
group_type_file = "../Input/group_type.txt"
claim_il_table = "claim_il"
claim_headers = ["claim_id","claim_claimnumber", "policy_number", "incident_id", "claim_lossdate", "claim_reporteddate", "claim_status", "claim_closedate", "claim_losstype", "claim_lob", "claim_severity", "claim_loss_add_state","claim_glass_ind","claim_primary_group","claim_primary_adjuster_id","claim_litigation_ind","claim_subrogation_status","claim_salvage_status","claim_litigation_status","claim_fatalities","claim_large_loss","claim_coverage_in_question","claim_siu_status","claim_siu_score","claim_resolution"]

# datetime in the format of year, month, date
claim_start_date = datetime(2018,1,1)
claim_end_date = datetime(2019,1,31)

claim_siu_status = {"Assigned":0.1, "Unassigned":0.9}
claim_litigation_status = {"Open":0.6, "Close":0.4}

connection_string = 'postgresql://data:gen123@10.20.202.43:5432/datagen'

min_siu_score = 1

max_siu_score = 10

litigation_ind = {"Y":0.1, "":0.9}

fatalities = {"Y":0.6, "":0.4}

large_loss = {"Y":0.6, "":0.4}

coverage_in_quest = {"Y":0.6, "":0.4}