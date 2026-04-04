USE netflix_project;
GO

-- Clean table
CREATE TABLE netflix_titles_clean (
    show_id NVARCHAR(50),
    type NVARCHAR(50),
    title NVARCHAR(300),
    date_added DATE,
    release_year INT,
    rating NVARCHAR(50),
    duration_value INT,
    duration_unit NVARCHAR(20),
    country NVARCHAR(MAX),
    listed_in NVARCHAR(MAX)
);

-- Insert transformed data
INSERT INTO netflix_titles_clean (
    show_id,
    type,
    title,
    date_added,
    release_year,
    rating,
    duration_value,
    duration_unit,
    country,
    listed_in
)
SELECT 
    show_id,
    type,
    title,
    TRY_CONVERT(DATE, date_added) AS date_added,
    release_year,
    rating,
    CAST(LEFT(duration, CHARINDEX(' ', duration) - 1) AS INT) AS duration_value,
    CASE 
        WHEN LTRIM(SUBSTRING(duration, CHARINDEX(' ', duration) + 1, LEN(duration))) IN ('Season', 'Seasons') THEN 'season'
        WHEN LTRIM(SUBSTRING(duration, CHARINDEX(' ', duration) + 1, LEN(duration))) = 'min' THEN 'min'
        ELSE 'unknown'
    END AS duration_unit,
    country,
    listed_in
FROM netflix_titles_raw;

-- Validation
SELECT COUNT(*) AS clean_row_count
FROM netflix_titles_clean;

SELECT TOP 10 *
FROM netflix_titles_clean;

-- Distinct duration units after standardization
SELECT DISTINCT duration_unit
FROM netflix_titles_clean
ORDER BY duration_unit;