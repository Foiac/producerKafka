from elasticsearch import Elasticsearch
from datetime import datetime

# you can use RFC-1738 to specify the url
es = Elasticsearch(['http://localhost:9200'])

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}

res = es.index(index="indice-teste", id=1, body=doc)
print(res['result'])