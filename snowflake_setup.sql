use role accountadmin; //superuser

create warehouse dbt_wh with warehouse_size="x-small";
create database if not exists dbt_db;
create role if not exists dbt_role;

show grants on warehouse dbt_wh;

grant usage on warehouse dbt_wh to role dbt_role;
grant role dbt_role to user ahuang;
grant all on database dbt_db to role dbt_role;

use role dbt_role;

create schema dbt_db.dbt_schema;

use role accountadmin;

drop warehouse if exists dbt_wh;
drop database if exists dbt_db;
drop role if exists dbt_role;
