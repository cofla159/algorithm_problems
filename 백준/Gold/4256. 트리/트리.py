from sys import stdin


def make_post_order(pre_s, pre_e, in_s, in_e, pre_order, in_order):
    if pre_s > pre_e or in_s > in_e:
        return []
    if pre_s == pre_e or in_s == in_e:
        return [pre_order[pre_s]]
    root = pre_order[pre_s]
    root_in_inorder = in_order.index(root)
    left_child = make_post_order(pre_s+1, pre_s+root_in_inorder-in_s, in_s,
                                 root_in_inorder-1, pre_order, in_order)
    right_child = make_post_order(
        pre_s+root_in_inorder-in_s+1, pre_e, root_in_inorder + 1, in_e, pre_order, in_order)
    return left_child + right_child + [root]


t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    pre_order = list(map(int, stdin.readline().split()))
    in_order = list(map(int, stdin.readline().split()))
    result = make_post_order(0, n-1, 0, n-1, pre_order, in_order)
    print(*result, sep=' ')
