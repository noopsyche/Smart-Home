<?php
namespace App\Http\Controllers\Admin;

use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Auth\Access\AuthorizesResources;
use Crypt;

/***
 * 用户登陆相关控制器
 *
 * Class PassportController
 * @package App\Http\Controllers\Admin
 */
class PassportController extends BaseController
{
    public function index(){
        dd(Crypt::encrypt("admin"));
    }
}
