#
#
#
from faker import Faker
from foo.indexes.models import BigItem

def dobulk(values, method, low, high):
    """
    Do bulk insert on DB

    values (array)
    low (integer)
    high(integer)
    """
    poms = []
    for val in values[low:high]:
        poms.append(BigItem(method=method,
                            first_name=val['first_name'],
                            last_name=val['last_name'],
                            email=val['email'],
                            email2=val['email2'],
                            address=val['address'],
                            address2=val['address2'],
                            address3=val['address3'],
                            city_suffix=val['city_suffix'],
                            city=val['city'],
                            country1=val['country1'],
                            country2=val['country2'],
                            color1=val['color1'],
                            color2=val['color2'],
                            code1=val['code1'],
                            code2=val['code2'],
                            code3=val['code3'],
                            code4=val['code4'],
                            description1=val['description1'],
                            description2=val['description2'],
                            description3=val['description3'],
                            price1=val['price1'],
                            price2=val['price2'],
                            price3=val['price3'],
                            latitude=val['latitude'],
                            longitude=val['longitude']
                            ))

    BigItem.objects.bulk_create(poms)
