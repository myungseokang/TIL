#### AWS INNOVATE 2016

DynamoDB
성능 - 일관적인 반응속도

확장성 - 각 테이블의 읽기 쓰기 대역폭 용량을 지정

DynamoDB는 확장성을 위해 내부적으로 다수의 파티션 관리

보안 - 개별 사용자 접근 제어, AWS IAM과 통합(중앙화된 관리)

Lessons Learned - {
인스턴스 기반의 NoSQL(3복제 및 운영)
데이터 증가에 따라 인스턴스 추가
인스턴스 최적화

DynamoDB - % 사용률 고려
item 사용에 따라 WCU / RCU 소모 고려

Reserved Capacity
Reserved Instance
RI는 EC2에서, RC는 DynamoDB에서 예약 구매를 통하여 비용을 절감할 수 있는 구매 방식입니다
}

[AWS Training](http://aws.amazon.com/training/)



안드로이드 테스트 자동화
{
	Android test

	Fuzz 테스트

	Fuzz 시험은 이벤트를 통해 ui 테스트 실시

	결과 리포트
	{
	성공 실패 정보
	크래쉬 로그
	디바이스 로그
	스크린샷
	성능 정보
	}
	개개 문제를 파고들어 조사 가능
	테스트 중 사용된 자원 확인 가능
	테스트에서 작성된 로그파일 확인 가능


	Jenkins 플러그인
	Devise Farm을 이용한 테스트의 자동화
	Jenkins를 이용, Jenkins CI서버와 AWS Devise Farm을 기능적으로 연계하는 플러그인
	테스트 결과 다운로드 가능


	Gradle 플러그인
	Github AWS-Labs 채널 확인
}


디바이스에 원격접속
아이폰 지원 X, 안드만 지원

웹을 통한 디바이스 접속
웹을 통해서 앱 업로드, 앱 실행 가능


Devise Farm 의 보안
모든 통신은 SSL

테스트 후 APP 삭제

AWS 저장 파일 30일 후 삭제

모든 외부 데이터 삭제

디바이스 독점 사용

각 기기는 독립적




