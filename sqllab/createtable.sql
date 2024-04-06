DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quaketime time with time zone,
  latitude real,
  longitude real,
  mag real,
  id text,
  quaketype text
);