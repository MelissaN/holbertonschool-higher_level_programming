-- Update data in table; change Bob's score to 10
--
-- score   name
-- 10  Bob
-- 10  John
-- 8   George
-- 3   Alex

UPDATE second_table SET `score` = 10 WHERE `name` = 'Bob';
