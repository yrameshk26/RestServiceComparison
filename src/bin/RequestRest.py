import requests
import sys
import ast
from CompareResponse import compareOutputs


def saveToFile(file_path, obj):
	orig_stdout = sys.stdout
	file = open(file_path, 'w')
	sys.stdout = file
	print(obj)
	sys.stdout = orig_stdout
	file.close()


def appendToFile(file_path, obj):
	orig_stdout = sys.stdout
	with open(file_path, 'a') as file:
		sys.stdout = file
		print(obj)
		sys.stdout = orig_stdout
	file.close()

def runSBS(base_url_dc_1, base_url_dc_2, path_param, username, password, headers):

	response_a = requests.get(base_url_dc_1 + path_param,
							  verify=False, auth=(username, password), headers=headers)

	response_b = requests.get(base_url_dc_2 + path_param,
							  verify=False, auth=(username, password), headers=headers)

	if response_a.status_code != 200 or response_b.status_code != 200:
		print("Requests weren't Successful")
	else:
		orig_stdout = sys.stdout

		errorText = 'Errors found for the parameter ' + path_param
		appendToFile('../reports/error.log', errorText)

		saveToFile('../reports/response1.json', response_a.text)
		saveToFile('../reports/response2.json', response_b.text)
		print('Compare JSON result is: ', compareOutputs())
