# Write your MySQL query statement below
/*
SELECT 
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
*/

Select score, DENSE_RANK() OVER (ORDER BY SCORE DESC) as `rank`
from Scores

