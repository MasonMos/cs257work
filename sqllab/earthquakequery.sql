-- Find all earthquakes that have a magnitude greater than 5.
SELECT * FROM earthquakes WHERE magnitude > 5;

-- Find all earthquakes that happen near the equation.
SELECT * FROM earthquakes WHERE latitude BETWEEN -5 AND 5;

-- Find all earthquakes that are near the equator and the Prime Meridian.
SELECT * FROM earthquakes WHERE latitude BETWEEN -5 AND 5 
INTERSECT 
SELECT * FROM earthquakes WHERE longitude BETWEEN -5 AND 5;

-- Find all major earthquakes from the time ranges.
SELECT * FROM earthquakes WHERE magnitude > 7 ORDER BY extract(year from quaketime) DESC;