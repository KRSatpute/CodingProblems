"""
test case for porblem 1
"""
# pylint: skip-file


import pytest

import problem1_sum_tree


def test_sum_tree():

    root = None

    root = problem1_sum_tree.new_node(8)
    root.left = problem1_sum_tree.new_node(-2)
    root.right = problem1_sum_tree.new_node(4)
    root.left.left = problem1_sum_tree.new_node(5)
    root.left.right = problem1_sum_tree.new_node(1)
    root.right.left = problem1_sum_tree.new_node(2)
    root.right.right = problem1_sum_tree.new_node(-7)

    tree_depth = problem1_sum_tree.max_tree_depth(root)

    problem1_sum_tree.to_sum_tree(root)

    sum_tree_depth = problem1_sum_tree.max_tree_depth(root)

    assert tree_depth == sum_tree_depth
    assert not all(problem1_sum_tree.get_leaf_nodes(root))
