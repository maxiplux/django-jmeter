from faker import Faker
import  random
from apps.products.models import Product

fake = Faker()

def load_products_for_test(number_of_records=10):
    for current_index in range(0,number_of_records):
        product=Product()
        name='{name}-{key}'.format(name=fake.bs(), key=str(random.randint(0,10000000)) )
        product.name=name[0:29]
        product.code=random.randint(0,10000000)
        product.price=random.random()
        product.save()

#from util.Utils import load_products_for_test
#load_products_for_test()