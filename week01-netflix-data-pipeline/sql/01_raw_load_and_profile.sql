-- Create database
CREATE DATABASE netflix_project;
GO

USE netflix_project;
GO

-- Raw table
CREATE TABLE netflix_titles_raw (
    show_id NVARCHAR(50),
    type NVARCHAR(50),
    title NVARCHAR(300),
    director NVARCHAR(MAX),
    cast NVARCHAR(MAX),
    country NVARCHAR(MAX),
    date_added NVARCHAR(100),
    release_year INT,
    rating NVARCHAR(50),
    duration NVARCHAR(50),
    listed_in NVARCHAR(MAX),
    description NVARCHAR(MAX)
);

-- Row count check
SELECT COUNT(*) AS total_rows
FROM netflix_titles_raw;

-- Preview data
SELECT TOP 10 *
FROM netflix_titles_raw;

-- Missing value checks
SELECT 
    COUNT(*) AS total_rows,
    SUM(CASE WHEN director IS NULL OR LTRIM(RTRIM(director)) = '' THEN 1 ELSE 0 END) AS missing_director,
    SUM(CASE WHEN cast IS NULL OR LTRIM(RTRIM(cast)) = '' THEN 1 ELSE 0 END) AS missing_cast,
    SUM(CASE WHEN country IS NULL OR LTRIM(RTRIM(country)) = '' THEN 1 ELSE 0 END) AS missing_country
FROM netflix_titles_raw;

-- Type distribution
SELECT 
    type,
    COUNT(*) AS total_count
FROM netflix_titles_raw
GROUP BY type;

-- Date completeness
SELECT 
    COUNT(*) AS total_rows,
    SUM(CASE WHEN date_added IS NULL OR LTRIM(RTRIM(date_added)) = '' THEN 1 ELSE 0 END) AS missing_date_added
FROM netflix_titles_raw;

-- Invalid date format check
SELECT 
    COUNT(*) AS invalid_date_format_count
FROM netflix_titles_raw
WHERE date_added IS NOT NULL
  AND LTRIM(RTRIM(date_added)) <> ''
  AND TRY_CONVERT(DATE, date_added) IS NULL;

-- Duration pattern check
SELECT DISTINCT duration
FROM netflix_titles_raw
WHERE duration IS NOT NULL
ORDER BY duration;