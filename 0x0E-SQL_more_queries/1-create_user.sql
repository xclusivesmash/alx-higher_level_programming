-- Creating a new user.
--
-- user to be added: user_0d_1 with all priviledges
-- on mysql server.

CREATE IF NOT EXISTS `user_0d_1`@`localhost` IDENTIFIED BY "user_0d_1_pwd";
GRANT ALL PRIVILEDGES ON *.* TO `user_0d_1`@`localhost`;
