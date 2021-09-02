from hash_map.hash_map import Hashmap
import pytest
@pytest.fixture
def hash_map():
    hashmap = Hashmap()

    return hashmap
# Adding a key/value to your hashtable results in the value being in the data structure
# Retrieving based on a key returns the value stored
def test_Adding_to_hashtable(hash_map):
    hash_map.add("Ali","009965555")
    assert hash_map.get("Ali") == "009965555"

# Successfully returns null for a key that does not exist in the hashtable
def test_returns_null(hash_map):
    assert hash_map.get("ali") == None
# Successfully handle a collision within the hashtable
# Successfully retrieve a value from a bucket within the hashtable that has a collision
def test_Adding_collision(hash_map):
    hash_map.add("lAi","syria")
    assert hash_map.get("lAi") == "syria"

# Successfully hash a key to an in-range value
def test_hash_key_not_contains(hash_map):
    hash_map.add("Ali","009965555")
    assert hash_map.contains("Rahhal") == False

def test_hash_key_contains(hash_map):
    hash_map.add("Ali","009965555")
    assert hash_map.contains("Ali") == True
