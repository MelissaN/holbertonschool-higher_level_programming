-- lists all the cities in the database hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
-- results must be sorted in ascending order by cities.id
-- can use only one SELECT statement
-- the database name will be passed as an argument of the mysql command

  SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states
   WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
