from google.cloud import datastore
import datetime

client = datastore.Client()

def put_urls(urls, date_added=None, source_repository='test', collection='TestURL'):
    if date_added is None:
        date_added = datetime.datetime.utcnow()

    entities = []
    for url in urls:
        key = client.key(collection, url)
        entity = datastore.Entity(key=key)
        entity.update(
            {
                'source_repository': source_repository,
                'last_updated': date_added.isoformat()
            }
        )
        entities.append(entity)

    return client.put_multi(entities)
