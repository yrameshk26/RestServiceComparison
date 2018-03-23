import yaml
import ast
from RequestRest import runSBS
from RequestRest import saveToFile


configData = []
with open("../config/offerInfo.yml", 'r') as stream:
	try:
		configData = yaml.load(stream)
		print('Successfully Loaded config Data')
	except yaml.YAMLError as exc:
		print(exc)
			
base_url_dc_1 = configData['base_url_dc_1']
base_url_dc_2 = configData['base_url_dc_2']
componentCodes =  configData['componentCodes']
username = configData['username']
password = configData['password']
try :
	headers = ast.literal_eval(configData['headers'])
except :
	headers = []

saveToFile('../reports/error.log', 'Running SBS Test for Offer Component')
		
for componentCode in componentCodes.split(","):
	runSBS(base_url_dc_1, base_url_dc_2, componentCode, username, password, headers) 