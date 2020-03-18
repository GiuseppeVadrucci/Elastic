# Import Elasticsearch package 
from elasticsearch import Elasticsearch 
# Connect to the elastic cluster


#Authentication with user and pass in http_auth
es = Elasticsearch([{'host': 'localhost', 'port': 9200}],http_auth=('', '')) 


i = 1

with open('filejson') as data_file:
	for line in data_file:
		
		res = es.index(index='test2',doc_type='sensordata',id=i+100000,body=line)
		i+=1
