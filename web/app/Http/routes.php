<?php

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It's a breeze. Simply tell Laravel the URIs it should respond to
| and give it the controller to call when that URI is requested.
|
*/

#引入自定义路由文件
#前台路由
require_once "Routers/App/index.router.php";

#后台路由
require_once "Routers/Admin/index.router.php";