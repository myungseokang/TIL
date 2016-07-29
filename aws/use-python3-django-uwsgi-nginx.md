## EC2에서 Nginx+uWSGI로 python3로 작성한 django 앱 배포하기 
> Python 3.x 버전 기준

매우 많이 참고한 곳
[유유자적 블로그](http://jeongyoungho80.blogspot.kr/2015/06/1404-django-uwsgi-nginx.html)
[nerogit.github.io](http://nerogit.github.io/2016/02/23/python3-django-nginx-uwsgi-deploy/)

OS     : Ubuntu 14.04
Python : 3.4.3(default python version에 virtualenv 만 사용)
Nginx  : 1.4.6
uWSGI  : 2.0.13.1
Django : 1.10.rc1


```shell
$ sudo apt-get update
$ sudo apt-get install python3-pip
$ sudo pip3 install virtualenv virtualenvwrapper
```

sudo apt-get 업데이트 한번 진행해주고
python3를 사용하기에 python3-pip를 설치해줍니다.
가상환경 관리를 위한 virtualenv+virtualenvwrapper도 사용해줍니다. + pyenv로 python 버전 관리를 할 생각입니다.

```shell
$ echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3"
$ echo "export WORKON_HOME=~/.virtualenvs" >> ~/.bashrc
$ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
$ source ~/.bashrc
```
그리고 virtualenvwrapper와 virtualenv 관한 설정을 bashrc에 넣어줍니다.

```shell
user@hostname:~$ mkvirtualenv ENV_NAME
(ENV_NAME)user@hostname:~$
(ENV_NAME)user@hostname:~$ pip install -r requirements.txt # or pip install --pre django
(ENV_NAME)user@hostname:~$ django-admin.py startproject PROJECT_NAME
(ENV_NAME)user@hostname:~$ cd ~/PROJECT_NAME
(ENV_NAME)user@hostname:~/PROJECT_NAME$ python manage.py migrate
(ENV_NAME)user@hostname:~/PROJECT_NAME$ python manage.py createsuperuser
(ENV_NAME)user@hostname:~/PROJECT_NAME$ python manage.py collectstatic
(ENV_NAME)user@hostname:~/PROJECT_NAME$ python manage runserver 0.0.0.0:8000
```
collectstatic 명령어 쓸 때, settings.py에 static_root는 설정되어 있다고 가정함
마지막으로 runserver로 확인함

잘 실행된다면 uwsgi 설정쪽으로 넘어감
```shell
$ sudo apt-get install python-dev
$ sudo pip3 install uwsgi # sudo를 이용한 전체 시스템에 설치
$ uwsgi --http :8000 --home /home/user/.virtualenvs/ENV_NAME --chdir /home/user/PROJECT_NAME -w PROJECT_NAME.wsgi
```
이 때 AWS security group에 8000 번 포트가 열려있는지 확인해야함


uwsgi emperor 모드로 실행해야함
default 디렉토리 삭제해야함

