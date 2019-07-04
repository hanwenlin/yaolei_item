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

 Date: 20/06/2019 14:32:25
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for issues_meterialissues
-- ----------------------------
DROP TABLE IF EXISTS `issues_meterialissues`;
CREATE TABLE `issues_meterialissues`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pubtime` datetime(6) NOT NULL,
  `histcode` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `issue_id` int(11) NOT NULL,
  `meterial_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `issues_meterialissues_issue_id_ed78b7a8_fk_issues_issues_id`(`issue_id`) USING BTREE,
  INDEX `issues_meterialissue_meterial_id_5aa99975_fk_material_`(`meterial_id`) USING BTREE,
  CONSTRAINT `issues_meterialissue_meterial_id_5aa99975_fk_material_` FOREIGN KEY (`meterial_id`) REFERENCES `material_meterials` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `issues_meterialissues_issue_id_ed78b7a8_fk_issues_issues_id` FOREIGN KEY (`issue_id`) REFERENCES `issues_issues` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of issues_meterialissues
-- ----------------------------
INSERT INTO `issues_meterialissues` VALUES (1, '2019-06-20 01:22:08.901264', '2145', 2, 5);
INSERT INTO `issues_meterialissues` VALUES (2, '2019-06-20 01:22:28.101907', '3566', 3, 5);
INSERT INTO `issues_meterialissues` VALUES (3, '2019-06-20 01:23:19.973167', '6788', 2, 1);
INSERT INTO `issues_meterialissues` VALUES (4, '2019-06-12 16:00:00.000000', '2145', 5, 5);
INSERT INTO `issues_meterialissues` VALUES (5, '2019-06-20 03:12:56.068938', '4577', 2, 5);

SET FOREIGN_KEY_CHECKS = 1;
