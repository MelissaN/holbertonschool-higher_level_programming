-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- run this first to import a SQL dump -->
--      echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
--      curl [link] -s | mysql -uroot -p hbtn_0d_tvshows
--
-- script that lists all non-Comedy shows in the database hbtn_0d_tvshows
-- tv_genres table contains only one record where name = Comedy (but the id can be different)
-- each record should display: tv_shows.title
-- results must be sorted in ascending order by the show title
-- can use max two SELECT statements
-- the database name will be passed as an argument of the mysql command

    SELECT tv_shows.title
      FROM tv_shows
     WHERE tv_shows.title NOT IN (
    SELECT tv_shows.title
      FROM tv_shows
INNER JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
     WHERE tv_genres.name = "Comedy")
  ORDER BY tv_shows.title ASC;
