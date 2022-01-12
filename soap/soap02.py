#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   Using the zeep library to service SOAP APIs"""

# python3 -m pip install zeep
import zeep

# set the WSDL URL
wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

# set method URL
method_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryIntPhoneCode"

# set service URL
service_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

# create the header element
header = zeep.xsd.Element(
    "Header",
    zeep.xsd.ComplexType(
        [
            zeep.xsd.Element(
                "{http://www.w3.org/2005/08/addressing}Action", zeep.xsd.String()
            ),
            zeep.xsd.Element(
                "{http://www.w3.org/2005/08/addressing}To", zeep.xsd.String()
            ),
        ]
    ),
)
# set the header value from header element
header_value = header(Action=method_url, To=service_url)

# initialize zeep client
client = zeep.Client(wsdl=wsdl_url)

# set country code for United States
country_code = "US"

# make the service call
result = client.service.CountryIntPhoneCode(
    sCountryISOCode=country_code,
    _soapheaders=[header_value]
)

# print the result
print(f"Phone Code for {country_code} is {result}")


# set country code for Japan
country_code = "JP"

# make the service call
result = client.service.CountryIntPhoneCode(
    sCountryISOCode=country_code,
    _soapheaders=[header_value]
)

# print the result
print(f"Phone Code for {country_code} is {result}")
print(result)

