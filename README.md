# ETL-pipline

## What Goes Down
1. snowflake (data warehouse)
    - stores raw and transformed data
    - handles role-based access control
        - warehouses: compute resources
        - roles: access control
        - schemas: data organization
        - users: authentication
2. dbt (transformation)
     - transforms data inside snowflake
     - dbt_project.yml: project configuration
     - source models: raw data definitions
     - staging models: initial cleaning
     - fact/dimension tables: business logic
     - tests: data quality checks
     - macros: reusable SQL
3. airflow (orchestration)
     - schedules and runs dbt transformations
     - manages task dependencies
     - handles retries and failures
4. docker (envrionment)
     - provides consistent environment
     - contains all required tools above + python packages
  
## Data Flow
- raw data lands in snowflake
- dbt transforms data in snowflake
- airflow orchestrates dbt runs
- docker ensures consistent environment

## Running Project
1. create snowflake account
2. run setup script in `snowflake_setup.sql` in snowflake worksheet
3. install docker desktop
4. install astronomer cli
5. clone repo and run
   - cd dbt-dag
   - astro dev start
6. access airflow UI at localhost:8080
   - username and password: admin

![image](https://github.com/user-attachments/assets/0e8c9a31-3822-4940-9966-a2e17f7e94ac)

Tutorial: [jayzern](https://www.youtube.com/watch?v=OLXkGB7krGo)
