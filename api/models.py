from django.db import models

# 投資家モデル
class Investor(models.Model):
    RISK_CHOICES = [
        ('High', '高'),
        ('Medium', '中'),
        ('Low', '低'),
    ]
    EXPERIENCE_CHOICES = [
        ('Beginner', '初心者'),
        ('Intermediate', '中級者'),
        ('Advanced', '上級者'),
    ]

    name = models.CharField(max_length=100)
    risk_tolerance = models.CharField(max_length=10, choices=RISK_CHOICES)
    experience = models.CharField(max_length=15, choices=EXPERIENCE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# 提案モデル
class Proposal(models.Model):
    investor = models.ForeignKey(Investor, related_name='proposals', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# チャットモデル
class ChatMessage(models.Model):
    investor = models.ForeignKey(Investor, related_name='messages', on_delete=models.CASCADE)
    sender = models.CharField(max_length=50)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.message[:20]}'
