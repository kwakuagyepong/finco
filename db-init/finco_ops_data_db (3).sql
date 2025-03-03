-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 03, 2025 at 01:01 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `finco_ops_data_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `account_id` int(100) NOT NULL,
  `amount` decimal(65,0) NOT NULL,
  `credit_union_id` varchar(100) NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`account_id`, `amount`, `credit_union_id`, `date`) VALUES
(1, 534, 'CUI001', '2025-02-24 12:59:08'),
(2, 66, 'CUI002', '2025-02-24 12:59:08');

-- --------------------------------------------------------

--
-- Table structure for table `account_deposit_history`
--

CREATE TABLE `account_deposit_history` (
  `deposit_history_id` varchar(100) NOT NULL,
  `amount` decimal(10,0) NOT NULL,
  `credit_union_id` varchar(100) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Triggers `account_deposit_history`
--
DELIMITER $$
CREATE TRIGGER `before_insert_accounts_deposit_history` BEFORE INSERT ON `account_deposit_history` FOR EACH ROW BEGIN
    DECLARE new_id VARCHAR(10);
    DECLARE last_number INT;
    DECLARE duplicate_count INT;

    -- Get the last generated number
    SELECT last_id INTO last_number FROM sequence_account_deposit_history FOR UPDATE;

    -- Increment the last number by 1
    SET last_number = last_number + 1;

    -- Loop to check for duplicates
    SET duplicate_count = 1;
    SET new_id = CONCAT('ACC', LPAD(last_number, 9, '1'));

    -- Check if the generated ID already exists, and if so, increment the number
    WHILE EXISTS (SELECT 1 FROM account_deposit_history WHERE deposit_history_id = new_id) DO
        SET last_number = last_number + 1;
        SET new_id = CONCAT('TRANS', LPAD(last_number, 9, '1'));
    END WHILE;

    -- Set the new deposit_history_id
    SET NEW.deposit_history_id = new_id;

    -- Update the last generated number in the helper table
    UPDATE sequence_account_deposit_history SET last_id = last_number;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `company_accounts`
--

CREATE TABLE `company_accounts` (
  `id` int(11) NOT NULL,
  `amount` decimal(10,0) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `credentials`
--

CREATE TABLE `credentials` (
  `credencials_id` varchar(50) NOT NULL,
  `Users_ID` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('admin','manager','teller','') NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `credentials`
--

INSERT INTO `credentials` (`credencials_id`, `Users_ID`, `password`, `role`, `timestamp`) VALUES
('CRDID001', 'CUU331', 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f', 'admin', '2024-08-09 15:22:58'),
('CRDID002', 'CUU333', 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f', 'teller', '2024-08-31 10:07:45'),
('CRDID003', 'CUU334', 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f', 'manager', '2024-08-31 10:07:45'),
('CRDID015', 'CUU335', '583201c1efbf30eb13b79352ab6ebd35103ec347953d8e99858a57b5bab3dde9', 'manager', '2025-02-04 13:44:08'),
('CRDID016', 'CUU336', 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f', 'teller', '2025-03-01 16:34:44'),
('CRDID017', 'CUU337', 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f', 'teller', '2025-03-01 16:49:09');

--
-- Triggers `credentials`
--
DELIMITER $$
CREATE TRIGGER `before_insert_credentials` BEFORE INSERT ON `credentials` FOR EACH ROW BEGIN
    DECLARE new_id VARCHAR(10);
    DECLARE last_number INT;

    -- Get the last generated number
    SELECT last_id INTO last_number FROM credentials_ID_Sequence FOR UPDATE;

    -- Increment the last number by 1
    SET last_number = last_number + 1;

    -- Create the new custom Rating_id
    SET new_id = CONCAT('CRDID', LPAD(last_number, 3, '0'));

    -- Set the new Rating_id
    SET NEW.credencials_id = new_id;

    -- Update the last generated number in the helper table
    UPDATE credentials_ID_Sequence SET last_id = last_number;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `credentials_id_sequence`
--

CREATE TABLE `credentials_id_sequence` (
  `last_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `credentials_id_sequence`
