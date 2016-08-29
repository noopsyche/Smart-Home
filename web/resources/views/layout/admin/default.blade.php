<!-- 默认后台模板 -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>@section("head_title")@show</title>
    <!-- SEO 优化区 -->
    @section("head_seo")
    @show
    <!-- CDN 加速资源 -->
    @section("head_cdn")
    <link href="//cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
        <link href="//cdn.bootcss.com/font-awesome/4.6.3/css/font-awesome.min.css" rel="stylesheet">
        <link href="//cdn.bootcss.com/nprogress/0.2.0/nprogress.min.css" rel="stylesheet">
        <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!--[if lt IE 9]>
        <script src="//cdn.bootcss.com/html5shiv/3.7.3/html5shiv.min.js"></script>
        <script src="//cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->
    @show
    <link href="/dict/admin/css/reset.css" rel="stylesheet">
    <!-- 自定义样式 -->
    @section("head_css")

    @show
</head>
<body>
<section class="container-fluid">
</section>
<section id="section_main">
@include("parts/admin/left")
<section id="section_right" class="col-lg-10">
    @section("page_content")
    @show
</section>
</section>
</body>
<!-- CDN 加速资源 -->
@section("foot_cdn")
    <script src="//cdn.bootcss.com/jquery/1.12.4/jquery.min.js"></script>
    <script src="//cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="//cdn.bootcss.com/jquery.pjax/1.9.6/jquery.pjax.min.js"></script>
    <script src="//cdn.bootcss.com/nprogress/0.2.0/nprogress.min.js"></script>
    <script>
        //初始化 pjax 和 nprogress
        $(document).ready(function()
        {
            $(document).pjax('a', 'body');

            $(document).on('pjax:start', function() {
                NProgress.start();
            });
            $(document).on('pjax:end', function() {
                NProgress.done();
                self.siteBootUp();
            });
        });
    </script>
@show
<!-- 自定义js -->
@section("foot_js")
@show
</html>