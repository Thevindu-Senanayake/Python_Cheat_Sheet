coordinates = (1,2,3)
val = coordinates[0] * coordinates[1] * coordinates[2]
print(val)

#instead of doing such thing we can do it like this
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

val2 = x * y * z

#that tales too line so we can do it more easy by using unpacking
a, b, c = coordinates
val3 = a*b*c
print(val3)