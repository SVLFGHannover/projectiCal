SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS `User`;
DROP TABLE IF EXISTS `VEvent`;
DROP TABLE IF EXISTS `RRule`;
DROP TABLE IF EXISTS `VCalendar`;
DROP TABLE IF EXISTS `RDate`;
DROP TABLE IF EXISTS `VAlarm`;
DROP TABLE IF EXISTS `Attach`;
DROP TABLE IF EXISTS `Exdate`;
DROP TABLE IF EXISTS `Categories`;
DROP TABLE IF EXISTS `Comment`;
DROP TABLE IF EXISTS `Contact`;
DROP TABLE IF EXISTS `Rstatus`;
DROP TABLE IF EXISTS `Related`;
DROP TABLE IF EXISTS `Resources`;
DROP TABLE IF EXISTS `Xprop`;
DROP TABLE IF EXISTS `Ianaprop`;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE `User` (
    `ID` INTEGER NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL,
    `email` VARCHAR(50) NOT NULL,
    `isattendee` CHAR NOT NULL,
    PRIMARY KEY (`ID`),
    UNIQUE (`ID`)
);

CREATE TABLE `VEvent` (
    `ID` INTEGER NOT NULL AUTO_INCREMENT,
    `description` VARCHAR(255) NOT NULL,
    `dtstamp` DATETIME NOT NULL,
    `uid` VARCHAR(20) NOT NULL,
    `dtstart` DATETIME NOT NULL,
    `dtend` DATETIME NOT NULL,
    `duration` VARCHAR(20) NOT NULL,
    `class` VARCHAR(12) NOT NULL,
    `created` DATETIME NOT NULL,
    `geolat` FLOAT NOT NULL,
    `geolng` FLOAT NOT NULL,
    `lastmod` DATETIME NOT NULL,
    `location` VARCHAR(100) NOT NULL,
    `organizer` VARCHAR(200) NOT NULL,
    `priority` INTEGER NOT NULL,
    `seq` INTEGER NOT NULL,
    `status` VARCHAR(20) NOT NULL,
    `summary` VARCHAR(100) NOT NULL,
    `transp` VARCHAR(11) NOT NULL,
    `url` VARCHAR(100) NOT NULL,
    `recurid` VARCHAR(20) NOT NULL,
    `attachID` INTEGER,
    `attendeeID` INTEGER,
    `categoriesID` INTEGER,
    `commentID` INTEGER,
    `contactID` INTEGER,
    `exdateID` INTEGER,
    `rstatusID` INTEGER,
    `relatedID` INTEGER,
    `resourcesID` INTEGER,
    `rdateID` INTEGER,
    `xpropID` INTEGER,
    `ianapropID` INTEGER,
    `valarmID` INTEGER,
    `rruleID` INTEGER,
    `vcalendarID` INTEGER NOT NULL,
    PRIMARY KEY (`ID`)
);

CREATE TABLE `RRule` (
    `ID` INTEGER NOT NULL AUTO_INCREMENT,
    `freq` VARCHAR(8) NOT NULL,
    `until` DATETIME NOT NULL,
    `count` INTEGER NOT NULL,
    `interval` INTEGER NOT NULL,
    `bysecond` VARCHAR(20) NOT NULL,
    `byminute` VARCHAR(20) NOT NULL,
    `byhour` VARCHAR(20) NOT NULL,
    `byday` VARCHAR(20) NOT NULL,
    `bymonthday` VARCHAR(20) NOT NULL,
    `byyearday` VARCHAR(20) NOT NULL,
    `byweekno` VARCHAR(20) NOT NULL,
    `bymonth` VARCHAR(20) NOT NULL,
    `bysetpos` VARCHAR(20) NOT NULL,
    `wkst` VARCHAR(2) NOT NULL,
    PRIMARY KEY (`ID`)
);

CREATE TABLE `VCalendar` (
    `ID` INTEGER NOT NULL AUTO_INCREMENT,
    `userID` INTEGER NOT NULL,
    `name` VARCHAR(20) NOT NULL,
    `description` VARCHAR(200),
    `prodid` VARCHAR(10) NOT NULL,
    `version` VARCHAR(10) NOT NULL,
    `calscale` VARCHAR(10) NOT NULL,
    `method` VARCHAR(10) NOT NULL,
    `xprop` VARCHAR(100),
    `ianaprop` VARCHAR(100),
    PRIMARY KEY (`ID`)
);

CREATE TABLE `RDate` (
    `ID` INTEGER NOT NULL AUTO_INCREMENT,
    `rdtparam` VARCHAR(20) NOT NULL,
    `rdtval` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`ID`)
);

