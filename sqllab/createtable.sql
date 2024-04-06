DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakedate date,
  latitude real,
  longitude real,
  mag real,
  id text,
  quaketype text
);