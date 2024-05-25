-- displays temperatures of all states order state name
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
