-- Lists all shows with their linked genre name (NULL included)
SELECT tv_shows.title AS title, tv_genres.name AS name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title, name ASC;
