import os
import urllib.parse
import random
import sys
print("python3 noisy.py url")
url = "https://developers.facebook.com/tools/debug/echo/?q=http://googleweblight.com/?lite_url=https://www.nsa.gov/DesktopModules/ArticleCS/RSS.ashx?ContentType=1&Site=1282&max=50000&s=1000000&source=wax-m"

parsed_url = urllib.parse.urlsplit(url)
query = parsed_url.query

# creates a dictionary of parameters and their values
parameters = urllib.parse.parse_qs(query)

noise_value = os.urandom(random.randint(32,128))

for key, value in parameters.items():
    value =  bytes(value[0], "utf-8")
    # add the noise value to the value
    value += noise_value
    parameters[key] = value

# rebuild the query string with the modified parameters
query = urllib.parse.urlencode(parameters, doseq=True)

# rebuild the URL with the modified query string
url = urllib.parse.urlunsplit((parsed_url.scheme, parsed_url.netloc, parsed_url.path, query, parsed_url.fragment))

curl_command = f"curl -b 'c_user=cookie; xs=cookie' -X GET {url} "
r = os.popen(curl_command).read()
print(r)



