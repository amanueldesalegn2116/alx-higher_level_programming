-- list all shows in db 'hbtn_0d_tvshows'
-- each record show display tv_shows.title, tv_show_genres.genre_id
-- if show doesn't have genre, display NULL
-- you can use only one SELECT statement
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
