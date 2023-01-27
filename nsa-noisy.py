import urllib.parse
import random
import requests
import base64

def add_noise_to_url(url: str) -> str:
    parsed_url = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parsed_url.query)
    for key, value in query.items():
        # Add random byte noise to the value
        noise = bytes([random.randint(0, 255) for _ in range(3)])
        noise_str = base64.b64encode(noise).decode()
        query[key] = [value[0] + noise_str]
    # Update the query string and return the modified URL
    new_query = urllib.parse.urlencode(query, doseq=True)
    return parsed_url._replace(query=new_query).geturl()

cookies = {'c_user': '[cookie]', 'xs': '[cookie]'}
original_url = "https://developers.facebook.com/tools/debug/echo/?q=http://googleweblight.com/?lite_url=https://www.nsa.gov/DesktopModules/ArticleCS/RSS.ashx?ContentType=1&Site=1282&max=20&s=1&source=wax-m"
noisy_url = add_noise_to_url(original_url)


r = requests.get(noisy_url, allow_redirects=False, cookies=cookies)
print(r.text)
