import requests
from datetime import datetime, timezone
import singer
import petl as etl
import sqlalchemy
from pprint import pprint

ip = requests.get('http://icanhazip.com').content.decode()
now = datetime.now().isoformat()


# schema = {
#     'properties':   {
#         'ip': {'type': 'string'},
#         'timestamp': {'type': 'string', 'format': 'date-time'},
#     },
# }

schema = {
    'properties':   {
    },
}


conn = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5433')
table = etl.fromdb(conn, 'select * from sports_hall').cut(['number_people', 'date', 'temperature'])
col = table[0]
data = table[1:10]
list_data = []
for i in data:
    dic = {}
    for j in range(0, len(col)):
        dic.update({col[j]: i[j]})
    list_data.append(dic)

for i in col:
    schema['properties'].update({i: {'type': 'string'}})


schema = {
    'properties':   {
        'ip': {'type': 'string'},
        'timestamp': {'type': 'string', 'format': 'date-time'},
    },
}


items = []
for i in schema['properties'].items():
    print(i)
pprint(schema)
# schema['properties']['index'] = 'int'
# singer.write_schema('test', schema, 'index')
# singer.write_records('test', list_data)
