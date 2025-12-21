-- this is a comment
SELECT g.name AS genre, COUNT(tsg.show_id) AS number_of_shows
FROM tv_show_genres tsg
JOIN genres g ON tsg.genre_id = g.id
GROUP BY g.id
ORDER BY number_of_shows DESC;
