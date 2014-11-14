import time

def print_console(name, count, delta):
    print "{:<15} {} time {} seconds".format(name, count, delta)
        
def regular_delete(code, model):
    """Delete books with an evaluated QuerySet
    """
    start = time.time()
    
    books = model.objects.filter(code=code)
    count = books.count()

    to_be_deleted_ref_list = [doc.id for doc in books]

    model.objects.filter(pk__in=to_be_deleted_ref_list).delete()

    delta = time.time() - start
    return (count, delta)

def del_delete(code, model):
    """Delete books directly
    """
    start = time.time()

    books = model.objects.filter(code=code)
    count = books.count()

    model.objects.filter(code=code).delete()

    delta = time.time() - start
    return (count, delta)

def list_delete(code, model):
    """Delete books with a non evaluated QuerySet
    """

    model.objects.raw("SELECT 'list_delete'") 
    start = time.time()

    books = model.objects.filter(code=code)
    count = books.count()

    book_list = model.objects.filter(code=code)

    model.objects.filter(pk__in=book_list).delete()

    delta = time.time() - start

    return (count, delta)

def raw_delete(code, model):
    """Delete books with raw  commands
    """
    start = time.time()

    books = model.objects.filter(code=code)
    count = books.count()

    model.objects.raw("DELETE FROM tuna_editor_books WHERE book_id IN (SELECT id FROM tuna_book WHERE code=%s", [code])
    model.objects.raw("DELETE FROM tuna_sinopsis WHERE book_id IN (SELECT id FROM tuna_book WHERE code=%s", [code])
    model.objects.raw("DELETE FROM tuna_book WHERE code=%s", [code])
    delta = time.time() - start

    return (count, delta)
