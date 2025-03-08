import warnings
import urllib3

# Suppress only InsecureRequestWarning
warnings.simplefilter("ignore", urllib3.exceptions.InsecureRequestWarning)