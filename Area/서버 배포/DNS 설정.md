### ✅ 도메인 적용을 위한 단계별 체크리스트

#### 1단계: DNS 설정 확인 (도메인이 서버를 가리키게 하기)

가장 먼저, 구매한 도메인 주소로 접속했을 때 내 Lightsail 서버의 IP 주소를 찾아올 수 있도록 해야 합니다. 이 과정은 이전 질문에서 답변드린 내용입니다.

1. **A 레코드 설정**: 도메인을 구매한 곳(가비아 등)이나 Cloudflare의 DNS 설정 메뉴로 갑니다.
2. 아래와 같이 **A 레코드**가 내 Lightsail **고정 IP 주소**로 설정되어 있는지 확인합니다.

|   |   |   |
|---|---|---|
|**종류(Type)**|**호스트/이름(Host/Name)**|**값/내용(Value)**|
|**A**|`@`|내 Lightsail 고정 IP 주소|
|**A**|`www`|내 Lightsail 고정 IP 주소|

3. **확인**: 터미널에서 아래 명령어를 실행하여 IP 주소가 잘 연결되었는지 확인합니다.
    
    Bash
    
    ```
    nslookup yournewdomain.com
    ```
    
    결과에 내 Lightsail IP 주소가 표시되어야 다음 단계로 진행할 수 있습니다.

#### 2단계: Django `settings.py` 업데이트 (Django가 새 주소 허용하기)

Django는 보안을 위해 `ALLOWED_HOSTS` 목록에 있는 주소로의 접속만 허용합니다. 여기에 새로운 도메인을 추가해야 합니다.

1. 서버의 `settings.py` 파일을 엽니다.
    
    Bash
    
    ```
    nano ~/BeanBrief-AI/config/settings.py  # 실제 경로에 맞게 수정
    ```
    
2. `ALLOWED_HOSTS` 리스트에 새로 구매한 도메인(www가 있는 것과 없는 것 둘 다)을 추가합니다.
    
    Python
    
    ```
    # 수정 전 예시
    # ALLOWED_HOSTS = ['43.202.254.208']
    
    # 수정 후 예시
    ALLOWED_HOSTS = ['43.202.254.208', 'yournewdomain.com', 'www.yournewdomain.com']
    ```
    
3. 파일을 저장한 뒤, **반드시 Gunicorn을 재시작**하여 변경된 설정을 적용합니다.
    
    Bash
    
    ```
    sudo systemctl restart gunicorn
    ```
    

#### 3단계: Nginx 설정 업데이트 (웹서버가 새 주소 인지하기)

Nginx에게 "이제부터 이 도메인 주소로 들어오는 요청은 네가 처리해야 해"라고 알려주어야 합니다.

1. 서버의 Nginx 설정 파일을 엽니다.
    
    Bash
    
    ```
    sudo nano /etc/nginx/sites-available/myproject  # 'myproject'는 본인의 설정 파일명
    ```
    
2. `server_name` 지시자에 새로운 도메인을 추가합니다. 보통 기존의 IP 주소는 지우고 도메인만 남겨두는 것이 깔끔합니다.
    
    Nginx
    
    ```
    # 수정 전 예시
    # server_name 43.202.254.208;
    
    # 수정 후 예시
    server_name yournewdomain.com www.yournewdomain.com;
    ```
    
3. 파일을 저장한 뒤, Nginx 설정에 문법 오류가 없는지 확인하고 재시작합니다.
    
    Bash
    
    ```
    # 설정 문법 검사 (필수!)
    sudo nginx -t
    
    # Nginx 재시작
    sudo systemctl restart nginx
    ```
    

이 단계까지 마치면, `http://yournewdomain.com`으로 접속했을 때 사이트가 보여야 합니다.

#### 4단계: HTTPS 적용하기 (SSL 인증서 발급 - 무료)

이제 사용자들이 안전하게 사이트를 이용할 수 있도록, 무료 SSL 인증서(Let's Encrypt)를 발급받아 `https://` 접속을 설정합니다. `Certbot` 이라는 도구를 사용하면 매우 간단합니다.

1. **Certbot 설치** (이미 설치했다면 생략 가능)
    
    Bash
    
    ```
    sudo apt update
    sudo apt install certbot python3-certbot-nginx -y
    ```
    
2. Certbot 실행하여 인증서 발급 및 Nginx 자동 설정
    
    아래 명령어에서 yournewdomain.com 부분을 실제 도메인으로 바꿔 실행합니다.
    
    Bash
    
    ```
    sudo certbot --nginx -d yournewdomain.com -d www.yournewdomain.com
    ```
    
3. **Certbot 질문에 답변**
    
    - 이메일 주소를 입력하라는 메시지가 나옵니다. (인증서 만료 시 알림용)
    - 서비스 이용 약관에 동의(A)합니다.
    - 마지막으로 **HTTP로 들어온 접속을 HTTPS로 자동 리디렉션할지** 묻는 질문이 나옵니다. **2번(Redirect)을 선택**하는 것을 강력히 추천합니다.
4. **Lightsail 방화벽 확인**
    
    - Lightsail 인스턴스의 [네트워킹] 탭으로 가서, 방화벽 규칙에 `HTTPS` (포트 443)가 추가되어 있는지 확인하고 없다면 추가해 주세요.

모든 과정이 끝나면 이제 `https://yournewdomain.com`으로 접속했을 때 주소창에 자물쇠 아이콘이 표시되며 안전하게 사이트가 열리는 것을 확인할 수 있습니다.
