-- transforms raw data from tpch orders table into a more usable format
-- renames columns to be more readable and consistent
select 
    o_orderkey as order_key,
    o_custkey as customer_key,
    o_orderstatus as status_code,
    o_totalprice as total_price,
    o_orderdate as order_date
from 
    {{ source('tpch', 'orders') }}