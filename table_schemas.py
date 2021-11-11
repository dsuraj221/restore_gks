
config = {
    "gke-backend-dev-gkeTable": {
        "KeySchema": [
            {
                'AttributeName': 'user_id',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'created_at',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        "AttributeDefinitions":[
            {
                'AttributeName': 'user_id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'created_at',
                'AttributeType': 'S'
            },

        ],
        "ProvisionedThroughput": {
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
     },
    "gks-backend-cognito-dev-eksTable": {
        "KeySchema": [
            {
                'AttributeName': 'user_id',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'created_at',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        "AttributeDefinitions":[
            {
                'AttributeName': 'user_id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'created_at',
                'AttributeType': 'S'
            },

        ],
        "ProvisionedThroughput": {
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
     },
    "gks-backend-cognito-dev-groupInfo": {
        "KeySchema": [
            {
                'AttributeName': 'group_name',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        "AttributeDefinitions":[
            {
                'AttributeName': 'group_name',
                'AttributeType': 'S'
            }

        ],
        "ProvisionedThroughput": {
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
     },
    "gks-cluster-provisioner-tf-locks-dev": {
        "KeySchema": [
            {
                'AttributeName': 'LockID',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        "AttributeDefinitions":[
            {
                'AttributeName': 'LockID',
                'AttributeType': 'S'
            }

        ],
        "ProvisionedThroughput": {
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
     },
    "gks-backend-cognito-dev-systemConfig": {
        "KeySchema": [
            {
                'AttributeName': 'config_name',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'region',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        "AttributeDefinitions":[
            {
                'AttributeName': 'config_name',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'region',
                'AttributeType': 'S'
            },

        ],
        "ProvisionedThroughput": {
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
     }

}