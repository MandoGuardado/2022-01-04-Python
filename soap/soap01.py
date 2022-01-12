#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   Using the requests library to service SOAP APIs"""

# python3 -m pip install requests
import requests

def main():
    # SOAP request URL
    url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
      
    # structured XML
    payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
                <soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
                    <soap:Body>
                        <CountryIntPhoneCode xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
                            <sCountryISOCode>IN</sCountryISOCode>
                        </CountryIntPhoneCode>
                    </soap:Body>
                </soap:Envelope>"""
    # headers
    headers = {
        'Content-Type': 'text/xml; charset=utf-8'
    }
    # POST request
    response = requests.request("POST", url, headers=headers, data=payload)
      
    # print the response
    print(response.text)
    print(response)
    
if __name__ == "__main__":
    main()

