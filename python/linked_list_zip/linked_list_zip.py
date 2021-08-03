from code_challenges.data_structures.linked_list.linked_list import LinkedList


def zipLists(list1, list2):
    len_ll1 = 0
    len_ll2 = 0
    current_item1 = list1.head
    current_item2 = list2.head
    while current_item1:
        current_item1 = current_item1.next
        len_ll1 += 1
    while current_item2:
        current_item2 = current_item2.next
        len_ll2 += 1

    if len_ll2 < len_ll1:

        current_item1 = list1.head
        current_item2 = list2.head
    else:
        head = list2.head.value
        current_item1 = list2.head
        current_item2 = list1.head

    while current_item1 != None or current_item2 != None:

        if current_item1 != None:

            new_next2 = current_item2.next

            new_next1 = current_item1.next
            current_item2.next = current_item1
            current_item1 = current_item1.next
            if new_next1 != None:
                current_item2.next = new_next2
                current_item2 = current_item2.next
            current_item1 = new_next1
        if current_item1.next == None and current_item2 == None:
            current_item1 = current_item1.next

        if current_item2 == None:
            if len_ll2 < len_ll1:
                list1.insert(head)
            return list1
