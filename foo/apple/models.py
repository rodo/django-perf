from django.db import models
from foo.aggtrigg.models import IntegerTriggerField


class Apple(models.Model):
    """An apple
    """
    name = models.CharField(max_length=300)
    alpha = models.CharField(max_length=30)
    beta = models.CharField(max_length=30)
    gamma = models.CharField(max_length=30)
    delta = models.CharField(max_length=30)
    epsilon = models.CharField(max_length=30)
    zeta = models.CharField(max_length=30)

    indice = IntegerTriggerField(default=0)
    indice.aggregate_trigger=['count']

    keyid = IntegerTriggerField(default=30, db_index=True)

    bigrand = models.IntegerField(default=3000)
    tinyrand = models.IntegerField(default=3)

    idx_bigrand = models.IntegerField(default=3000, db_index=True)
    idx_tinyrand = models.IntegerField(default=3, db_index=True)

    title = models.CharField(max_length=30)
    serie = models.IntegerField(default=0)
    nbpages = models.IntegerField(default=0)

    synopsis = models.TextField(blank=True)
    intro = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    def create_trigger(self):
        """Meta datas
        """
        
