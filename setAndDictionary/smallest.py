k={23,34,123,42,56,75}
smallest = next(iter(k))
for i in k:
    if i<smallest:
        smallest=i
print(smallest)