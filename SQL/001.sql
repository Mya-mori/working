///////////////////////////////////////////////////
SELECT
	substr(stamp, 1, 10) AS dt
	,COUNT(1) AS search_count
	,SUM(CASE WHEN result_num  = 0 THEN 1 ELSE 0 END) AS no_match_count
	,AVG(CASE WHEN result_num  = 0 THEN 1 ELSE 0 END) AS no_match_rate
FROM
	bigdatasql.c8.access_log
WHERE
	action = 'search'
GROUP BY
	dt


///////////////////////////////////////////////////
WITH search_keyword_stat AS (
	SELECT
		keyword
		,result_num
		,COUNT(1) AS search_count
		,100.0 * COUNT(1)/ COUNT(1) OVER() AS search_share
	FROM
		bigdatasql.c8.access_log
	WHERE
		action = 'search'
	GROUP BY
		keyword
		,result_num
)

SELECT
	keyword
	,search_count
	,search_share
	,100.0 * search_count / SUM(search_count) OVER() AS no_match_share
FROM
	search_keyword_stat
WHERE
	
	result_num = 0

///////////////////////////////////////////////////
WITH access_log_with_next_action AS (
	SELECT
		stamp
		,session
		,action
		,LEAD(action)
			OVER(PARTITION BY session ORDER BY stamp ASC)
			AS next_action 
	FROM
		bigdatasql.c8.access_log
)
SELECT *
FROM access_log_with_next_action
ORDER BY
	session
	,stamp
///////////////////////////////////////////////////