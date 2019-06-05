# from mydict import Dict
import unittest

class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d.key, 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_Attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


if __name__ == '__main__':
    unittest.main()