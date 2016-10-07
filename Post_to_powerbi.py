#<-----Shebang------>
# coding=utf-8

import urllib2
imoprt time

def post(url,data):

'''Function to post data to powerbi streaming dataset.
  
   Argv: PowerBI rest API url 
  
   Output: Returns the HTTP response code 
  
   Dependencies: urllib2 and time packages
'''
    try:
        # make HTTP POST request to Power BI REST API
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        print("POST request to Power BI with data:{0}".format(data))
        print("Response: HTTP {0} {1}\n".format(response.getcode(), response.read()))
        return [response.getcode(),response.read()]
        time.sleep(1)
       
    except urllib2.HTTPError as e:
        return [e.reason,e.code]
        
    except urllib2.URLError as e:
        return [e.reason,e.code]
        
    except Exception as e:
        return [e.reason,e.code]
        
