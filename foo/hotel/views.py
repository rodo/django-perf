# -*- coding: utf-8 *-*
from django import http
from django.db import connection
from psycopg2 import extras
from django.views.generic import DetailView, TemplateView
from foo.hotel.models import Hotel
from django.views.generic import ListView


class HotelLimitListView(ListView):
    """
    Limite le nombre de colones lues et retournees de façon plus
    drastique que only()
    """
    model = Hotel

    def get_queryset(self):
        qry = Hotel.objects.filter(color__indice=3).filter(indice__gt=3).select_related('skin','door').order_by('indice')[:10]
        # First remove all columns
        qry.query.clear_select_clause()
        qry.query.add_fields(['name','color__name'])
        # 
        return qry

class HotelLimitNoOrderListView(ListView):
    """
    - Limite le nombre de colones lues et retournees de façon plus
    drastique que only()
    - Supprime la clause ORDER BY

    Warning : l'utilisation de values() final a un effet de bord dangeureux TOUTES les colonnes du modèle
    principal sont à nouveau lues depuis la base de données
    """
    model = Hotel

    def get_queryset(self):
        qry = Hotel.objects.filter(color__indice=3).filter(indice__gt=3).select_related('skin','door').order_by('indice')[:10]
        # First remove all columns
        qry.query.clear_select_clause()
        qry.query.add_fields(['name','color__name'])
        # remove ordering clause
        qry.query.clear_ordering(True)
        # 
        return qry.values()
