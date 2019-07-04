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

 Date: 27/06/2019 17:00:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for issues_issues
-- ----------------------------
DROP TABLE IF EXISTS `issues_issues`;
CREATE TABLE `issues_issues`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `issueType` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `issue` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `reason` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `solution` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of issues_issues
-- ----------------------------
INSERT INTO `issues_issues` VALUES (1, 'A', '混匀是会有大量浮胶出现，并且装填效果不好', '填料里含有未清除干净，影响柱效', '1.新旧填料都存在碎胶，以及上浮部分也存在好觉 2.对于新填料，以及旧的Mabselect填料生产的时候');
INSERT INTO `issues_issues` VALUES (2, 'B', '层析柱装填后，生产时取出层析柱使用时出现层析柱干涸的现象', '层析柱中有气泡导致柱子干', '1.建议装填完成保存结束后，将层析柱出口关闭  2.若柱子已经干涸可在填料耐受的最大压力下对柱子反冲，使干涸的地方恢复正常');
INSERT INTO `issues_issues` VALUES (3, 'C', '层析柱柱头漏液', '1.填料粒径小 2.胶圈老化', '1.填料的问题，2.胶圈大小的问题');
INSERT INTO `issues_issues` VALUES (4, 'D', '中试层析柱部分筛网老旧，胶圈老化出现漏液的现象', '筛网和胶圈太长，长期为期进行维保', '后期出现场层析柱漏液情况');
INSERT INTO `issues_issues` VALUES (5, 'E', '层析柱装填时出现局部胶圈下陷', '筛网损坏', '更换刷网');

SET FOREIGN_KEY_CHECKS = 1;
