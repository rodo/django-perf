from foo.loader.models import ComplexItem, Item
from faker import Faker

def dobulk(values, method, low, high):
    """
    Do bulk insert on DB

    values (array)
    low (integer)
    high(integer)
    """
    poms = []
    for val in values[low:high]:
        poms.append(Item(datetms=val['datetms'],
                         method=method,
                         name=val['name'],
                         email=val['email'],
                         value=val['value']))

    Item.objects.bulk_create(poms)

def dobulkcomplex(values, low, high):
    """
    Do bulk insert on DB

    values (array)
    low (integer)
    high(integer)
    """
    poms = []
    for val in values[low:high]:
        poms.append(ComplexItem(company=Company(pk=val['company']),
                                method=method,
                                name=val['name'],
                                street_address=val['street_address'],
                                email=val['email'],
                                value=val['value'],
                                vali=val['vali'],
                                country=val['country'],
                                latitude=val['latitude'],
                                longitude=val['longitude'],
                                city=val['city'],
                                city_suffix=val['city_suffix'],
                                locale=val['locale']))

    ComplexItem.objects.bulk_create(poms)

def valueset(nbvalues, step):
    """
    Generate the values
    """
    values = []
    
    f = Faker()
    for i in range(nbvalues):
        values.append({"name": f.name(),
                       "datetms": float(f.latitude()),
                       "email": "{}-{}".format(step, f.email()),
                       "value": f.random_number() + step})

    return values
