DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quaketime timestamptz,
  latitude real,
  longitude real,
  mag real,
  id text,
  quaketype text
);