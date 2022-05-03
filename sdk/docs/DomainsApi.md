# finbourne_identity.DomainsApi

All URIs are relative to *https://fbn-ci.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_domain**](DomainsApi.md#create_domain) | **POST** /api/domains | CreateDomain: Create Domain
[**get_agreement**](DomainsApi.md#get_agreement) | **HEAD** /api/domains/me/agreements/{agreement} | GetAgreement: Get Agreement
[**get_my_domain**](DomainsApi.md#get_my_domain) | **GET** /api/domains/me | GetMyDomain: Get current Domain
[**list_agreements**](DomainsApi.md#list_agreements) | **GET** /api/domains/me/agreements | ListAgreements: List Agreements
[**sign_agreement**](DomainsApi.md#sign_agreement) | **PUT** /api/domains/me/agreements/{agreement} | SignAgreement: Sign Agreement


# **create_domain**
> DomainResponse create_domain(code, create_domain_request)

CreateDomain: Create Domain

Creates a Domain

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/identity
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_identity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_identity.DomainsApi(api_client)
    code = 'code_example' # str | The verification code necessary to create domains
create_domain_request = {"domain":"MyCo","companyName":"MyCo USA","owner":{"firstName":"Owner","lastName":"OfAccount","emailAddress":"owner.ofaccount@myco.com","login":"owner.ofaccount@myco.com","type":"Personal"},"signedAgreements":["TermsAndConditions_01012019_Gb"]} # CreateDomainRequest | The definition of the domain

    try:
        # CreateDomain: Create Domain
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

GetAgreement: Get Agreement

Check whether the domain has signed a specific agreement

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/identity
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_identity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_identity.DomainsApi(api_client)
    agreement = 'agreement_example' # str | Name of the agreement

    try:
        # GetAgreement: Get Agreement
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

GetMyDomain: Get current Domain

Gets the Domain of the requesting User

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/identity
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_identity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_identity.DomainsApi(api_client)
    
    try:
        # GetMyDomain: Get current Domain
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

ListAgreements: List Agreements

Lists the signed agreements for the current domain

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/identity
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_identity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_identity.DomainsApi(api_client)
    
    try:
        # ListAgreements: List Agreements
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

SignAgreement: Sign Agreement

Signs a specified agreement. Only the owner of a domain can sign an agreement

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/identity
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_identity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_identity.DomainsApi(api_client)
    agreement = 'agreement_example' # str | Name of the agreement being signed

    try:
        # SignAgreement: Sign Agreement
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

