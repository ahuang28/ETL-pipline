FROM quay.io/astronomer/astro-runtime:12.7.1

# # install dbt snowflake
# RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
#     pip install --no-cache-dir dbt-snowflake && deactivate

USER root

# Install dbt packages globally
RUN pip install --no-cache-dir \
    dbt-core==1.7.3 \
    dbt-snowflake==1.7.1 \
    astronomer-cosmos==1.0.3

# Ensure dbt is in PATH
ENV PATH="/usr/local/bin:${PATH}"

USER astro