/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80028
 Source Host           : localhost:3306
 Source Schema         : fyp

 Target Server Type    : MySQL
 Target Server Version : 80028
 File Encoding         : 65001

 Date: 10/03/2022 00:59:58
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for team_info
-- ----------------------------
DROP TABLE IF EXISTS `team_info`;
CREATE TABLE `team_info`  (
  `team_num` int(0) NOT NULL,
  `tutor` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `team_mem_two` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `team_mem_three` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `team_type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `video_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`team_num`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of team_info
-- ----------------------------
INSERT INTO `team_info` VALUES (1, '叶李华', '褚超钧', '无', '褚超钧', '1095622812@qq.com', 'test.mp4');
INSERT INTO `team_info` VALUES (2, '2', '2', '2', '2', 'zqchenjiajie@outlook.com', 'zqchenjiajie@outlook.com_test.mp4');
INSERT INTO `team_info` VALUES (4, '4', '4', '4', '4', 'zqchenjiajie98@163.com', 'test.mp4');

SET FOREIGN_KEY_CHECKS = 1;
