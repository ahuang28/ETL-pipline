# this file creates an AirFlow DAG that orchestrates dbt transformations in snowflake
import os
from datetime import datetime
from pathlib import Path

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

# set up snowflake connection
profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn", 
        profile_args={"database": "dbt_db", "schema": "dbt_schema"},
    )
)

dbt_snowflake_dag = DbtDag(
    # dbt project location in Airflow container
    project_config=ProjectConfig("/usr/local/airflow/dags/dbt/data_pipeline",),
    # Automatically install dbt dependencies
    operator_args={"install_deps": True},
    # Use profile configuration defined above
    profile_config=profile_config,
    # Specify dbt executable path
    execution_config=ExecutionConfig(dbt_executable_path="dbt"),    
    # Scheduling parameters
    schedule_interval="@daily",
    start_date=datetime(2023, 9, 10),
    catchup=False,
    dag_id="dbt_dag",
)