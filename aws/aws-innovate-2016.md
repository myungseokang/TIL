#### AWS INNOVATE 2016

DynamoDB
성능 - 일관적인 반응속도

확장성 - 각 테이블의 읽기 쓰기 대역폭 용량을 지정

DynamoDB는 확장성을 위해 내부적으로 다수의 파티션 관리

보안 - 개별 사용자 접근 제어, AWS IAM과 통합(중앙화된 관리)

Lessons Learned - 인스턴스 기반의 NoSQL(3복제 및 운영)
데이터 증가에 따라 인스턴스 추가
인스턴스 최적화

DynamoDB - % 사용률 고려
item 사용에 따라 WCU / RCU 소모 고려

Reserved Capacity
Reserved Instance
RI는 EC2에서, RC는 DynamoDB에서 예약 구매를 통하여 비용을 절감할 수 있는 구매 방식입니다
