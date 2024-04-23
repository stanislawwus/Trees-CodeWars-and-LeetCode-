def tree_by_levels(node):
    visited = [node] if node else []
    for node in visited:
        if node.left:
            visited.append(node.left)
        if node.right:
            visited.append(node.right)
    return [node.value for node in visited]
