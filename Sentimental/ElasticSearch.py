from elasticsearch import helpers, Elasticsearch
import csv
import warnings
import filesname


# authentication tokens
auth = ('admin', 'NWJNWMJBDGSOXTPW')
index_value = 'senti'
doc_value = 'senti'
hostname_port = 'https://portal-ssl504-12.bmix-lon-yp-a9a1234e-76c2-42d0-96f1-fd4906a717d4.3649481945.composedb.com:' \
                '29874/'


# ignore certificate warnings
warnings.filterwarnings("ignore")


# making connection to elastic search
test = Elasticsearch(hostname_port, http_auth=auth, use_ssl=True, verify_certs=False)


# uploading data to cloud
def elatic_data_upload():
    with open(filesname.sentimentalfinal) as file:
        reader = csv.DictReader(file)
        print("Uploading ........")
        print("------------------------------------------------------------------------------------------------------"
              "--")
        helpers.bulk(test, reader, index=index_value, doc_type=doc_value)

def elastic_data_search():
    print(test.search(index='senti', body={'query': {'match_all': {}}}))


elatic_data_upload()
print("Completed Uploading")
print("--------------------------------------------------------------------------------------------------------")
print("Searching........")
print("--------------------------------------------------------------------------------------------------------")
elastic_data_search()

