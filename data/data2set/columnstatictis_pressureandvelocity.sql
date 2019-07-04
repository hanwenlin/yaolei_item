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

 Date: 27/06/2019 17:00:16
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for columnstatictis_pressureandvelocity
-- ----------------------------
DROP TABLE IF EXISTS `columnstatictis_pressureandvelocity`;
CREATE TABLE `columnstatictis_pressureandvelocity`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `packingproject` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `columnid` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `resinid` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `minipackingvelocity` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `maxpackingvelocity` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `packingpressure` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `productionvelocity` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `columnheight` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `columndimeter` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `symmetry` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `hetp` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `comment` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `resin_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `columnstatictis_pres_resin_id_a99f1519_fk_material_`(`resin_id`) USING BTREE,
  CONSTRAINT `columnstatictis_pres_resin_id_a99f1519_fk_material_` FOREIGN KEY (`resin_id`) REFERENCES `material_resinlabel` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of columnstatictis_pressureandvelocity
-- ----------------------------
INSERT INTO `columnstatictis_pressureandvelocity` VALUES (1, '2074', 'BP246-23', '', '150', '450', '3', '2', '21', '', '1.25', '0.1239', 'NA', 3);
INSERT INTO `columnstatictis_pressureandvelocity` VALUES (2, '2064', 'BP236-07', 'xc-02-45', '150', '350', '3', '', '23.5', '234', '1.25', '0.2345', '', 3);
INSERT INTO `columnstatictis_pressureandvelocity` VALUES (3, '2080', 'BP246-23', 'MMR-213-67', '120', '300', '3', '8.9', '33.4', '246', '1.47', '0.12357', 'NA', 4);
INSERT INTO `columnstatictis_pressureandvelocity` VALUES (4, '2368', 'BPG1234-34', 'xc-02-45', '', '380', '4', '2', '23.0', '673', '2.31', '0.1245', 'NA', 5);
INSERT INTO `columnstatictis_pressureandvelocity` VALUES (5, '2988', 'BP255-35', 'xs-12-A', '170', '444', '3', '', '12,9', '123', '2.34', '0.356', '', 1);

SET FOREIGN_KEY_CHECKS = 1;
