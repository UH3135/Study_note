### 웹서버 컴퓨팅
1. 웹서비스 구현
2. django 사용
3. 자율 프로젝트
4. Server
HTTP
- request
	- get
	- put
- response
database - server의 연동

### DRF
- 장고를 클래스화
#### model
- DB model
#### Template
- HTML이라고 생각
- 서버가 원하는 데이터 (form)을 요청
- 렌더링: 웹사이트에서 화면을 띄우는 것
#### View
- 메인 컨트롤
- DB와 클라이언트를 연결
- Route
	- DNS 관련 설정
	- URL 핸들링 -> 데이터 전송 or 구체적인 방법
	- 네트워크에서 최적 경로를 찾아서 전달해주는 방법
- 함수 기반 -> 클래스 기반

### 평가 방식
절대 + 상대
중간: 실기+시험
기말: 실기+시험
학기말 AD 프로젝트 - aws 아카데미를 활용하여 직접 배포
과제 4개
AD 프로젝트 결과물 출품

#### Django 보안
1. CSRF, XSS 방지

프론트는 이벤트 리스너로 확인 -> 이벤트 핸들러로 (이 이벤트 핸들러가 서버)

DRY, 명시적