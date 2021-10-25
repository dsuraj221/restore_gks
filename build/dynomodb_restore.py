import os
from decimal import Decimal
import json
import boto3


def load_items(items, db_table_name):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(db_table_name)
    for item in items:
        table.put_item(Item=item)


def pick_json_files(db_file, db_table_name):

    with open(db_file) as json_file:
        items = json.load(json_file, parse_float=Decimal)
    load_items(items, db_table_name)


directory = '/BackupFolder/dynamodb_backup'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    table_name = filename.split('.')[0]
    pick_json_files(f, table_name)
