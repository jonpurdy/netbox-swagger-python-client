# swagger_client.ExtrasApi

All URIs are relative to *https://nb.knowroaming.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_templates_create**](ExtrasApi.md#export_templates_create) | **POST** /api/extras/export-templates/ | 
[**export_templates_delete**](ExtrasApi.md#export_templates_delete) | **DELETE** /api/extras/export-templates/{id}/ | 
[**export_templates_list**](ExtrasApi.md#export_templates_list) | **GET** /api/extras/export-templates/ | 
[**export_templates_partial_update**](ExtrasApi.md#export_templates_partial_update) | **PATCH** /api/extras/export-templates/{id}/ | 
[**export_templates_read**](ExtrasApi.md#export_templates_read) | **GET** /api/extras/export-templates/{id}/ | 
[**export_templates_update**](ExtrasApi.md#export_templates_update) | **PUT** /api/extras/export-templates/{id}/ | 
[**graphs_create**](ExtrasApi.md#graphs_create) | **POST** /api/extras/graphs/ | 
[**graphs_delete**](ExtrasApi.md#graphs_delete) | **DELETE** /api/extras/graphs/{id}/ | 
[**graphs_list**](ExtrasApi.md#graphs_list) | **GET** /api/extras/graphs/ | 
[**graphs_partial_update**](ExtrasApi.md#graphs_partial_update) | **PATCH** /api/extras/graphs/{id}/ | 
[**graphs_read**](ExtrasApi.md#graphs_read) | **GET** /api/extras/graphs/{id}/ | 
[**graphs_update**](ExtrasApi.md#graphs_update) | **PUT** /api/extras/graphs/{id}/ | 
[**image_attachments_create**](ExtrasApi.md#image_attachments_create) | **POST** /api/extras/image-attachments/ | 
[**image_attachments_delete**](ExtrasApi.md#image_attachments_delete) | **DELETE** /api/extras/image-attachments/{id}/ | 
[**image_attachments_list**](ExtrasApi.md#image_attachments_list) | **GET** /api/extras/image-attachments/ | 
[**image_attachments_partial_update**](ExtrasApi.md#image_attachments_partial_update) | **PATCH** /api/extras/image-attachments/{id}/ | 
[**image_attachments_read**](ExtrasApi.md#image_attachments_read) | **GET** /api/extras/image-attachments/{id}/ | 
[**image_attachments_update**](ExtrasApi.md#image_attachments_update) | **PUT** /api/extras/image-attachments/{id}/ | 
[**recent_activity_list**](ExtrasApi.md#recent_activity_list) | **GET** /api/extras/recent-activity/ | List all UserActions to provide a log of recent activity.
[**recent_activity_read**](ExtrasApi.md#recent_activity_read) | **GET** /api/extras/recent-activity/{id}/ | List all UserActions to provide a log of recent activity.
[**topology_maps_create**](ExtrasApi.md#topology_maps_create) | **POST** /api/extras/topology-maps/ | 
[**topology_maps_delete**](ExtrasApi.md#topology_maps_delete) | **DELETE** /api/extras/topology-maps/{id}/ | 
[**topology_maps_list**](ExtrasApi.md#topology_maps_list) | **GET** /api/extras/topology-maps/ | 
[**topology_maps_partial_update**](ExtrasApi.md#topology_maps_partial_update) | **PATCH** /api/extras/topology-maps/{id}/ | 
[**topology_maps_read**](ExtrasApi.md#topology_maps_read) | **GET** /api/extras/topology-maps/{id}/ | 
[**topology_maps_render**](ExtrasApi.md#topology_maps_render) | **GET** /api/extras/topology-maps/{id}/render/ | 
[**topology_maps_update**](ExtrasApi.md#topology_maps_update) | **PUT** /api/extras/topology-maps/{id}/ | 


# **export_templates_create**
> export_templates_create(data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
data = swagger_client.Data87() # Data87 |  (optional)

try: 
    api_instance.export_templates_create(data=data)
except ApiException as e:
    print("Exception when calling ExtrasApi->export_templates_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data87**](Data87.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_templates_delete**
> export_templates_delete(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
id = 56 # int | A unique integer value identifying this export template.

try: 
    api_instance.export_templates_delete(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->export_templates_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this export template. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_templates_list**
> export_templates_list(limit=limit, offset=offset, content_type=content_type, name=name)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
content_type = 'content_type_example' # str |  (optional)
name = 'name_example' # str |  (optional)

try: 
    api_instance.export_templates_list(limit=limit, offset=offset, content_type=content_type, name=name)
except ApiException as e:
    print("Exception when calling ExtrasApi->export_templates_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **content_type** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_templates_partial_update**
> export_templates_partial_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
id = 56 # int | A unique integer value identifying this export template.
data = swagger_client.Data89() # Data89 |  (optional)

try: 
    api_instance.export_templates_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling ExtrasApi->export_templates_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this export template. | 
 **data** | [**Data89**](Data89.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_templates_read**
> export_templates_read(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
id = 56 # int | A unique integer value identifying this export template.

try: 
    api_instance.export_templates_read(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->export_templates_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this export template. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_templates_update**
> export_templates_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
id = 56 # int | A unique integer value identifying this export template.
data = swagger_client.Data88() # Data88 |  (optional)

try: 
    api_instance.export_templates_update(id, data=data)
except ApiException as e:
    print("Exception when calling ExtrasApi->export_templates_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this export template. | 
 **data** | [**Data88**](Data88.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graphs_create**
> graphs_create(data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
data = swagger_client.Data90() # Data90 |  (optional)

try: 
    api_instance.graphs_create(data=data)
except ApiException as e:
    print("Exception when calling ExtrasApi->graphs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data90**](Data90.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graphs_delete**
> graphs_delete(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
id = 56 # int | A unique integer value identifying this graph.

try: 
    api_instance.graphs_delete(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->graphs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this graph. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graphs_list**
> graphs_list(limit=limit, offset=offset, type=type, name=name)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
type = 'type_example' # str |  (optional)
name = 'name_example' # str |  (optional)

try: 
    api_instance.graphs_list(limit=limit, offset=offset, type=type, name=name)
except ApiException as e:
    print("Exception when calling ExtrasApi->graphs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **type** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graphs_partial_update**
> graphs_partial_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
id = 56 # int | A unique integer value identifying this graph.
data = swagger_client.Data92() # Data92 |  (optional)

try: 
    api_instance.graphs_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling ExtrasApi->graphs_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this graph. | 
 **data** | [**Data92**](Data92.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graphs_read**
> graphs_read(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
id = 56 # int | A unique integer value identifying this graph.

try: 
    api_instance.graphs_read(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->graphs_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this graph. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graphs_update**
> graphs_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
id = 56 # int | A unique integer value identifying this graph.
data = swagger_client.Data91() # Data91 |  (optional)

try: 
    api_instance.graphs_update(id, data=data)
except ApiException as e:
    print("Exception when calling ExtrasApi->graphs_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this graph. | 
 **data** | [**Data91**](Data91.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_attachments_create**
> image_attachments_create(data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
data = swagger_client.Data93() # Data93 |  (optional)

try: 
    api_instance.image_attachments_create(data=data)
except ApiException as e:
    print("Exception when calling ExtrasApi->image_attachments_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data93**](Data93.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_attachments_delete**
> image_attachments_delete(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
id = 56 # int | A unique integer value identifying this image attachment.

try: 
    api_instance.image_attachments_delete(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->image_attachments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this image attachment. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_attachments_list**
> image_attachments_list(limit=limit, offset=offset)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try: 
    api_instance.image_attachments_list(limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling ExtrasApi->image_attachments_list: %s\n" % e)
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

# **image_attachments_partial_update**
> image_attachments_partial_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
id = 56 # int | A unique integer value identifying this image attachment.
data = swagger_client.Data95() # Data95 |  (optional)

try: 
    api_instance.image_attachments_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling ExtrasApi->image_attachments_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this image attachment. | 
 **data** | [**Data95**](Data95.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_attachments_read**
> image_attachments_read(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
id = 56 # int | A unique integer value identifying this image attachment.

try: 
    api_instance.image_attachments_read(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->image_attachments_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this image attachment. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_attachments_update**
> image_attachments_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
id = 56 # int | A unique integer value identifying this image attachment.
data = swagger_client.Data94() # Data94 |  (optional)

try: 
    api_instance.image_attachments_update(id, data=data)
except ApiException as e:
    print("Exception when calling ExtrasApi->image_attachments_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this image attachment. | 
 **data** | [**Data94**](Data94.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recent_activity_list**
> recent_activity_list(limit=limit, offset=offset, user=user, username=username)

List all UserActions to provide a log of recent activity.

List all UserActions to provide a log of recent activity.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
user = 'user_example' # str |  (optional)
username = 'username_example' # str |  (optional)

try: 
    # List all UserActions to provide a log of recent activity.
    api_instance.recent_activity_list(limit=limit, offset=offset, user=user, username=username)
except ApiException as e:
    print("Exception when calling ExtrasApi->recent_activity_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **user** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recent_activity_read**
> recent_activity_read(id)

List all UserActions to provide a log of recent activity.

List all UserActions to provide a log of recent activity.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
id = 56 # int | A unique integer value identifying this user action.

try: 
    # List all UserActions to provide a log of recent activity.
    api_instance.recent_activity_read(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->recent_activity_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user action. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topology_maps_create**
> topology_maps_create(data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
data = swagger_client.Data96() # Data96 |  (optional)

try: 
    api_instance.topology_maps_create(data=data)
except ApiException as e:
    print("Exception when calling ExtrasApi->topology_maps_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data96**](Data96.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topology_maps_delete**
> topology_maps_delete(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
id = 56 # int | A unique integer value identifying this topology map.

try: 
    api_instance.topology_maps_delete(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->topology_maps_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this topology map. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topology_maps_list**
> topology_maps_list(limit=limit, offset=offset, name=name, slug=slug, site_id=site_id, site=site)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)

try: 
    api_instance.topology_maps_list(limit=limit, offset=offset, name=name, slug=slug, site_id=site_id, site=site)
except ApiException as e:
    print("Exception when calling ExtrasApi->topology_maps_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **name** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
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

# **topology_maps_partial_update**
> topology_maps_partial_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
id = 56 # int | A unique integer value identifying this topology map.
data = swagger_client.Data98() # Data98 |  (optional)

try: 
    api_instance.topology_maps_partial_update(id, data=data)
except ApiException as e:
    print("Exception when calling ExtrasApi->topology_maps_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this topology map. | 
 **data** | [**Data98**](Data98.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topology_maps_read**
> topology_maps_read(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
id = 56 # int | A unique integer value identifying this topology map.

try: 
    api_instance.topology_maps_read(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->topology_maps_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this topology map. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topology_maps_render**
> topology_maps_render(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
id = 56 # int | A unique integer value identifying this topology map.

try: 
    api_instance.topology_maps_render(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->topology_maps_render: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this topology map. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topology_maps_update**
> topology_maps_update(id, data=data)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtrasApi()
id = 56 # int | A unique integer value identifying this topology map.
data = swagger_client.Data97() # Data97 |  (optional)

try: 
    api_instance.topology_maps_update(id, data=data)
except ApiException as e:
    print("Exception when calling ExtrasApi->topology_maps_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this topology map. | 
 **data** | [**Data97**](Data97.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

