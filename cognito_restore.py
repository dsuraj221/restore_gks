import json
import boto3
import os
from decimal import Decimal

client = boto3.client('cognito-idp')
user_pool_id = os.environ["USER_POOL_ID"]
temp_password = os.environ["TEMP_PASSWORD"]


def create_groups(grp):
    try:
        response = client.create_group(
            GroupName=grp,
            UserPoolId=user_pool_id
        )
        print(response)
    except client.exceptions.GroupExistsException as e:
        print(e)


def create_user(users=[]):
    for user in users:
        try:
            response = client.admin_create_user(
                UserPoolId=user_pool_id,
                Username=user.get('Username'),
                UserAttributes=user.get('Attributes'),
                TemporaryPassword=temp_password,
                ForceAliasCreation=True if user.get('UserStatus') == 'CONFIRMED' else False,
                DesiredDeliveryMediums=['EMAIL']
            )
            print(response)
        except client.exceptions.UsernameExistsException as e:
            print(e)


full_path = './BackupFolder/cognito_backup/'
file_name = "cognito_data.json"
completePath = os.path.join(full_path, file_name)
if os.path.exists(completePath):
    with open(completePath) as json_file:
        cognito_items = json.load(json_file, parse_float=Decimal)
        for item in cognito_items:
            create_groups(item.get('group_name'))
            create_user(item.get('users'))

