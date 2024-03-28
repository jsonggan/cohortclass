from mapreduce import *

def read_db(filename):
    db = []
    with open(filename, 'r') as f:
        for l in f:
            db.append(l)
    f.close()
    return db
            
test_db = read_db("./data/price.csv")

# MAPPER
def map_supplier_price(record):
  col = record.split(',')
  supplier_id = col[1]
  price = col[2]
  return (supplier_id, float(price))

# reducer 
def reduce(p):
  supplier = p[0]
  prices = p[1]
  return (supplier,sum(prices)/len(prices))

# TODO: FIXME
# the result should contain a list of suppliers, 
# with the average sale price for all items by this supplier.
m_out = map(map_supplier_price,test_db)

result = reduceByKey2(reduce, m_out)

# mapped_values = flatMap(map_supplier_price, test_db)
# result = reduceByKey2(reduce_average_price, mapped_values)

# print the results
for supplier,avg_price in result:
    print(supplier, avg_price)
    