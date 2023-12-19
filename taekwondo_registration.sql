-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 19, 2023 at 10:40 AM
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
-- Database: `taekwondo_registration`
--

-- --------------------------------------------------------

--
-- Table structure for table `member_information`
--

CREATE TABLE `member_information` (
  `Name` varchar(30) NOT NULL,
  `ID_Number` int(20) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Year_of_Born` int(10) NOT NULL,
  `Age` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `member_information`
--

INSERT INTO `member_information` (`Name`, `ID_Number`, `Gender`, `Year_of_Born`, `Age`) VALUES
('ummi', 0, '20288', 2004, 4054092),
('ummi kalsum', 0, '2022820722', 2004, 19),
('Hairiena', 0, '2022829308', 2021, 2),
('ummi', 0, '2022820722', 2004, 19);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
