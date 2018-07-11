1. Check django version: django-admin --version

2. Start new project: django-admin startproject wordcount

3. Start server : python manage.py runserver

4. Creating new project : django-admin startproject portfolio

5. Create gitignore file:
    1. git init
    2. git config --global user.name "John Doe"
    3. git config --global user.email johndoe@example.com
    4. create '.gitignore' file in the root of project folder
    5. open 'gitignore.io' website and type 'django'
    6. copy generated code info '.gitignore' file, /media, /static
    7. git add -A
    8. git commit -m "Our first"

6. Bind repository to github:
    1. Create ssh key: ssh-keygen
    2. Copy key: cat ~/.ssh/id_rsa.pub
    3. Paste key on github: add ssh and gpg keys
    4. Type into terminal: git remote add origin git@github.com:timfirst/portfolio.git
    5. git push origin -u master

7. Create django-app:
    1. python manage.py startapp blog
    2. python manage.py startapp jobs
    3. git commit -m "Add jobs and blog"

6. Models:
    1. Open 'models.py' inside jobs:
        class Job(models.Model):
            image = models.ImageField(upload_to='images/')
            summary = models.CharField(max_length=200)

    2. go to portfolio -> settings :
        1. add item to INSTALLED_APPS: 'jobs.apps.JobsConfig'

        2. Create variables to the bottom:
            MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
            MEDIA_URL = '/media/'

    3. Update database:
        1. install Pillow
        2. python manage.py makemigrations
        3. python manage.py migrate

7. Interact with job model:
    1. Create superuser: python manage.py createsuperuser or winpty python manage.py createsuperuser

    2. runserver and try to login: localhost:8000/login

    3. go to jobs -> admin.py:
        from .models import Job
        admin.site.register(Job)

    4. Add path to open images:
        1. go to portfolio -> urls.py -> urlpatterns:
            after ']' + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
            from django.conf import settings
            from django.conf.urls.static import static

    5. runserver, login, add new job

8. Postgresql:
    1. install Postgresql
    2. show users: du
    3. Set password: \password postgres
    4. Create db: CREATE DATABASE portfoliodb;
    5. Connect to portfoliodb - go to portfolio -> settings -> DATABASES:
        change engine: 'django.db.backends.postgresql'
        change name: 'portfoliodb'
        'USER': 'postgres'
        'PASSWORD':'PASSWORD'
        'HOST':'localhost'
        'PORT':'4532'
    6. pip install psycopg2
    7. migrate
    8. create new superuser
    9. login

9. Create homepage:
    1. go to jobs -> views.py:
        def home(request):
            return render(request, 'jobs/home.html')
    2. go to portfolio -> urls.py -> urlpatterns:
        path('', jobs.views.home, name='home'),
    3. import jobs.views
    4. create folder 'templates' into 'jobs'
    5. create folder 'jobs' into 'templates'
    6. into jobs create 'home.html'
    7. runserver

10. Create blog page:
    1. Create a Blog model:
        1. blog -> models.py:
            class Blog(models.Model):
                title = models.CharField(max_length=255)
                pub_date = models.DateTimeField()
                body = models.TextField()
                image = models.ImageField(upload_to='images/')

        2. portfolio -> settings.py -> installed_apps:
            'blog.apps.BlogConfig'
    2. Add the blog app to the settings:
        1. python manage.py makemigrations

    3. python manage.py migrate

    4. add to the admin - blog->admin :
        admin.site.register(Blog)

11. Integrate bootstrap:
    1. getbootstrap.com -> examples -> album
    2. copy and paste page source code into jobs -> templates -> jobs -> home.html
    3. bootstrap.com -> bootstrap cdn: copy ccs only link into home.html
    4. delete custom style album.css
    5. bootstrap.com -> bootstrap cdn: copy js, popper.js, jquery links into home.html
    6. search navbar on getbootstrap.com, copy code of navbar, paste into header in home.html
    7. change home.html:
        1. nav: navbar-dark, bg-dark
        2. navbar-nav add ml-auto
        3. change nav-links
        4. change all texts
        5. <a href="mailto:test@mail.com">Email Me</a>
        6. footer:
            1. delete all in container: .text-center
            2. <p>CopyRight Test Website {% now "Y" %}

12. Get data from db:
    1. From home.html delete all jobs except one
    2. Inside job card delete all except image and text
    3. inside jobs -> views.py:
        1. from .models import Job
        2. def home(request):
            jobs = Job.objects
            return render(request, 'jobs/home.html', {'jobs':jobs})

        3. home.html -> row:
            {% for job in jobs.all %}
            <div class="col-md-4">
                <div class="card mb-4 box-shadow">
            <img class="card-img-top" src="{{ job.image }}"/>
                    <div class="card-body">
                        <p class="card-text">{{ job.summary }}</p>
                    </div>
                </div>
            </div>
            {% endfor %}

