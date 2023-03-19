from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    # タグの名前は100文字
    name = models.CharField(max_length=100)
    # 誰が新規で作成したのかをわかるようにuserを追加
    user = models.ForeignKey(
        User,
        # 選択しているuserが消えた場合は、自動で消えるように
        on_delete=models.CASCADE,
    )

    # 戻り値を指定-タグ名を返す
    def __str__(self):
        return self.name


class Blog(models.Model):
    # どのuserが作成したのかをわかるように
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=300)
    content = models.TextField()
    # タグと関連付ける
    tags = models.ManyToManyField('Tag')
    created_at = models.DateTimeField(auto_now_add=True)

    # 戻り値を指定-記事名を返す
    def __str__(self):
        return self.title
