--  lists all records of the table second_table
-- Dont list rows without a name value

SELECT score, name FROM second_table WHERE name != '' AND name IS NOT NULL ORDER BY score DESC;
