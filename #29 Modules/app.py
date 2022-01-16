from converters import Newton_To_KG
import converters
import timeit


new_1 = converters
print(converters.cm_to_m(753))

length = new_1.m_to_cm(8.64)
print(length)


newton = Newton_To_KG
print(newton(9.81))

print(Newton_To_KG(80))
