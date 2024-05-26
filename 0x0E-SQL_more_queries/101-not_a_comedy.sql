-- lists all shows without genre comedy
-- sorted in ascending order
SELECT ts.title
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
LEFT JOIN tv_genres AS tg ON tsg.genre_id = tg.id
WHERE tg.name != 'Comedy' OR tg.name IS NULL
GROUP BY ts.title
ORDER BY ts.title ASC;

