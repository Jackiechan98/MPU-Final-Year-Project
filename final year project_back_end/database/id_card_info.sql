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

 Date: 10/03/2022 01:00:04
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for id_card_info
-- ----------------------------
DROP TABLE IF EXISTS `id_card_info`;
CREATE TABLE `id_card_info`  (
  `bir_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `sex` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `birthday` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_upload_video` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `is_upload_instruction` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `is_upload_statement` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`email`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of id_card_info
-- ----------------------------
INSERT INTO `id_card_info` VALUES ('1000248(3)', 'F', '22-06-1961', '宗,家強', '1095622812@qq.com', 'true', 'true', 'true');
INSERT INTO `id_card_info` VALUES ('1000248(3)', 'F', '08-11-1998', '曾,依文', '1095622812qq@gmail.com', 'true', 'true', 'true');
INSERT INTO `id_card_info` VALUES ('1000248(3)', 'M', '22-06-1961', '宗,家強', 'p1807524@ipm.edu.mo', 'true', 'true', 'true');
INSERT INTO `id_card_info` VALUES ('1000248(3)', 'M', '22-06-1961', '宗,家強', 'zqchenjiajie@outlook.com', 'true', 'true', 'true');
INSERT INTO `id_card_info` VALUES ('1000248(3)', 'F', '22-06-1961', '宗,家強', 'zqchenjiajie98@163.com', 'true', 'true', 'true');

SET FOREIGN_KEY_CHECKS = 1;
