from django.db import models

from common.utils import generate_unique_id
from course.models import Course, BaseModel, StatusInfo


class Payment(BaseModel, StatusInfo):
    MODEL_NAME = "결제"
    STATUS_REFERENCE = {
        "pending": 1,  # 결제 요청
        "failed": 21,  # 결제 실패
        "complete": 22,  # 결제 완료
        "refund": 3,  # 환불
    }
    amount = models.IntegerField(help_text="결제 금액")
    uid = models.CharField(max_length=16, unique=True, help_text="주문 번호 (merchant_uid)")
    description = models.CharField(max_length=256, null=True, help_text="거래 상세 내용")

    @staticmethod
    def get_uid() -> str:
        return generate_unique_id()


class Order(BaseModel):
    MODEL_NAME = "주문"
    payment = models.OneToOneField('Payment', related_name="order", on_delete=models.DO_NOTHING, null=True,
                                   help_text="결제 정보")
    Course = models.ForeignKey(Course, related_name="courses", on_delete=models.DO_NOTHING, null=True,
                               help_text="코스 정보")