CREATE TABLE `VAlarm` (
    `ID` INTEGER NOT NULL AUTO_INCREMENT,
    `action` VARCHAR(20) NOT NULL,
    `trigger` VARCHAR(20) NOT NULL,
    `duration` VARCHAR(20) NOT NULL,
    `repeat` INTEGER NOT NULL,
    `attachID` INTEGER,
    `description` VARCHAR(50) NOT NULL,
    `attendeeID` INTEGER,
    `summary` VARCHAR(100) NOT NULL,
    `xprop` VARCHAR(100) NOT NULL,
    `ianaprop` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`ID`)
);

CREATE TABLE `Attach` (
    `ID` INTEGER NOT NULL AUTO_INCREMENT,
    `attachment` BLOB NOT NULL,
    PRIMARY KEY (`ID`)
);

CREATE TABLE `Exdate` (
    `ID` INTEGER NOT NULL AUTO_INCREMENT,
    `exdate` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`ID`)
);

CREATE TABLE `Categories` (
    `ID` INTEGER NOT NULL AUTO_INCREMENT,
    `category` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`ID`)
);

CREATE TABLE `Comment` (
    `ID` INTEGER NOT NULL AUTO_INCREMENT,
    `comment` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`ID`)
);

CREATE TABLE `Contact` (
    `ID` INTEGER NOT NULL AUTO_INCREMENT,
    `contact` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`ID`)
);

CREATE TABLE `Rstatus` (
    `ID` INTEGER NOT NULL AUTO_INCREMENT,
    `statcode` VARCHAR(100) NOT NULL,
    `Column1` INTEGER NOT NULL,
    `statdesc` VARCHAR(100) NOT NULL,
    `exdata` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`ID`)
);

CREATE TABLE `Related` (
    `ID` INTEGER NOT NULL AUTO_INCREMENT,
    `related` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`ID`)
);

CREATE TABLE `Resources` (
    `ID` INTEGER NOT NULL AUTO_INCREMENT,
    `resource` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`ID`)
);

CREATE TABLE `Xprop` (
    `ID` INTEGER NOT NULL AUTO_INCREMENT,
    `xprop` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`ID`)
);

CREATE TABLE `Ianaprop` (
    `ID` INTEGER NOT NULL AUTO_INCREMENT,
    `ianaprop` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`ID`)
);

ALTER TABLE `VEvent` ADD FOREIGN KEY (`rruleID`) REFERENCES `RRule`(`ID`);
ALTER TABLE `VEvent` ADD FOREIGN KEY (`vcalendarID`) REFERENCES `VCalendar`(`ID`);
ALTER TABLE `VEvent` ADD FOREIGN KEY (`attachID`) REFERENCES `Attach`(`ID`);
ALTER TABLE `VEvent` ADD FOREIGN KEY (`attendeeID`) REFERENCES `User`(`ID`);
ALTER TABLE `VEvent` ADD FOREIGN KEY (`categoriesID`) REFERENCES `Categories`(`ID`);
ALTER TABLE `VEvent` ADD FOREIGN KEY (`commentID`) REFERENCES `Comment`(`ID`);
ALTER TABLE `VEvent` ADD FOREIGN KEY (`contactID`) REFERENCES `Contact`(`ID`);
ALTER TABLE `VEvent` ADD FOREIGN KEY (`exdateID`) REFERENCES `Exdate`(`ID`);
ALTER TABLE `VEvent` ADD FOREIGN KEY (`rstatusID`) REFERENCES `Rstatus`(`ID`);
ALTER TABLE `VEvent` ADD FOREIGN KEY (`relatedID`) REFERENCES `Related`(`ID`);
ALTER TABLE `VEvent` ADD FOREIGN KEY (`resourcesID`) REFERENCES `Resources`(`ID`);
ALTER TABLE `VEvent` ADD FOREIGN KEY (`rdateID`) REFERENCES `RDate`(`ID`);
ALTER TABLE `VEvent` ADD FOREIGN KEY (`xpropID`) REFERENCES `Xprop`(`ID`);
ALTER TABLE `VEvent` ADD FOREIGN KEY (`ianapropID`) REFERENCES `Ianaprop`(`ID`);
ALTER TABLE `VEvent` ADD FOREIGN KEY (`valarmID`) REFERENCES `VAlarm`(`ID`);
ALTER TABLE `VCalendar` ADD FOREIGN KEY (`userID`) REFERENCES `User`(`ID`);
ALTER TABLE `VAlarm` ADD FOREIGN KEY (`attachID`) REFERENCES `Attach`(`ID`);
ALTER TABLE `VAlarm` ADD FOREIGN KEY (`attendeeID`) REFERENCES `User`(`ID`);