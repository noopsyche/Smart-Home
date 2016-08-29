<?php
namespace App\Http\Controllers\Admin;

use Illuminate\Routing\Controller as BaseController;
use Illuminate\Foundation\Auth\Access\AuthorizesResources;
use Illuminate\Support\Facades\Crypt;

/***
 * 首页显示相关控制器
 *
 * Class PassportController
 * @package App\Http\Controllers\Admin
 */
class IndexController extends BaseController
{
    public function Index(){
        return view("admin.index");
    }
}
