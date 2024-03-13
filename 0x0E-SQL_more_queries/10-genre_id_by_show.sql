-- list all shows in 'hbtn_0d_tvshows' that have at least one genre linked
-- each record should display
-- tv_shows.title, tv_show_genres.genre_id
-- results must be in ascending order by tv_shows.title and tv_show_genres.genre_id
-- you can only use one SELECT statement
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
