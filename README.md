# tencent-serverless-python

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

腾讯云云函数SDK，集成云函数业务流接口

## Install
```shell
pip install tencentserverless
```

## Example01

本地测试：
```python
from tencentserverless import scf
from tencentserverless.exception import TencentServerlessSDKException

try:
    data = scf.invoke('test',secret_id="your secret id",
           secret_key="your secret key", data={"a":"b"})
    print data
except TencentServerlessSDKException as e:
    print e
except TencentCloudSDKException as e:
    print e
except Exception as e:
    print e
```

云函数环境测试：
```python
from tencentserverless.scf import invoke
from tencentserverless.exception import TencentServerlessSDKException

try:
    data = invoke('test', data={"a":"b"})
    print data
except TencentServerlessSDKException as e:
    print e
except TencentCloudSDKException as e:
    print e
except Exception as e:
    print e
```

## Example02

本地测试：
```python
from tencentserverless.scf import client
from tencentserverless.exception import TencentServerlessSDKException

scf = client(secret_id="your secret id",
           secret_key="your secret key")

try:
    data = scf.invoke('test',data={"a":"b"})
    print data
except TencentServerlessSDKException as e:
    print e
except TencentCloudSDKException as e:
    print e
except Exception as e:
    print e
```
云函数环境测试：
```python
from tencentserverless.scf import client
from tencentserverless.exception import TencentServerlessSDKException

scf = client()

try:
    data = scf.invoke('test',data={"a":"b"})
    print data
except TencentServerlessSDKException as e:
    print e
except TencentCloudSDKException as e:
    print e
except Exception as e:
    print e
```


## API Reference
- [client](#client)
- [invoke](#invoke)
- [TencentServerlessSDKException](#TencentServerlessSDKException)

### client
- [____init____]
 
 **Params:**
 
| 参数名        | 是否必填 |  类型  |                    描述                                      |
| :------------ | :------: | :----: | ----------------------:                                      |
| region        |    否    | string |地域信息，默认与调用接口的函数所属地域相同，本地调用默认是广州|
| secret_id     |    否    | string |用户 secret_id， 默认是从云函数环境变量中获取，本地调试必填|
| secret_key    |    否    | string |用户 secret_key， 默认是从云函数环境变量中获取，本地调试必填|
| token         |    否    | string |用户 token，默认是从云函数环境变量中获取|

- [__invoke__]

 **Params:**

| 参数名        | 是否必填 |  类型  |                    描述 |
| :------------ | :------: | :----: | ----------------------: |
| function_name |    是    | string |                函数名称 |
| qualifier     |    否    | string | 函数版本，默认为$LATEST |
| data          |    否    | 对象   | 函数运行入参，必须可以被json.dumps的对象 |
| namespace     |    否    | string | 命名空间，默认为default |

### Invoke
调用函数。暂时只支持同步调用。

**Params:**

| 参数名        | 是否必填 |  类型  |                    描述                                      |
| :------------ | :------: | :----: | ----------------------:                                      |
| region        |    否    | string |地域信息，默认与调用接口的函数所属地域相同，本地调用默认是广州|
| secret_id     |    否    | string |用户 secret_id， 默认是从云函数环境变量中获取，本地调试必填|
| secret_key    |    否    | string |用户 secret_key， 默认是从云函数环境变量中获取，本地调试必填|
| token         |    否    | string |用户 token，默认是从云函数环境变量中获取|
| function_name |    是    | string |                函数名称 |
| qualifier     |    否    | string | 函数版本，默认为$LATEST |
| data          |    否    | string |函数运行入参，必须可以被json.dumps的对象 |
| namespace     |    否    | string | 命名空间，默认为default |

### TencentServerlessSDKException
#### 属性
- [__code__]
- [__message__]
- [__request_id__]
- [__response__]
- [__stack_trace__]

#### 方法
- [__get_code__]
```
返回错误码信息
```
- [__get_message__]
```
返回错误信息
```
- [__get_request_id__]
```
返回request_id信息
```
- [__get_response__]
```
返回response信息
```
- [__get_stack_trace__]
```
返回stack_trace信息
```

## TODO List
* [ ] 支持管理流接口

## Licence

[MIT](./LICENSE)