CREATE VIEW vw_league_data AS
SELECT l.name AS league_name
    , r.name AS round_name, r.description AS round_description
    , c.name AS submitter
    , s.spotify_uri, s.title, s.album, s.artists, s.created AS submission_date, s.comment AS submission_comment
    , cv.name AS voter
    , v.created AS vote_date, v.points_assigned, v.comment AS vote_comment
FROM league l
INNER JOIN round r ON r.league_id = l.id
INNER JOIN submission s ON s.round_id = r.id AND s.league_id = l.id
INNER JOIN competitor c ON c.id = s.submitter_id
INNER JOIN vote v ON v.round_id = r.id AND v.league_id = l.id AND v.spotify_uri = s.spotify_uri
INNER JOIN competitor cv ON cv.id = v.voter_id
;
