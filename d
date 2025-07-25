[1mdiff --git a/.idea/misc.xml b/.idea/misc.xml[m
[1mindex 6dc8354..6d060fd 100644[m
[1m--- a/.idea/misc.xml[m
[1m+++ b/.idea/misc.xml[m
[36m@@ -3,5 +3,5 @@[m
   <component name="Black">[m
     <option name="sdkName" value="Python 3.13 (xsports)" />[m
   </component>[m
[31m-  <component name="ProjectRootManager" version="2" project-jdk-name="Python 3.13 (xsports)" project-jdk-type="Python SDK" />[m
[32m+[m[32m  <component name="ProjectRootManager" version="2" project-jdk-name="Python 3.11 (xsports)" project-jdk-type="Python SDK" />[m
 </project>[m
\ No newline at end of file[m
[1mdiff --git a/.idea/xsports.iml b/.idea/xsports.iml[m
[1mindex 0af7594..81a9230 100644[m
[1m--- a/.idea/xsports.iml[m
[1m+++ b/.idea/xsports.iml[m
[36m@@ -16,7 +16,7 @@[m
     <content url="file://$MODULE_DIR$">[m
       <excludeFolder url="file://$MODULE_DIR$/.venv" />[m
     </content>[m
[31m-    <orderEntry type="jdk" jdkName="Python 3.13 (xsports)" jdkType="Python SDK" />[m
[32m+[m[32m    <orderEntry type="jdk" jdkName="Python 3.11 (xsports)" jdkType="Python SDK" />[m
     <orderEntry type="sourceFolder" forTests="false" />[m
   </component>[m
   <component name="TemplatesService">[m
[1mdiff --git a/article_module/templates/article_module/article_detail.html b/article_module/templates/article_module/article_detail.html[m
[1mindex 8c3bb87..9f32104 100644[m
[1m--- a/article_module/templates/article_module/article_detail.html[m
[1m+++ b/article_module/templates/article_module/article_detail.html[m
[36m@@ -1,6 +1,7 @@[m
 {% extends 'shared/_layout.html' %}[m
 {% load thumbnail %}[m
 {% load static %}[m
[32m+[m[32m{% load render_partial %}[m
 {% block title %}وبلاگ | {{ object.title }}{% endblock %}[m
 {% block content %}[m
     <!-- GT News-details Section Start -->[m
[36m@@ -43,7 +44,8 @@[m
                                 </div>[m
                                 <div class="gt-blog-single-comment d-flex gap-4 pt-4 pb-4">[m
                                     <div class="image">[m
[31m-                                        <img src="{% static 'xsports/img/inner-page/news-details/comment-1.jpg' %}" alt="img">[m
[32m+[m[32m                                        <img src="{% static 'xsports/img/inner-page/news-details/comment-1.jpg' %}"[m
[32m+[m[32m                                             alt="img">[m
                                     </div>[m
                                     <div class="gt-content">[m
                                         <div class="head d-flex flex-wrap gap-2 align-items-center justify-content-between">[m
[36m@@ -65,7 +67,8 @@[m
                                 </div>[m
                                 <div class="gt-blog-single-comment d-flex gap-4 pt-4 pb-4">[m
                                     <div class="image">[m
[31m-                                        <img src="{% static 'xsports/img/inner-page/news-details/comment-2.jpg' %}" alt="img">[m
[32m+[m[32m                                        <img src="{% static 'xsports/img/inner-page/news-details/comment-2.jpg' %}"[m
[32m+[m[32m                                             alt="img">[m
                                     </div>[m
                                     <div class="gt-content">[m
                                         <div class="head d-flex flex-wrap gap-2 align-items-center justify-content-between">[m
[36m@@ -116,129 +119,7 @@[m
                             </div>[m
                         </div>[m
                     </div>[m
[31m-                    <div class="col-lg-4 col-12">[m
[31m-                        <div class="gt-main-sideber sticky-style">[m
[31m-                            <div class="gt-single-sideber-widget">[m
[31m-                                <div class="gt-widget-title">[m
[31m-                                    <h3>اینجا جستجو کنید</h3>[m
[31m-                                </div>[m
[31m-                                <div class="gt-search-widget">[m
[31m-                                    <form action="#">[m
[31m-                                        <input type="text" placeholder="اینجا جستجو کنید">[m
[31m-                                        <button type="submit"><i class="fa-solid fa-magnifying-glass"></i></button>[m
[31m-                                    </form>[m
[31m-                                </div>[m
[31m-                            </div>[m
[31m-                            <div class="gt-single-sideber-widget">[m
[31m-                                <div class="gt-widget-title">[m
[31m-                                    <h3>دسته بندی ها</h3>[m
[31m-                                </div>[m
[31m-                                <ul>[m
[31m-                                    <li><a href="#">بازی لایو</a><span>(01)</span></li>[m
[31m-                                    <li><a href="#">فانتزی</a><span>(02)</span></li>[m
[31m-                                    <li><a href="#">گیمینگ</a><span>(03)</span></li>[m
[31m-                                    <li><a href="#">ایکس باکس</a><span>(04)</span></li>[m
[31m-                                    <li><a href="#">شلیک</a><span>(05)</span></li>[m
[31m-                                </ul>[m
[31m-                            </div>[m
[31m-                            <div class="gt-single-sideber-widget">[m
[31m-                                <div class="gt-widget-title">[m
[31m-                                    <h3>پست اخیر</h3>[m
[31m-                                </div>[m
[31m-                                <div class="gt-recent-post-area">[m
[31m-                                    <div class="gt-recent-items">[m
[31m-                                        <div class="gt-recent-thumb">[m
[31m-                                            <img src="{% static 'xsports/img/inner-page/news-details/post-1.jpg' %}" alt="img">[m
[31m-                                        </div>[m
[31m-                                        <div class="gt-recent-content">[m
[31m-                                            <h6>[m
[31m-                                                <a href="#">[m
[31m-                                                    یک روز در زندگی یک رویداد ورزش‌های الکترونیکی[m
[31m-                                                </a>[m
[31m-                                            </h6>[m
[31m-                                            <ul>[m
[31m-                                                <li>[m
[31m-                                                    شش اسفند 1404[m
[31m-                                                </li>[m
[31m-                                            </ul>[m
[31m-                                        </div>[m
[31m-                                    </div>[m
[31m-                                    <div class="gt-recent-items">[m
[31m-                                        <div class="gt-recent-thumb">[m
[31m-                                            <img src="{% static 'xsports/img/inner-page/news-details/post-2.jpg' %}" alt="img">[m
[31m-                                        </div>[m
[31m-                                        <div class="gt-recent-content">[m
[31m-                                            <h6>[m
[31m-                                                <a href="#">[m
[31m-                                                    شخصیت های تأثیرگذار در تاریخ<br>[m
[31m-                                                    لورم اپسیوم[m
[31m-                                                </a>[m
[31m-                                            </h6>[m
[31m-                                            <ul>[m
[31m-                                                <li>[m
[31m-                                                    شش اسفند 1404[m
[31m-                                                </li>[m
[31m-                                            </ul>[m
[31m-                                        </div>[m
[31m-                                    </div>[m
[31m-                                    <div class="gt-recent-items">[m
[31m-                                        <div class="gt-recent-thumb">[m
[31m-                                            <img src="{% static 'xsports/img/inner-page/news-details/post-3.jpg' %}" alt="img">[m
[31m-                                        </div>[m
[31m-                                        <div class="gt-recent-content">[m
[31m-                                            <h6>[m
[31m-                                                <a href="#">[m
[31m-                                                    پشت صحنه‌های مورد علاقه شما<br>[m
[31m-                                                    لورم اپسیوم[m
[31m-                                                </a>[m
[31m-                                            </h6>[m
[31m-                                            <ul>[m
[31m-                                                <li>[m
[31m-                                                    شش اسفند 1404[m
[31m-                                                </li>[m
[31m-                                            </ul>[m
[31m-                                        </div>[m
[31m-                                    </div>[m
[31m-                                </div>[m
[31m-                            </div>[m
[31m-                            <div class="gt-contact-bg bg-cover"[m
[31m-                                 style="background-image: url({% static 'xsports/img/inner-page/match-details/bg.jpg' %});">[m
[31m-                                <div class="gt-contact-content">[m
[31m-                                    <h3>نیاز به کمک دارید؟</h3>[m
[31m-                                    <p>نیاز به کمک دارید؟ با ما تماس بگیرید – پشتیبانی کامل </p>[m
[31m-                                    <div class="gt-contact-item">[m
[31m-                                        <div class="gt-icon">[m
[31m-                                            <i class="fa-solid fa-phone"></i>[m
[31m-                                        </div>[m
[31m-                                        <ul class="gt-list">[m
[31m-                                            <li><span>تماس با ما:</span></li>[m
[31m-                                            <li><a href="tel:+0094382229540">09120000000</a></li>[m
[31m-                                        </ul>[m
[31m-                                    </div>[m
[31m-                                    <div class="gt-contact-item">[m
[31m-                                        <div class="gt-icon">[m
[31m-                                            <i class="fa-regular fa-envelope"></i>[m
[31m-                                        </div>[m
[31m-                                        <ul class="gt-list">[m
[31m-                                            <li><span>ایمیل ما</span></li>[m
[31m-                                            <li><a href="#">[m
[31m-                                                infor@xridergamil.com[m
[31m-                                            </a></li>[m
[31m-                                        </ul>[m
[31m-                                    </div>[m
[31m-                                    <div class="gt-contact-item mb-0">[m
[31m-                                        <div class="gt-icon">[m
[31m-                                            <i class="fa-solid fa-location-dot"></i>[m
[31m-                                        </div>[m
[31m-                                        <ul class="gt-list">[m
[31m-                                            <li><span>لوکیشن:</span></li>[m
[31m-                                            <li>ایران استان البرز</li>[m
[31m-                                        </ul>[m
[31m-                                    </div>[m
[31m-                                </div>[m
[31m-                            </div>[m
[31m-                        </div>[m
[31m-                    </div>[m
[32m+[m[32m                    {% render_partial 'article_module.views.article_sidebar' %}[m
                 </div>[m
             </div>[m
         </div>[m
[1mdiff --git a/cheateSheet b/cheateSheet[m
[1mindex 05285d1..b5d887f 100644[m
[1m--- a/cheateSheet[m
[1m+++ b/cheateSheet[m
[36m@@ -1,5 +1,6 @@[m
 Python Start : 70[m
 Django Start : 100[m
[32m+[m[32mgit start : 4[m
 [m
 TODO :[m
 make url copy from title + persian lang[m
