# coding=utf-8
# code
import uuid

name = 'test_name'
# namespace = 'test_namespace'
namespace = uuid.NAMESPACE_URL

for i in range(10000000):
    print(uuid.uuid1())
    print(uuid.uuid3(namespace, name))
    print(uuid.uuid4())
    print(uuid.uuid5(namespace, name))
