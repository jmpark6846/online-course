from django.db import models

from common.utils import get_now


class ServiceLog(models.Model):
    ref_data = models.CharField(max_length=16, help_text="참고 데이터", null=True)
    status_from = models.PositiveIntegerField(help_text="상태 변경 전", null=True)
    status_to = models.PositiveIntegerField(help_text="상태 변경 후", null=True)
    message = models.CharField(max_length=256, help_text="로그 메세지")


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text="생성 일시")
    updated_at = models.DateTimeField(auto_now=True, help_text="수정 일시")
    deleted_at = models.DateTimeField(default=None, null=True, help_text="삭제 일시")

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        """완전히 데이터를 제거하는 대신 삭제 플래그만 삽입하여 삭제를 마킹합니다."""
        self.deleted_at = get_now()
        super(BaseModel, self).save()


class StatusInfo(models.Model):
    STATUS_REFERENCE = {}
    status = models.PositiveIntegerField(null=True, help_text="상태")

    class Meta:
        abstract = True

    def update_status(self, new_status, msg, ref_data=None):
        ServiceLog.objects.create(
            status_from=self.status,
            status_to=new_status,
            message=msg,
            ref_data=ref_data
        )
        self.status = new_status
        self.save()


# class Chapter(BaseModel):
#     pass
#
#
# class Page(BaseModel):
#     pass


class Course(BaseModel, StatusInfo):
    MODEL_NAME="코스"
    STATUS_REFERENCE = {
        'created':1,
        'open':2,
        'finished':3
    }

    title = models.CharField(max_length=128, help_text="제목")
    base_price = models.IntegerField(default=0, help_text="기본 가격")
    # chapters = models.ForeignKey(Chapter, on_delete=models.DO_NOTHING, null=True)

    def calculate_price(self):
        pass