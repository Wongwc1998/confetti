from .test_utils import TestCase
from confetti import Config, Metadata

class MetadataTest(TestCase):
    def setUp(self):
        super(MetadataTest, self).setUp()
        self.config = Config({
            "key1" : "value1" // Metadata(a=1, b=2),
            "key2" : "value2",
            "key3" : 1 // Metadata(a=1) // Metadata(b=2),
            })
    def test__metadata_access(self):
        self.assertEquals(self.config.get_config("key1").metadata, {"a" : 1, "b" : 2})
    def test__metadata_access_through_parent(self):
        self.assertIsNone(self.config.get_config("key2").metadata)
    def test__chained_metadata(self):
        self.assertEquals(self.config.get_config("key3").metadata, {"a" : 1, "b" : 2})
