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

# import from lib
from django.contrib import admin
# import from apps here
from app_control.models import FunctionController


class FunctionControllerAdmin(admin.ModelAdmin):
    """
    功能开关表注册设置
    """
    list_display = ('func_code', 'func_name', 'enabled', 'create_time', 'func_developer')
    list_filter = ('func_code',)
    search_fields = ('func_code',)


admin.site.register(FunctionController, FunctionControllerAdmin)
