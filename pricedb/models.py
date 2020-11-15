from django.db import models

class SearchHistory(models.Model):
    '''
    This model store user's search query
    '''
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'History'

    def __str__(self):
        return self.title

class RealEstateProperty(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    price = models.IntegerField()
    history = models.ForeignKey(SearchHistory, on_delete=models.CASCADE, related_name='properties')

    class Meta:
        verbose_name_plural = 'Real Estate Properties'

    def __str__(self):
        return self.name
