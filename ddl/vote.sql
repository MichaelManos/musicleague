CREATE TABLE vote (
    round_id STRING,
    spotify_uri STRING,
    voter_id STRING,
    league_id INT,
    created TIMESTAMP,
    points_assigned INT,
    comment STRING,
    PRIMARY KEY (round_id, spotify_uri, voter_id, league_id)
);