--

INSERT INTO `credentials_id_sequence` (`last_id`) VALUES
(17);

-- --------------------------------------------------------

--
-- Table structure for table `creditunions`
--

CREATE TABLE `creditunions` (
  `credit_union_id` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `address` varchar(255) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `Status` enum('enabled','disabled') NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `creditunions`
--

INSERT INTO `creditunions` (`credit_union_id`, `name`, `address`, `phone_number`, `email`, `Status`, `created_at`) VALUES
('CUI001', 'First Choice', 'Adenta', '7686768768', 'koko@gmail.com', 'enabled', '2024-07-13 16:26:32'),
('CUI002', 'Mona Union', 'Kumasi', '02433242144', 'mona@gmail.com', 'disabled', '2024-08-16 08:16:56'),
('CUI003', 'Chance Credit Union', 'Accra', '0789657', 'chance@gmail.com', 'enabled', '2024-08-31 09:56:28'),
('CUI004', 'King Credit Union', 'Tema', '02433242144', 'king@gmail.com', 'enabled', '2024-08-31 09:57:58');

--
-- Triggers `creditunions`
--
DELIMITER $$
CREATE TRIGGER `before_insert_CreditUnions` BEFORE INSERT ON `creditunions` FOR EACH ROW BEGIN
    DECLARE new_id VARCHAR(10);
    DECLARE last_number INT;

    -- Get the last generated number
    SELECT last_id INTO last_number FROM CreditUnions_ID_Sequence FOR UPDATE;

    -- Increment the last number by 1
    SET last_number = last_number + 1;

    -- Create the new custom Rating_id
    SET new_id = CONCAT('CUI', LPAD(last_number, 3, '0'));

    -- Set the new Rating_id
    SET NEW.credit_union_id = new_id;

    -- Update the last generated number in the helper table
    UPDATE CreditUnions_ID_Sequence SET last_id = last_number;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `creditunions_id_sequence`
--

CREATE TABLE `creditunions_id_sequence` (
  `last_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `creditunions_id_sequence`
--

INSERT INTO `creditunions_id_sequence` (`last_id`) VALUES
(4);

-- --------------------------------------------------------

--
-- Table structure for table `customer_feedback`
--

CREATE TABLE `customer_feedback` (
  `id` int(11) NOT NULL,
  `cutomer_email` varchar(100) NOT NULL,
  `feedback_message` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `managers`
--

CREATE TABLE `managers` (
  `id` int(50) NOT NULL,
  `users_id` varchar(50) NOT NULL,
  `credit_union_id` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `managers`
--

INSERT INTO `managers` (`id`, `users_id`, `credit_union_id`) VALUES
(1, 'CUU335', 'CUI001');

-- --------------------------------------------------------

--
-- Table structure for table `sequence_account_deposit_history`
--

CREATE TABLE `sequence_account_deposit_history` (
  `last_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tokens`
--

CREATE TABLE `tokens` (
  `id` int(11) NOT NULL,
  `token` varchar(255) NOT NULL,
  `expiry_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tokens`
--

INSERT INTO `tokens` (`id`, `token`, `expiry_date`) VALUES
(1, 'qiwii233j2i3joijoiewoiejoio2i3', '2025-09-30 14:30:00');

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `TRANSACTION_ID` varchar(50) NOT NULL,
  `CUSTOMER_FIRST_NAME` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `CUSTOMER_LAST_NAME` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `TRANSACTION_TYPE` enum('CREDIT','DEBIT') CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `AMOUNT` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `ACCOUNT_NUMBER` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `CUSTOMER_ID` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `CUSTOMER_ID_CARD_IMAGE` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `CREDIT_UNION_DESTINATION_ID` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `CREDIT_UNION_ORIGINATING_ID` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `TELLER_NAME` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `ORIGINATING_MANAGER_ID` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `DESTINATION_MANAGER_ID` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `TIMESTAMP` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `DATE` date DEFAULT current_timestamp(),
  `status_transaction` enum('disbursed','not-disbursed','','') NOT NULL DEFAULT 'not-disbursed'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transactions`
--

INSERT INTO `transactions` (`TRANSACTION_ID`, `CUSTOMER_FIRST_NAME`, `CUSTOMER_LAST_NAME`, `TRANSACTION_TYPE`, `AMOUNT`, `ACCOUNT_NUMBER`, `CUSTOMER_ID`, `CUSTOMER_ID_CARD_IMAGE`, `CREDIT_UNION_DESTINATION_ID`, `CREDIT_UNION_ORIGINATING_ID`, `TELLER_NAME`, `ORIGINATING_MANAGER_ID`, `DESTINATION_MANAGER_ID`, `TIMESTAMP`, `DATE`, `status_transaction`) VALUES
('TRANS00000', 'Nana', 'Agyepong', 'DEBIT', '34', '7883637373', 'GHA-89877788-1', 'sfvsfvsvsfvf', 'CUI002', 'CUI001', 'CUU332', 'CUU331', 'CUU331', '2025-02-24 12:59:08', '2024-08-19', 'disbursed'),
('TRANS11111', 'Kay', 'Agye', 'CREDIT', '34', '12345678', 'GHA-89877788-1', 'ddfgdgdfg', 'CUI002', 'CUI001', 'CUU331', NULL, NULL, '2025-02-24 14:08:09', '2024-12-14', 'not-disbursed'),
('TRANS11112', 'Kay', 'Agyepong', 'CREDIT', '34', '12345678', 'GHA-89877788-1', 'ddfgdgdfg', 'CUI002', 'CUI001', 'CUU331', NULL, NULL, '2025-02-24 14:08:14', '2024-12-14', 'not-disbursed'),
('TRANS11113', 'Kay', 'Agyepong', 'DEBIT', '37', '12345678', 'GHA-89877788-1', 'ddfgdgdfg', 'CUI002', 'CUI001', 'CUU331', NULL, NULL, '2025-02-24 14:08:17', '2024-12-14', 'not-disbursed');

--
-- Triggers `transactions`
--
DELIMITER $$
CREATE TRIGGER `before_insert_transactions` BEFORE INSERT ON `transactions` FOR EACH ROW BEGIN
    DECLARE new_id VARCHAR(10);
    DECLARE last_number INT;
    DECLARE duplicate_count INT;

    -- Get the last generated number
    SELECT last_id INTO last_number FROM transaction_id_sequence FOR UPDATE;

    -- Increment the last number by 1
    SET last_number = last_number + 1;

    -- Loop to check for duplicates
    SET duplicate_count = 1;
    SET new_id = CONCAT('TRANS', LPAD(last_number, 9, '1'));

    -- Check if the generated ID already exists, and if so, increment the number
    WHILE EXISTS (SELECT 1 FROM transactions WHERE TRANSACTION_ID = new_id) DO
        SET last_number = last_number + 1;
        SET new_id = CONCAT('TRANS', LPAD(last_number, 9, '1'));
    END WHILE;

    -- Set the new TRANSACTION_ID
    SET NEW.TRANSACTION_ID = new_id;

    -- Update the last generated number in the helper table
    UPDATE transaction_id_sequence SET last_id = last_number;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `transaction_id_sequence`
--

CREATE TABLE `transaction_id_sequence` (
  `last_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transaction_id_sequence`
--

INSERT INTO `transaction_id_sequence` (`last_id`) VALUES
(30000);

-- --------------------------------------------------------

--
-- Table structure for table `users_of_credit_union`
--

CREATE TABLE `users_of_credit_union` (
  `credit_union_user_id` varchar(50) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone_number` int(11) NOT NULL,
  `credit_union_id` varchar(11) NOT NULL,
  `status` enum('active','inactive','','') NOT NULL,
  `Timestamp` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `users_of_credit_union`
--

INSERT INTO `users_of_credit_union` (`credit_union_user_id`, `first_name`, `last_name`, `email`, `phone_number`, `credit_union_id`, `status`, `Timestamp`) VALUES
('CUU331', 'Prince', 'Koo', 'testing@gmail.com', 3546446, 'CUI001', 'active', '2024-07-13 16:15:12'),
('CUU332', 'Ama', 'Agyemang', 'koko@gmail.com', 2433242, 'CUI001', 'active', '2024-08-17 15:15:18'),
('CUU333', 'Joseph', 'Gbekley', 'joe@gmail.com', 9090988, 'CUI001', 'active', '2024-08-31 10:52:13'),
('CUU334', 'Kay', 'Agyemang', 'kay@gmail.com', 980998, 'CUI002', 'active', '2024-08-31 10:52:13'),
('CUU335', 'Kwame', 'Agye', 'kay@gmail.com', 266758475, 'CUI001', 'active', '2025-01-23 21:26:35'),
('CUU336', 'Kwame', 'Yaw', 'koko@gmail.com', 88595878, 'CUI002', 'inactive', '2025-03-01 16:34:44'),
('CUU337', 'yaa ', 'Mansah', 'yaa@yahoo.com', 78945945, 'CUI001', 'inactive', '2025-03-01 16:49:09');

--
-- Triggers `users_of_credit_union`
--
DELIMITER $$
CREATE TRIGGER `after_insert_create_credentials` AFTER INSERT ON `users_of_credit_union` FOR EACH ROW BEGIN
    INSERT INTO credentials (Users_ID, password, role)
    VALUES (NEW.credit_union_user_id, 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f', 'teller');
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `before_insert_Users_of_credit_union` BEFORE INSERT ON `users_of_credit_union` FOR EACH ROW BEGIN
    DECLARE new_id VARCHAR(10);
    DECLARE last_number INT;

    -- Get the last generated number
    SELECT last_id INTO last_number FROM Users_of_credit_union_ID_Sequence FOR UPDATE;

    -- Increment the last number by 1
    SET last_number = last_number + 1;

    -- Create the new custom Rating_id
    SET new_id = CONCAT('CUU', LPAD(last_number, 3, '3'));

    -- Set the new Rating_id
    SET NEW.credit_union_user_id = new_id;

    -- Update the last generated number in the helper table
    UPDATE Users_of_credit_union_ID_Sequence SET last_id = last_number;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `users_of_credit_union_id_sequence`
--

CREATE TABLE `users_of_credit_union_id_sequence` (
  `last_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `users_of_credit_union_id_sequence`
--

INSERT INTO `users_of_credit_union_id_sequence` (`last_id`) VALUES
(7);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`account_id`),
  ADD KEY `fk_account_credit_union` (`credit_union_id`);

--
-- Indexes for table `account_deposit_history`
--
ALTER TABLE `account_deposit_history`
  ADD PRIMARY KEY (`deposit_history_id`),
  ADD KEY `credit_union_id` (`credit_union_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `company_accounts`
--
ALTER TABLE `company_accounts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `credentials`
--
ALTER TABLE `credentials`
  ADD PRIMARY KEY (`credencials_id`),
  ADD KEY `Users_ID` (`Users_ID`);

--
-- Indexes for table `creditunions`
--
ALTER TABLE `creditunions`
  ADD PRIMARY KEY (`credit_union_id`);

--
-- Indexes for table `customer_feedback`
--
ALTER TABLE `customer_feedback`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `managers`
--
ALTER TABLE `managers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_manager_user` (`users_id`),
  ADD KEY `fk_manager_credit_union` (`credit_union_id`);

--
-- Indexes for table `tokens`
--
ALTER TABLE `tokens`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `token` (`token`);

--
-- Indexes for table `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`TRANSACTION_ID`),
  ADD KEY `CREDIT_UNION_ID_INBOUND` (`CREDIT_UNION_ORIGINATING_ID`),
  ADD KEY `CREDIT_UNION_ID_OUTBOUND` (`CREDIT_UNION_DESTINATION_ID`),
  ADD KEY `TELLER_NAME` (`TELLER_NAME`),
  ADD KEY `INBOUND_MANAGER` (`ORIGINATING_MANAGER_ID`),
  ADD KEY `OUTBOUND_MANAGER` (`DESTINATION_MANAGER_ID`);

--
-- Indexes for table `users_of_credit_union`
--
ALTER TABLE `users_of_credit_union`
  ADD PRIMARY KEY (`credit_union_user_id`),
  ADD KEY `fk_credit_union_id` (`credit_union_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts`
--
ALTER TABLE `accounts`
  MODIFY `account_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `company_accounts`
--
ALTER TABLE `company_accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customer_feedback`
--
ALTER TABLE `customer_feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `managers`
--
ALTER TABLE `managers`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tokens`
--
ALTER TABLE `tokens`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts`
--
ALTER TABLE `accounts`
  ADD CONSTRAINT `fk_account_credit_union` FOREIGN KEY (`credit_union_id`) REFERENCES `creditunions` (`credit_union_id`) ON UPDATE CASCADE;

--
-- Constraints for table `account_deposit_history`
--
ALTER TABLE `account_deposit_history`
  ADD CONSTRAINT `account_deposit_history_ibfk_1` FOREIGN KEY (`credit_union_id`) REFERENCES `creditunions` (`credit_union_id`),
  ADD CONSTRAINT `account_deposit_history_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users_of_credit_union` (`credit_union_user_id`);

--
-- Constraints for table `company_accounts`
--
ALTER TABLE `company_accounts`
  ADD CONSTRAINT `company_accounts_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users_of_credit_union` (`credit_union_user_id`);

--
-- Constraints for table `credentials`
--
ALTER TABLE `credentials`
  ADD CONSTRAINT `credentials_ibfk_1` FOREIGN KEY (`Users_ID`) REFERENCES `users_of_credit_union` (`credit_union_user_id`) ON UPDATE CASCADE;

--
-- Constraints for table `managers`
--
ALTER TABLE `managers`
  ADD CONSTRAINT `fk_manager_credit_union` FOREIGN KEY (`credit_union_id`) REFERENCES `creditunions` (`credit_union_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_manager_user` FOREIGN KEY (`users_id`) REFERENCES `users_of_credit_union` (`credit_union_user_id`) ON UPDATE CASCADE;

--
-- Constraints for table `transactions`
--
ALTER TABLE `transactions`
  ADD CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`CREDIT_UNION_ORIGINATING_ID`) REFERENCES `creditunions` (`credit_union_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `transactions_ibfk_2` FOREIGN KEY (`CREDIT_UNION_DESTINATION_ID`) REFERENCES `creditunions` (`credit_union_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `transactions_ibfk_3` FOREIGN KEY (`TELLER_NAME`) REFERENCES `users_of_credit_union` (`credit_union_user_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `transactions_ibfk_4` FOREIGN KEY (`ORIGINATING_MANAGER_ID`) REFERENCES `users_of_credit_union` (`credit_union_user_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `transactions_ibfk_5` FOREIGN KEY (`DESTINATION_MANAGER_ID`) REFERENCES `users_of_credit_union` (`credit_union_user_id`) ON UPDATE CASCADE;

--
-- Constraints for table `users_of_credit_union`
--
ALTER TABLE `users_of_credit_union`
  ADD CONSTRAINT `fk_credit_union_id` FOREIGN KEY (`credit_union_id`) REFERENCES `creditunions` (`credit_union_id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
