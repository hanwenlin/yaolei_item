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

 Date: 27/06/2019 17:00:59
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for material_resinlabel
-- ----------------------------
DROP TABLE IF EXISTS `material_resinlabel`;
CREATE TABLE `material_resinlabel`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `resinName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `resinaType` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `brand` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `matrix` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ligand` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `diameter` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Pmax` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `phRange` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `storageMethod` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `compactFactor` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `dbc` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `LoadingRangeinProject` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `PackingVmaxandPmax` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expiry` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `TypeofColomuPackingMethod` varchar(5) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ColomuPackingMethod` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of material_resinlabel
-- ----------------------------
INSERT INTO `material_resinlabel` VALUES (1, 'Mabselect', 'Affinity', 'GE', 'Sepharose(琼脂糖)', 'rProtain A', '85', '', '2-12', '20%EtOH', '1.06', '>=30', '3', '3', '', 'B', '');
INSERT INTO `material_resinlabel` VALUES (2, 'Mabselect Xtra', 'Affinity', 'GE', 'Sepharose(琼脂糖)', 'rProtain A variant', '75', '', '2-12', '20%EtOH/2%benzy1', '2.34', '>=40', '9', '3', '', 'C', '');
INSERT INTO `material_resinlabel` VALUES (3, 'Mabselect SuRe', 'Affinity', 'GE', 'Sepharose(琼脂糖)', 'rProtain A', '85', '', '2-14', '', '1.06', '>=30', '', '3', '', 'D', '');
INSERT INTO `material_resinlabel` VALUES (4, 'POROS', 'Affinity', 'Life', '苯乙酸', 'rProtain A', '50', '', '2·13', '', '1.78', '>=45', '7', '3.8', '', 'D', '');
INSERT INTO `material_resinlabel` VALUES (5, 'JWT203', 'Affinity', 'JSR', '多孔聚甲基丙烯酸', 'rProtain A', '75', '', '1.5-13.5', '', '', '>=37', '', '3.8', '', 'E', '');
INSERT INTO `material_resinlabel` VALUES (6, 'Eshmunoa', 'Affinity', 'Millipore', '聚乙烯醚', 'rProtain A', '49', '', '2·13', '', '2.34', '>=45', '', '', '', 'B', '');

SET FOREIGN_KEY_CHECKS = 1;
