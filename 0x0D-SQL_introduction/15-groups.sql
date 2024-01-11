-- grouping in sql.
--
-- group records according to same score
SELECT score, COUNT(score) as `number` FROM second_table  GROUP BY score
ORDER BY number DESC;
