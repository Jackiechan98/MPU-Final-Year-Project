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

 Date: 10/03/2022 00:59:51
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `uName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `uTel` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `uid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `team_num` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `register_time` timestamp(6) NULL DEFAULT NULL,
  PRIMARY KEY (`email`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1095622812@qq.com', '1800c1a172518ebd2552219a4993f965468eec1b', 'Jacky', '18938301036', '1095622812', NULL, '2022-02-27 23:46:07.000000');
INSERT INTO `user` VALUES ('1095622812qq@gmail.com', '1800c1a172518ebd2552219a4993f965468eec1b', 'Yiwen', '189383310000', '232425', NULL, '2022-03-09 23:46:07.000000');
INSERT INTO `user` VALUES ('p1807524@ipm.edu.mo', '1800c1a172518ebd2552219a4993f965468eec1b', 'Tom', '18929896529', '18938301036', NULL, '2022-03-09 23:46:07.000000');
INSERT INTO `user` VALUES ('zqchenjiajie@outlook.com', '2497f18fa00428de197bd8c13e4d36ca28980a60', 'SamSung', '13822600778', '35515530', '2', '2022-03-09 23:46:07.000000');
INSERT INTO `user` VALUES ('zqchenjiajie98@163.com', '1800c1a172518ebd2552219a4993f965468eec1b', 'Maggie', '18938301037', '65216638', '4', '2022-03-09 23:46:07.000000');

SET FOREIGN_KEY_CHECKS = 1;
