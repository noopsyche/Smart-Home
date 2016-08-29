/*
Navicat MySQL Data Transfer

Source Server         : 本地
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : smart_home

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2016-08-30 01:47:05
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL COMMENT '用户名',
  `password` varchar(512) DEFAULT NULL COMMENT '密码',
  `name` varchar(255) DEFAULT NULL COMMENT '姓名',
  `email` varchar(255) DEFAULT NULL COMMENT '邮箱',
  `mobile` int(11) DEFAULT NULL COMMENT '手机号码',
  `isnotifiy` int(1) DEFAULT NULL COMMENT '发生异常是否通知(0 不通知 1 通知)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('1', 'admin', 'eyJpdiI6IjBheHk0ZXEzQkR0YXB5MkhPRFlIeFE9PSIsInZhbHVlIjoiOEJZOE1BN25uakM3NVg5WWNrcWd1UT09IiwibWFjIjoiNjkyMzIwNDUyMjNjMmQ5ODJjNzU1NmRiNjAyZDVkZDAwZDJjNDU1ZDFjY2JmZDJmZDc1ZjFjMDgxOTIzODA1MCJ9', '管理员', 'admin@amdin.com', '111', '0');

-- ----------------------------
-- Table structure for command
-- ----------------------------
DROP TABLE IF EXISTS `command`;
CREATE TABLE `command` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `content` varchar(255) DEFAULT NULL COMMENT '指令内容',
  `status` int(5) DEFAULT '0' COMMENT '状态 (0 未执行 1 已执行)',
  `posttime` int(15) DEFAULT NULL COMMENT '提交时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=452 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of command
-- ----------------------------
INSERT INTO `command` VALUES ('451', '天气', '0', '1472492823');

-- ----------------------------
-- Table structure for translates
-- ----------------------------
DROP TABLE IF EXISTS `translates`;
CREATE TABLE `translates` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '递增序列id',
  `command` varchar(5120) DEFAULT NULL COMMENT '指令列表',
  `script_name` varchar(255) DEFAULT NULL COMMENT '执行脚本名称',
  `arvg` varchar(2550) DEFAULT NULL COMMENT '脚本参数',
  `type` int(11) DEFAULT '0' COMMENT '命令匹配类型(0 模糊匹配 1精确匹配）',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of translates
-- ----------------------------
INSERT INTO `translates` VALUES ('1', '开灯,光，但我将给你们带来光明', 'serial_switch.py', 'FF-01-01-02-EE', '0');
INSERT INTO `translates` VALUES ('2', '关灯,黑暗,但我喜欢黑暗', 'serial_switch.py', 'FF-01-00-01-EE', '0');
INSERT INTO `translates` VALUES ('3', '今天天气,天气', 'weather.py', 'today', '0');
INSERT INTO `translates` VALUES ('4', '明天天气', 'weather.py', 'tomorrow', '0');
INSERT INTO `translates` VALUES ('5', '现在几点,时间', 'time.py', 'now', '0');
INSERT INTO `translates` VALUES ('6', '今天日期,日期,今天几号', 'time.py', 'today', '0');
