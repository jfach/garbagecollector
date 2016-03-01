class Asset():
	
	def __init__(self,
		     ip,
		     ad_checked,
		     ad_present,
		     result_code,
		     name=None):
		self.ip = ip
		self.ad_checked = ad_checked
		self.ad_present = ad_present
		self.result_code = result_code
		self.ad_results = {}
		for ad in ad_checked:
			if ad.name not in ad_present:
				self.ad_results[ad.name] = "Not Present"
			else:
				self.ad_results[ad.name] = "Present"
		if name:
			self.name = name

