-- wget https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql
-- after importing table dump into database, cat [filename] | mysql -hlocalhost -uroot -p [database_name]
-- script that displays the average temperature by city ordered by temperature (descending)

SELECT city, AVG(value) AS 'avg_temp' FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
