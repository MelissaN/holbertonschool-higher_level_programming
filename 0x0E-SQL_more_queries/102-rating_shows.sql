-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql
-- run this first to import a SQL dump -->
--      echo "CREATE DATABASE hbtn_0d_tvshows_rate;" | mysql -uroot -p
--      curl [link] -s | mysql -uroot -p hbtn_0d_tvshows_rate
--
-- script that lists all shows from hbtn_0d_tvshows_rate by their rating
-- each record should display: tv_shows.title - rating sum
-- results must be sorted in descending order by the rating
-- can use only one SELECT statement
-- the database name will be passed as an argument of the mysql command

    SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS 'rating'
      FROM tv_shows
INNER JOIN tv_show_ratings
        ON tv_shows.id = tv_show_ratings.show_id
  GROUP BY title
  ORDER BY rating DESC;
