-- script lists all records of second table of database
-- does not list without rows
-- displays score and name in that order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
