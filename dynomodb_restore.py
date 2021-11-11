import os
from decimal import Decimal
import json
import boto3
from table_schemas import config

def load_items(items, db_table_name):
    dynamodb = boto3.resource("dynamodb")
    print(db_table_name)
    table_config = config.get(db_table_name)
    if not table_config:
        print(f"{db_table_name} Not found")
        return
    table = dynamodb.create_table(db_table_name,
                          KeySchema=table_config.get("KeySchema"),
                          AttributeDefinitions=table_config.get("AttributeDefinitions"),
                          ProvisionedThroughput=table_config.get("ProvisionedThroughput"))
    print("Table status:", table.table_status)
    print(table)
    for item in items:
        table.put_item(Item=item)


def pick_json_files(db_file, db_table_name):
    with open(db_file) as json_file:
        items = json.load(json_file, parse_float=Decimal)
    load_items(items, db_table_name)


directory = './BackupFolder/dynamodb_backup'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    table_name = filename.split('.')[0]
    pick_json_files(f, table_name)
