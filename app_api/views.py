from django.utils.translation import gettext as _
from django.db.migrations.recorder import MigrationRecorder

from utils.response_utils import APPResponse, DownloadResponse
from test.global_request_test import global_request_test
from utils.decorator_utils import track_performance
from utils.decorator_utils import recycle_db_conns
from utils.file_utils import parser_csv, export_data


def test_global_request(request):
    """测试全局访问请求对象"""
    global_request_test()
    return APPResponse()


def test_multiple_language(request):
    """测试多语言配置是否生效"""
    data = {
        'test': _('this is a test msg.')
    }
    return APPResponse(data=data)


@track_performance(threshold=100)
def test_api_performance(request):
    """测试接口耗时装饰器"""
    for i in range(1000000):
        print(i)
    return APPResponse()


@track_performance(threshold=100)
@recycle_db_conns
def test_recycle_db(request):
    """测试回收断掉的数据库链接"""
    is_export = request.GET.get('is_export', 0)

    record_data = list()
    recorder = MigrationRecorder.Migration.objects.all()
    for migration in recorder:
        record_dict = dict(
            app=migration.app,
            name=migration.name,
            applied=migration.applied
        )
        record_data.append(record_dict)

    filename = 'django_migration.csv'
    if is_export == '1':
        # 正常调用接口获取文件内容
        key_title_tuple = (
            ('app', 'App'),
            ('name', 'Name'),
            ('applied', 'Applied'),
        )
        csv_data = parser_csv(key_title_tuple, record_data)
        return DownloadResponse(filename=filename, content=csv_data)
    elif is_export == '2':
        # 直接在浏览器访问接口链接即可下载文件
        csv_data = list()
        title = ['App', 'Name', 'Applied']
        csv_data.append(title)
        for record in record_data:
            csv_data.append([
                record['app'],
                record['name'],
                record['applied'],
            ])
        return export_data(csv_data, filename=filename)
    else:
        return APPResponse(data=record_data)