13. Working with blog:
    1. Add urls:
        add to portfolio -> urls.py -> urlpatterns:
            path('blog/', include('blog.urls')),
    2. create urls.py into blog:
        from django.urls import path
        import . import views

        urlpatterns = [
            path('', views.allblogs, name='allblogs')
        ]

    3. blog -> views.py:
        from django.shortcuts import render
        def allblogs(request):
            return render(request, 'blog/allblogs.html')

    4. into blog create file templates/blog/allblogs.html
    5. copy all from jobs -> home.html in blog -> allblogs.html
    6. code blog -> allblogs.html
    7. Add id of each post in the url:
        add in blog -> urls.py -> urlpatterns:
            path('<int:blog_id>/', views.detail, name='detail')

        blog -> views.py:
            from django.shortcuts import get_object_or_404
            def detail(request, blog_id):
                detailblog = get_object_404(Blog, pk=blog_id)
                return render(request, 'blog/detail.html', {'blog':detailblog})

    8. create file /blog/templates/blog/detail.html:
        {{blog.title}}

14. Working with static files:
    1. Copy one image in folder portfolio/static
    2. portfolio -> settings.py:
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'portfolio/static/')
        ]
        STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    3. python manage.py collectstatic
    4. use static file:
        jobs -> templates -> jobs -> home.html:
            add in header: {% load staticfiles %}
            href: {% static 'resume.pdf '%}
15. paste url: href="{% url 'home' %}"
16. reference to blog: href="{% url 'detail' blog.id %}"

17. post website to the internet lesson 45-51:
18. Create requirements.txt: pip freeze > requirements.txt

# *** Clone website *** #
1. Create project
2. connect to postgesql:
    1. product -> settings.py -> DATABASES:
        DATABASES = {
            'default':{
                'ENGINE': 'django.db.backends.postgresql',
                'NAME':'productdb',
                'USER':'postgres',
                'PASSWORD':'postgres123',
                'HOST':'localhost',
                'PORT':'5432'
            }
        }
3. Add two apps: products and accounts
4. Add home page:
    1. product -> urls.py add:
        from products import views

        urlpatterns = [
            path('', views.home, name='home'),
        ]

    2. products -> views add:
        def home(request):
            return render(request, 'products/home.html')

    3. Create file products/templates/products/home.html:
        {% extends 'base.html' %}

        {% block content%}

        <h1>Home!</h1>

        {% endblock %}
    4. product -> settings -> INSTALLED_APPS add:
        'products.apps.ProductsConfig',
        'accounts.apps.AccountsConfig',
    5. runserver and check
    6. Create file product/templates/base.html:
        <h1>Hello this is the topics</h1>

        {% block content %}
        {% endblock %}

        <h1>Hello this is the bottom</h1>
    7. product -> settings.py -> TEMPLATES -> 'DIRS' add:
        'DIRS':['product/templates'],

    8. Add logo:
        1. download and save icon from flaticon.com to folder product -> static
        2. <img src="{% static 'logo.png'%}" class="d-inline-block align-top">
        3. product -> settings.py:
            STATICFILES_DIRS = [
                os.path.join(BASE_DIR, 'product/static/')
            ]

            STATIC_ROOT = os.path.join(BASE_DIR, 'static')
            STATIC_URL = '/static/'
        4. python manage.py collectstatic
        5. add {% load staticfiles %} to head in base.html
        6. run and check

    9. Authentication:
        1. Add url patterns:
            1. Add to product -> urls.py -> urlpatterns:
                path('accounts/', include('accounts.urls')),
            2. create file accounts -> urls.py:
                from django.urls import path
                from . import views

                urlpatterns = [
                    path('signup', views.signup, name='signup'),
                    path('login', views.login, name='login'),
                    path('logout', views.logout, name='logout'),
                ]
            3. accounts -> views.py:
                from django.shortcuts import render

                def signup(request):
                    return render(request, 'accounts/signup.html')

                def login(request):
                    return render(request, 'accounts/login.html')

                def logout(request):
                    # TODO  need to route to homepage
                    # and don't forget logout
                    return render(request, 'accounts/signup.html')
            4. Create files accounts/templates/accounts/signup.html and accounts/templates/accounts/login.html

Download icons: useiconic.com
