-- import the temperatures into hbtn_0c_0
-- DML querys to display average temperature by city
SELECT city,
AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY AVG(value) DESC;
