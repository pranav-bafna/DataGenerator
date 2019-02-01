headers = ["policysource", "policynumber", "policylob", "policytype","policystate","policyaddressid","termeffectivedate","termexpirationdate","policyinceptiondate","renewal_cycle","renewalterm","policystatus","policystatusreason","premiumamount","recordstartdate","recordenddate"]
total_records = 25000
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
contact_id_file = "/input/id_list.csv"
table_name = "policy"
table_il = "policy_il"
source = ["System1","System2","System3"]
inception_year_probabilty = {"2000-2015":0.2, "2015-2018":0.7, "current_year":0.1}