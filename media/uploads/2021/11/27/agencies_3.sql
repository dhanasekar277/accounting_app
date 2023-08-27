-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 25, 2021 at 11:56 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 7.4.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `agencies`
--

-- --------------------------------------------------------

--
-- Table structure for table `agency_agency`
--

CREATE TABLE `agency_agency` (
  `id` bigint(20) NOT NULL,
  `Agency_Name` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Phone` varchar(100) DEFAULT NULL,
  `Logo` varchar(100) DEFAULT NULL,
  `Active` tinyint(1) NOT NULL,
  `Timestamp` datetime(6) NOT NULL,
  `Updated` datetime(6) NOT NULL,
  `GST_Number` varchar(100) DEFAULT NULL,
  `PAN_Number` varchar(100) DEFAULT NULL,
  `Tin` varchar(100) DEFAULT NULL,
  `User_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `agency_agency`
--

INSERT INTO `agency_agency` (`id`, `Agency_Name`, `Email`, `Phone`, `Logo`, `Active`, `Timestamp`, `Updated`, `GST_Number`, `PAN_Number`, `Tin`, `User_id`) VALUES
(2, 'Mathi Agencies', 'mathiagency@gmail.com', '8567657767', 'uploads/2021/11/17/mathiagencies.png', 0, '2021-11-22 09:44:47.356288', '2021-11-23 18:39:46.760892', '54359350982', '2343244', '8345989435', 1),
(3, 'Kavi Agencies', 'kavithagency@gmail.com', '8578987989', 'uploads/2021/11/17/rakeagencies.png', 0, '2021-11-22 09:44:47.356288', '2021-11-23 18:39:26.409196', '54359350982', '2343244', '8345989435', 1),
(6, 'Hari Agencies', 'hariagencies@gmaiil.com', '8884734594', 'uploads/2021/11/21/hariagencies.png', 1, '2021-11-22 10:07:20.316510', '2021-11-23 18:35:20.423006', '54359350982', '123456', '8345989435', 1);

-- --------------------------------------------------------

--
-- Table structure for table `agency_agencybankaccount`
--

CREATE TABLE `agency_agencybankaccount` (
  `id` bigint(20) NOT NULL,
  `Account_Number` varchar(100) DEFAULT NULL,
  `IFSC_Code` varchar(100) DEFAULT NULL,
  `Branch` varchar(100) DEFAULT NULL,
  `Register_Email` varchar(100) DEFAULT NULL,
  `Register_Phone` varchar(100) DEFAULT NULL,
  `Timestamp` datetime(6) NOT NULL,
  `Updated` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `agency_agencybankaccount`
--

INSERT INTO `agency_agencybankaccount` (`id`, `Account_Number`, `IFSC_Code`, `Branch`, `Register_Email`, `Register_Phone`, `Timestamp`, `Updated`) VALUES
(1, '983249324798324', '324234', 'taramani', 'hariagencies@gmail.com', '7834587435', '2021-11-22 10:05:43.105616', '2021-11-22 10:05:43.105616'),
(2, '231231232', '1234', 'velachery', 'issac@gmail.com', '87237486823', '2021-11-23 03:05:46.775411', '2021-11-23 03:05:46.775411'),
(6, '123123', '1324', 'tarmani', 'taramani@gmail.com', '456456645', '2021-11-23 03:16:53.514200', '2021-11-23 03:16:53.514200');

-- --------------------------------------------------------

--
-- Table structure for table `agency_agencycertificate`
--

CREATE TABLE `agency_agencycertificate` (
  `id` bigint(20) NOT NULL,
  `Certificate_Name` varchar(100) DEFAULT NULL,
  `Certificate_Scan_Copy` varchar(100) DEFAULT NULL,
  `Timestamp` datetime(6) NOT NULL,
  `Updated` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `agency_agencycertificate`
--

INSERT INTO `agency_agencycertificate` (`id`, `Certificate_Name`, `Certificate_Scan_Copy`, `Timestamp`, `Updated`) VALUES
(1, 'Gst certificate', 'uploads/2021/11/22/registration-certificate-1.png', '2021-11-22 10:06:59.183001', '2021-11-22 10:06:59.183001'),
(37, 'Gst certificates', 'uploads/2021/11/23/registration-certificate-1_1_9oskXyC.png', '2021-11-23 08:32:29.709092', '2021-11-23 08:32:29.709092');

-- --------------------------------------------------------

--
-- Table structure for table `agency_agency_bank_account`
--

CREATE TABLE `agency_agency_bank_account` (
  `id` bigint(20) NOT NULL,
  `agency_id` bigint(20) NOT NULL,
  `agencybankaccount_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `agency_agency_bank_account`
--

INSERT INTO `agency_agency_bank_account` (`id`, `agency_id`, `agencybankaccount_id`) VALUES
(9, 2, 1),
(10, 2, 2),
(8, 3, 2),
(1, 6, 1),
(7, 6, 2);

-- --------------------------------------------------------

--
-- Table structure for table `agency_agency_certificates`
--

CREATE TABLE `agency_agency_certificates` (
  `id` bigint(20) NOT NULL,
  `agency_id` bigint(20) NOT NULL,
  `agencycertificate_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `agency_agency_certificates`
--

INSERT INTO `agency_agency_certificates` (`id`, `agency_id`, `agencycertificate_id`) VALUES
(8, 2, 1),
(9, 2, 37),
(6, 3, 1),
(7, 3, 37),
(1, 6, 1);

-- --------------------------------------------------------

--
-- Table structure for table `authtoken_token`
--

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add agency bank account', 7, 'add_agencybankaccount'),
(26, 'Can change agency bank account', 7, 'change_agencybankaccount'),
(27, 'Can delete agency bank account', 7, 'delete_agencybankaccount'),
(28, 'Can view agency bank account', 7, 'view_agencybankaccount'),
(29, 'Can add agency certificate', 8, 'add_agencycertificate'),
(30, 'Can change agency certificate', 8, 'change_agencycertificate'),
(31, 'Can delete agency certificate', 8, 'delete_agencycertificate'),
(32, 'Can view agency certificate', 8, 'view_agencycertificate'),
(33, 'Can add agency', 9, 'add_agency'),
(34, 'Can change agency', 9, 'change_agency'),
(35, 'Can delete agency', 9, 'delete_agency'),
(36, 'Can view agency', 9, 'view_agency'),
(37, 'Can add customer bank accounts', 10, 'add_customerbankaccounts'),
(38, 'Can change customer bank accounts', 10, 'change_customerbankaccounts'),
(39, 'Can delete customer bank accounts', 10, 'delete_customerbankaccounts'),
(40, 'Can view customer bank accounts', 10, 'view_customerbankaccounts'),
(41, 'Can add customer delivery address', 11, 'add_customerdeliveryaddress'),
(42, 'Can change customer delivery address', 11, 'change_customerdeliveryaddress'),
(43, 'Can delete customer delivery address', 11, 'delete_customerdeliveryaddress'),
(44, 'Can view customer delivery address', 11, 'view_customerdeliveryaddress'),
(45, 'Can add customer gst billing address', 12, 'add_customergstbillingaddress'),
(46, 'Can change customer gst billing address', 12, 'change_customergstbillingaddress'),
(47, 'Can delete customer gst billing address', 12, 'delete_customergstbillingaddress'),
(48, 'Can view customer gst billing address', 12, 'view_customergstbillingaddress'),
(49, 'Can add customer staff', 13, 'add_customerstaff'),
(50, 'Can change customer staff', 13, 'change_customerstaff'),
(51, 'Can delete customer staff', 13, 'delete_customerstaff'),
(52, 'Can view customer staff', 13, 'view_customerstaff'),
(53, 'Can add customer', 14, 'add_customer'),
(54, 'Can change customer', 14, 'change_customer'),
(55, 'Can delete customer', 14, 'delete_customer'),
(56, 'Can view customer', 14, 'view_customer'),
(57, 'Can add material order', 15, 'add_materialorder'),
(58, 'Can change material order', 15, 'change_materialorder'),
(59, 'Can delete material order', 15, 'delete_materialorder'),
(60, 'Can view material order', 15, 'view_materialorder'),
(61, 'Can add po number', 16, 'add_ponumber'),
(62, 'Can change po number', 16, 'change_ponumber'),
(63, 'Can delete po number', 16, 'delete_ponumber'),
(64, 'Can view po number', 16, 'view_ponumber'),
(65, 'Can add order', 17, 'add_order'),
(66, 'Can change order', 17, 'change_order'),
(67, 'Can delete order', 17, 'delete_order'),
(68, 'Can view order', 17, 'view_order'),
(69, 'Can add product', 18, 'add_product'),
(70, 'Can change product', 18, 'change_product'),
(71, 'Can delete product', 18, 'delete_product'),
(72, 'Can view product', 18, 'view_product'),
(73, 'Can add vendor certificate', 19, 'add_vendorcertificate'),
(74, 'Can change vendor certificate', 19, 'change_vendorcertificate'),
(75, 'Can delete vendor certificate', 19, 'delete_vendorcertificate'),
(76, 'Can view vendor certificate', 19, 'view_vendorcertificate'),
(77, 'Can add vendor gst bank account', 20, 'add_vendorgstbankaccount'),
(78, 'Can change vendor gst bank account', 20, 'change_vendorgstbankaccount'),
(79, 'Can delete vendor gst bank account', 20, 'delete_vendorgstbankaccount'),
(80, 'Can view vendor gst bank account', 20, 'view_vendorgstbankaccount'),
(81, 'Can add vendor staff detail', 21, 'add_vendorstaffdetail'),
(82, 'Can change vendor staff detail', 21, 'change_vendorstaffdetail'),
(83, 'Can delete vendor staff detail', 21, 'delete_vendorstaffdetail'),
(84, 'Can view vendor staff detail', 21, 'view_vendorstaffdetail'),
(85, 'Can add vendor gst', 22, 'add_vendorgst'),
(86, 'Can change vendor gst', 22, 'change_vendorgst'),
(87, 'Can delete vendor gst', 22, 'delete_vendorgst'),
(88, 'Can view vendor gst', 22, 'view_vendorgst'),
(89, 'Can add vendor', 23, 'add_vendor'),
(90, 'Can change vendor', 23, 'change_vendor'),
(91, 'Can delete vendor', 23, 'delete_vendor'),
(92, 'Can view vendor', 23, 'view_vendor'),
(93, 'Can add Token', 24, 'add_token'),
(94, 'Can change Token', 24, 'change_token'),
(95, 'Can delete Token', 24, 'delete_token'),
(96, 'Can view Token', 24, 'view_token'),
(97, 'Can add token', 25, 'add_tokenproxy'),
(98, 'Can change token', 25, 'change_tokenproxy'),
(99, 'Can delete token', 25, 'delete_tokenproxy'),
(100, 'Can view token', 25, 'view_tokenproxy');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$DboCJDnkMQqFVQqIjoO5Dr$cxsZHOR+Wh8Z/Qzh+By7oNN/gFHTTCueIEvgtdq0ARw=', '2021-11-25 05:08:20.455855', 1, 'root', '', '', '', 1, 1, '2021-11-25 04:59:38.004884');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `customers_customer`
--

CREATE TABLE `customers_customer` (
  `id` bigint(20) NOT NULL,
  `Founder_Name` varchar(100) DEFAULT NULL,
  `Company_Name` varchar(100) DEFAULT NULL,
  `Founder_Phone` varchar(50) DEFAULT NULL,
  `Founder_Email` varchar(50) DEFAULT NULL,
  `Founder_Address` longtext DEFAULT NULL,
  `GST_Type` varchar(1) NOT NULL,
  `PAN_No` varchar(100) DEFAULT NULL,
  `PAN_Scan_Copy` varchar(100) DEFAULT NULL,
  `No_Of_Project` varchar(10) DEFAULT NULL,
  `Remarks` longtext DEFAULT NULL,
  `Payment_Terms` varchar(100) DEFAULT NULL,
  `published` datetime(6) NOT NULL,
  `GST_No_id` bigint(20) DEFAULT NULL,
  `User_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `customers_customerbankaccounts`
--

CREATE TABLE `customers_customerbankaccounts` (
  `id` bigint(20) NOT NULL,
  `Category` varchar(1) NOT NULL,
  `Account_No` varchar(100) DEFAULT NULL,
  `IFSC_Code` varchar(100) DEFAULT NULL,
  `Branch` varchar(100) DEFAULT NULL,
  `Register_Phone` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `customers_customerdeliveryaddress`
--

CREATE TABLE `customers_customerdeliveryaddress` (
  `id` bigint(20) NOT NULL,
  `Branch` varchar(200) DEFAULT NULL,
  `URL_Location_Of_The_Unloading_Place` varchar(200) DEFAULT NULL,
  `URL_Office_Location` varchar(200) DEFAULT NULL,
  `URL_Of_Owner_House` varchar(200) DEFAULT NULL,
  `Invoice_Submitting_URL` varchar(200) DEFAULT NULL,
  `Payment_Collecting_URL` varchar(200) DEFAULT NULL,
  `Add_other_URL` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `customers_customergstbillingaddress`
--

CREATE TABLE `customers_customergstbillingaddress` (
  `id` bigint(20) NOT NULL,
  `GST_No` varchar(100) DEFAULT NULL,
  `Scan_Copy` varchar(100) DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `City` varchar(20) DEFAULT NULL,
  `State` varchar(30) DEFAULT NULL,
  `Zip` varchar(10) DEFAULT NULL,
  `Country` varchar(30) DEFAULT NULL,
  `Location_Url` varchar(100) DEFAULT NULL,
  `Mobile` varchar(20) DEFAULT NULL,
  `Mail_Id` varchar(50) DEFAULT NULL,
  `Photo` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `customers_customerstaff`
--

CREATE TABLE `customers_customerstaff` (
  `id` bigint(20) NOT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `Contact_No` varchar(20) DEFAULT NULL,
  `Email` varchar(30) DEFAULT NULL,
  `Position` varchar(2) NOT NULL,
  `Location` varchar(100) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  `Zip` varchar(50) DEFAULT NULL,
  `State` varchar(50) DEFAULT NULL,
  `Country` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `customers_customer_bank_account`
--

CREATE TABLE `customers_customer_bank_account` (
  `id` bigint(20) NOT NULL,
  `customer_id` bigint(20) NOT NULL,
  `customerbankaccounts_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `customers_customer_delivery_address`
--

CREATE TABLE `customers_customer_delivery_address` (
  `id` bigint(20) NOT NULL,
  `customer_id` bigint(20) NOT NULL,
  `customerdeliveryaddress_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-11-25 08:03:14.768157', '4', 'None', 3, '', 19, 1),
(2, '2021-11-25 08:03:14.875927', '3', 'None', 3, '', 19, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(9, 'agency', 'agency'),
(7, 'agency', 'agencybankaccount'),
(8, 'agency', 'agencycertificate'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(24, 'authtoken', 'token'),
(25, 'authtoken', 'tokenproxy'),
(5, 'contenttypes', 'contenttype'),
(14, 'customers', 'customer'),
(10, 'customers', 'customerbankaccounts'),
(11, 'customers', 'customerdeliveryaddress'),
(12, 'customers', 'customergstbillingaddress'),
(13, 'customers', 'customerstaff'),
(15, 'orders', 'materialorder'),
(17, 'orders', 'order'),
(16, 'orders', 'ponumber'),
(18, 'products', 'product'),
(6, 'sessions', 'session'),
(23, 'vendors', 'vendor'),
(19, 'vendors', 'vendorcertificate'),
(22, 'vendors', 'vendorgst'),
(20, 'vendors', 'vendorgstbankaccount'),
(21, 'vendors', 'vendorstaffdetail');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-11-25 04:22:00.751787'),
(2, 'auth', '0001_initial', '2021-11-25 04:22:10.576544'),
(3, 'admin', '0001_initial', '2021-11-25 04:22:12.721956'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-11-25 04:22:12.812392'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-11-25 04:22:12.874882'),
(6, 'agency', '0001_initial', '2021-11-25 04:22:19.837084'),
(7, 'contenttypes', '0002_remove_content_type_name', '2021-11-25 04:22:21.166783'),
(8, 'auth', '0002_alter_permission_name_max_length', '2021-11-25 04:22:22.089210'),
(9, 'auth', '0003_alter_user_email_max_length', '2021-11-25 04:22:22.220573'),
(10, 'auth', '0004_alter_user_username_opts', '2021-11-25 04:22:22.274525'),
(11, 'auth', '0005_alter_user_last_login_null', '2021-11-25 04:22:22.827776'),
(12, 'auth', '0006_require_contenttypes_0002', '2021-11-25 04:22:22.890274'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2021-11-25 04:22:22.995035'),
(14, 'auth', '0008_alter_user_username_max_length', '2021-11-25 04:22:23.196838'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2021-11-25 04:22:23.342443'),
(16, 'auth', '0010_alter_group_name_max_length', '2021-11-25 04:22:23.495996'),
(17, 'auth', '0011_update_proxy_permissions', '2021-11-25 04:22:23.569579'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2021-11-25 04:22:23.680151'),
(19, 'authtoken', '0001_initial', '2021-11-25 04:22:25.064501'),
(20, 'authtoken', '0002_auto_20160226_1747', '2021-11-25 04:22:25.314940'),
(21, 'authtoken', '0003_tokenproxy', '2021-11-25 04:22:25.366606'),
(22, 'customers', '0001_initial', '2021-11-25 04:22:34.853032'),
(23, 'vendors', '0001_initial', '2021-11-25 04:22:49.890110'),
(24, 'products', '0001_initial', '2021-11-25 04:22:52.399850'),
(25, 'orders', '0001_initial', '2021-11-25 04:23:06.349167'),
(26, 'sessions', '0001_initial', '2021-11-25 04:23:07.584586'),
(27, 'vendors', '0002_auto_20211125_1146', '2021-11-25 06:16:59.837714'),
(28, 'vendors', '0003_vendorcertificate_vendor_company_name', '2021-11-25 08:25:21.049698'),
(29, 'vendors', '0004_vendorgstbankaccount_vendor_company_name', '2021-11-25 08:27:39.606197'),
(30, 'vendors', '0005_alter_vendorgst_vendor_company_name', '2021-11-25 08:54:30.101496'),
(31, 'vendors', '0006_alter_vendorgst_vendor_gst_type', '2021-11-25 08:59:46.565532'),
(32, 'vendors', '0007_alter_vendor_vendor_type', '2021-11-25 09:00:20.431051'),
(33, 'vendors', '0008_rename_name_vendorstaffdetail_vendor_company_name', '2021-11-25 09:09:42.605928'),
(34, 'vendors', '0009_alter_vendor_published', '2021-11-25 10:26:05.244479');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('umg41ivzl5ujglru19y6fbo8bonsgeka', '.eJxVjDsOwyAQRO9CHSE-hoWU6X0GtLAQnERYMnYV5e6xJRdJNdK8N_NmAbe1hq3nJUzErkyyy28XMT1zOwA9sN1nnua2LlPkh8JP2vk4U37dTvfvoGKv-9oq0EVSElEBirznQF6nCIPQUJxW1hdQiNmDcU4QGmeskZiUNKgkss8X2Q83Yg:1mq6zc:jl6RDDcm8FlUYTZaI4mky0fEUKNxJbnFksj7_yO_9nw', '2021-12-09 05:08:20.586957');

-- --------------------------------------------------------

--
-- Table structure for table `orders_materialorder`
--

CREATE TABLE `orders_materialorder` (
  `id` bigint(20) NOT NULL,
  `Material_Name` varchar(100) DEFAULT NULL,
  `Offer_Price` varchar(50) DEFAULT NULL,
  `No_Of_Load` varchar(50) DEFAULT NULL,
  `Expected_Date` date NOT NULL,
  `Quantity` varchar(50) DEFAULT NULL,
  `HSNCode` varchar(50) DEFAULT NULL,
  `Quality_Material_Type` varchar(1) DEFAULT NULL,
  `Moisture` varchar(1) DEFAULT NULL,
  `Moisture_Number` varchar(50) DEFAULT NULL,
  `Material_Term` varchar(100) DEFAULT NULL,
  `Others` longtext NOT NULL,
  `Product_Name_id` bigint(20) NOT NULL,
  `User_id` int(11) NOT NULL,
  `Vendor_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `orders_order`
--

CREATE TABLE `orders_order` (
  `id` bigint(20) NOT NULL,
  `Billing_Address` longtext NOT NULL,
  `Expected_Delivery_Date` date NOT NULL,
  `Remarks` longtext NOT NULL,
  `Approved` tinyint(1) NOT NULL,
  `Agency_id` bigint(20) NOT NULL,
  `PO_Number_id` bigint(20) NOT NULL,
  `Sales_Company_id` bigint(20) NOT NULL,
  `User_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `orders_order_materials`
--

CREATE TABLE `orders_order_materials` (
  `id` bigint(20) NOT NULL,
  `order_id` bigint(20) NOT NULL,
  `materialorder_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `orders_order_sales_delivery_address`
--

CREATE TABLE `orders_order_sales_delivery_address` (
  `id` bigint(20) NOT NULL,
  `order_id` bigint(20) NOT NULL,
  `customerdeliveryaddress_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `orders_ponumber`
--

CREATE TABLE `orders_ponumber` (
  `id` bigint(20) NOT NULL,
  `PO_Type` varchar(2) NOT NULL,
  `PO_Number` varchar(100) DEFAULT NULL,
  `Scan_Copy` varchar(100) DEFAULT NULL,
  `PO_Recived_From_Name` varchar(50) DEFAULT NULL,
  `PO_Recived_From_Mail` varchar(50) DEFAULT NULL,
  `PO_Approved_By` varchar(50) DEFAULT NULL,
  `PO_Quantity` varchar(10) DEFAULT NULL,
  `PO_Material` varchar(50) DEFAULT NULL,
  `PO_Rate` varchar(50) DEFAULT NULL,
  `PO_Date` date DEFAULT NULL,
  `Sales_Rate` varchar(100) DEFAULT NULL,
  `Order_Recieved_Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `products_product`
--

CREATE TABLE `products_product` (
  `id` bigint(20) NOT NULL,
  `Product` varchar(100) NOT NULL,
  `Price` varchar(100) NOT NULL,
  `GST` varchar(100) NOT NULL,
  `User_id` int(11) NOT NULL,
  `Vendor_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products_product`
--

INSERT INTO `products_product` (`id`, `Product`, `Price`, `GST`, `User_id`, `Vendor_id`) VALUES
(30, '6MM Aggregates', '130', '5%', 1, 1),
(31, '6MM Aggregates', '110', '5%', 1, 6),
(32, '6MM Aggregates', '150', '5%', 1, 7),
(33, '6MM Aggregates', '105', '5%', 1, 8),
(34, '12MM AGGREGATES', '210', '5%', 1, 11),
(35, '12MM AGGREGATES', '205', '5%', 1, 12),
(36, '12MM AGGREGATES', '240', '5%', 1, 13),
(37, '12MM AGGREGATES', '250', '5%', 1, 14),
(38, '20MM AGGREGATES', '305', '5%', 1, 15),
(39, '20MM AGGREGATES', '310', '5%', 1, 16),
(40, '20MM AGGREGATES', '362', '5%', 1, 16),
(41, '20MM AGGREGATES', '380', '5%', 1, 17),
(42, '25MM AGGREGATES', '330', '5%', 1, 18),
(43, '25MM AGGREGATES', '320', '5%', 1, 19),
(44, '25MM AGGREGATES', '400', '5%', 1, 23),
(45, '25MM AGGREGATES', '400', '5%', 1, 51),
(46, '40MM AGGREGATES', '450', '5%', 1, 51),
(47, '40MM AGGREGATES', '500', '5%', 1, 18),
(48, '40MM AGGREGATES', '510', '5%', 1, 9),
(49, '40MM AGGREGATES', '530', '5%', 1, 51),
(50, '40MM AGGREGATES', '550', '5%', 1, 19),
(75, 'QUARY DUST', '200', '5%', 1, 6),
(76, 'QUARY DUST', '150', '5%', 1, 20),
(77, 'QUARY DUST', '160', '5%', 1, 22),
(78, 'QUARY DUST', '170', '5%', 1, 4),
(95, 'FINE DUST', '300', '5%', 1, 6),
(96, 'FINE DUST', '332', '5%', 1, 18),
(97, 'FINE DUST', '350', '5%', 1, 51),
(98, 'FINE DUST', '360', '5%', 1, 20),
(99, 'WATER WASHED  M SAND COARSE', '550', '5%', 1, 10),
(100, 'WATER WASHED  M SAND COARSE', '500', '5%', 1, 51),
(101, 'WATER WASHED  M SAND COARSE', '500', '5%', 1, 50),
(102, 'WATER WASHED  M SAND COARSE', '510', '5%', 1, 47),
(103, 'WATER WASHED PLASTERING SAND', '600', '5%', 1, 5),
(104, 'WATER WASHED PLASTERING SAND', '590', '5%', 1, 50),
(105, 'WATER WASHED PLASTERING SAND', '510', '5%', 1, 48),
(106, 'WATER WASHED PLASTERING SAND', '650', '5%', 1, 9),
(269, 'RIVER SAND COARSE', '800', '5%', 1, 4),
(270, 'RIVER SAND COARSE', '750', '5%', 1, 22),
(271, 'RIVER SAND COARSE', '700', '5%', 1, 21),
(272, 'RIVER SAND COARSE', '820', '5%', 1, 20),
(273, 'RIVER SAND NICE', '450', '5%', 1, 8),
(274, 'RIVER SAND NICE', '400', '5%', 1, 12),
(275, 'RIVER SAND NICE', '500', '5%', 1, 18),
(276, 'RIVER SAND NICE', '600', '5%', 1, 49),
(277, 'RED BRICKS', '700', '5%', 1, 32),
(278, 'RED BRICKS', '550', '5%', 1, 31),
(279, 'RED BRICKS', '600', '5%', 1, 15),
(280, 'RED BRICKS', '650', '5%', 1, 12),
(281, 'FLY ASH BRICKS', '450', '5%', 1, 12),
(282, 'FLY ASH BRICKS', '550', '5%', 1, 38),
(283, 'FLY ASH BRICKS', '700', '5%', 1, 46),
(284, 'SOLID BLOCKS 4\" ( 200*200*100 )', '200', '18%', 1, 21),
(285, 'SOLID BLOCKS 4\" ( 200*200*100 )', '150', '18%', 1, 51),
(286, 'SOLID BLOCKS 4\" ( 200*200*100 )', '110', '18%', 1, 17),
(287, 'SOLID BLOCKS 6\" ( 200*200*150 )', '200', '18%', 1, 5),
(288, 'SOLID BLOCKS 6\" ( 200*200*150 )', '210', '18%', 1, 12),
(289, 'SOLID BLOCKS 6\" ( 200*200*150 )', '196', '18%', 1, 21),
(290, 'SOLID BLOCKS 8\" ( 200*200*200 )', '100', '18%', 1, 16),
(291, 'SOLID BLOCKS 8\" ( 200*200*200 )', '95', '18%', 1, 21),
(292, 'SOLID BLOCKS 8\" ( 200*200*200 )', '80', '5%', 1, 50),
(293, 'AAC BLOCKS 4\" ( 600*200*100 )', '150', '5%', 1, 5),
(294, 'AAC BLOCKS 4\" ( 600*200*100 )', '100', '5%', 1, 7),
(295, 'AAC BLOCKS 4\" ( 600*200*100 )', '90', '5%', 1, 24),
(296, 'AAC BLOCKS 6\" ( 600*200*150 )', '200', '5%', 1, 4),
(297, 'AAC BLOCKS 6\" ( 600*200*150 )', '160', '5%', 1, 5),
(298, 'AAC BLOCKS 6\" ( 600*200*150 )', '160', '5%', 1, 12),
(299, 'AAC BLOCKS 8\" ( 600*200*200 )', '500', '5%', 1, 11),
(300, 'AAC BLOCKS 8\" ( 600*200*200 )', '450', '5%', 1, 20),
(301, 'AAC BLOCKS 8\" ( 600*200*200 )', '490', '5%', 1, 17),
(302, 'AAC BLOCKS 9\" ( 600*200*230 )', '600', '5%', 1, 14),
(303, 'AAC BLOCKS 9\" ( 600*200*230 )', '500', '5%', 1, 15),
(304, 'AAC BLOCKS 9\" ( 600*200*230 )', '550', '5%', 1, 12),
(319, 'HILL EARTH', '300', '5%', 1, 49),
(320, 'HILL EARTH', '555', '5%', 1, 17),
(321, 'HILL EARTH', '500', '5%', 1, 18),
(322, 'HILL EARTH', '545', '5%', 1, 50),
(323, 'FILLING EARTH', '130', '5%', 1, 20),
(324, 'FILLING EARTH', '120', '5%', 1, 23),
(325, 'FILLING EARTH', '100', '5%', 1, 51),
(326, 'GRAVEL', '100', '5%', 1, 45),
(327, 'GRAVEL', '90', '5%', 1, 44),
(328, 'GRAVEL', '80', '5%', 1, 21),
(329, 'GRAVEL', '89', '5%', 1, 23),
(330, 'WED ASH', '50', '5%', 1, 5),
(331, 'WED ASH', '45', '5%', 1, 6),
(332, 'WED ASH', '40', '5%', 1, 7),
(333, 'WED ASH', '35', '5%', 1, 8),
(334, 'RED SOIL', '99', '5%', 1, 9),
(335, 'RED SOIL', '98', '5%', 1, 10),
(336, 'RED SOIL', '97', '5%', 1, 10),
(337, 'RIVER PEBBLE STONE', '75', '5%', 1, 12),
(338, 'IVER PEBBLE STONE', '76', '5%', 1, 28),
(339, 'IVER PEBBLE STONE', '70', '5%', 1, 24),
(340, 'SB', '550', '5%', 1, 50),
(341, 'SB', '500', '5%', 1, 49),
(342, 'SB', '460', '5%', 1, 17),
(343, 'GSB', '400', '5%', 1, 4),
(344, 'WET MIX ( WMM )', '55', '5%', 1, 22),
(345, 'BOULDERS', '100', '5%', 1, 26),
(346, 'BOULDERS', '90', '5%', 1, 44),
(347, 'BOULDERS', '80', '5%', 1, 50),
(348, 'BOULDERS', '60', '5%', 1, 49),
(349, 'RR TONE', '700', '5%', 1, 8),
(350, 'RR TONE', '705', '5%', 1, 9),
(351, 'RR TONE', '321', '5%', 1, 6),
(352, 'STEELS', '222', '18%', 1, 5),
(353, 'STEELS', '230', '18%', 1, 15),
(354, 'STEELS', '600', '5%', 1, 21),
(355, 'STEELS', '500', '18%', 1, 7),
(356, 'ARS 8MM', '200', '5%', 1, 4),
(357, 'ARS 8MM', '180', '18%', 1, 6),
(358, 'ARS 8MM', '100', '18%', 1, 7),
(359, 'JSW', '300', '28%', 1, 50),
(360, 'JSW', '300', '28%', 1, 14),
(361, 'JSW', '350', '28%', 1, 20),
(362, 'ULTRATECH', '100', '28%', 1, 13),
(363, 'ULTRATECH', '90', '28%', 1, 11),
(364, 'sajdasd asd asd', '54', '5%', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `vendors_vendor`
--

CREATE TABLE `vendors_vendor` (
  `id` bigint(20) NOT NULL,
  `Vendor_Type` varchar(1) DEFAULT NULL,
  `Vendor_Name` varchar(100) DEFAULT NULL,
  `Company_Name` varchar(100) DEFAULT NULL,
  `Phone` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `City` varchar(100) DEFAULT NULL,
  `State` varchar(100) DEFAULT NULL,
  `Zip` varchar(100) DEFAULT NULL,
  `Country` varchar(100) DEFAULT NULL,
  `Origin_Of_The_Material` varchar(100) DEFAULT NULL,
  `No_Of_Trucks` varchar(100) DEFAULT NULL,
  `Material_Supplying` varchar(100) DEFAULT NULL,
  `published` datetime(6) NOT NULL,
  `User_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vendors_vendor`
--

INSERT INTO `vendors_vendor` (`id`, `Vendor_Type`, `Vendor_Name`, `Company_Name`, `Phone`, `Email`, `Address`, `City`, `State`, `Zip`, `Country`, `Origin_Of_The_Material`, `No_Of_Trucks`, `Material_Supplying`, `published`, `User_id`) VALUES
(1, '0', 'Thirumala', 'Thirumala Traders', '8825847261', 'thirumala@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(2, '0', 'A. Sathees', 'A. Sathees Kumar', '883232435', 'sathees@gmail.com', 'kalaingar str', 'chennai', 'TN', '113', 'India', 'tambaram', '1', 'tambaram', '2021-11-24 08:01:51.000000', 1),
(3, '0', 'TAJ', 'TAJ Transport', '8825847261', 'taj@gmail.com', 'taramani', 'chennai', 'TN', '113', 'India', 'Taj', '1', 'material supplying', '2021-11-24 08:06:00.000000', 1),
(4, '0', 'Kesavan', 'Kesavan', '8825847261', 'Kesavan@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(5, '0', 'S.S.Transport', 'S.S.Transport', '8825847261', 'S.S.Transport@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(6, '0', 'Srikar enterprises', 'Srikar enterprises', '8825847261', 'srikarenterprises@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(7, '0', 'Sri venkatachalapathy', 'Sri venkatachalapathy', '8825847261', 'srivenkatachalapathy@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(8, '0', 'Suresh g', 'Suresh g', '8825847261', 'sureshg@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(9, '0', 'SStp earth mover', 'SStp earth mover', '8825847261', 'stpearthmover@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(10, '0', 'A.S.M transport', 'A.S.M transport', '8825847261', 'asmtransport@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(11, '0', 'Kuppusamy', 'Kuppusamy', '8825847261', 'Kuppusamy@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(12, '0', 'Sai wire cut brik', 'Sai wire cut brik', '8825847261', 'saiwirecutbrik@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(13, '0', 'Light house', 'Light house', '8825847261', 'lighthouse@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(14, '0', 'agr rock', 'agr rock', '8825847261', 'agrrock@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(15, '0', 'han agency', 'han agency', '8825847261', 'hanagency@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(16, '0', 'cchennan', 'cchennan', '8825847261', 'cchennan@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(17, '0', 'Chandra babu', 'Chandra babu', '8825847261', 'chandrababu@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(18, '0', 'D.Vedhavalli', 'D.Vedhavalli', '8825847261', 'dvedhavalli@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(19, '0', 'Mam enterprises', 'Mam enterprises', '8825847261', 'mamenterprises@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(20, '0', 'Baby p', 'Baby p', '8825847261', 'babyp@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(21, '0', 'Santhosh agency', 'Santhosh agency', '8825847261', 'santhoshagency@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(22, '0', 's.palani', 's.palani', '8825847261', 's.palani@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(23, '0', 'Goodwin Fly Ash', 'goodwin fly ash', '8825847261', 'goodwinflyash@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(24, '0', 'b.arun raj', 'b.arun raj', '8825847261', 'b.arunraj@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(25, '0', 'E.Teekaraman', 'E.Teekaraman', '8825847261', 'eteekaraman@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(26, '0', 'R.Baskaran', 'R.Baskaran', '8825847261', 'r.baskaran@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(27, '0', 'Rs concrete block', 'Rs concrete block', '8825847261', 'rsconcreteblock@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(28, '0', 'Asir pon doss', 'Asir pon doss', '8825847261', 'asirpondoss@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(29, '0', 'Sam enterprises', 'Sam enterprises', '8825847261', 'samenterprises@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(30, '0', 'Surahs pakiri', 'Surahs pakiri', '8825847261', 'surahspakiri@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(31, '0', 'Skvs', 'Skvs', '8825847261', 'skvs@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(32, '0', 'murugan', 'murugan', '8825847261', 'murugan@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(33, '0', 'Deejay minarals', 'Deejay minarals', '8825847261', 'deejayminarals@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(34, '0', 'Rr fal g bricks', 'Rr fal g bricks', '8825847261', 'rrfalgbricks@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(35, '0', 'Vedhaprakash', 'Vedhaprakash', '8825847261', 'vedhaprakash@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(36, '0', 'S.K.Transport', 'S.K.Transport', '8825847261', 'sktransport@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(37, '0', 'A.Alphones', 'A.Alphones', '8825847261', 'aalphones@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(38, '0', 'S.Vetrivel', 'S.Vetrivel', '8825847261', 'svetrivel@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(39, '0', 'S.V.Gopalakrishnan', 'S.V.Gopalakrishnan', '8825847261', 'svgopalakrishnan@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(40, '0', 'Grk', 'Grk', '8825847261', 'grk@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(41, '0', 'Raja d', 'Raja d', '8825847261', 'rajad@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(42, '0', 'G.Augustin', 'G.Augustin', '8825847261', 'gaugustin@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(43, '0', 'Nandha kumar', 'Nandha kumar', '8825847261', 'nandhakumar@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(44, '0', 'Santhanamuthu', 'Santhanamuthu', '8825847261', 'santhanamuthu@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(45, '0', 'Ramu m', 'Ramu m', '8825847261', 'ramum@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(46, '0', 'C.Prashanth', 'C.Prashanth', '8825847261', 'cprashanth@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(47, '0', 'V.Shrinivasan', 'V.Shrinivasan', '8825847261', 'vshrinivasan@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(48, '0', 'K.S.Aswin kumar', 'K.S.Aswin kumar', '8825847261', 'ksaswinkumar@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(49, '0', 'Vetrivelavan traders', 'Vetrivelavan traders', '8825847261', 'vetrivelavantraders@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(50, '0', 'Sasindiran agency', 'Sasindiran agency', '8825847261', 'sasindiranagency@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1),
(51, '0', 'Raghuventhiran', 'Raghuventhiran', '8825847261', 'raghuventhiran@gmail.com', 'Kalaingar street', 'Chennai', 'TN', '113', 'India', 'origin', '1', 'driver', '2021-11-24 07:55:29.000000', 1);

-- --------------------------------------------------------

--
-- Table structure for table `vendors_vendorcertificate`
--

CREATE TABLE `vendors_vendorcertificate` (
  `id` bigint(20) NOT NULL,
  `Vendor_Certificate_Name` varchar(100) DEFAULT NULL,
  `Vendor_Certificate_Scan_Copy` varchar(100) DEFAULT NULL,
  `Vendor_Company_Name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vendors_vendorcertificate`
--

INSERT INTO `vendors_vendorcertificate` (`id`, `Vendor_Certificate_Name`, `Vendor_Certificate_Scan_Copy`, `Vendor_Company_Name`) VALUES
(1, 'GST Certificate', 'uploads/2021/11/24/registration-certificate-1_1.png', NULL),
(2, 'Taj GST', 'uploads/2021/11/24/registration-certificate-1_1_Ra6c6oH.png', NULL),
(5, 'gst certificates', 'uploads/2021/11/25/registration-certificate-1.png', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `vendors_vendorgst`
--

CREATE TABLE `vendors_vendorgst` (
  `id` bigint(20) NOT NULL,
  `Vendor_Company_Name` varchar(100) DEFAULT NULL,
  `Vendor_GST_Type` varchar(1) DEFAULT NULL,
  `Vendor_GST_No` varchar(50) DEFAULT NULL,
  `Vendor_PAN_No` varchar(50) DEFAULT NULL,
  `Vendor_Tin` varchar(50) DEFAULT NULL,
  `Vendor_Phone_Number` varchar(50) DEFAULT NULL,
  `Vendor_Email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vendors_vendorgst`
--

INSERT INTO `vendors_vendorgst` (`id`, `Vendor_Company_Name`, `Vendor_GST_Type`, `Vendor_GST_No`, `Vendor_PAN_No`, `Vendor_Tin`, `Vendor_Phone_Number`, `Vendor_Email`) VALUES
(1, 'Thirumala Traders', '0', '782344874237878', '234324324', '12323', '893782778', 'thirumala@gmail.com'),
(2, 'A. Sathees', '0', '893472394887923', '342324234', '32421323', '984398587943', 'tester@gmail.com'),
(3, 'Taj', '0', '78932987478932', '3278483', '123124332', '9435987437', 'taj@gmail.com'),
(4, 'vendorscompanyname', '0', '213123231', '7832478234', '234234324', '2348723486', 'vendorgst@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `vendors_vendorgstbankaccount`
--

CREATE TABLE `vendors_vendorgstbankaccount` (
  `id` bigint(20) NOT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  `State` varchar(50) DEFAULT NULL,
  `Zip` varchar(50) DEFAULT NULL,
  `Vendor_Company_Name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vendors_vendorgstbankaccount`
--

INSERT INTO `vendors_vendorgstbankaccount` (`id`, `Address`, `City`, `State`, `Zip`, `Vendor_Company_Name`) VALUES
(1, 'velachery', 'chennai', 'tamilnadu', '600113', NULL),
(2, 'tnagar', 'chennai', 'tamilnadu', '600113', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `vendors_vendorgst_vendor_bank_account`
--

CREATE TABLE `vendors_vendorgst_vendor_bank_account` (
  `id` bigint(20) NOT NULL,
  `vendorgst_id` bigint(20) NOT NULL,
  `vendorgstbankaccount_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vendors_vendorgst_vendor_bank_account`
--

INSERT INTO `vendors_vendorgst_vendor_bank_account` (`id`, `vendorgst_id`, `vendorgstbankaccount_id`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 1),
(4, 4, 1),
(5, 4, 2);

-- --------------------------------------------------------

--
-- Table structure for table `vendors_vendorgst_vendor_certificate`
--

CREATE TABLE `vendors_vendorgst_vendor_certificate` (
  `id` bigint(20) NOT NULL,
  `vendorgst_id` bigint(20) NOT NULL,
  `vendorcertificate_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vendors_vendorgst_vendor_certificate`
--

INSERT INTO `vendors_vendorgst_vendor_certificate` (`id`, `vendorgst_id`, `vendorcertificate_id`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 2),
(4, 4, 1),
(5, 4, 2),
(6, 4, 5);

-- --------------------------------------------------------

--
-- Table structure for table `vendors_vendorstaffdetail`
--

CREATE TABLE `vendors_vendorstaffdetail` (
  `id` bigint(20) NOT NULL,
  `Vendor_Company_Name` varchar(50) DEFAULT NULL,
  `Account_Name` varchar(50) DEFAULT NULL,
  `Mobile` varchar(50) DEFAULT NULL,
  `Mail_Id` varchar(50) DEFAULT NULL,
  `Address` longtext DEFAULT NULL,
  `Payment_Name` varchar(50) DEFAULT NULL,
  `Payment_Mobile` varchar(50) DEFAULT NULL,
  `Payment_Mail_Id` varchar(50) DEFAULT NULL,
  `Payment_Address` longtext DEFAULT NULL,
  `Driver_Details` longtext DEFAULT NULL,
  `Published` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vendors_vendorstaffdetail`
--

INSERT INTO `vendors_vendorstaffdetail` (`id`, `Vendor_Company_Name`, `Account_Name`, `Mobile`, `Mail_Id`, `Address`, `Payment_Name`, `Payment_Mobile`, `Payment_Mail_Id`, `Payment_Address`, `Driver_Details`, `Published`) VALUES
(1, 'staff user', 'staff account name', '9783248682', 'staff@gmail.com', 'staff address', 'staff payment name', '9783248682', 'staff@gmail.com', 'Velacher, taramani, chennai', 'tnagar, taramani, chennai', '2021-11-24 08:00:39.081022'),
(2, 'vendorcompanyname', 'surendar', '3498392498', 'ven@gmail.com', '2, kalaingar street, mgr nagar, taramani, che-113', 'payment name', '8932498234', 'pay@gmail.com', '2, kalaingar street, mgr nagar, taramani, che-113', '2, kalaingar street, mgr nagar, taramani, che-113', '2021-11-25 09:46:41.175879');

-- --------------------------------------------------------

--
-- Table structure for table `vendors_vendor_agency`
--

CREATE TABLE `vendors_vendor_agency` (
  `id` bigint(20) NOT NULL,
  `vendor_id` bigint(20) NOT NULL,
  `agency_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vendors_vendor_agency`
--

INSERT INTO `vendors_vendor_agency` (`id`, `vendor_id`, `agency_id`) VALUES
(1, 1, 2),
(2, 1, 3),
(3, 1, 6),
(4, 2, 2),
(5, 2, 3),
(6, 2, 6),
(7, 3, 2),
(8, 3, 3),
(9, 3, 6);

-- --------------------------------------------------------

--
-- Table structure for table `vendors_vendor_gst_no`
--

CREATE TABLE `vendors_vendor_gst_no` (
  `id` bigint(20) NOT NULL,
  `vendor_id` bigint(20) NOT NULL,
  `vendorgst_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vendors_vendor_gst_no`
--

INSERT INTO `vendors_vendor_gst_no` (`id`, `vendor_id`, `vendorgst_id`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3);

-- --------------------------------------------------------

--
-- Table structure for table `vendors_vendor_vendor_staff_detail`
--

CREATE TABLE `vendors_vendor_vendor_staff_detail` (
  `id` bigint(20) NOT NULL,
  `vendor_id` bigint(20) NOT NULL,
  `vendorstaffdetail_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vendors_vendor_vendor_staff_detail`
--

INSERT INTO `vendors_vendor_vendor_staff_detail` (`id`, `vendor_id`, `vendorstaffdetail_id`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `agency_agency`
--
ALTER TABLE `agency_agency`
  ADD PRIMARY KEY (`id`),
  ADD KEY `agency_agency_User_id_a7a6aae7_fk_auth_user_id` (`User_id`);

--
-- Indexes for table `agency_agencybankaccount`
--
ALTER TABLE `agency_agencybankaccount`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `agency_agencycertificate`
--
ALTER TABLE `agency_agencycertificate`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `agency_agency_bank_account`
--
ALTER TABLE `agency_agency_bank_account`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `agency_agency_Bank_Accou_agency_id_agencybankacco_c4317ebb_uniq` (`agency_id`,`agencybankaccount_id`),
  ADD KEY `agency_agency_Bank_A_agencybankaccount_id_d34d84e5_fk_agency_ag` (`agencybankaccount_id`);

--
-- Indexes for table `agency_agency_certificates`
--
ALTER TABLE `agency_agency_certificates`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `agency_agency_Certificat_agency_id_agencycertific_1cff6ff3_uniq` (`agency_id`,`agencycertificate_id`),
  ADD KEY `agency_agency_Certif_agencycertificate_id_1dd1977b_fk_agency_ag` (`agencycertificate_id`);

--
-- Indexes for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `customers_customer`
--
ALTER TABLE `customers_customer`
  ADD PRIMARY KEY (`id`),
  ADD KEY `customers_customer_GST_No_id_1737d733_fk_customers` (`GST_No_id`),
  ADD KEY `customers_customer_User_id_b3a7d399_fk_auth_user_id` (`User_id`);

--
-- Indexes for table `customers_customerbankaccounts`
--
ALTER TABLE `customers_customerbankaccounts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customers_customerdeliveryaddress`
--
ALTER TABLE `customers_customerdeliveryaddress`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customers_customergstbillingaddress`
--
ALTER TABLE `customers_customergstbillingaddress`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customers_customerstaff`
--
ALTER TABLE `customers_customerstaff`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customers_customer_bank_account`
--
ALTER TABLE `customers_customer_bank_account`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `customers_customer_Bank__customer_id_customerbank_9ff29d78_uniq` (`customer_id`,`customerbankaccounts_id`),
  ADD KEY `customers_customer_B_customerbankaccounts_0b5f39fe_fk_customers` (`customerbankaccounts_id`);

--
-- Indexes for table `customers_customer_delivery_address`
--
ALTER TABLE `customers_customer_delivery_address`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `customers_customer_Deliv_customer_id_customerdeli_259b0b80_uniq` (`customer_id`,`customerdeliveryaddress_id`),
  ADD KEY `customers_customer_D_customerdeliveryaddr_f86f60ae_fk_customers` (`customerdeliveryaddress_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `orders_materialorder`
--
ALTER TABLE `orders_materialorder`
  ADD PRIMARY KEY (`id`),
  ADD KEY `orders_materialorder_Product_Name_id_97396c3b_fk_products_` (`Product_Name_id`),
  ADD KEY `orders_materialorder_User_id_888e35c5_fk_auth_user_id` (`User_id`),
  ADD KEY `orders_materialorder_Vendor_id_b5163fc9_fk_vendors_vendor_id` (`Vendor_id`);

--
-- Indexes for table `orders_order`
--
ALTER TABLE `orders_order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `orders_order_Agency_id_a1cbd161_fk_agency_agency_id` (`Agency_id`),
  ADD KEY `orders_order_PO_Number_id_94d34fe0_fk_orders_ponumber_id` (`PO_Number_id`),
  ADD KEY `orders_order_Sales_Company_id_286caa14_fk_customers_customer_id` (`Sales_Company_id`),
  ADD KEY `orders_order_User_id_3c8bfcc4_fk_auth_user_id` (`User_id`);

--
-- Indexes for table `orders_order_materials`
--
ALTER TABLE `orders_order_materials`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `orders_order_Materials_order_id_materialorder_id_4e122da8_uniq` (`order_id`,`materialorder_id`),
  ADD KEY `orders_order_Materia_materialorder_id_75974efc_fk_orders_ma` (`materialorder_id`);

--
-- Indexes for table `orders_order_sales_delivery_address`
--
ALTER TABLE `orders_order_sales_delivery_address`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `orders_order_Sales_Deliv_order_id_customerdeliver_a6d72492_uniq` (`order_id`,`customerdeliveryaddress_id`),
  ADD KEY `orders_order_Sales_D_customerdeliveryaddr_ccbd9f43_fk_customers` (`customerdeliveryaddress_id`);

--
-- Indexes for table `orders_ponumber`
--
ALTER TABLE `orders_ponumber`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `products_product`
--
ALTER TABLE `products_product`
  ADD PRIMARY KEY (`id`),
  ADD KEY `products_product_User_id_79bbf320_fk_auth_user_id` (`User_id`),
  ADD KEY `products_product_Vendor_id_94985c94_fk_vendors_vendor_id` (`Vendor_id`);

--
-- Indexes for table `vendors_vendor`
--
ALTER TABLE `vendors_vendor`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vendors_vendor_User_id_625dc071_fk_auth_user_id` (`User_id`);

--
-- Indexes for table `vendors_vendorcertificate`
--
ALTER TABLE `vendors_vendorcertificate`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vendors_vendorgst`
--
ALTER TABLE `vendors_vendorgst`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vendors_vendorgstbankaccount`
--
ALTER TABLE `vendors_vendorgstbankaccount`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vendors_vendorgst_vendor_bank_account`
--
ALTER TABLE `vendors_vendorgst_vendor_bank_account`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `vendors_vendorgst_Vendor_vendorgst_id_vendorgstba_735c0123_uniq` (`vendorgst_id`,`vendorgstbankaccount_id`),
  ADD KEY `vendors_vendorgst_Ve_vendorgstbankaccount_ee151881_fk_vendors_v` (`vendorgstbankaccount_id`);

--
-- Indexes for table `vendors_vendorgst_vendor_certificate`
--
ALTER TABLE `vendors_vendorgst_vendor_certificate`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `vendors_vendorgst_Vendor_vendorgst_id_vendorcerti_f0387992_uniq` (`vendorgst_id`,`vendorcertificate_id`),
  ADD KEY `vendors_vendorgst_Ve_vendorcertificate_id_5e5f5f2c_fk_vendors_v` (`vendorcertificate_id`);

--
-- Indexes for table `vendors_vendorstaffdetail`
--
ALTER TABLE `vendors_vendorstaffdetail`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vendors_vendor_agency`
--
ALTER TABLE `vendors_vendor_agency`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `vendors_vendor_Agency_vendor_id_agency_id_fa368014_uniq` (`vendor_id`,`agency_id`),
  ADD KEY `vendors_vendor_Agency_agency_id_e806e191_fk_agency_agency_id` (`agency_id`);

--
-- Indexes for table `vendors_vendor_gst_no`
--
ALTER TABLE `vendors_vendor_gst_no`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `vendors_vendor_GST_No_vendor_id_vendorgst_id_010ea366_uniq` (`vendor_id`,`vendorgst_id`),
  ADD KEY `vendors_vendor_GST_N_vendorgst_id_0a707f08_fk_vendors_v` (`vendorgst_id`);

--
-- Indexes for table `vendors_vendor_vendor_staff_detail`
--
ALTER TABLE `vendors_vendor_vendor_staff_detail`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `vendors_vendor_Vendor_St_vendor_id_vendorstaffdet_c7fcea96_uniq` (`vendor_id`,`vendorstaffdetail_id`),
  ADD KEY `vendors_vendor_Vendo_vendorstaffdetail_id_eb7a56ea_fk_vendors_v` (`vendorstaffdetail_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `agency_agency`
--
ALTER TABLE `agency_agency`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `agency_agencybankaccount`
--
ALTER TABLE `agency_agencybankaccount`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `agency_agencycertificate`
--
ALTER TABLE `agency_agencycertificate`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `agency_agency_bank_account`
--
ALTER TABLE `agency_agency_bank_account`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `agency_agency_certificates`
--
ALTER TABLE `agency_agency_certificates`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customers_customer`
--
ALTER TABLE `customers_customer`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customers_customerbankaccounts`
--
ALTER TABLE `customers_customerbankaccounts`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customers_customerdeliveryaddress`
--
ALTER TABLE `customers_customerdeliveryaddress`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customers_customergstbillingaddress`
--
ALTER TABLE `customers_customergstbillingaddress`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customers_customerstaff`
--
ALTER TABLE `customers_customerstaff`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customers_customer_bank_account`
--
ALTER TABLE `customers_customer_bank_account`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customers_customer_delivery_address`
--
ALTER TABLE `customers_customer_delivery_address`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `orders_materialorder`
--
ALTER TABLE `orders_materialorder`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `orders_order`
--
ALTER TABLE `orders_order`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `orders_order_materials`
--
ALTER TABLE `orders_order_materials`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `orders_order_sales_delivery_address`
--
ALTER TABLE `orders_order_sales_delivery_address`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `orders_ponumber`
--
ALTER TABLE `orders_ponumber`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `products_product`
--
ALTER TABLE `products_product`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=365;

--
-- AUTO_INCREMENT for table `vendors_vendor`
--
ALTER TABLE `vendors_vendor`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `vendors_vendorcertificate`
--
ALTER TABLE `vendors_vendorcertificate`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `vendors_vendorgst`
--
ALTER TABLE `vendors_vendorgst`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `vendors_vendorgstbankaccount`
--
ALTER TABLE `vendors_vendorgstbankaccount`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `vendors_vendorgst_vendor_bank_account`
--
ALTER TABLE `vendors_vendorgst_vendor_bank_account`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `vendors_vendorgst_vendor_certificate`
--
ALTER TABLE `vendors_vendorgst_vendor_certificate`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `vendors_vendorstaffdetail`
--
ALTER TABLE `vendors_vendorstaffdetail`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `vendors_vendor_agency`
--
ALTER TABLE `vendors_vendor_agency`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `vendors_vendor_gst_no`
--
ALTER TABLE `vendors_vendor_gst_no`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `vendors_vendor_vendor_staff_detail`
--
ALTER TABLE `vendors_vendor_vendor_staff_detail`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `agency_agency`
--
ALTER TABLE `agency_agency`
  ADD CONSTRAINT `agency_agency_User_id_a7a6aae7_fk_auth_user_id` FOREIGN KEY (`User_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `agency_agency_bank_account`
--
ALTER TABLE `agency_agency_bank_account`
  ADD CONSTRAINT `agency_agency_Bank_A_agency_id_292e99c1_fk_agency_ag` FOREIGN KEY (`agency_id`) REFERENCES `agency_agency` (`id`),
  ADD CONSTRAINT `agency_agency_Bank_A_agencybankaccount_id_d34d84e5_fk_agency_ag` FOREIGN KEY (`agencybankaccount_id`) REFERENCES `agency_agencybankaccount` (`id`);

--
-- Constraints for table `agency_agency_certificates`
--
ALTER TABLE `agency_agency_certificates`
  ADD CONSTRAINT `agency_agency_Certif_agency_id_d68dd401_fk_agency_ag` FOREIGN KEY (`agency_id`) REFERENCES `agency_agency` (`id`),
  ADD CONSTRAINT `agency_agency_Certif_agencycertificate_id_1dd1977b_fk_agency_ag` FOREIGN KEY (`agencycertificate_id`) REFERENCES `agency_agencycertificate` (`id`);

--
-- Constraints for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `customers_customer`
--
ALTER TABLE `customers_customer`
  ADD CONSTRAINT `customers_customer_GST_No_id_1737d733_fk_customers` FOREIGN KEY (`GST_No_id`) REFERENCES `customers_customergstbillingaddress` (`id`),
  ADD CONSTRAINT `customers_customer_User_id_b3a7d399_fk_auth_user_id` FOREIGN KEY (`User_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `customers_customer_bank_account`
--
ALTER TABLE `customers_customer_bank_account`
  ADD CONSTRAINT `customers_customer_B_customer_id_e28b0624_fk_customers` FOREIGN KEY (`customer_id`) REFERENCES `customers_customer` (`id`),
  ADD CONSTRAINT `customers_customer_B_customerbankaccounts_0b5f39fe_fk_customers` FOREIGN KEY (`customerbankaccounts_id`) REFERENCES `customers_customerbankaccounts` (`id`);

--
-- Constraints for table `customers_customer_delivery_address`
--
ALTER TABLE `customers_customer_delivery_address`
  ADD CONSTRAINT `customers_customer_D_customer_id_560f10d3_fk_customers` FOREIGN KEY (`customer_id`) REFERENCES `customers_customer` (`id`),
  ADD CONSTRAINT `customers_customer_D_customerdeliveryaddr_f86f60ae_fk_customers` FOREIGN KEY (`customerdeliveryaddress_id`) REFERENCES `customers_customerdeliveryaddress` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `orders_materialorder`
--
ALTER TABLE `orders_materialorder`
  ADD CONSTRAINT `orders_materialorder_Product_Name_id_97396c3b_fk_products_` FOREIGN KEY (`Product_Name_id`) REFERENCES `products_product` (`id`),
  ADD CONSTRAINT `orders_materialorder_User_id_888e35c5_fk_auth_user_id` FOREIGN KEY (`User_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `orders_materialorder_Vendor_id_b5163fc9_fk_vendors_vendor_id` FOREIGN KEY (`Vendor_id`) REFERENCES `vendors_vendor` (`id`);

--
-- Constraints for table `orders_order`
--
ALTER TABLE `orders_order`
  ADD CONSTRAINT `orders_order_Agency_id_a1cbd161_fk_agency_agency_id` FOREIGN KEY (`Agency_id`) REFERENCES `agency_agency` (`id`),
  ADD CONSTRAINT `orders_order_PO_Number_id_94d34fe0_fk_orders_ponumber_id` FOREIGN KEY (`PO_Number_id`) REFERENCES `orders_ponumber` (`id`),
  ADD CONSTRAINT `orders_order_Sales_Company_id_286caa14_fk_customers_customer_id` FOREIGN KEY (`Sales_Company_id`) REFERENCES `customers_customer` (`id`),
  ADD CONSTRAINT `orders_order_User_id_3c8bfcc4_fk_auth_user_id` FOREIGN KEY (`User_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `orders_order_materials`
--
ALTER TABLE `orders_order_materials`
  ADD CONSTRAINT `orders_order_Materia_materialorder_id_75974efc_fk_orders_ma` FOREIGN KEY (`materialorder_id`) REFERENCES `orders_materialorder` (`id`),
  ADD CONSTRAINT `orders_order_Materials_order_id_6bca35e0_fk_orders_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders_order` (`id`);

--
-- Constraints for table `orders_order_sales_delivery_address`
--
ALTER TABLE `orders_order_sales_delivery_address`
  ADD CONSTRAINT `orders_order_Sales_D_customerdeliveryaddr_ccbd9f43_fk_customers` FOREIGN KEY (`customerdeliveryaddress_id`) REFERENCES `customers_customerdeliveryaddress` (`id`),
  ADD CONSTRAINT `orders_order_Sales_D_order_id_1344ca9d_fk_orders_or` FOREIGN KEY (`order_id`) REFERENCES `orders_order` (`id`);

--
-- Constraints for table `products_product`
--
ALTER TABLE `products_product`
  ADD CONSTRAINT `products_product_User_id_79bbf320_fk_auth_user_id` FOREIGN KEY (`User_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `products_product_Vendor_id_94985c94_fk_vendors_vendor_id` FOREIGN KEY (`Vendor_id`) REFERENCES `vendors_vendor` (`id`);

--
-- Constraints for table `vendors_vendor`
--
ALTER TABLE `vendors_vendor`
  ADD CONSTRAINT `vendors_vendor_User_id_625dc071_fk_auth_user_id` FOREIGN KEY (`User_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `vendors_vendorgst_vendor_bank_account`
--
ALTER TABLE `vendors_vendorgst_vendor_bank_account`
  ADD CONSTRAINT `vendors_vendorgst_Ve_vendorgst_id_9333cdf0_fk_vendors_v` FOREIGN KEY (`vendorgst_id`) REFERENCES `vendors_vendorgst` (`id`),
  ADD CONSTRAINT `vendors_vendorgst_Ve_vendorgstbankaccount_ee151881_fk_vendors_v` FOREIGN KEY (`vendorgstbankaccount_id`) REFERENCES `vendors_vendorgstbankaccount` (`id`);

--
-- Constraints for table `vendors_vendorgst_vendor_certificate`
--
ALTER TABLE `vendors_vendorgst_vendor_certificate`
  ADD CONSTRAINT `vendors_vendorgst_Ve_vendorcertificate_id_5e5f5f2c_fk_vendors_v` FOREIGN KEY (`vendorcertificate_id`) REFERENCES `vendors_vendorcertificate` (`id`),
  ADD CONSTRAINT `vendors_vendorgst_Ve_vendorgst_id_6e63ff9d_fk_vendors_v` FOREIGN KEY (`vendorgst_id`) REFERENCES `vendors_vendorgst` (`id`);

--
-- Constraints for table `vendors_vendor_agency`
--
ALTER TABLE `vendors_vendor_agency`
  ADD CONSTRAINT `vendors_vendor_Agency_agency_id_e806e191_fk_agency_agency_id` FOREIGN KEY (`agency_id`) REFERENCES `agency_agency` (`id`),
  ADD CONSTRAINT `vendors_vendor_Agency_vendor_id_585217e1_fk_vendors_vendor_id` FOREIGN KEY (`vendor_id`) REFERENCES `vendors_vendor` (`id`);

--
-- Constraints for table `vendors_vendor_gst_no`
--
ALTER TABLE `vendors_vendor_gst_no`
  ADD CONSTRAINT `vendors_vendor_GST_N_vendorgst_id_0a707f08_fk_vendors_v` FOREIGN KEY (`vendorgst_id`) REFERENCES `vendors_vendorgst` (`id`),
  ADD CONSTRAINT `vendors_vendor_GST_No_vendor_id_703f6931_fk_vendors_vendor_id` FOREIGN KEY (`vendor_id`) REFERENCES `vendors_vendor` (`id`);

--
-- Constraints for table `vendors_vendor_vendor_staff_detail`
--
ALTER TABLE `vendors_vendor_vendor_staff_detail`
  ADD CONSTRAINT `vendors_vendor_Vendo_vendor_id_ade9efba_fk_vendors_v` FOREIGN KEY (`vendor_id`) REFERENCES `vendors_vendor` (`id`),
  ADD CONSTRAINT `vendors_vendor_Vendo_vendorstaffdetail_id_eb7a56ea_fk_vendors_v` FOREIGN KEY (`vendorstaffdetail_id`) REFERENCES `vendors_vendorstaffdetail` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
