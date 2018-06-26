-- list all records with [score >= 10] in descending order
--
-- score   name
-- 14  Bob
-- 10  John

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
