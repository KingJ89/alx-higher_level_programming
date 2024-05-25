-- script lists all cities that can be found in the adtabase
SELECT id, name 
FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'California') 
ORDER BY id ASC;
