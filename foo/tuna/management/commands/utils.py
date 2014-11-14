import time
from django.db import connection

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
    """Delete books on Model
    """
    start = time.time()

    books = model.objects.filter(code=code)
    count = books.count()

    model.objects.filter(code=code).delete()

    delta = time.time() - start
    return (count, delta)

def direct_delete(code, model):
    """Delete books directly
    """
    start = time.time()

    books = model.objects.filter(code=code)
    count = books.count()

    books.delete()

    delta = time.time() - start
    return (count, delta)

def list_delete(code, model):
    """Delete books with a non evaluated QuerySet
    """
    start = time.time()

    books = model.objects.filter(code=code)
    count = books.count()

    book_list = model.objects.filter(code=code)

    model.objects.filter(pk__in=book_list).delete()

    delta = time.time() - start

    return (count, delta)

def raw_delete_book(code, model):
    """Delete books with raw  commands
    """
    start = time.time()

    books = model.objects.filter(code=code)
    count = books.count()


    cursor = connection.cursor()

    cursor.execute("DELETE FROM tuna_editor_books WHERE book_id IN (SELECT id FROM tuna_book WHERE code=%s)", [code])
    cursor.execute("DELETE FROM tuna_sinopsis WHERE book_id IN (SELECT id FROM tuna_book WHERE code=%s)", [code])
    cursor.execute("DELETE FROM tuna_book WHERE code=%s", [code])
    delta = time.time() - start

    return (count, delta)

def raw_delete_company(code, model):
    """Delete companies with raw commands
    """
    start = time.time()

    books = model.objects.filter(code=code)
    count = books.count()

    cursor = connection.cursor()
    cursor.execute("DELETE FROM tuna_company WHERE code=%s", [code])

    delta = time.time() - start

    return (count, delta)
