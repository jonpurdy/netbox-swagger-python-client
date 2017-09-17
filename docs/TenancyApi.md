# swagger_client.TenancyApi

All URIs are relative to *https://nb.knowroaming.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenant_groups_create**](TenancyApi.md#tenant_groups_create) | **POST** /api/tenancy/tenant-groups/ | 
[**tenant_groups_delete**](TenancyApi.md#tenant_groups_delete) | **DELETE** /api/tenancy/tenant-groups/{id}/ | 
[**tenant_groups_list**](TenancyApi.md#tenant_groups_list) | **GET** /api/tenancy/tenant-groups/ | 
[**tenant_groups_partial_update**](TenancyApi.md#tenant_groups_partial_update) | **PATCH** /api/tenancy/tenant-groups/{id}/ | 
[**tenant_groups_read**](TenancyApi.md#tenant_groups_read) | **GET** /api/tenancy/tenant-groups/{id}/ | 
[**tenant_groups_update**](TenancyApi.md#tenant_groups_update) | **PUT** /api/tenancy/tenant-groups/{id}/ | 
[**tenants_create**](TenancyApi.md#tenants_create) | **POST** /api/tenancy/tenants/ | 
[**tenants_delete**](TenancyApi.md#tenants_delete) | **DELETE** /api/tenancy/tenants/{id}/ | 
[**tenants_list**](TenancyApi.md#tenants_list) | **GET** /api/tenancy/tenants/ | 
[**tenants_partial_update**](TenancyApi.md#tenants_partial_update) | **PATCH** /api/tenancy/tenants/{id}/ | 
[**tenants_read**](TenancyApi.md#tenants_read) | **GET** /api/tenancy/tenants/{id}/ | 
[**tenants_update**](TenancyApi.md#tenants_update) | **PUT** /api/tenancy/tenants/{id}/ | 


# **tenant_groups_create**
> tenant_groups_create(data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenancyApi()
data = swagger_client.Data132() # Data132 |  (optional)

try: 
    api_instance.tenant_groups_create(data=data)
except ApiException as e:
    print("Exception when calling TenancyApi->tenant_groups_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data132**](Data132.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_groups_delete**
> tenant_groups_delete(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenancyApi()
id = 56 # int | A unique integer value identifying this tenant group.

try: 
    api_instance.tenant_groups_delete(id)
except ApiException as e:
    print("Exception when calling TenancyApi->tenant_groups_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant group. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_groups_list**
> tenant_groups_list(limit=limit, offset=offset)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenancyApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try: 
    api_instance.tenant_groups_list(limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling TenancyApi->tenant_groups_list: %s\n" % e)
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

# **tenant_groups_partial_update**
> tenant_groups_partial_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenancyApi()
id = 56 # int | A unique integer value identifying this tenant group.
data = swagger_client.Data134() # Data134 |  (optional)

try: 
    api_instance.tenant_groups_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling TenancyApi->tenant_groups_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant group. | 
 **data** | [**Data134**](Data134.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_groups_read**
> tenant_groups_read(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenancyApi()
id = 56 # int | A unique integer value identifying this tenant group.

try: 
    api_instance.tenant_groups_read(id)
except ApiException as e:
    print("Exception when calling TenancyApi->tenant_groups_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant group. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_groups_update**
> tenant_groups_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenancyApi()
id = 56 # int | A unique integer value identifying this tenant group.
data = swagger_client.Data133() # Data133 |  (optional)

try: 
    api_instance.tenant_groups_update(id, data=data)
except ApiException as e:
    print("Exception when calling TenancyApi->tenant_groups_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant group. | 
 **data** | [**Data133**](Data133.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_create**
> tenants_create(data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenancyApi()
data = swagger_client.Data135() # Data135 |  (optional)

try: 
    api_instance.tenants_create(data=data)
except ApiException as e:
    print("Exception when calling TenancyApi->tenants_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data135**](Data135.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_delete**
> tenants_delete(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenancyApi()
id = 56 # int | A unique integer value identifying this tenant.

try: 
    api_instance.tenants_delete(id)
except ApiException as e:
    print("Exception when calling TenancyApi->tenants_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_list**
> tenants_list(limit=limit, offset=offset, name=name, id__in=id__in, q=q, group_id=group_id, group=group)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenancyApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
name = 'name_example' # str |  (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
group_id = 'group_id_example' # str |  (optional)
group = 'group_example' # str |  (optional)

try: 
    api_instance.tenants_list(limit=limit, offset=offset, name=name, id__in=id__in, q=q, group_id=group_id, group=group)
except ApiException as e:
    print("Exception when calling TenancyApi->tenants_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **name** | **str**|  | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **group_id** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_partial_update**
> tenants_partial_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenancyApi()
id = 56 # int | A unique integer value identifying this tenant.
data = swagger_client.Data137() # Data137 |  (optional)

try: 
    api_instance.tenants_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling TenancyApi->tenants_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant. | 
 **data** | [**Data137**](Data137.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_read**
> tenants_read(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenancyApi()
id = 56 # int | A unique integer value identifying this tenant.

try: 
    api_instance.tenants_read(id)
except ApiException as e:
    print("Exception when calling TenancyApi->tenants_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenants_update**
> tenants_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TenancyApi()
id = 56 # int | A unique integer value identifying this tenant.
data = swagger_client.Data136() # Data136 |  (optional)

try: 
    api_instance.tenants_update(id, data=data)
except ApiException as e:
    print("Exception when calling TenancyApi->tenants_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant. | 
 **data** | [**Data136**](Data136.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

