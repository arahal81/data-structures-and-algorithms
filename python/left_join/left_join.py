from hash_map.hash_map import Hashmap


def left_join(h_m1, h_m2) -> list:
    ht = Hashmap()
    output = []
    for item in h_m1._buckets:
        if item:
            current = item.head
            while current:
                if h_m2.contains(current.key):
                    ht.add(current.key, [current.value, h_m2.get(current.key)])
                else:
                    ht.add(current.key, [current.value, None])
                current = current.next

    for item in ht._buckets:
        if item:
            current = item.head
            while current:
                output.append(
                    [current.key, current.value[0], current.value[1]])
                current = current.next
    return output


if __name__ == '__main__':

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

    print(left_join(ht1, ht2))
