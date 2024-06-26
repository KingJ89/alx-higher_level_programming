-- lists all shows and genres connected to said show
-- used select statement and shuould display in ascending order
SELECT ts.title, tg.name
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
LEFT JOIN tv_genres AS tg ON tsg.genre_id = tg.id
ORDER BY ts.title, tg.name;

