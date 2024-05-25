-- The database hbtn_0d_usa is created only if it does not already exist.
-- The table states is created only if it does not already exist.
-- The table cities is created only if it does not already exist.
-- The id field in both tables is unique, auto-incremented, cannot be null, and is the primary key.
-- The state_id field in the cities table cannot be null and must reference the id field in the states table, enforcing referential integrity.
-- The name field in both tables cannot be null.
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    UNIQUE (id)
);

CREATE TABLE IF NOT EXISTS cities
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
