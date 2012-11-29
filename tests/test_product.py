#!python

import pytest
from datetime import datetime

from mtconnect.fixtures import ProductFixture


class TestProduct:

    def test_create_product(self, testmoztrap):
        dt_string = datetime.utcnow().isoformat()

        fields = {
            'id_name': 'test_create_product_%s' % dt_string,
            'id_description': 'test_create_product %s' % dt_string,
            'id_version': 'test_create_product_%s' % dt_string,
            'id_profile': '1',
        }
        res = ProductFixture.create(testmoztrap.connect, fields)
        print res.text
        assert False

    def test_edit_product(self, testmoztrap):
        assert False

    def test_list_products(self, testmoztrap):
        prods = ProductFixture.list(testmoztrap.connect)
        print "products:\n%s" % prods
        found = False
        for prod in prods:
            if prod.name == 'Macaron':
                found = True
        assert found, "product Macaron not found in %s" % prods


    def test_find_product_by_name(self, testmoztrap):
        prod = ProductFixture.find(testmoztrap.connect, name="Macaron")
        print "product:\n%s" % prod
        assert prod.id == '15'

    def test_find_product_by_id(self, testmoztrap):
        prod = ProductFixture.find(testmoztrap.connect, id=15)
        print "product:\n%s" % prod
        assert prod.name == 'Macaron'

    def test_product_not_found_by_name(self, testmoztrap):
        prod = ProductFixture.find(testmoztrap.connect, name="this product does not exist")
        assert prod == None

    def test_product_not_found_by_id(self, testmoztrap):
        prod = ProductFixture.find(testmoztrap.connect, id=99999999)
        assert prod == None

    def test_delete_product(self, testmoztrap):
        assert False


# {u'productversions': [
#     {u'product': u'/api/v1/product/24/', 
#     u'codename': u'hippies', 
#     u'version': u'long hair', 
#     u'id': u'48', u'resource_uri': 
#     u'/api/v1/productversion/48/'}, 
#     {u'product': u'/api/v1/product/24/', 
#     u'codename': u'', 
#     u'version': u'1', 
#     u'id': u'44', 
#     u'resource_uri': u'/api/v1/productversion/44/'}
# ], u'resource_uri': u'/api/v1/product/24/', 
# u'description': u'for the wool', 
# u'name': u'!! llama !!', 
# u'id': u'24'}