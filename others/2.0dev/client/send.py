from inspect import Traceback
from urllib import response
import requests # 需要安装
try:res=requests.post(url='http://127.0.0.1:5702', data={"user_id":'','message':'测试3'})
except ConnectionError:print('error')
print(str(res))