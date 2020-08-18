def delete_nth(order, max_e):
    new_order = []

    for item in order:
        if new_order.count(item) < max_e:
            new_order.append(item)

    return new_order


print(delete_nth([20, 37, 20, 21], 1))
# delete_nth([20, 37, 20, 21], 1)
# [20,37,21]

print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))
# [1, 1, 3, 3, 7, 2, 2, 2]
