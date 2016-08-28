<?php
Route::group(["prefix"=>"/",'namespace' => 'App'], function(){
    Route::get('/', "IndexController@Index");
});
