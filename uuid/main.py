
import uuid
from random import random

if __name__ == '__main__':
    # UUID 4 basic
    print("uuid 4 = %s" %uuid.uuid4())
    # Generate a UUID based on the SHA-1 hash of a namespace identifier (which is a UUID) and a name (which is a
    # string).
    url = "https://www.vertexinc.datafabric.com/ingestion/instance1"
    print("uuid 5 with namespace = %s" % uuid.uuid5(uuid.NAMESPACE_URL, url))
    print("uuid 5 with random = %s" % uuid.uuid5(uuid.NAMESPACE_OID, str(random())))


