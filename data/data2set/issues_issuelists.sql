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

 Date: 27/06/2019 17:00:26
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for issues_issuelists
-- ----------------------------
DROP TABLE IF EXISTS `issues_issuelists`;
CREATE TABLE `issues_issuelists`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pubtime` datetime(6) NOT NULL,
  `Practiceissue` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ColumnID` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `solutionMethod` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `issue_id` int(11) NOT NULL,
  `meterial_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `issues_issuelists_issue_id_803d028f_fk_issues_issues_id`(`issue_id`) USING BTREE,
  INDEX `issues_issuelists_meterial_id_bbd3d786_fk_material_resinlabel_id`(`meterial_id`) USING BTREE,
  CONSTRAINT `issues_issuelists_issue_id_803d028f_fk_issues_issues_id` FOREIGN KEY (`issue_id`) REFERENCES `issues_issues` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `issues_issuelists_meterial_id_bbd3d786_fk_material_resinlabel_id` FOREIGN KEY (`meterial_id`) REFERENCES `material_resinlabel` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of issues_issuelists
-- ----------------------------
INSERT INTO `issues_issuelists` VALUES (1, '2019-06-24 01:47:36.861227', '问题C', '2145', '有如下解决方案，第一条方案是', 3, 4);
INSERT INTO `issues_issuelists` VALUES (2, '2019-06-24 01:48:04.837401', '问题D', '2356', '有如下解决方案，我们可以解决的问题是', 4, 1);
INSERT INTO `issues_issuelists` VALUES (3, '2019-06-23 16:00:00.000000', '问题E', '2370', 'forexample241236', 5, 4);

SET FOREIGN_KEY_CHECKS = 1;
