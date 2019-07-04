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

 Date: 20/06/2019 14:32:29
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for material_meterials
-- ----------------------------
DROP TABLE IF EXISTS `material_meterials`;
CREATE TABLE `material_meterials`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `meterialName` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `meterialType` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `brand` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `matrix` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ligand` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `diameter` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tolePressure` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `phRange` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `storeMethod` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `comFactor` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `dbc` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `capacityRange` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `velocityPressure` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `validtyPeriod` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `packingMethod` varchar(5) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `packingdetail` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of material_meterials
-- ----------------------------
INSERT INTO `material_meterials` VALUES (1, 'Mabselect', 'Affinity', 'GE', 'Sepharose(琼脂糖)', 'rProtain A', '85', '', '2-12', '20%EtOH', '1.06', '>=30', '3', '3', '', 'B', '');
INSERT INTO `material_meterials` VALUES (2, 'Mabselect Xtra', 'Affinity', 'GE', 'Sepharose(琼脂糖)', 'rProtain A', '75', '', '2-12', '20%EtOH/2%benzy1', '', '>=40', '3', '', '', 'C', '');
INSERT INTO `material_meterials` VALUES (3, 'Mabselect SuRe', 'Affinity', 'GE', 'Sepharose(琼脂糖)', 'rProtain A', '85', '', '2-14', '', '', '>=30', '3', '', '', 'C', '');
INSERT INTO `material_meterials` VALUES (4, 'POROS', 'Affinity', 'Life', '苯乙酸', 'rProtain A', '45', '', '2-13', '', '', '>=37', '', '', '', 'D', '');
INSERT INTO `material_meterials` VALUES (5, 'JWT203', 'Affinity', 'JSR', '多孔聚甲基丙烯酸', 'rProtain A', '49', '', '2-14', '', '', '>=40', '', '', '', 'E', '');
INSERT INTO `material_meterials` VALUES (6, 'Eshmunoa', 'Affinity', 'Millipore', '聚乙烯醚', 'rProtain A', '50', '', '1.5-13.5', '', '', '>=45', '2', '3', '', 'D', '');

SET FOREIGN_KEY_CHECKS = 1;
