# swagger_client.SecretsApi

All URIs are relative to *https://nb.knowroaming.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_rsa_key_pair_list**](SecretsApi.md#generate_rsa_key_pair_list) | **GET** /api/secrets/generate-rsa-key-pair/ | This endpoint can be used to generate a new RSA key pair. The keys are returned in PEM format.
[**get_session_key_create**](SecretsApi.md#get_session_key_create) | **POST** /api/secrets/get-session-key/ | Retrieve a temporary session key to use for encrypting and decrypting secrets via the API. The user&#39;s private RSA
[**secret_roles_create**](SecretsApi.md#secret_roles_create) | **POST** /api/secrets/secret-roles/ | 
[**secret_roles_delete**](SecretsApi.md#secret_roles_delete) | **DELETE** /api/secrets/secret-roles/{id}/ | 
[**secret_roles_list**](SecretsApi.md#secret_roles_list) | **GET** /api/secrets/secret-roles/ | 
[**secret_roles_partial_update**](SecretsApi.md#secret_roles_partial_update) | **PATCH** /api/secrets/secret-roles/{id}/ | 
[**secret_roles_read**](SecretsApi.md#secret_roles_read) | **GET** /api/secrets/secret-roles/{id}/ | 
[**secret_roles_update**](SecretsApi.md#secret_roles_update) | **PUT** /api/secrets/secret-roles/{id}/ | 
[**secrets_create**](SecretsApi.md#secrets_create) | **POST** /api/secrets/secrets/ | 
[**secrets_delete**](SecretsApi.md#secrets_delete) | **DELETE** /api/secrets/secrets/{id}/ | 
[**secrets_list**](SecretsApi.md#secrets_list) | **GET** /api/secrets/secrets/ | 
[**secrets_partial_update**](SecretsApi.md#secrets_partial_update) | **PATCH** /api/secrets/secrets/{id}/ | 
[**secrets_read**](SecretsApi.md#secrets_read) | **GET** /api/secrets/secrets/{id}/ | 
[**secrets_update**](SecretsApi.md#secrets_update) | **PUT** /api/secrets/secrets/{id}/ | 


# **generate_rsa_key_pair_list**
> generate_rsa_key_pair_list()

This endpoint can be used to generate a new RSA key pair. The keys are returned in PEM format.

This endpoint can be used to generate a new RSA key pair. The keys are returned in PEM format.  { \"public_key\": \"<public key>\", \"private_key\": \"<private key>\" }

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretsApi()

try: 
    # This endpoint can be used to generate a new RSA key pair. The keys are returned in PEM format.
    api_instance.generate_rsa_key_pair_list()
except ApiException as e:
    print("Exception when calling SecretsApi->generate_rsa_key_pair_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session_key_create**
> get_session_key_create()

Retrieve a temporary session key to use for encrypting and decrypting secrets via the API. The user's private RSA

Retrieve a temporary session key to use for encrypting and decrypting secrets via the API. The user's private RSA key is POSTed with the name `private_key`. An example:  curl -v -X POST -H \"Authorization: Token <token>\" -H \"Accept: application/json; indent=4\" \\ --data-urlencode \"private_key@<filename>\" https://netbox/api/secrets/get-session-key/  This request will yield a base64-encoded session key to be included in an `X-Session-Key` header in future requests:  { \"session_key\": \"+8t4SI6XikgVmB5+/urhozx9O5qCQANyOk1MNe6taRf=\" }  This endpoint accepts one optional parameter: `preserve_key`. If True and a session key exists, the existing session key will be returned instead of a new one.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretsApi()

try: 
    # Retrieve a temporary session key to use for encrypting and decrypting secrets via the API. The user's private RSA
    api_instance.get_session_key_create()
except ApiException as e:
    print("Exception when calling SecretsApi->get_session_key_create: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_roles_create**
> secret_roles_create(data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretsApi()
data = swagger_client.Data126() # Data126 |  (optional)

try: 
    api_instance.secret_roles_create(data=data)
except ApiException as e:
    print("Exception when calling SecretsApi->secret_roles_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data126**](Data126.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_roles_delete**
> secret_roles_delete(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretsApi()
id = 56 # int | A unique integer value identifying this secret role.

try: 
    api_instance.secret_roles_delete(id)
except ApiException as e:
    print("Exception when calling SecretsApi->secret_roles_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this secret role. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_roles_list**
> secret_roles_list(limit=limit, offset=offset)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretsApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try: 
    api_instance.secret_roles_list(limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling SecretsApi->secret_roles_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_roles_partial_update**
> secret_roles_partial_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretsApi()
id = 56 # int | A unique integer value identifying this secret role.
data = swagger_client.Data128() # Data128 |  (optional)

try: 
    api_instance.secret_roles_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling SecretsApi->secret_roles_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this secret role. | 
 **data** | [**Data128**](Data128.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_roles_read**
> secret_roles_read(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretsApi()
id = 56 # int | A unique integer value identifying this secret role.

try: 
    api_instance.secret_roles_read(id)
except ApiException as e:
    print("Exception when calling SecretsApi->secret_roles_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this secret role. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_roles_update**
> secret_roles_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretsApi()
id = 56 # int | A unique integer value identifying this secret role.
data = swagger_client.Data127() # Data127 |  (optional)

try: 
    api_instance.secret_roles_update(id, data=data)
except ApiException as e:
    print("Exception when calling SecretsApi->secret_roles_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this secret role. | 
 **data** | [**Data127**](Data127.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_create**
> secrets_create(data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretsApi()
data = swagger_client.Data129() # Data129 |  (optional)

try: 
    api_instance.secrets_create(data=data)
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data129**](Data129.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_delete**
> secrets_delete(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretsApi()
id = 56 # int | A unique integer value identifying this secret.

try: 
    api_instance.secrets_delete(id)
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this secret. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_list**
> secrets_list(limit=limit, offset=offset, name=name, id__in=id__in, q=q, role_id=role_id, role=role, device_id=device_id, device=device)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretsApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
name = 'name_example' # str |  (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
role_id = 'role_id_example' # str |  (optional)
role = 'role_example' # str |  (optional)
device_id = 'device_id_example' # str |  (optional)
device = 'device_example' # str |  (optional)

try: 
    api_instance.secrets_list(limit=limit, offset=offset, name=name, id__in=id__in, q=q, role_id=role_id, role=role, device_id=device_id, device=device)
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **name** | **str**|  | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **role_id** | **str**|  | [optional] 
 **role** | **str**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **device** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_partial_update**
> secrets_partial_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretsApi()
id = 56 # int | A unique integer value identifying this secret.
data = swagger_client.Data131() # Data131 |  (optional)

try: 
    api_instance.secrets_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this secret. | 
 **data** | [**Data131**](Data131.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_read**
> secrets_read(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretsApi()
id = 56 # int | A unique integer value identifying this secret.

try: 
    api_instance.secrets_read(id)
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this secret. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_update**
> secrets_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretsApi()
id = 56 # int | A unique integer value identifying this secret.
data = swagger_client.Data130() # Data130 |  (optional)

try: 
    api_instance.secrets_update(id, data=data)
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this secret. | 
 **data** | [**Data130**](Data130.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

