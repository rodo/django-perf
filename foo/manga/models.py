from django.db import models
from cte_tree.models import CTENode
from mptt.models import MPTTModel, TreeForeignKey

class Category(CTENode):
    """
    """
    name = models.CharField(max_length=300)

    def __unicode__(self):
        return '%s @ %s' % (self.name, self.depth)



class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
