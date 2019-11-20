unified_prefix = '/interface/v1'
from views.v1.source import api as source_api
from views.v1.admin import api as admin_api
from views.v1.public import api as public_api
from views.v1.system import api as system_api
from views.v1.advertising import api as advertising_api
from views.v1.news import api as news_api


__all__ = [
    # 后台蓝图
    source_api,
    admin_api,
    public_api,
    system_api,
    advertising_api,
    news_api
]