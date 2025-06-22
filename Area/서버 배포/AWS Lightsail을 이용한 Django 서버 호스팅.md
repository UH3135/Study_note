네, AWS Lightsail을 이용하여 Django 프로젝트를 호스팅하는 방법을 단계별로 안내해 드리겠습니다.

AWS Lightsail에서 Django 프로젝트를 호스팅하는 가장 일반적이고 안정적인 방법은 **Ubuntu/Linux 서버**를 생성한 뒤, **Nginx**를 웹 서버로, **Gunicorn**을 애플리케이션 서버로 사용하는 것입니다.

---

### ## 🚀 전체 과정 요약

1. **Lightsail 인스턴스 생성**: Ubuntu 운영체제가 설치된 가상 서버를 생성합니다.
2. **서버 초기 설정**: 서버에 접속하여 필요한 기본 패키지(Python, pip 등)를 설치하고 시스템을 업데이트합니다.
3. **Django 프로젝트 준비**: 서버에 내 Django 프로젝트 코드를 가져오고, 가상 환경을 설정한 뒤 필요한 라이브러리를 설치합니다.
4. **Gunicorn 설정**: Django 애플리케이션을 실행할 WSGI 서버(Gunicorn)를 설정하고 시스템 서비스로 등록하여 서버가 재시작되어도 자동으로 실행되게 합니다.
5. **Nginx 설정**: 외부의 HTTP 요청을 받아 Gunicorn으로 전달해주는 리버스 프록시(Reverse Proxy) 역할을 하도록 Nginx를 설정합니다. 정적 파일(static files)도 Nginx가 직접 처리하도록 설정합니다.
6. **방화벽 및 도메인/SSL 설정**: Lightsail 방화벽에서 HTTP/HTTPS 포트를 열고, 도메인을 연결한 뒤 SSL 인증서(HTTPS)를 적용하여 보안을 강화합니다.

---

### ## 🔧 1단계: AWS Lightsail 인스턴스 생성

1. AWS Lightsail 콘솔에 접속합니다.
2. **'인스턴스 생성'** 버튼을 클릭합니다.
3. **인스턴스 위치**: 사용자와 가장 가까운 리전(예: 서울)을 선택합니다.
4. **플랫폼 선택**: **'Linux/Unix'**를 선택합니다.
5. **블루프린트 선택**: **'OS 전용'** 탭에서 **'Ubuntu 22.04 LTS'** (또는 최신 LTS 버전)를 선택합니다.
6. **SSH 키 페어**: 기본 키를 사용하거나 새로 생성합니다. 이 키는 서버에 접속할 때 필요하므로 안전하게 보관해야 합니다.
7. **인스턴스 플랜 선택**: 프로젝트 규모에 맞는 사양을 선택합니다. 처음에는 가장 저렴한 플랜으로 시작해도 충분합니다.
8. 인스턴스 이름을 지정하고 **'인스턴스 생성'**을 클릭합니다.

잠시 후 인스턴스가 생성되면 고정 IP를 할당받는 것이 좋습니다. **'네트워킹'** 탭에서 **'고정 IP 생성'**을 클릭하여 방금 만든 인스턴스에 연결하세요. 이렇게 하면 인스턴스를 재부팅해도 IP 주소가 변경되지 않습니다.

---

### ## 🔧 2단계: 서버 초기 설정 및 접속

1. Lightsail 콘솔에서 생성된 인스턴스 옆의 주황색 터미널 아이콘을 클릭하거나, 다운로드한 SSH 키를 이용해 개인 터미널에서 접속합니다.
    
    Bash
    
    ```
    # <Your-Key.pem> 파일에 올바른 권한 부여
    chmod 400 <Your-Key.pem>
    
    # SSH 접속 (고정 IP 주소 사용)
    ssh -i <Your-Key.pem> ubuntu@<Your-Instance-Public-IP>
    ```
    
2. 서버에 접속한 후, 시스템 패키지를 최신 상태로 업데이트하고 필수 도구를 설치합니다.
    
    Bash
    
    ```
    sudo apt update
    sudo apt upgrade -y
    sudo apt install python3-pip python3-dev python3-venv nginx -y
    ```
    

---

### ## 🔧 3단계: Django 프로젝트 준비

1. **프로젝트 코드 가져오기** (Git 사용을 권장)
    
    Bash
    
    ```
    # Git 설치
    sudo apt install git -y
    
    # 프로젝트 클론
    git clone https://github.com/your-username/your-django-project.git
    cd your-django-project
    ```
    
2. **가상환경 생성 및 활성화**
    
    Bash
    
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
    
3. 프로젝트 라이브러리 설치
    
    프로젝트에 requirements.txt 파일이 있다고 가정합니다. Gunicorn은 프로덕션 환경에서 Django를 실행하기 위해 필수적입니다.
    
    Bash
    
    ```
    pip install -r requirements.txt
    pip install gunicorn
    ```
    
    - **참고**: PostgreSQL 데이터베이스를 사용한다면 `psycopg2-binary` 라이브러리도 설치해야 합니다.
4. settings.py 설정 변경
    
    프로덕션 환경에 맞게 settings.py 파일을 수정해야 합니다.
    
    Python
    
    ```
    # myproject/settings.py
    
    # 보안 경고를 피하기 위해 개발 환경과 다른 강력한 키로 교체
    SECRET_KEY = 'your-super-secret-key'
    
    # 프로덕션 환경에서는 반드시 False로 설정
    DEBUG = False
    
    # 서버의 고정 IP 주소와 연결할 도메인 주소를 추가
    ALLOWED_HOSTS = ['<Your-Instance-Public-IP>', 'yourdomain.com']
    
    # 정적 파일(CSS, JS, 이미지)을 한 곳에 모을 경로 설정
    STATIC_ROOT = BASE_DIR / 'static'
    ```
    
