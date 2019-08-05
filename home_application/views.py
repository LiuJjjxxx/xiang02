# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from common.mymako import render_mako_context,render_json
from blueking.component.shortcuts import get_client_by_request
from  django.http import JsonResponse
from django.shortcuts import render
import json

def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')



def get_token(request):
    global token
    client = get_client_by_request(request)
    kwargs = {
        "bk_app_code": "xiang02",
        "bk_app_secret": "c64c5a65-e369-498d-8a8e-9cdcfd3b3ac4",
        "bk_username": "admin",
        "jsonrpc": "2.0",
        "id": 1,
        "auth": None,
        "method": "user.login",
        "params": {
            "user": "Admin",
            "password": "zabbix"
        }
    }
    resp = client.zabbix.get_token(**kwargs)
    token = resp.get("result")
    return token
def get_network_server_hostid(request):
    client = get_client_by_request(request)
    data = []
    kwargs = {
        "bk_app_code": "xiang02",
        "bk_app_secret": "c64c5a65-e369-498d-8a8e-9cdcfd3b3ac4",
        "bk_username": "admin",
        "jsonrpc": "2.0",
        "id": 2,
        "auth": "68a7a33cf513f1a77a3d0f87b76ac8a8",
        "method": "host.get",
        "params": {
            "output": ["name", "interfaces", "host", "status", "available"],
            "groupids": 15,
            "selectInterfaces": ["hostid", "host", "ip"]
        }
    }
    resp = client.zabbix.get_token(**kwargs)
    result = resp.get("result")
    sum = len(result)
    for i in range(0,sum,1):
        data.insert(i,result[i].get("interfaces")[0])

    return data

def get_network_server_key(request):
    data = get_network_server_hostid(request)
    client = get_client_by_request(request)
    sum = len(data)
    for  i in range(0,sum,1):
        kwargs={
            "bk_app_code": "xiang02",
            "bk_app_secret": "c64c5a65-e369-498d-8a8e-9cdcfd3b3ac4",
            "bk_username": "admin",
            "jsonrpc": "2.0",
            "id": 2,
            "auth": "68a7a33cf513f1a77a3d0f87b76ac8a8",
            "method": "item.get",
            "params": {
                "output": ["itemid", "name", "key_", "status", "value_type"],
                "hostids": data[i].get("hostid"),
                "filter": {
                    "value_type": 3
                }
            }
        }
        resp = client.zabbix.get_token(**kwargs)
        if len(resp.get("result")) == 0:
            pass
        else:
            itemid = resp.get("result")[0].get("itemid")
            data[i]['itemid'] = itemid
    return data
#-----------------------------------------------------------------------------------------------------------
def get_count_server(request):
    client = get_client_by_request(request)
    kwargs = {
        "bk_app_code": "xiang02",
        "bk_app_secret": "c64c5a65-e369-498d-8a8e-9cdcfd3b3ac4",
        "bk_username": "admin",
        "jsonrpc": "2.0",
        "id": 2,
        "auth": "68a7a33cf513f1a77a3d0f87b76ac8a8",
        "method": "host.get",
        "params": {
            "output": ["name", "interfaces", "host", "status", "available"],
            "groupids": 16,
            "selectInterfaces": ["hostid", "host", "ip"]
        }
    }
    resp = client.zabbix.get_token(**kwargs)
    result = resp.get("result")
    return render_json(result)

def get_count_network_server(request):
    client = get_client_by_request(request)
    kwargs = {
        "bk_app_code": "xiang02",
        "bk_app_secret": "c64c5a65-e369-498d-8a8e-9cdcfd3b3ac4",
        "bk_username": "admin",
        "jsonrpc": "2.0",
        "id": 2,
        "auth": "68a7a33cf513f1a77a3d0f87b76ac8a8",
        "method": "host.get",
        "params": {
            "output": ["name", "interfaces", "host", "status", "available"],
            "groupids": 15,
            "selectInterfaces": ["hostid", "host", "ip"]
        }
    }
    resp = client.zabbix.get_token(**kwargs)
    result = resp.get("result")
    return render_json(result)


def get_warn_server(request):
    client = get_client_by_request(request)
    kwargs = {
        "bk_app_code": "xiang02",
        "bk_app_secret": "c64c5a65-e369-498d-8a8e-9cdcfd3b3ac4",
        "bk_username": "admin",
        "jsonrpc": "2.0",
        "id": 2,
        "auth": "68a7a33cf513f1a77a3d0f87b76ac8a8",
        "method": "problem.get",
        "params": {
            "output": "extend",
            "groupids": 16,
            "filter":{
                "severity": [3, 4, 5]
            }
        }
    }
    resp = client.zabbix.get_token(**kwargs)
    result = resp.get("result")
    return render_json(result)

def get_warn_network_server(request):
    client = get_client_by_request(request)
    kwargs = {
        "bk_app_code": "xiang02",
        "bk_app_secret": "c64c5a65-e369-498d-8a8e-9cdcfd3b3ac4",
        "bk_username": "admin",
        "jsonrpc": "2.0",
        "id": 2,
        "auth": "68a7a33cf513f1a77a3d0f87b76ac8a8",
        "method": "problem.get",
        "params": {
            "output": "extend",
            "groupids": 15,
            "filter":{
                "severity": [3, 4, 5]
            }
        }
    }
    resp = client.zabbix.get_token(**kwargs)
    result = resp.get("result")
    return render_json(result)

def get_network_server_value(request):
    data = get_network_server_key(request)
    ip_value = []
    client = get_client_by_request(request)
    sum = len(data)
    for i in range(0,sum,1):
        if(data[i].has_key('itemid')):
            kwargs = {
                "bk_app_code": "xiang02",
                "bk_app_secret": "c64c5a65-e369-498d-8a8e-9cdcfd3b3ac4",
                "bk_username": "admin",
                "jsonrpc": "2.0",
                "id": 2,
                "auth": "68a7a33cf513f1a77a3d0f87b76ac8a8",
                "method": "history.get",
                "params": {
                    "output": "extend",
                    "history": 3,
                    "itemids": data[i].get("itemid"),
                    "sortfield": "clock",
                    "sortorder": "DESC",
                    "limit": 1
                }
            }
            resp = client.zabbix.get_token(**kwargs)
            result = resp.get("result")
            if (len(result) ==0):
                data[i]["value"] = -1
            else:
                data[i]["value"] = int(result[0].get("value"))
        else:
            data[i]["value"] = -1
    data.sort(reverse=True, key=lambda x: x["value"])
    sum =len(data)
    for i in range(0,sum,1):
        data[i]["index"] = i+1
    return render_json(data)
def get_jiaoben(request):
    client = get_client_by_request(request)
    get_token(request)
    kwargs = {
        "bk_app_code": "xiang02",
        "bk_app_secret": "c64c5a65-e369-498d-8a8e-9cdcfd3b3ac4",
        "bk_username": "admin",
        "jsonrpc": "2.0",
        "id": 1,
        "auth": token,
        "method": "hostgroup.get",
        "params": {"output": ["name","groupid"]}
}

    resp = client.zabbix.get_token(**kwargs)
    result = resp.get("result")
    return render_json(result)

