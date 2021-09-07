from left_join.left_join import left_join
from hash_map.hash_map import Hashmap


def test_all_keys_exist():
    ht1 = Hashmap()
    ht1.add('fond', 'enamored')
    ht1.add('wrath', 'anger')
    ht1.add('diligent', 'employed')
    ht1.add('guide', 'usher')

    ht2 = Hashmap()
    ht2.add('fond', 'averse')
    ht2.add('wrath', 'delight')
    ht2.add('diligent', 'idle')
    ht2.add('guide', 'follow')
    assert left_join(ht1, ht2) == [['guide', 'usher', 'follow'], ['fond', 'enamored', 'averse'], [
        'diligent', 'employed', 'idle'], ['wrath', 'anger', 'delight']]


def test_not_all_keys_exist():
    ht1 = Hashmap()
    ht1.add('fond', 'enamored')
    ht1.add('wrath', 'anger')
    ht1.add('diligent', 'employed')
    ht1.add('outift', 'garb')
    ht1.add('guide', 'usher')

    ht2 = Hashmap()
    ht2.add('fond', 'averse')
    ht2.add('wrath', 'delight')
    ht2.add('diligent', 'idle')
    ht2.add('guide', 'follow')
    ht2.add('flow', 'jam')

    assert left_join(ht1, ht2) == [['guide', 'usher', 'follow'], ['fond', 'enamored', 'averse'], [
        'outift', 'garb', None], ['diligent', 'employed', 'idle'], ['wrath', 'anger', 'delight']]
