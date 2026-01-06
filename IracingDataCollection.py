from iracingdataapi.client import irDataClient
use_pydantic=True

USERNAME = "probala24@gmail.com"
PASSWORD = "Iamthebest#420"

idc = irDataClient(access_token=[]

driver_Name = "Max Probala"

drivers_lookup = idc.lookup_drivers(search_terms=driver_Name)

if drivers_lookup and drivers_lookup.data:
    customer_id = drivers_lookup.data[0]['cust_id']
    print(f"Found {driver_Name} with Customer ID: {customer_id}")

    driver_stats = idc.driver_stats(cust_id=customer_id)

    if driver_stats and driver_stats.data:
        print(f"Career iRating: {driver_stats.data['career_stats']['irating']}")
        print(f"Career License Class: {driver_stats.data['career_stats']['license_class']}")
    else:
        print("Could not retrieve driver stats.")   
else:
    print(f"Driver '{driver_Name}' not found or an error occurred.")
