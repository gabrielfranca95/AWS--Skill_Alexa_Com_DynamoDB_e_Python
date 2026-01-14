import os
from ask_sdk_dynamodb.adapter import DynamoDbAdapter

def get_persistence_adapter():
    """
    Returns a DynamoDB persistence adapter.
    Uses environment variable DYNAMODB_PERSISTENCE_TABLE for table name.
    """
    table_name = os.environ.get("DYNAMODB_PERSISTENCE_TABLE", "Connect_DynamoDB")
    return DynamoDbAdapter(
        table_name=table_name, 
        create_table=True, 
        partition_key_name="userId"
    )
