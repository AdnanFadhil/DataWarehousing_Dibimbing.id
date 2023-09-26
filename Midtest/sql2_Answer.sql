CREATE TABLE email_list (
    id INT PRIMARY KEY,
    email VARCHAR(255) 
);

INSERT INTO email_list (id, email)
VALUES
    (1, 'user1@example.com'),
    (2, 'user2@example.com'),
    (3, 'user3@example.com'),
    (4, 'user3@example.com'),
    (5, 'user3@example.com'),
    (6, 'user6@example.com'),
    (7, 'user7@example.com'),
    (8, 'user8@example.com'),
    (9, 'user9@example.com'),
    (10, 'user10@example.com'),
    (11, 'user11@example.com'),
    (12, 'user12@example.com'),
    (13, 'user13@example.com'),
    (14, 'user14@example.com'),
    (15, 'user15@example.com'),
    (16, 'user16@example.com'),
    (17, 'user17@example.com'),
    (18, 'user18@example.com'),
    (19, 'user19@example.com'),
    (20, 'user20@example.com'),
    (21, 'user1@example.com'),  -- Duplicate email
    (22, 'user2@example.com'),  -- Duplicate email
    (23, 'user3@example.com'),  -- Duplicate email
    (24, 'user24@example.com'),
    (25, 'user25@example.com'),
    (26, 'user26@example.com'),
    (27, 'user27@example.com'),
    (28, 'user28@example.com'),
    (29, 'user29@example.com'),
    (30, 'user30@example.com');  -- Duplicate email, more than 2 times

SELECT DISTINCT email
FROM email_list
WHERE email IN (
    SELECT email
    FROM email_list
    GROUP BY email
    HAVING COUNT(email) > 1
);