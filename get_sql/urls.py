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
from get_sql import views

urlpatterns = patterns('get_sql.views',
    #数据库操作
        #趋势图
    (r'^get_warn_sum_count/$', 'get_warn_sum_count'),
        #服务器磁盘大小
    (r'^get_server_value_in_sql/$', 'get_server_value_in_sql'),
        #网络设备进流量
    (r'^get_netwokr_server_flow_in_sql/$', 'get_netwokr_server_flow_in_sql'),
        #网络设备CPU
    (r'^get_netwokr_server_cpu_in_sql/$', 'get_netwokr_server_cpu_in_sql'),
        #业务系统CPU
    (r'^get_yewu_value/$', 'get_yewu_value'),

    )
