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
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')

#获取网络设备告警
def get_warn_network_server(request):
    client = get_client_by_request(request)
    kwargs = {
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
    warn = len(resp.get("result"))
    return warn
#获取服务器告警
def get_warn_server(request):
    client = get_client_by_request(request)
    kwargs = {
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
    warn = len(resp.get("result"))
    return warn
#获取token
def get_token(request):
    global token
    client = get_client_by_request(request)
    kwargs = {
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
#获取服务器的hostid
def get_network_server_hostid(request,groupids):
    client = get_client_by_request(request)
    data = []
    kwargs = {
        "jsonrpc": "2.0",
        "id": 2,
        "auth": "68a7a33cf513f1a77a3d0f87b76ac8a8",
        "method": "host.get",
        "params": {
            "output": ["name", "interfaces", "host", "status", "available"],
            "groupids": groupids,
            "selectInterfaces": ["hostid", "host", "ip"]
        }
    }
    resp = client.zabbix.get_token(**kwargs)
    result = resp.get("result")
    sum = len(result)
    for i in range(sum):
        data.insert(i,result[i].get("interfaces")[0])

    return data

#获取网络设备的CPU的itemid
def get_network_server_key(request):
    data = get_network_server_hostid(request,groupids=15)
    client = get_client_by_request(request)
    sum = len(data)
    for  i in range(sum):
        kwargs={
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
#获取网络设备的进流量
def get_network_server_flow_key(request):
    data = get_network_server_hostid(request, groupids=15)
    client = get_client_by_request(request)
    sum = len(data)
    itemid = []
    for j in range(sum):
        kwargs = {
            "jsonrpc": "2.0",
            "id": 2,
            "auth": "68a7a33cf513f1a77a3d0f87b76ac8a8",
            "method": "item.get",
            "params": {
                "output": ["itemid", "name", "key_", "status", "value_type"],
                "hostids": data[j].get("hostid"),
                "search": {
                    "key_": "port.inbytes"
                }
            }
        }
        resp = client.zabbix.get_token(**kwargs)
        if len(resp.get("result")) == 0:
            pass
        else:
            sum = len(resp.get("result"))
            for i in range(sum):
                itemid.insert(i,resp.get("result")[i].get("itemid"))
                data[j]["itemid"] = itemid
        itemid = []
    return data


#获取服务器设备的磁盘空间
def get_server_disk_key(request):
    data = get_network_server_hostid(request, groupids=16)
    client = get_client_by_request(request)
    sum = len(data)
    itemid = []
    for j in range(sum):
        kwargs = {
            "jsonrpc": "2.0",
            "id": 2,
            "auth": "68a7a33cf513f1a77a3d0f87b76ac8a8",
            "method": "item.get",
            "params": {
                "output": ["itemid", "name", "key_", "status", "value_type"],
                "hostids": data[j].get("hostid"),
                "filter": {
                    "value_type": 3,
                    "name": ["Port 1I Box 2 Bay 1: Disk size", "Port 1I Box 2 Bay 2: Disk size",
                             "Port 1I Box 2 Bay 3: Disk size"]
                }
            }
        }
        resp = client.zabbix.get_token(**kwargs)
        if len(resp.get("result")) == 0:
            print("我失败了")
        else:
            sum = len(resp.get("result"))
            for i in range(sum):
                itemid.insert(i,resp.get("result")[i].get("itemid"))
                data[j]["itemid"] = itemid
        itemid = []

    return data
#-----------------------------------------------------------------------------------------------------------
#获取服务器总数
def get_count_server(request):
    warn = get_warn_server(request)
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
            "output": ["status"],
            "groupids": 16
        }
    }
    resp = client.zabbix.get_token(**kwargs)
    result = {'result':resp.get("result"),'warn':warn}
    return render_json(result)
#获取网络设备总数
def get_count_network_server(request):
    warn  = get_warn_network_server(request)
    client = get_client_by_request(request)
    kwargs = {
        "jsonrpc": "2.0",
        "id": 2,
        "auth": "68a7a33cf513f1a77a3d0f87b76ac8a8",
        "method": "host.get",
        "params": {
            "output": ["status"],
            "groupids": 15
        }
    }
    resp = client.zabbix.get_token(**kwargs)
    result = {'result':resp.get("result"),'warn':warn}
    return render_json(result)


#-----------------------------------------------------------------------------------------------------------

#获取网络设备的CPU的利用率
def get_network_server_value(request):
    data = get_network_server_key(request)
    ip_value = []
    client = get_client_by_request(request)
    sum = len(data)
    for i in range(sum):
        what = data[i].has_key('itemid')
        if(what):
            kwargs = {
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
                data[i]["value"] = 0
            else:
                data[i]["value"] = int(result[0].get("value"))
        else:
            data[i]["value"] = 0
    data.sort(reverse=True, key=lambda x: x["value"])
    sum =len(data)
    for i in range(sum):
        data[i]["index"] = i+1
    return render_json(data)
#-----------------------------------------------------------------------------------------------------------
#获取服务器磁盘大小
def get_server_value(request):
    data = get_server_disk_key(request)
    client = get_client_by_request(request)
    value = 0
    sum =len(data)
    for i in range(sum):
        itemid_sum = len(data[i].get("itemid"))
        for  j in range(itemid_sum):
            kwargs = {
                "jsonrpc": "2.0",
                "id": 2,
                "auth": "68a7a33cf513f1a77a3d0f87b76ac8a8",
                "method": "history.get",
                "params": {
                    "output": "extend",
                    "history": 3,
                    "itemids": data[i].get("itemid")[j],
                    "sortfield": "clock",
                    "sortorder": "DESC",
                    "limit": 1
                }
            }
            resp = client.zabbix.get_token(**kwargs)
            result = resp.get("result")
            value += int(result[0].get("value"))
        value =format(float(value)/1073741824,'.2f')
        data[i]['value'] = value
        value = 0
    data.sort(reverse=False, key=lambda x: x["value"])
    for i in range(sum):
        data[i]["index"] = i + 1
    return render_json(data)

#--------------------------------------------------------
def get_network_server_flow_value(request):
    data = get_network_server_flow_key(request)
    client = get_client_by_request(request)
    value =0
    sum = len(data)
    for i in range(sum):
        if(data[i].get("itemid")==None):
            data[i]["value"] = 0
        else:
            itemid_sum = len(data[i].get("itemid"))
            for j in range(itemid_sum):
                kwargs = {
                    "jsonrpc": "2.0",
                    "id": 2,
                    "auth": "68a7a33cf513f1a77a3d0f87b76ac8a8",
                    "method": "trend.get",
                    "params": {
                        "output": "extend",
                        "itemids": data[i].get("itemid")[j],
                        "sortfield": "clock",
                        "sortorder": "DESC",
                        "limit": 1
                    }
                }
                resp = client.zabbix.get_token(**kwargs)
                result = resp.get("result")
                value += float(result[0].get("value_avg"))
            value = format(float(value) / 8192, '.0f')
            data[i]['value'] = value
            value = 0
    data.sort(reverse=True, key=lambda x: x["value"])
    for i in range(sum):
        data[i]["index"] = i + 1
    return render_json(data)


def get_jiaoben(request):
    data = get_network_server_hostid(request,groupids=15)
    results = map(1,data)
    print(data)
    return render_mako_context(request, '/home_application/ceshi.html')



