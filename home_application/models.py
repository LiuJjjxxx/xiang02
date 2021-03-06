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

from django.db import models

class warn_sum(models.Model):
    name = models.CharField(max_length=64)
    warn_count = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


class server_value(models.Model):
    index = models.IntegerField()
    ip  = models.CharField(max_length=64)
    value = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)

class network_server_flow_value(models.Model):
    index = models.IntegerField()
    ip  = models.CharField(max_length=64)
    value = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)

class network_server_cpu_value(models.Model):
    index = models.IntegerField()
    ip  = models.CharField(max_length=64)
    value = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)

class yewu_cpu_value(models.Model):
    name = models.CharField(max_length=64)
    cpu_value = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
