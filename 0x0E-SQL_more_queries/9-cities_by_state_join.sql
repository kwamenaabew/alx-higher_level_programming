-- using a join to display info about two tables
-- statements to do join query
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC;