5. **데이터베이스 마이그레이션 및 정적 파일 수집**
    
    Bash
    
    ```
    python manage.py migrate
    python manage.py collectstatic
    ```
    
    `collectstatic` 명령을 실행하면 `settings.py`에 정의된 `STATIC_ROOT` 경로(이 예에서는 `static` 폴더)에 모든 정적 파일이 복사됩니다.
    

---

### ## 🔧 4단계: Gunicorn 설정 및 서비스 등록

Gunicorn이 서버 부팅 시 자동으로 실행되도록 `systemd` 서비스를 설정합니다.

1. **Gunicorn 서비스 파일 생성**
    
    Bash
    
    ```
    sudo nano /etc/systemd/system/gunicorn.service
    ```
    
2. 서비스 파일 내용 작성
    
    아래 내용을 붙여넣고, [Your-Username]과 [Your-Project-Directory]를 실제 값으로 수정하세요.
    
````
[Unit]

Description=gunicorn daemon

After=network.target


[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/your-django-project
ExecStart=/home/ubuntu/your-django-project/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/home/ubuntu/your-django-project/myproject.sock \
          myproject.wsgi:application

[Install]
WantedBy=multi-user.target
```
* `WorkingDirectory`: `manage.py` 파일이 있는 프로젝트 루트 디렉토리
* `ExecStart`: Gunicorn 실행 경로와 설정. `myproject.wsgi:application`에서 `myproject`는 `wsgi.py` 파일이 위치한 디렉토리 이름입니다.
* `--bind unix:/path/to/socket`: Nginx와 통신하기 위해 유닉스 소켓을 사용합니다.
````

3. **Gunicorn 서비스 시작 및 활성화**
    
    Bash
    
    ```
    sudo systemctl start gunicorn
    sudo systemctl enable gunicorn # 재부팅 시 자동 시작 설정
    
    # 상태 확인 (active (running)이 표시되어야 함)
    sudo systemctl status gunicorn
    ```
    

---

### ## 🔧 5단계: Nginx 설정 (리버스 프록시)

Nginx가 외부 요청을 받아 Gunicorn 소켓으로 전달하도록 설정합니다.

1. **Nginx 설정 파일 생성**
    
    Bash
    
    ```
    sudo nano /etc/nginx/sites-available/myproject
    ```
    
2. 설정 파일 내용 작성
    
    아래 내용을 붙여넣고 yourdomain.com과 프로젝트 경로를 수정하세요.
    
    Nginx
    
    ```
    server {
        listen 80;
        server_name <Your-Instance-Public-IP> yourdomain.com;
    
        location = /favicon.ico { access_log off; log_not_found off; }
    
        location /static/ {
            root /home/ubuntu/your-django-project;
        }
    
        location / {
            include proxy_params;
            proxy_pass http://unix:/home/ubuntu/your-django-project/myproject.sock;
        }
    }
    ```
    
    - `server_name`: 서버 IP와 연결할 도메인을 적습니다.
    - `location /static/`: 정적 파일 요청은 Gunicorn으로 보내지 않고, Nginx가 직접 `STATIC_ROOT`에서 처리하도록 합니다.
    - `location /`: 나머지 모든 요청은 Gunicorn 소켓으로 전달합니다.
3. **설정 파일 활성화 및 Nginx 재시작**
    
    Bash
    
    ```
    # 생성한 설정 파일을 sites-enabled에 링크
    sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled/
    
    # Nginx 설정 문법 오류 확인
    sudo nginx -t
    
    # Nginx 재시작
    sudo systemctl restart nginx
    ```
    

---

### ## 🔒 6단계: 방화벽, 도메인 및 SSL 설정

1. **Lightsail 방화벽 설정**
    
    - Lightsail 인스턴스 관리 페이지의 **'네트워킹'** 탭으로 이동합니다.
    - **'방화벽'** 섹션에서 **'규칙 추가'**를 클릭합니다.
    - `HTTP` (포트 80)와 `HTTPS` (포트 443) 규칙을 추가하여 모든 IP(`0.0.0.0/0`)에서 접속할 수 있도록 허용합니다.
2. **도메인 연결** (선택 사항이지만 권장)
    
    - 보유한 도메인의 DNS 설정에서 A 레코드를 Lightsail 인스턴스의 **고정 IP** 주소로 지정합니다.
3. SSL 인증서 적용 (HTTPS)
    
    Let's Encrypt의 Certbot을 사용하면 무료로 SSL 인증서를 발급받고 자동으로 Nginx에 설정할 수 있습니다.
    
    Bash
    
    ```
    # Certbot 설치
    sudo apt install certbot python3-certbot-nginx -y
    
    # Certbot 실행 (yourdomain.com을 실제 도메인으로 변경)
    sudo certbot --nginx -d yourdomain.com
    ```
    
    Certbot이 몇 가지 질문을 합니다 (이메일 주소, 서비스 약관 동의 등). 마지막에 HTTP 요청을 HTTPS로 리디렉션할지 물으면 2번을 선택하는 것이 좋습니다.
    

이제 웹 브라우저에서 `http://<Your-Instance-Public-IP>` 또는 `https://yourdomain.com` 으로 접속하면 성공적으로 배포된 Django 프로젝트를 확인할 수 있습니다. ✅