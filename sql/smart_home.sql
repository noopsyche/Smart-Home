/*
Navicat MySQL Data Transfer

Source Server         : 本地
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : smart_home

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2016-08-28 23:40:09
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
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8;


