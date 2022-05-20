
  create view "dbt_training"."public"."hoge__dbt_tmp" as (
    select
    *
from "dbt_training"."raw"."employees"
  );