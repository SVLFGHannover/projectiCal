-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Erstellungszeit: 15. Nov 2021 um 17:16
-- Server-Version: 10.4.21-MariaDB
-- PHP-Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `iCal`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Attach`
--

CREATE TABLE `Attach` (
  `ID` int(11) NOT NULL,
  `attachment` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Categories`
--

CREATE TABLE `Categories` (
  `ID` int(11) NOT NULL,
  `category` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Comment`
--

CREATE TABLE `Comment` (
  `ID` int(11) NOT NULL,
  `comment` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Contact`
--

CREATE TABLE `Contact` (
  `ID` int(11) NOT NULL,
  `contact` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Exdate`
--

CREATE TABLE `Exdate` (
  `ID` int(11) NOT NULL,
  `exdate` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Ianaprop`
--

CREATE TABLE `Ianaprop` (
  `ID` int(11) NOT NULL,
  `ianaprop` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `RDate`
--

CREATE TABLE `RDate` (
  `ID` int(11) NOT NULL,
  `rdtparam` varchar(20) NOT NULL,
  `rdtval` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Related`
--

CREATE TABLE `Related` (
  `ID` int(11) NOT NULL,
  `related` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Resources`
--

CREATE TABLE `Resources` (
  `ID` int(11) NOT NULL,
  `resource` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `RRule`
--

CREATE TABLE `RRule` (
  `ID` int(11) NOT NULL,
  `freq` varchar(8) NOT NULL,
  `until` datetime NOT NULL,
  `count` int(11) NOT NULL,
  `interval` int(11) NOT NULL,
  `bysecond` varchar(20) NOT NULL,
  `byminute` varchar(20) NOT NULL,
  `byhour` varchar(20) NOT NULL,
  `byday` varchar(20) NOT NULL,
  `bymonthday` varchar(20) NOT NULL,
  `byyearday` varchar(20) NOT NULL,
  `byweekno` varchar(20) NOT NULL,
  `bymonth` varchar(20) NOT NULL,
  `bysetpos` varchar(20) NOT NULL,
  `wkst` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Rstatus`
--

CREATE TABLE `Rstatus` (
  `ID` int(11) NOT NULL,
  `statcode` varchar(100) NOT NULL,
  `Column1` int(11) NOT NULL,
  `statdesc` varchar(100) NOT NULL,
  `exdata` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `User`
--

CREATE TABLE `User` (
  `ID` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `isattendee` char(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `User`
--

INSERT INTO `User` (`ID`, `name`, `email`, `isattendee`) VALUES
(1, 'Frank', 'frank@mail.de', 'i'),
(2, 'Marten', 'marten@mail.de', 'i'),
(3, 'Stefan', 'stefan@mail.de', 'i');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `VAlarm`
--

CREATE TABLE `VAlarm` (
  `ID` int(11) NOT NULL,
  `action` varchar(20) NOT NULL,
  `trigger` varchar(20) NOT NULL,
  `duration` varchar(20) NOT NULL,
  `repeat` int(11) NOT NULL,
  `attachID` int(11) DEFAULT NULL,
  `description` varchar(50) NOT NULL,
  `attendeeID` int(11) DEFAULT NULL,
  `summary` varchar(100) NOT NULL,
  `xprop` varchar(100) NOT NULL,
  `ianaprop` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `VCalendar`
--

CREATE TABLE `VCalendar` (
  `ID` int(11) NOT NULL,
  `userID` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `description` varchar(200) DEFAULT NULL,
  `prodid` varchar(10) NOT NULL,
  `version` varchar(10) NOT NULL,
  `calscale` varchar(10) NOT NULL,
  `method` varchar(10) NOT NULL,
  `xprop` varchar(100) DEFAULT NULL,
  `ianaprop` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `VCalendar`
--

INSERT INTO `VCalendar` (`ID`, `userID`, `name`, `description`, `prodid`, `version`, `calscale`, `method`, `xprop`, `ianaprop`) VALUES
(1, 3, 'SVLFG', 'Treffen dienstlich.', '', '', '', '', NULL, NULL),
(2, 3, 'Urlaub Stefan', 'Urlaubstage 2021', '', '', '', '', NULL, NULL),
(3, 2, 'Urlaub Marten', 'Urlaubstage 2021', '', '', '', '', NULL, NULL);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `VEvent`
--

CREATE TABLE `VEvent` (
  `ID` int(11) NOT NULL,
  `description` varchar(255) NOT NULL,
  `dtstamp` datetime NOT NULL,
  `uid` varchar(20) NOT NULL,
  `dtstart` datetime NOT NULL,
  `dtend` datetime NOT NULL,
  `duration` varchar(20) NOT NULL,
  `class` varchar(12) NOT NULL,
  `created` datetime NOT NULL,
  `geolat` float NOT NULL,
  `geolng` float NOT NULL,
  `lastmod` datetime NOT NULL,
  `location` varchar(100) NOT NULL,
  `organizer` varchar(200) NOT NULL,
  `priority` int(11) NOT NULL,
  `seq` int(11) NOT NULL,
  `status` varchar(20) NOT NULL,
  `summary` varchar(100) NOT NULL,
  `transp` varchar(11) NOT NULL,
  `url` varchar(100) NOT NULL,
  `recurid` varchar(20) NOT NULL,
  `attachID` int(11) DEFAULT NULL,
  `attendeeID` int(11) DEFAULT NULL,
  `categoriesID` int(11) DEFAULT NULL,
  `commentID` int(11) DEFAULT NULL,
  `contactID` int(11) DEFAULT NULL,
  `exdateID` int(11) DEFAULT NULL,
  `rstatusID` int(11) DEFAULT NULL,
  `relatedID` int(11) DEFAULT NULL,
  `resourcesID` int(11) DEFAULT NULL,
  `rdateID` int(11) DEFAULT NULL,
  `xpropID` int(11) DEFAULT NULL,
  `ianapropID` int(11) DEFAULT NULL,
  `valarmID` int(11) DEFAULT NULL,
  `rruleID` int(11) DEFAULT NULL,
  `vcalendarID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `VEvent`
--

INSERT INTO `VEvent` (`ID`, `description`, `dtstamp`, `uid`, `dtstart`, `dtend`, `duration`, `class`, `created`, `geolat`, `geolng`, `lastmod`, `location`, `organizer`, `priority`, `seq`, `status`, `summary`, `transp`, `url`, `recurid`, `attachID`, `attendeeID`, `categoriesID`, `commentID`, `contactID`, `exdateID`, `rstatusID`, `relatedID`, `resourcesID`, `rdateID`, `xpropID`, `ianapropID`, `valarmID`, `rruleID`, `vcalendarID`) VALUES
(1, 'Meeting Python-Aufgabe', '2021-11-15 11:43:00', '', '2021-12-23 14:00:00', '2021-12-23 15:00:00', '', '', '2021-11-15 11:43:00', 1, 1, '2021-11-15 11:43:00', '', '', 1, 1, '1', 'Meeting Stefan', '', '', '', NULL, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1),
(2, 'Urlaub Dezember', '2021-11-15 11:47:25', '', '2021-12-24 00:00:00', '2021-12-31 23:59:59', '', '', '2021-11-15 11:47:25', 1, 1, '2021-11-15 11:47:25', '', '', 1, 1, '1', 'Urlaub Stefan', '', '', '', NULL, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2),
(3, 'Urlaub Dezember', '2021-11-15 11:49:24', '', '2021-12-24 00:00:00', '2021-12-31 23:59:59', '', '', '2021-11-15 11:49:24', 1, 1, '2021-11-15 11:49:24', '', '', 1, 1, '1', 'Urlaub Marten', '', '', '', NULL, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Xprop`
--

CREATE TABLE `Xprop` (
  `ID` int(11) NOT NULL,
  `xprop` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `Attach`
--
ALTER TABLE `Attach`
  ADD PRIMARY KEY (`ID`);

--
-- Indizes für die Tabelle `Categories`
--
ALTER TABLE `Categories`
  ADD PRIMARY KEY (`ID`);

--
-- Indizes für die Tabelle `Comment`
--
ALTER TABLE `Comment`
  ADD PRIMARY KEY (`ID`);

--
-- Indizes für die Tabelle `Contact`
--
ALTER TABLE `Contact`
  ADD PRIMARY KEY (`ID`);

--
-- Indizes für die Tabelle `Exdate`
--
ALTER TABLE `Exdate`
  ADD PRIMARY KEY (`ID`);

--
-- Indizes für die Tabelle `Ianaprop`
--
ALTER TABLE `Ianaprop`
  ADD PRIMARY KEY (`ID`);

--
-- Indizes für die Tabelle `RDate`
--
ALTER TABLE `RDate`
  ADD PRIMARY KEY (`ID`);

--
-- Indizes für die Tabelle `Related`
--
ALTER TABLE `Related`
  ADD PRIMARY KEY (`ID`);

--
-- Indizes für die Tabelle `Resources`
--
ALTER TABLE `Resources`
  ADD PRIMARY KEY (`ID`);

--
-- Indizes für die Tabelle `RRule`
--
ALTER TABLE `RRule`
  ADD PRIMARY KEY (`ID`);

--
-- Indizes für die Tabelle `Rstatus`
--
ALTER TABLE `Rstatus`
  ADD PRIMARY KEY (`ID`);

--
-- Indizes für die Tabelle `User`
--
ALTER TABLE `User`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `ID` (`ID`);

--
-- Indizes für die Tabelle `VAlarm`
--
ALTER TABLE `VAlarm`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `attachID` (`attachID`),
  ADD KEY `attendeeID` (`attendeeID`);

--
-- Indizes für die Tabelle `VCalendar`
--
ALTER TABLE `VCalendar`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `userID` (`userID`);

--
-- Indizes für die Tabelle `VEvent`
--
ALTER TABLE `VEvent`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `rruleID` (`rruleID`),
  ADD KEY `vcalendarID` (`vcalendarID`),
  ADD KEY `attachID` (`attachID`),
  ADD KEY `attendeeID` (`attendeeID`),
  ADD KEY `categoriesID` (`categoriesID`),
  ADD KEY `commentID` (`commentID`),
  ADD KEY `contactID` (`contactID`),
  ADD KEY `exdateID` (`exdateID`),
  ADD KEY `rstatusID` (`rstatusID`),
  ADD KEY `relatedID` (`relatedID`),
  ADD KEY `resourcesID` (`resourcesID`),
  ADD KEY `rdateID` (`rdateID`),
  ADD KEY `xpropID` (`xpropID`),
  ADD KEY `ianapropID` (`ianapropID`),
  ADD KEY `valarmID` (`valarmID`);

--
-- Indizes für die Tabelle `Xprop`
--
ALTER TABLE `Xprop`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `Attach`
--
ALTER TABLE `Attach`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `Categories`
--
ALTER TABLE `Categories`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `Comment`
--
ALTER TABLE `Comment`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `Contact`
--
ALTER TABLE `Contact`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `Exdate`
--
ALTER TABLE `Exdate`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `Ianaprop`
--
ALTER TABLE `Ianaprop`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `RDate`
--
ALTER TABLE `RDate`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `Related`
--
ALTER TABLE `Related`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `Resources`
--
ALTER TABLE `Resources`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `RRule`
--
ALTER TABLE `RRule`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `Rstatus`
--
ALTER TABLE `Rstatus`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `User`
--
ALTER TABLE `User`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT für Tabelle `VAlarm`
--
ALTER TABLE `VAlarm`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT für Tabelle `VCalendar`
--
ALTER TABLE `VCalendar`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT für Tabelle `VEvent`
--
ALTER TABLE `VEvent`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT für Tabelle `Xprop`
--
ALTER TABLE `Xprop`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `VAlarm`
--
ALTER TABLE `VAlarm`
  ADD CONSTRAINT `valarm_ibfk_1` FOREIGN KEY (`attachID`) REFERENCES `Attach` (`ID`),
  ADD CONSTRAINT `valarm_ibfk_2` FOREIGN KEY (`attendeeID`) REFERENCES `User` (`ID`);

--
-- Constraints der Tabelle `VCalendar`
--
ALTER TABLE `VCalendar`
  ADD CONSTRAINT `vcalendar_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `User` (`ID`);

--
-- Constraints der Tabelle `VEvent`
--
ALTER TABLE `VEvent`
  ADD CONSTRAINT `vevent_ibfk_1` FOREIGN KEY (`rruleID`) REFERENCES `RRule` (`ID`),
  ADD CONSTRAINT `vevent_ibfk_10` FOREIGN KEY (`relatedID`) REFERENCES `Related` (`ID`),
  ADD CONSTRAINT `vevent_ibfk_11` FOREIGN KEY (`resourcesID`) REFERENCES `Resources` (`ID`),
  ADD CONSTRAINT `vevent_ibfk_12` FOREIGN KEY (`rdateID`) REFERENCES `RDate` (`ID`),
  ADD CONSTRAINT `vevent_ibfk_13` FOREIGN KEY (`xpropID`) REFERENCES `Xprop` (`ID`),
  ADD CONSTRAINT `vevent_ibfk_14` FOREIGN KEY (`ianapropID`) REFERENCES `Ianaprop` (`ID`),
  ADD CONSTRAINT `vevent_ibfk_15` FOREIGN KEY (`valarmID`) REFERENCES `VAlarm` (`ID`),
  ADD CONSTRAINT `vevent_ibfk_2` FOREIGN KEY (`vcalendarID`) REFERENCES `VCalendar` (`ID`),
  ADD CONSTRAINT `vevent_ibfk_3` FOREIGN KEY (`attachID`) REFERENCES `Attach` (`ID`),
  ADD CONSTRAINT `vevent_ibfk_4` FOREIGN KEY (`attendeeID`) REFERENCES `User` (`ID`),
  ADD CONSTRAINT `vevent_ibfk_5` FOREIGN KEY (`categoriesID`) REFERENCES `Categories` (`ID`),
  ADD CONSTRAINT `vevent_ibfk_6` FOREIGN KEY (`commentID`) REFERENCES `Comment` (`ID`),
  ADD CONSTRAINT `vevent_ibfk_7` FOREIGN KEY (`contactID`) REFERENCES `Contact` (`ID`),
  ADD CONSTRAINT `vevent_ibfk_8` FOREIGN KEY (`exdateID`) REFERENCES `Exdate` (`ID`),
  ADD CONSTRAINT `vevent_ibfk_9` FOREIGN KEY (`rstatusID`) REFERENCES `Rstatus` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
