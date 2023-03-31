from google.cloud import bigquery
from google.oauth2 import service_account
import json

#pip install google-cloud
#pip install google-cloud-bigquery[pandas]
#pip install google-cloud-storage

def query_dict(query):
    #from flask import jsonify
    #returns data with json from a query to bigquery
    key_path = './ripa-1022-9e33467b33c4.json'
    credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    client = bigquery.Client(credentials=credentials, project=credentials.project_id,)

    query_job = client.query(query)
    records = [dict(row) for row in query_job] #transforma en diccionario y luego en json
    #json_obj = json.dumps(str(records))
    return records #jsonify(records) #using functionality json



def pubs_detail(slug):
    query = """
        SELECT id_gs,id_insttitution as institution,title,authors,journal,cites,year FROM `ripa-1022.gscholar.pubs` 
        where id_gs =  '""" + slug +"'"
        
    return query_dict(query)


print(pubs_detail("EQfyAUAAAAAJ"))

