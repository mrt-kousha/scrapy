from scrapy import signals
import os
from scrapy.conf import settings


# Send "Change IP" signal to tor control port 
class TorMiddleware(object):
	def process_request(self, request, spider):
		"""
			You must first install the nc program and Tor service on your GNU Linux operating system
			After that and change /etc/tor/torrc, add
			control port and password to it.
			install privoxy for having HTTP and HTTPS over torSOCKS5
		"""
		# Deploy : add controlport and password to /etc/tor/torrc
		os.system("""(echo authenticate '"yourpassword"'; echo signal newnym; echo quit) | nc localhost 9051""")
		request.meta['proxy'] = settings.get('HTTP_PROXY')

