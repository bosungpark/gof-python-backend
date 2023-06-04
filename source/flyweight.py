import weakref
import uuid


class Flyweight:
    # 참조 카운트를 증가 X, 비싼 비용이 드는 큰 객체를 cache할 때, 부담을 줄일 수 있다.
    _pool = weakref.WeakValueDictionary()

    def __new__(cls, key):
        obj = cls._pool.get(key, None)
        if obj is None:
            obj = object.__new__(Flyweight)
            obj.key = key
            cls._pool[key] = obj
        return obj

    def __repr__(self):
        return f"Flyweight, key: {self.key}"
    
    
flyweight1 = Flyweight(key=uuid.uuid4())
print([i for i in Flyweight._pool.items()])  # [(UUID('efa02cf0-7ee9-40d3-8703-33ad6a4c531d'), Flyweight, key: efa02cf0-7ee9-40d3-8703-33ad6a4c531d)]

del flyweight1  # GC test
assert [i for i in Flyweight._pool.items()] == []

key = uuid.uuid4()
flyweight2 = Flyweight(key=key)
flyweight3 = Flyweight(key=key)

assert flyweight2 == flyweight3

flyweight2.key = "whatever"
assert flyweight3.key == "whatever"  # it is exactly same object!
