-- LIST CITIES OF A PLACE FOUND IN hbtn_0d_usa.
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id ASC;
