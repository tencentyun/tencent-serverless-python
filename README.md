# tencent-serverless-python

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

---------------

## 什么是tencent-serverless-python

tencent-serverless-python是腾讯云无服务器云函数SDK，集成云函数业务流接口。简化云函数的调用方法。在在使用该 sdk 的情况下，用户可以方便的从本地、cvm、容器、以及云端函数里快速调用某一个云函数，无需再进行公有云API的接口封装。

## 功能特性

通过tencent serverless SDK，你可以：

* 高性能，低时延的进行函数调用和访问
* 快速进行函数之间的调用，填写必须的参数即可使用（SDK会默认获取环境变量中的参数如region, secretId等）
* 支持内网域名的访问
* 支持keepalive能力

## 运行环境

tencent serverless SDK可以在 Windows、Linux、Mac 上运行。由于该SDK基于 Python 开发完成，因此在安装及运行前需要系统中安装有 Python 环境和pip。此外，该SDK也可以直接在云端进行调用。

## 快速开始

### 本地SDK函数互调

#### 安装tencent serverless SDK

```shell
pip install tencentserverless
```

#### 升级tencent serverless SDK

```shell
pip install tencentserverless -U
```

#### 查看tencent serverless 信息

```shell
pip list | grep tencentserverless
```

#### 调用示例

首先在云端创建一个被调用的Python云函数，地域为广州，命名为‘FuncInvoked’。函数内容如下：
```python
# -*- coding: utf8 -*-
def main_handler(event, context):
    if 'key1' in event.keys():
        print("value1 = " + event['key1'])
    if 'key2' in event.keys():
        print("value2 = " + event['key2'])
    return "Hello World from the function being invoked"  #return
```
创建完毕后，本地创建一个名为scfSDK.py的函数，内容如下：
```python
# -*- coding: utf8 -*-
from tencentserverless import scf
from tencentserverless.exception import TencentServerlessSDKException
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

def main_handler(event, context):
    print("prepare to invoke a function!")
    try:
        data = scf.invoke('FuncInvoked', secret_id="AKIxxxxxxxxxxxxxxxxxxxxxxggB4Sa",
             secret_key="3vZzxxxxxxxxxxxaeTC", region="ap-guangzhou",data={"a":"b"})
        print (data)
    except TencentServerlessSDKException as e:
        print (e)
    except TencentCloudSDKException as e:
        print (e)
    except Exception as e:
        print (e)
    return "Already invoked a function!" # return

main_handler("","")
```
进入scfSDK.py所在文件目录，执行函数查看结果：
```shell
python scfSDK.py
```
输出如下结果：
```shell
prepare to invoke a function!
"Hello World form the function being invoked"
```
之后将scfSDK函数打包（需要包含tencentserverless pip包），上传到云端即可。

如果需要频繁调用函数，则可以通过client的方式连接并触发。对应的scfSDK.py示例如下：
```python
# -*- coding: utf8 -*-
from tencentserverless.scf import Client
from tencentserverless.exception import TencentServerlessSDKException
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

scf = Client(secret_id="AKIxxxxxxxxxxxxxxxgB4Sa",
             secret_key="3vZxxxxxxxxxxxxxxxxxxxxxeTC", region="ap-guangzhou")

def main_handler(event, context):
    print("prepare to invoke a function!")
    try:
        data = scf.invoke('FuncInvoked', data={"a": "b"})
        print (data)
    except TencentServerlessSDKException as e:
        print (e)
    except TencentCloudSDKException as e:
        print (e)
    except Exception as e:
        print (e)
    return "Already invoked a function!" # return

main_handler("","")
```

### 云端SDK函数互调(即将支持)

SCF即将支持内置tencentserverless SDK，即可直接在云端进行函数互相调用。

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
