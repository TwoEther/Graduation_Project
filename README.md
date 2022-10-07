# 반드시 읽어주세요

* 1단계
    - sql_query.py 반드시 실행하세요
* 2단계
    - 클론했지만 안되는 경우
        1. django-admin startproject fortravler
        2. django-admin startapp post
        3. fortravler.settings.py 수정
            1. my_settings.py 생성
            2. 다음과 같은 내용 입력
                <pre><code>
                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.mysql',
                        'NAME': '[DB name]',        # DB name
                        'USER': 'root',         # DB user
                        'PASSWORD': '[Password]', # DB password
                        'HOST': 'localhost', 
                        'PORT': '3306',
                    }
                }
                </code></pre>
            3. settings.py에 DATABASES 추가
                <pre><code>
                import my_settings
                DATABASES = my_settings.DATABASES
                </code></pre>
            4. 시간과 언어 수정
                + LANGUAGE_CODE = 'ko-kr'
                + TIME_ZONE = 'Asia/Seoul'
            5. post앱 추가
                + INSTALLED_APPS 에 'post' 추가
* 3단계
    - model 설정
        1. 다음 명령어를 입력
        <pre><code>
            python manage.py inspectdb  
        </code></pre>
        2. 모델중에 User, Post, Category를 가져옴
        3. 모델 적용
        <pre><code>
            python manage.py makemigrations
            python manage.py migrate
        </code></pre> 
    - url 설정
        1. fortraveler.urls.py 설정
            - from django.urls import path, include
            - path('', include('post.urls'))
        2. post.urls.py 설정
            - 새로 만든다
            - 다음과 같이 작성한다.
                <pre><code>
                    urlpatterns = [
                        path('', views.show_post),
                        path('login.html/', views.login),
                        path('register.html/', views.register),
                        path('login.html/register.html/', views.register),
                        path('search_page.html/', views.search_result),
                    ]
                </code></pre>

        3. post.views.py 설정
            - 다음과 같이 작성한다.
                <pre><code>
                    def [함수 이름](request):
                        return render(
                            request,
                            'post/[해당 템플릿]',
                        )
                </code></pre>    
        4. 나머지는 검색으로 알아서...

- 4단계
