from foo.loader.models import ComplexItem, Item

def dobulk(values, low, high):
    """
    Do bulk insert on DB

    values (array)
    low (integer)
    high(integer)
    """
    poms = []
    for val in values[low:high]:
        poms.append(Item(datetms=val['datetms'],
                         name=val['name'],
                         email=val['email'],
                         value=val['value'],
                         method='bulk'))

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
