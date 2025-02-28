# ResourceListOfSystemLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[SystemLog]**](SystemLog.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from finbourne_identity.models.resource_list_of_system_log import ResourceListOfSystemLog

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfSystemLog from a JSON string
resource_list_of_system_log_instance = ResourceListOfSystemLog.from_json(json)
# print the JSON string representation of the object
print ResourceListOfSystemLog.to_json()

# convert the object into a dict
resource_list_of_system_log_dict = resource_list_of_system_log_instance.to_dict()
# create an instance of ResourceListOfSystemLog from a dict
resource_list_of_system_log_form_dict = resource_list_of_system_log.from_dict(resource_list_of_system_log_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


