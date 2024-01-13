-- listing selected records
--
-- listing all the cities of California in the
-- database hbtn_0d_usa.
SELECT id, name FROM cities where state_id = (SELECT id FROM states WHERE name = "California")
GROUP BY id
ORDER BY id ASC;
