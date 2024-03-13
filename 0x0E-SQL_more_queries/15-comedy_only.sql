-- list all Comedy shows in 'hbtn_0d_tvshows'
-- 'tv_genres' table contains only one record where name = Comedy
-- results must be sorted in ascending order by the show title
-- you can only use one SELECT statement
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres m ON tv_shows.id = m.show_id
INNER JOIN tv_genres g ON m.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY tv_shows.title ASC;
