# -*- coding: utf-8 -*-
"""
codeproj - v1 apis for base

v1 接口定义，供服务内部、开放接口

URL前缀：/api/base/
"""

from django.urls import path

from apps.codeproj.apis import v1

# url前缀： /api/base/
urlpatterns = [
    path("pkgrulemapsync/", v1.CheckPackageRuleMapSyncApiView.as_view(),
         name="apiv1_package_rule_map_sync"),
]
