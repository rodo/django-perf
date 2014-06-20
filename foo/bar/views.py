# Create your views here.


from django.views.generic import DetailView

from foo.bar.models import Client

class ClientDetail(DetailView):
    model = Client


class ClientIdxDetail(DetailView):
    model = Client

    def get_queryset(self):
        return Client.objects.all().values('name').order_by('id')


class ClientPrepDetail(DetailView):
    """
    Using a prepared statement
    """
    model = Client

    def get_queryset(self):

        getDiscountsById = PreparedStatement("getusers","""SELECT users FROM bar_client WHERE id = $1""")        
        getDiscountsById.execute(self.id)

        return Client.objects.all().values('name').order_by('id')



class PreparedStatement(object):

    def __init__(self,name,query):
        self.name = name
        self.query = query
        self.vars = []

    def setVar(self,name,var):
        name = "@%s" % name
        if name not in self.vars:
            self.vars.append(name)
        SQL = "SET %s = " % (name)
        self.__executeQuery(SQL+" %s;",var)

    def prepare(self):
        SQL = "PREPARE %s AS " % self.name
        self.__executeQuery("%s %s" % (SQL, self.query))

    def get_prepared(self):
        qry = "SELECT name FROM pg_prepared_statements WHERE name = %s"
        result = self.__executeQuery(qry, self.name)
        return len(result.fetchall())
            

    def f_execute(self):
        return self.execute().fetchall()

    def execute(self, args):
        if self.get_prepared() == 0:
            self.prepare()
        SQL = "EXECUTE %s(%s) " % (self.name, args)
        if len(self.vars):
            params = ""
            for var in self.vars:
                params += var + ", "
            params = params[:-2]
            SQL += "USING %s " % params
        result =  self.__executeQuery(SQL)
        self.vars = []
        return result

    def __executeQuery(self,query,*args):
        cursor = connection.cursor()
        if args:
            cursor.execute(query,args)
        else:
            cursor.execute(query)
        return cursor
