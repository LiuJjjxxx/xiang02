# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse
from common.mymako import render_json
from  home_application.models import warn_sum,server_value,network_server_cpu_value,network_server_flow_value

# Create your views here.


# 运维大屏(一)中间的趋势图
def get_warn_sum_count(request):
    fuwuqi = warn_sum.objects.filter(name='fuwuqi').order_by('-date')[:5].values('date', 'warn_count')
    wangluo = warn_sum.objects.filter(name='wangluo').order_by('-date')[:5].values('date', 'warn_count')
    sum = len(wangluo)
    data = {}
    fuwuqi_count = []
    wangluo_count = []
    timeer = []
    for i in range(sum):
        fuwuqi_count.insert(i, fuwuqi[i].get("warn_count"))
        wangluo_count.insert(i, wangluo[i].get("warn_count"))
        timeer.insert(i, fuwuqi[i].get("date").strftime('%d/%m %H:%M'))
    data["fuwuqi"] = fuwuqi_count
    data["wangluo"] = wangluo_count
    data["date"] = timeer

    return render_json(data)

# 运维大屏(一)存储空间排行
def get_server_value_in_sql(request):
    index = server_value.objects.filter(index=1)
    start = index[len(index) - 1].date
    server_value_sum = server_value.objects.filter(date__range=(start, start)).values()
    sum = len(server_value_sum)
    data = []
    value = {}
    for i in range(sum):
        value['index'] = server_value_sum[i].get("index")
        value['ip'] = server_value_sum[i].get("ip")
        value['value'] = server_value_sum[i].get("value")
        data.insert(i, value)
        value = {}
    return render_json(data)
# 运维大屏(一)流量排行
def get_netwokr_server_flow_in_sql(request):
    index = network_server_flow_value.objects.filter(index=1)
    start = index[len(index) - 1].date
    server_value_sum = network_server_flow_value.objects.filter(date__range=(start, start)).values()
    sum = len(server_value_sum)
    data = []
    value = {}
    for i in range(sum):
        value['index'] = server_value_sum[i].get("index")
        value['ip'] = server_value_sum[i].get("ip")
        value['value'] = server_value_sum[i].get("value")
        data.insert(i, value)
        value = {}
    return render_json(data)
# 运维大屏(一)网络设备CPU排行
def get_netwokr_server_cpu_in_sql(request):
    index = network_server_cpu_value.objects.filter(index=1)
    start = index[len(index) - 1].date
    server_value_sum = network_server_cpu_value.objects.filter(date__range=(start, start)).values()
    sum = len(server_value_sum)
    data = []
    value = {}
    for i in range(sum):
        value['index'] = server_value_sum[i].get("index")
        value['ip'] = server_value_sum[i].get("ip")
        value['value'] = server_value_sum[i].get("value")
        data.insert(i, value)
        value = {}
    return render_json(data)
