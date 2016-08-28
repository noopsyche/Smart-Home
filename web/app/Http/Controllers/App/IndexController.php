<?php
namespace App\Http\Controllers\App;

use Illuminate\Routing\Controller as BaseController;
use Crypt;
use Illuminate\Support\Facades\Cache;
use Illuminate\Support\Facades\Session;

/***
 * 用户登陆相关控制器
 *
 * Class PassportController
 * @package App\Http\Controllers\Admin
 */
class IndexController extends BaseController
{
    public function Index(){
        return view("app.index");
    }
}
