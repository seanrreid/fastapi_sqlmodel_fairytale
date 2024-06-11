-- Create the Pigs table
CREATE TABLE pigs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
);

-- Create the Houses table
CREATE TABLE houses (
    id SERIAL PRIMARY KEY,
    material VARCHAR(50) NOT NULL,
    pig_id INTEGER REFERENCES pigs(id)
);

-- Create the Wolves table
CREATE TABLE wolves (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

-- Create the House_Attacks table
CREATE TABLE attacks (
    id SERIAL PRIMARY KEY,
    wolf_id INTEGER REFERENCES wolves(id),
    house_id INTEGER REFERENCES houses(id),
    success BOOLEAN
);
