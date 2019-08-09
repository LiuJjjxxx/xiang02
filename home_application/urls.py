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

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    #服务器
    (r'^get_count_server/$', 'get_count_server'),
    (r'^get_warn_server/$', 'get_warn_server'),
    (r'^get_server_disk_key/$', 'get_server_disk_key'),
    (r'^get_server_value/$', 'get_server_value'),
    #网络设备
    (r'^get_count_network_server/$', 'get_count_network_server'),
    (r'^get_warn_network_server/$', 'get_warn_network_server'),
    (r'^get_network_server_hostid/$', 'get_network_server_hostid'),
    (r'^get_network_server_key/$', 'get_network_server_key'),
    (r'^get_network_server_value/$', 'get_network_server_value'),
    (r'^get_network_server_flow_value/$', 'get_network_server_flow_value'),
    (r'^get_network_server_flow_key/$', 'get_network_server_flow_key'),
    #业务系统
    (r'^get_business_cpu/$', 'get_business_cpu'),
)
