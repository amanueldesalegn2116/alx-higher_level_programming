-- list all cities in db 'hbtn_0d_usa'
-- each record should display cities.id, cities.name, and states.name
-- can only use SELECT statement once
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
ON states.id = cities.state_id;
