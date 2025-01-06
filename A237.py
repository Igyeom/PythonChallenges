def print_list(node):
    l = []
    while node is not None:
        l.append(node)
        node = node.next
    print(node)
