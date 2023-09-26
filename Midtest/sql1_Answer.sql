CREATE TABLE input_table (
    id INT PRIMARY KEY,
    num INT
);

INSERT INTO input_table (id, num) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 2),
(5, 2),
(6, 3),
(7, 3),
(8, 3),
(9, 4),
(10, 4);

WITH Morethan3 AS (
    SELECT id,num,
        LAG(num) OVER (ORDER BY id) AS prev_num,
        LEAD(num) OVER (ORDER BY id) AS next_num
    FROM input_table
)
SELECT DISTINCT num
FROM Morethan3
WHERE num = prev_num AND num = next_num
ORDER BY num ASC;