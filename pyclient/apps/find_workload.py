
import os
from typing import ItemsView
from apigroups.client.apis import WorkloadV1Api
from apigroups.client import configuration, api_client
import pytz 
import time
from tzlocal import get_localzone
import argparse
import datetime
import warnings

warnings.simplefilter("ignore")

HOME = os.environ['HOME']

configuration = configuration.Configuration(
    psm_config_path=HOME+"/.psm/config.json",
    interactive_mode=True
)
configuration.verify_ssl = False

client = api_client.ApiClient(configuration)
api_instance = WorkloadV1Api(client)


parser = argparse.ArgumentParser()
parser.add_argument("-a", "--age", dest="age", help="creation date: <number>d|w|m")
parser.add_argument("--dsc", dest="dsc", help = "MAC address of DSC" )
parser.add_argument("--label", dest="label", help = 'label of workload')
parser.add_argument("--host", dest="host", help = 'host name of workload')
args = parser.parse_args()


workload = api_instance.list_workload(o_tenant = 'default')
items = workload.get('items')
workload_list = []
new_item_list =[]


#adjusting timezone difference: UTC -> PST
PST = pytz.timezone('US/Pacific')
utc_dt = datetime.datetime.now()
current_time = utc_dt.astimezone(PST)
desired_time = datetime.datetime.now()

if args.age:
    date_number = int(args.age[0:-1])
    date_type = args.age[-1]
    if date_type == "m":
        desired_time = current_time - datetime.timedelta(days = ( int(date_number) * 31 ))
    elif date_type == "w":
        desired_time = current_time - datetime.timedelta(weeks = int(date_number))
    elif date_type == "d":
        desired_time = current_time - datetime.timedelta(days = int(date_number))
    for x in items:
        if desired_time < x['meta']['creation_time']: 
            workload_list.append(x)   

#set default creation_time: recent 2 months workload
if not args.age:
    desired_time = current_time - datetime.timedelta(weeks = int(8))
    for item in items:
            if desired_time < item['meta']['creation_time']: 
                workload_list.append(item)


if args.dsc:
    new_item_list = workload_list
    workload_list = []
    for item in new_item_list:
        if args.dsc in item.get('spec').get('interfaces')[0].get('mac_address'):
            workload_list.append(item)


if args.host:
    new_item_list = workload_list
    workload_list = []
    for item in new_item_list:
        if args.host in item.get('spec').get('host_name'):
            workload_list.append(item)


if args.label:
    key = args.label.split(":")[0]
    value = args.label.split(":")[1]
    new_item_list = workload_list
    workload_list = []
    for item in new_item_list:
        if item.get('meta').get('labels'):
            if value in item.get('meta').get('labels').get(key):
                workload_list.append(item)


if not workload_list:
    print('There are no workloads matching the descriptions.')
if workload_list:
    print(workload_list)