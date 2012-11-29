from json import loads

class _Fixture(object):

    _edit_args = []
    _create_args = [_edit_args, ]
    _filter_args = []

    @classmethod
    def _verify_args(cls, actual_args, allowed_args, method):
        for arg in actual_args.keys():
            if not arg in allowed_args:
                raise Exception("%s not an allowed arguement for %s.%s." % (
                    arg, cls, method))


    def __init__(self, connect, _data=None, **kwargs):
        '''Instance constructor. Use the API to create a object.

        ::Args::
        connect - an mtconnect.connect.Connect object

        ::Keyword Args::
        '''
        self._verify_args(kwargs, self._create_args, '__init__')
        if _data:
            # create object for existing record
            self.__dict__.update(_data)
        else:
            # XXX do API create
            self.__dict__.update(kwargs)

    def edit(self, **kwargs):
        '''Instance method. Use the API to edit the object.

        ::Keyword Args::
        '''
        self._verify_args(kwargs, _edit_args, 'edit')

    def delete(self):
        '''Instance method. Use the API to delete the object.'''
        pass

    @classmethod
    def list(connect):
        '''Class method. Query the API for existing object.

        ::Args::
        connect - an mtconnect.connect.Connect object.

        ::Returns::
        A list of _Fixture objects will be returned.
        '''

    @classmethod
    def find(connect, **filters):
        '''Class method. Query the API for a specific existing project.

        ::Args::
        connect - an mtconnect.connect.Connect object

        ::Keyword Args (filters)::

        ::Returns::
        A single _Fixture or None will be returned.
        '''
        self._verify_args(filters, _filter_args, 'edit')

class ProductFixture(_Fixture):
    _uri = '/manage/product/add/'
    _edit_args = ['id_description', 'id_profile']
    _create_args = _edit_args + ['id_name', 'id_version']
    _filter_args = ['name', 'id']

    @classmethod
    def create(cls, connect, data):
        cls._verify_args(data, cls._create_args, 'create')
        return connect.do_post(cls._uri, data)

    @classmethod
    def list(cls, connect):
        r = connect.do_get("product")
        products = loads(r.text)["objects"]
        return [cls(connect, _data=prod) for prod in products]

    @classmethod
    def find(cls, connect, **filters):
        '''Class method. Query the API for a specific existing project.

        ::Args::
        connect - an mtconnect.connect.Connect object

        ::Keyword Args (filters)::
        name - name of project
        id - id of project

        ::Returns::
        A single ProductFixture or None will be returned.
        '''
        cls._verify_args(filters, cls._filter_args, 'find')

        eyedee = str(filters.pop('id', None))

        r = connect.do_get("product", params=filters)
        products = loads(r.text)["objects"]

        if len(products) == 1:
            return cls(connect, _data=products[0].items())
        if eyedee:
            for product in products:
                if product['id'] == eyedee:
                    return cls(connect, _data=product.items())
        
        return None


# class ProjectVersionFixture(_Fixture):
#     _edit_args = []
#     _create_args = [_edit_args, ]
#     _filter_args = []

#     @classmethod
#     def list(cls, connect, ):
#         r = connect.do_get("product")
#         products = loads(r.text)["objects"]
#         return [cls(connect, _data=prod) for prod in products]

#     @classmethod
#     def find(cls, connect, **filters):
#         '''Class method. Query the API for a specific existing project.

#         ::Args::
#         connect - an mtconnect.connect.Connect object

#         ::Keyword Args (filters)::
#         name - name of project
#         id - id of project

#         ::Returns::
#         A single ProductFixture or None will be returned.
#         '''
#         cls._verify_args(filters, cls._filter_args, 'find')

#         eyedee = str(filters.pop('id', None))

#         r = connect.do_get("product", params=filters)
#         products = loads(r.text)["objects"]

#         if len(products) == 1:
#             return cls(connect, _data=products[0].items())
#         if eyedee:
#             for product in products:
#                 if product['id'] == eyedee:
#                     return cls(connect, _data=product.items())
        
#         return None


# class SuiteFixture(_Fixture):
#     _edit_args = []
#     _create_args = [_edit_args, ]
#     _filter_args = []


# class CaseFixture(_Fixture):
#     _edit_args = []
#     _create_args = [_edit_args, ]
#     _filter_args = []


# class RunFixture(_Fixture):
#     _edit_args = []
#     _create_args = [_edit_args, ]
#     _filter_args = []
