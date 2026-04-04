USE netflix_project;
GO

-- Movies vs TV Shows
SELECT 
    type,
    COUNT(*) AS total_count
FROM netflix_titles_clean
GROUP BY type;

-- Content added by year
SELECT 
    YEAR(date_added) AS year_added,
    COUNT(*) AS total_content
FROM netflix_titles_clean
WHERE date_added IS NOT NULL
GROUP BY YEAR(date_added)
ORDER BY year_added;

-- Average movie duration
SELECT 
    AVG(duration_value * 1.0) AS avg_movie_duration
FROM netflix_titles_clean
WHERE duration_unit = 'min';

-- Average number of seasons
SELECT 
    AVG(duration_value * 1.0) AS avg_seasons
FROM netflix_titles_clean
WHERE duration_unit = 'season';