USE local_elbowspace;
INSERT INTO `users` (FirstName, LastName, Email, Password)
VALUES ('User1', 'ULast', 'test@local.com', '1234abcd'), 
('User2','U2Last','test2@local.com','AbCd1234')
;
COMMIT;