# finbourne_identity.DomainsApi

All URIs are relative to *https://www.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_domain**](DomainsApi.md#create_domain) | **POST** /api/domains | Create Domain
[**get_agreement**](DomainsApi.md#get_agreement) | **HEAD** /api/domains/me/agreements/{agreement} | Get Agreement
[**get_my_domain**](DomainsApi.md#get_my_domain) | **GET** /api/domains/me | Get current Domain
[**list_agreements**](DomainsApi.md#list_agreements) | **GET** /api/domains/me/agreements | List Agreements
[**sign_agreement**](DomainsApi.md#sign_agreement) | **PUT** /api/domains/me/agreements/{agreement} | Sign Agreement


# **create_domain**
> DomainResponse create_domain(code, create_domain_request)

Create Domain

Creates a Domain

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
configuration = finbourne_identity.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://www.lusid.com/identity
configuration.host = "https://www.lusid.com/identity"
# Create an instance of the API class
api_instance = finbourne_identity.DomainsApi(finbourne_identity.ApiClient(configuration))
code = 'code_example' # str | The verification code necessary to create domains
create_domain_request = {"domain":"MyCo","companyName":"MyCo USA","owner":{"firstName":"Owner","lastName":"OfAccount","emailAddress":"owner.ofaccount@myco.com","login":"owner.ofaccount@myco.com","type":"Personal"},"signedAgreements":["TermsAndConditions_01012019_Gb"]} # CreateDomainRequest | The definition of the domain

try:
    # Create Domain
    api_response = api_instance.create_domain(code, create_domain_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->create_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The verification code necessary to create domains | 
 **create_domain_request** | [**CreateDomainRequest**](CreateDomainRequest.md)| The definition of the domain | 

### Return type

[**DomainResponse**](DomainResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created domain |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agreement**
> bool get_agreement(agreement)

Get Agreement

Check whether the domain has signed a specific agreement

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
configuration = finbourne_identity.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://www.lusid.com/identity
configuration.host = "https://www.lusid.com/identity"
# Create an instance of the API class
api_instance = finbourne_identity.DomainsApi(finbourne_identity.ApiClient(configuration))
agreement = 'agreement_example' # str | Name of the agreement

try:
    # Get Agreement
    api_response = api_instance.get_agreement(agreement)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->get_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agreement** | **str**| Name of the agreement | 

### Return type

**bool**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | Whether agreement is signed |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_domain**
> DomainResponse get_my_domain()

Get current Domain

Gets the Domain of the requesting User

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
configuration = finbourne_identity.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://www.lusid.com/identity
configuration.host = "https://www.lusid.com/identity"
# Create an instance of the API class
api_instance = finbourne_identity.DomainsApi(finbourne_identity.ApiClient(configuration))

try:
    # Get current Domain
    api_response = api_instance.get_my_domain()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->get_my_domain: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DomainResponse**](DomainResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current domain |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_agreements**
> dict(str, AgreementResponse) list_agreements()

List Agreements

Lists the signed agreements for the current domain

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
configuration = finbourne_identity.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://www.lusid.com/identity
configuration.host = "https://www.lusid.com/identity"
# Create an instance of the API class
api_instance = finbourne_identity.DomainsApi(finbourne_identity.ApiClient(configuration))

try:
    # List Agreements
    api_response = api_instance.list_agreements()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->list_agreements: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, AgreementResponse)**](AgreementResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List the signed agreements for the current domain |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_agreement**
> AgreementResponse sign_agreement(agreement)

Sign Agreement

Signs a specified agreement. Only the owner of a domain can sign an agreement

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
configuration = finbourne_identity.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://www.lusid.com/identity
configuration.host = "https://www.lusid.com/identity"
# Create an instance of the API class
api_instance = finbourne_identity.DomainsApi(finbourne_identity.ApiClient(configuration))
agreement = 'agreement_example' # str | Name of the agreement being signed

try:
    # Sign Agreement
    api_response = api_instance.sign_agreement(agreement)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->sign_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agreement** | **str**| Name of the agreement being signed | 

### Return type

[**AgreementResponse**](AgreementResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Signs a specified agreement |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

