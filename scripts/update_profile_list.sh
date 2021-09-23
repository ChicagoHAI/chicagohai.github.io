# !/bin/bash

echo "Update Profile CSV"
curl -L "https://docs.google.com/spreadsheets/d/1mXljUtLB_Ry_FsCKY2CMaRVEutHy5R-wocbRDFAK2sY/export?format=csv" > scripts/data/profile.csv
python -m scripts.src.generate_profile_list