# -*- coding: utf-8 -*-
from  ..base import ComponentAPI

class CollectionsZABBIX(object):
    def __init__(self,client):
        self.client = client

        self.get_token = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/self-service-api/zabbix/get_token/',
            description=u'获取Token'
        )