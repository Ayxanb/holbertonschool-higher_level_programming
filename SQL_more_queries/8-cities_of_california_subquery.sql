-- this is a comment
SELECT cities.id, cities.name, cities.state_id
FROM cities, states
WHERE cities.state_id = states.id
  AND states.name = 'California'
ORDER BY cities.id ASC;
