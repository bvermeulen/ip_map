''' making a map of ip locations '''
from pprint import pprint
import json
import pandas as pd

class IpMap:

    def __init__(self, ip_json_file):
        self.ip_json_file = ip_json_file

    def read_json_to_df(self):
        with open(self.ip_json_file) as json_file:
            ip_log = json.load(json_file)

        columns = ['ip', 'date', 'count', 'city', 'country',
                   'latitude', 'longitude', 'region']
        rows = []
        for ip, val in ip_log.items():
            if val['ipgeo']:
                rows.append([ip, val['date'], val['count'],
                             val['ipgeo']['city'], val['ipgeo']['country'],
                             val['ipgeo']['latitude'], val['ipgeo']['longitude'],
                             val['ipgeo']['region']])

            else:
                rows.append([ip, val['date'], val['count'],
                             None, None,
                             None, None,
                             None])

        ip_log_df = pd.DataFrame(rows, columns)

        print(ip_log_df.head(20))

if __name__ == '__main__':
    ip_json_file = 'ip_log_file.json'
    ipmap = IpMap(ip_json_file)
    ipmap.read_json_to_df()
