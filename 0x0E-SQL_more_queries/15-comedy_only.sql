-- lists all comedy shows in database tvshows
-- Each record should display: tv_shows.title Results must be sorted in ascending order by the show title
SELECT ts.title
FROM tv_shows AS ts
INNER JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
INNER JOIN tv_genres AS tg ON tsg.genre_id = tg.id
WHERE tg.name = 'comedy'
ORDER BY ts.title;

