-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 02, 2024 at 05:52 AM
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
  `Age` int(10) NOT NULL,
  `Discount` int(30) NOT NULL,
  `Total_Amount` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `member_information`
--

INSERT INTO `member_information` (`Name`, `ID_Number`, `Gender`, `Year_of_Born`, `Age`, `Discount`, `Total_Amount`) VALUES
('Ummi', 2004880067, 'Female', 2004, 19, 0, 50),
('Izzati', 2013559990, 'Female', 2013, 10, 10, 45);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
