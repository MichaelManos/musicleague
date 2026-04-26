CREATE SEQUENCE leagueid_autoincrement START 1;
CREATE TABLE league (
    league_id INT PRIMARY KEY DEFAULT NEXTVAL('leagueid_autoincrement'),
    name str
);
