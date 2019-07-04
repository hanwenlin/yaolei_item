/*
 Navicat MySQL Data Transfer

 Source Server         : user
 Source Server Type    : MySQL
 Source Server Version : 50719
 Source Host           : localhost:3306
 Source Schema         : yaolei

 Target Server Type    : MySQL
 Target Server Version : 50719
 File Encoding         : 65001

 Date: 20/06/2019 14:32:10
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for columnstatictis_columnstatictis
-- ----------------------------
DROP TABLE IF EXISTS `columnstatictis_columnstatictis`;
CREATE TABLE `columnstatictis_columnstatictis`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `packingitem` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `histcode` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `resincode` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `lowestspeed` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `hightspeed` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pressure` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `yieldspeed` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `columnheight` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `columndimeter` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `symmetry` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `hetp` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `comment` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `resin_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `columnstatictis_colu_resin_id_e3c97ecd_fk_material_`(`resin_id`) USING BTREE,
  CONSTRAINT `columnstatictis_colu_resin_id_e3c97ecd_fk_material_` FOREIGN KEY (`resin_id`) REFERENCES `material_meterials` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of columnstatictis_columnstatictis
-- ----------------------------
INSERT INTO `columnstatictis_columnstatictis` VALUES (3, '2078', 'BP246-23', '12', '150', '260', '3', '2', '23.5', '', '1.25', '0.1234', '', 1);
INSERT INTO `columnstatictis_columnstatictis` VALUES (4, '2064', 'BP236-07', 'xc-02-45', '120', '128', '3', '', '21', '', '1.09', '0.1234', 'NA', 4);
INSERT INTO `columnstatictis_columnstatictis` VALUES (5, '2070', 'BP246-23', '12', '150', 'NA', '', '2', '46', '', '0.94', '0.576', '', 2);
INSERT INTO `columnstatictis_columnstatictis` VALUES (7, '810', 'BPG1234-34', 'XM-23123-3', '150', '350', '', '', '235', '', '1.14', '0.0112456', '', 5);
INSERT INTO `columnstatictis_columnstatictis` VALUES (9, '', '', '', '', '', '', '', '', '', '', '', '', 5);

SET FOREIGN_KEY_CHECKS = 1;
