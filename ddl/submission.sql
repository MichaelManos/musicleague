CREATE TABLE submission (
    round_id STRING,
    spotify_uri STRING,
    league_id INT,
    title STRING,
    album STRING,
    artists STRING,
    submitter_id STRING,
    created TIMESTAMP,
    comment STRING,
    visible_to_voters STRING,
    PRIMARY KEY (round_id, spotify_uri, league_id)
);
