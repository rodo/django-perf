from django.db import models
from cte_tree.models import CTENode
from mptt.models import MPTTModel, TreeForeignKey

# ['DoesNotExist', 'Meta', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', u'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__unicode__', '__weakref__', '_base_manager', '_cte_node_children', '_cte_node_delete_method', '_cte_node_depth', '_cte_node_ordering', '_cte_node_parent', '_cte_node_parent_attname', '_cte_node_path', '_cte_node_primary_key_type', '_cte_node_table', '_cte_node_traversal', '_default_manager', '_deferred', '_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks', '_save_parents', '_save_table', '_set_pk_val', '_state',

# 'ancestors', 'as_tree', 'attribute_path',
# 'catid', 'children', 'clean', 'clean_fields',
# 'date_error_message', 'delete', 'depth', 'descendants',
# 'full_clean', 'id',
# 'is_ancestor_of', 'is_branch', 'is_child_of', 'is_descendant_of', 'is_leaf', 'is_parent_of', 'is_sibling_of',
# 'move', 'name', 'objects', 'ordering', 'parent', 'parent_id',
# 'path', 'pk', 'prepare_database_save',
# 'root', 'save', 'save_base', 'serializable_value', 'siblings', 'unique_error_message', 'validate_unique']


class Category(CTENode):
    """
    """
    name = models.CharField(max_length=50)
    catid = models.IntegerField()

    def __unicode__(self):
        return '%s @ %s' % (self.name, self.depth)


class CategoryCatidCount(models.Model):
    catid = models.IntegerField()
    counter = models.IntegerField()

    class Meta:
        db_table = 'manga_category__catid_counter'
        managed = False
    

class Genre(MPTTModel):
    name = models.CharField(max_length=50)
    catid = models.IntegerField()
    parent = TreeForeignKey('self',
                            null=True,
                            blank=True,
                            related_name='children')


# ['DoesNotExist', 'Meta', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', u'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_base_manager', '_default_manager', '_deferred', '_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_is_saved', '_meta', '_mptt_cached_fields', '_mptt_is_tracking', '_mptt_meta', '_mptt_start_tracking', '_mptt_stop_tracking', '_mptt_track_tree_insertions', '_mptt_track_tree_modified', '_mptt_tracking_base', '_mptt_updates_enabled', '_mpttfield', '_perform_date_checks', '_perform_unique_checks', '_save_parents', '_save_table', '_set_mptt_updates_enabled', '_set_pk_val', '_state', '_threadlocal', '_tree_manager', 'catid', 'children', 'clean', 'clean_fields', 'date_error_message', 'delete', 'full_clean', 'get_ancestors', 'get_children', 'get_descendant_count', 'get_descendants', 'get_leafnodes', 'get_level', 'get_next_sibling', 'get_previous_sibling', 'get_root', 'get_siblings', 'id', 'insert_at', 'is_ancestor_of', 'is_child_node', 'is_descendant_of', 'is_leaf_node', 'is_root_node', 'level', 'lft', 'move_to', 'name', 'objects', 'parent', 'parent_id', 'pk', 'prepare_database_save', 'rght', 'save', 'save_base', 'serializable_value', 'tree_id', 'unique_error_message', 'validate_unique']
