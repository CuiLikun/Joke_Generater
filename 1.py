def print_christmas_tree(height=8):
    for i in range(height):
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))
    # Tree trunk
    for _ in range(2):
        print(' ' * (height - 2) + '|||')

print_christmas_tree()