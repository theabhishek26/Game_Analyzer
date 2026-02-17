CREATE TABLE matches_raw (
    id SERIAL PRIMARY KEY,
    puuid VARCHAR(100),
    match_id VARCHAR(100),
    match_json JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE analytics_weekly (
    id SERIAL PRIMARY KEY,
    puuid VARCHAR(100),
    week_start DATE,
    kd FLOAT,
    win_rate FLOAT,
    early_death_percent FLOAT,
    fatigue_slope FLOAT,
    tilt_index FLOAT,
    ai_summary TEXT
);
