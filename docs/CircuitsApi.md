# swagger_client.CircuitsApi

All URIs are relative to *https://nb.knowroaming.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**circuit_terminations_create**](CircuitsApi.md#circuit_terminations_create) | **POST** /api/circuits/circuit-terminations/ | 
[**circuit_terminations_delete**](CircuitsApi.md#circuit_terminations_delete) | **DELETE** /api/circuits/circuit-terminations/{id}/ | 
[**circuit_terminations_list**](CircuitsApi.md#circuit_terminations_list) | **GET** /api/circuits/circuit-terminations/ | 
[**circuit_terminations_partial_update**](CircuitsApi.md#circuit_terminations_partial_update) | **PATCH** /api/circuits/circuit-terminations/{id}/ | 
[**circuit_terminations_read**](CircuitsApi.md#circuit_terminations_read) | **GET** /api/circuits/circuit-terminations/{id}/ | 
[**circuit_terminations_update**](CircuitsApi.md#circuit_terminations_update) | **PUT** /api/circuits/circuit-terminations/{id}/ | 
[**circuit_types_create**](CircuitsApi.md#circuit_types_create) | **POST** /api/circuits/circuit-types/ | 
[**circuit_types_delete**](CircuitsApi.md#circuit_types_delete) | **DELETE** /api/circuits/circuit-types/{id}/ | 
[**circuit_types_list**](CircuitsApi.md#circuit_types_list) | **GET** /api/circuits/circuit-types/ | 
[**circuit_types_partial_update**](CircuitsApi.md#circuit_types_partial_update) | **PATCH** /api/circuits/circuit-types/{id}/ | 
[**circuit_types_read**](CircuitsApi.md#circuit_types_read) | **GET** /api/circuits/circuit-types/{id}/ | 
[**circuit_types_update**](CircuitsApi.md#circuit_types_update) | **PUT** /api/circuits/circuit-types/{id}/ | 
[**circuits_create**](CircuitsApi.md#circuits_create) | **POST** /api/circuits/circuits/ | 
[**circuits_delete**](CircuitsApi.md#circuits_delete) | **DELETE** /api/circuits/circuits/{id}/ | 
[**circuits_list**](CircuitsApi.md#circuits_list) | **GET** /api/circuits/circuits/ | 
[**circuits_partial_update**](CircuitsApi.md#circuits_partial_update) | **PATCH** /api/circuits/circuits/{id}/ | 
[**circuits_read**](CircuitsApi.md#circuits_read) | **GET** /api/circuits/circuits/{id}/ | 
[**circuits_update**](CircuitsApi.md#circuits_update) | **PUT** /api/circuits/circuits/{id}/ | 
[**providers_create**](CircuitsApi.md#providers_create) | **POST** /api/circuits/providers/ | 
[**providers_delete**](CircuitsApi.md#providers_delete) | **DELETE** /api/circuits/providers/{id}/ | 
[**providers_graphs**](CircuitsApi.md#providers_graphs) | **GET** /api/circuits/providers/{id}/graphs/ | A convenience method for rendering graphs for a particular provider.
[**providers_list**](CircuitsApi.md#providers_list) | **GET** /api/circuits/providers/ | 
[**providers_partial_update**](CircuitsApi.md#providers_partial_update) | **PATCH** /api/circuits/providers/{id}/ | 
[**providers_read**](CircuitsApi.md#providers_read) | **GET** /api/circuits/providers/{id}/ | 
[**providers_update**](CircuitsApi.md#providers_update) | **PUT** /api/circuits/providers/{id}/ | 


# **circuit_terminations_create**
> circuit_terminations_create(data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
data = swagger_client.Data() # Data |  (optional)

try: 
    api_instance.circuit_terminations_create(data=data)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuit_terminations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data**](Data.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuit_terminations_delete**
> circuit_terminations_delete(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
id = 56 # int | A unique integer value identifying this circuit termination.

try: 
    api_instance.circuit_terminations_delete(id)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuit_terminations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit termination. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuit_terminations_list**
> circuit_terminations_list(limit=limit, offset=offset, term_side=term_side, site=site, circuit_id=circuit_id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
term_side = 'term_side_example' # str |  (optional)
site = 'site_example' # str |  (optional)
circuit_id = 'circuit_id_example' # str |  (optional)

try: 
    api_instance.circuit_terminations_list(limit=limit, offset=offset, term_side=term_side, site=site, circuit_id=circuit_id)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuit_terminations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **term_side** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 
 **circuit_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuit_terminations_partial_update**
> circuit_terminations_partial_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
id = 56 # int | A unique integer value identifying this circuit termination.
data = swagger_client.Data2() # Data2 |  (optional)

try: 
    api_instance.circuit_terminations_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuit_terminations_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit termination. | 
 **data** | [**Data2**](Data2.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuit_terminations_read**
> circuit_terminations_read(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
id = 56 # int | A unique integer value identifying this circuit termination.

try: 
    api_instance.circuit_terminations_read(id)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuit_terminations_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit termination. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuit_terminations_update**
> circuit_terminations_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
id = 56 # int | A unique integer value identifying this circuit termination.
data = swagger_client.Data1() # Data1 |  (optional)

try: 
    api_instance.circuit_terminations_update(id, data=data)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuit_terminations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit termination. | 
 **data** | [**Data1**](Data1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuit_types_create**
> circuit_types_create(data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
data = swagger_client.Data3() # Data3 |  (optional)

try: 
    api_instance.circuit_types_create(data=data)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuit_types_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data3**](Data3.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuit_types_delete**
> circuit_types_delete(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
id = 56 # int | A unique integer value identifying this circuit type.

try: 
    api_instance.circuit_types_delete(id)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuit_types_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit type. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuit_types_list**
> circuit_types_list(limit=limit, offset=offset)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try: 
    api_instance.circuit_types_list(limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuit_types_list: %s\n" % e)
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

# **circuit_types_partial_update**
> circuit_types_partial_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
id = 56 # int | A unique integer value identifying this circuit type.
data = swagger_client.Data5() # Data5 |  (optional)

try: 
    api_instance.circuit_types_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuit_types_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit type. | 
 **data** | [**Data5**](Data5.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuit_types_read**
> circuit_types_read(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
id = 56 # int | A unique integer value identifying this circuit type.

try: 
    api_instance.circuit_types_read(id)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuit_types_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit type. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuit_types_update**
> circuit_types_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
id = 56 # int | A unique integer value identifying this circuit type.
data = swagger_client.Data4() # Data4 |  (optional)

try: 
    api_instance.circuit_types_update(id, data=data)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuit_types_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit type. | 
 **data** | [**Data4**](Data4.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_create**
> circuits_create(data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
data = swagger_client.Data6() # Data6 |  (optional)

try: 
    api_instance.circuits_create(data=data)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data6**](Data6.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_delete**
> circuits_delete(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
id = 56 # int | A unique integer value identifying this circuit.

try: 
    api_instance.circuits_delete(id)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_list**
> circuits_list(limit=limit, offset=offset, install_date=install_date, id__in=id__in, q=q, provider_id=provider_id, provider=provider, type_id=type_id, type=type, tenant_id=tenant_id, tenant=tenant, site_id=site_id, site=site)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
install_date = 'install_date_example' # str |  (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
provider_id = 'provider_id_example' # str |  (optional)
provider = 'provider_example' # str |  (optional)
type_id = 'type_id_example' # str |  (optional)
type = 'type_example' # str |  (optional)
tenant_id = 'tenant_id_example' # str |  (optional)
tenant = 'tenant_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)

try: 
    api_instance.circuits_list(limit=limit, offset=offset, install_date=install_date, id__in=id__in, q=q, provider_id=provider_id, provider=provider, type_id=type_id, type=type, tenant_id=tenant_id, tenant=tenant, site_id=site_id, site=site)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **install_date** | **str**|  | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **provider_id** | **str**|  | [optional] 
 **provider** | **str**|  | [optional] 
 **type_id** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **tenant** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_partial_update**
> circuits_partial_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
id = 56 # int | A unique integer value identifying this circuit.
data = swagger_client.Data8() # Data8 |  (optional)

try: 
    api_instance.circuits_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit. | 
 **data** | [**Data8**](Data8.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_read**
> circuits_read(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
id = 56 # int | A unique integer value identifying this circuit.

try: 
    api_instance.circuits_read(id)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_update**
> circuits_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
id = 56 # int | A unique integer value identifying this circuit.
data = swagger_client.Data7() # Data7 |  (optional)

try: 
    api_instance.circuits_update(id, data=data)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit. | 
 **data** | [**Data7**](Data7.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_create**
> providers_create(data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
data = swagger_client.Data9() # Data9 |  (optional)

try: 
    api_instance.providers_create(data=data)
except ApiException as e:
    print("Exception when calling CircuitsApi->providers_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data9**](Data9.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_delete**
> providers_delete(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
id = 56 # int | A unique integer value identifying this provider.

try: 
    api_instance.providers_delete(id)
except ApiException as e:
    print("Exception when calling CircuitsApi->providers_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this provider. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_graphs**
> providers_graphs(id)

A convenience method for rendering graphs for a particular provider.

A convenience method for rendering graphs for a particular provider.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
id = 56 # int | A unique integer value identifying this provider.

try: 
    # A convenience method for rendering graphs for a particular provider.
    api_instance.providers_graphs(id)
except ApiException as e:
    print("Exception when calling CircuitsApi->providers_graphs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this provider. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_list**
> providers_list(limit=limit, offset=offset, name=name, account=account, asn=asn, id__in=id__in, q=q, site_id=site_id, site=site)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
name = 'name_example' # str |  (optional)
account = 'account_example' # str |  (optional)
asn = 'asn_example' # str |  (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)

try: 
    api_instance.providers_list(limit=limit, offset=offset, name=name, account=account, asn=asn, id__in=id__in, q=q, site_id=site_id, site=site)
except ApiException as e:
    print("Exception when calling CircuitsApi->providers_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **name** | **str**|  | [optional] 
 **account** | **str**|  | [optional] 
 **asn** | **str**|  | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_partial_update**
> providers_partial_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
id = 56 # int | A unique integer value identifying this provider.
data = swagger_client.Data11() # Data11 |  (optional)

try: 
    api_instance.providers_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling CircuitsApi->providers_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this provider. | 
 **data** | [**Data11**](Data11.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_read**
> providers_read(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
id = 56 # int | A unique integer value identifying this provider.

try: 
    api_instance.providers_read(id)
except ApiException as e:
    print("Exception when calling CircuitsApi->providers_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this provider. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_update**
> providers_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CircuitsApi()
id = 56 # int | A unique integer value identifying this provider.
data = swagger_client.Data10() # Data10 |  (optional)

try: 
    api_instance.providers_update(id, data=data)
except ApiException as e:
    print("Exception when calling CircuitsApi->providers_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this provider. | 
 **data** | [**Data10**](Data10.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

