-- Calculate the average temperature (AVG(temperature)) for each city.
-- Group the results by city.
-- Order the results by avg_temp (average temperature) in descending order

SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
