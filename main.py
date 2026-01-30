import requests

def get_document_from_github(target_url):
    try:
        #1. requests to github
        response = requests.get(target_url)
        
        #2. check status (200 is ok)
        if response.status_code == 200:
            # setting to support thailand language
            response.encoding = 'utf-8'
            
            #3. content to text
            content = response.text
            return content
        else:
            return f"X not found file. (Error Code: {response.status_code})"
    except Exception as e: # ย้ายมาให้ตรงกับ try
        return f"Error not connect to server: {e}"
	   	    	
# test program
# example : pull text from github
url = "https://raw.githubusercontent.com/python/cpython/main/LICENSE"
document_text = get_document_from_github(url)

print("starting to read document")
print(document_text)
print("ending to read document")
