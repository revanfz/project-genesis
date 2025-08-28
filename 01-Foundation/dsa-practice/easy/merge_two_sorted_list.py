class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_list(list1, list2):
    # This is the solution i come up with, i get 0ms runtime idk maybe this is a bug
    # ordered_list = ListNode()
    # current_node = ordered_list

    # left = list1
    # right = list2
    # if not left:
    #     return right
    # elif not right:
    #     return left

    # while left is not None or right is not None:
    #     if left is None:
    #         current_node.val = right.val
    #         right = right.next
    #     elif right is None:
    #         current_node.val = left.val
    #         left = left.next
    #     else:
    #         if left.val <= right.val:
    #             current_node.val = left.val
    #             left = left.next
    #         else:
    #             current_node.val = right.val
    #             right = right.next
        
    #     if left is not None or right is not None:
    #         current_node.next = ListNode()
    #         current_node = current_node.next

    # return ordered_list

    # this is the better solution
    ordered_list = ListNode()
    current_node = ordered_list

    while list1 and list2:
        if list1.val <= list2.val:
            current_node.next = list1
            list1 = list1.next
        else:
            current_node.next = list2
            list2 = list2.next
        
        current_node = current_node.next
    
    if list1:
        current_node.next = list1
    elif list2:
        current_node.next = list2

    return ordered_list.next

input1 = ListNode(-9, ListNode(3))
input2 = ListNode(5, ListNode(7))
hasil = merge_two_sorted_list(input1, input2)
while hasil is not None:
    print(hasil.val)
    hasil = hasil.next