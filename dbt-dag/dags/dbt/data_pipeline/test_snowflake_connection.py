import snowflake.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

try:
    conn = snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        warehouse='dbt_wh',
        database='snowflake_sample_data',
        schema='tpch_sf1'
    )
    print("Connection successful!")
    
    # Test a simple query
    cur = conn.cursor()
    cur.execute("SELECT current_version()")
    print("Snowflake version:", cur.fetchone()[0])
    
except Exception as e:
    print(f"Connection failed: {str(e)}")
finally:
    if 'conn' in locals():
        conn.close()