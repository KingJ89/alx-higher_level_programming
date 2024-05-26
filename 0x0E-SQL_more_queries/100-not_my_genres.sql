-- lists all genres not connected to show dextarand tv_shows table contains only one record 
SELECT tg.name 
FROM tv_genres AS tg
WHERE tg.name NOT IN (
    SELECT tg2.name 
    FROM tv_genres AS tg2
    LEFT JOIN tv_show_genres AS tsg ON tg2.id = tsg.genre_id
    LEFT JOIN tv_shows AS ts ON tsg.show_id = ts.id
    WHERE ts.title = 'Dexter'
)
GROUP BY tg.name
ORDER BY tg.name ASC;

