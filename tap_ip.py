# 完成tap的关键package：singer-python
import singer
import requests
from datetime import datetime

# 需要extract的数据
ip = requests.get('http://icanhazip.com').content.decode().replace('\n', '')
now = datetime.now().isoformat()
now_1 = datetime.now().isoformat()

# 数据格式设定
schema = {
    'properties':   {
        'ip': {'type': 'string'},
        'timestamp': {'type': 'string', 'format': 'date-time'},
    },
}

# ip为stream流的名称，在数据库中对应为表名
# schema在数据库中对应为各个字段
# timestamp在数据库中对应为主键
singer.write_schema('ip', schema, 'timestamp')

# 数据部分，在一个列表中以键值对的形式，一个字典对应数据库中的一行数据
singer.write_records('ip', [{'timestamp': now, 'ip': ip}, {'timestamp': now_1, 'ip': ip}])
