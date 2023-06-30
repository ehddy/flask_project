from pybo import db
from pybo.models import Question
from datetime import datetime

for i in range(300):
    q = Question(subject=f'테스트 데이터 입니다 {i}', content='내용 무', create_date=datetime.now())
    db.session.add(q)
    db.session.commit()