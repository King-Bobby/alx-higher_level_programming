--lists all the cities of California that can be found in the database hbtn_0d_usa
-- states table contain 1 record name = California but the id can be different
-- sorted in ascending order by cities.id

SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California") GROUP BY id ORDER BY id ASC;
