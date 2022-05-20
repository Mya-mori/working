
      

    insert into "dbt_training"."public"."employee_names" ("employee_id", "full_name")
    (
        select "employee_id", "full_name"
        from "employee_names__dbt_tmp000254729735"
    )
  