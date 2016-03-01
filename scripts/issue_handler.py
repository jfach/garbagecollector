import json
import requests
import configmanager

cm = configmanager.ConfigManager()
git_credentials = (cm.git_user, cm.git_pass)
issues_url = cm.issues_url

def gen_issue(asset):
	if asset.result_code == 0:
		# all good, no need for an issue
		return False
	elif asset.result_code == 1:
		# No DNS
		title = ("Garbage-Collection: "
			     "{0} not in DNS").format(asset.ip)
		body = ("Details:\n"
		        "{0} is present on the network and not found in DNS.")
		body = body.format(asset.ip)
		body += "\n\nRC: 1"
		if check_issue(get_issues(), asset.ip, "RC: 1"):
			create_issue(title, body)
	elif asset.result_code == 2:
		# Only found in some AD
		title = ("Garbage-Collection: "
			     "{0} not in some AD servers").format(asset.ip)
		body = ("Details:\n"
		        "Hostname: {0}\n"
		        "{1} is present on the network "
			    "and not found in some AD servers.")
		body = body.format(asset.name, asset.ip)
		table = ("\n\n| Controller | Result |\n"
			     "| ---------- | ------ |")
		for result in asset.ad_results:
			table += "\n|{0}|{1}|".format(
					result,
					asset_collect.ad_results[result])
		body += table + "\n\nRC: 2"
		if check_issue(get_issues(), asset.ip, "RC: 2"):
			create_issue(title, body)
	elif asset.result_code == 3:
		# Not found on any AD
		title = ("Garbage-Collection: "
			    "{0} not in any AD servers").format(asset.ip)
		body = ("Details:\n"
			"Hostname: {0}\n"
			"{1} is present on the network "
			"and not found in any AD servers.")
		body = body.format(asset.name, asset.ip)
		table = ("\n\n| Controller | Result |\n"
			     "| ---------- | ------ |")
		for result in asset.ad_results:
			table += "\n|{0}|{1}|".format(
					result,
					asset.ad_results[result])
		body += table + "\n\nRC: 3"
		if check_issue(get_issues(), asset.ip, "RC: 3"):
			create_issue(title, body)
	else:
		# incorrect result code
		return False

def create_table(arg):
	return False

def create_issue(title, body):
	url = issues_url
	payload = {"title": title,
               "body": body,
		       "labels": ["info:garbage-collection"]}
	req = requests.post(url,
			            data=json.dumps(payload),
			            auth=git_credentials)

def get_issues():
	url = issues_url
	payload = {"state": "open", "labels": "info:garbage-collections"}
	req = requests.get(url,
                       data=json.dumps(payload),
		               auth=git_credentials)
	return req.json()

def check_issue(issues, ip, result_code):
	for issue in issues:
		if ip in issue['title']:
			if result_code in issue['body']:
				return False
	return True


