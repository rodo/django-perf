from django.db import models

class IntegerTriggerField(models.IntegerField):
    
    description = "An IntegerField with trigger"
    
    def __init__(self, *args, **kwargs):
        self.aggregate_trigger = ['count']
        super(IntegerTriggerField, self).__init__(*args, **kwargs)

class trigger(models.Model):
    """
    """
    relation = models.CharField(max_length=300)
    attribute = models.IntegerField(db_index=True)
    columns = models.CharField(max_length=33)
    status  = models.IntegerField(default=0)
