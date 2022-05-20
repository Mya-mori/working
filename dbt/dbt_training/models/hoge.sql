-- select
--     *
-- from {{ source('staging', 'employees') }}
select * from {{ ref('jobs_jp') }}