import urllib3
import os


def get_data(url):
    s = url.split('/')
    filename = s[len(s) - 1]
    # if file exists, return none
    if os.path.exists(filename):
        return None
    # if file does not exist, download from url
    else:
            # if url is valid,download and return true
        try:
            http = urllib3.PoolManager()
            response = http.request('GET', url)
            with open(filename, 'wb') as f:
                f.write(response.data)
            return True
            # if url is not valid, raise exeption
        except:
            raise ValueError("URL is not valid.")



def remove_data(filename):
    if os.path.exists(filename):
        os.remove(filename)
        return True
    else:
        raise ValueError("File does not exist.")


