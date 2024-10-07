# Crear conjuntos
conjunto_a = {1,2,3,4}
conjunto_b = {3,4,5,6}
conjunto_c = {7,8,9}

# Subconjunto
es_subconjunto = conjunto_a.issubset(conjunto_b)
print(f"¿Es conjunto a un subconjunto de b?: {es_subconjunto})")

# Superconjunto
es_superconjunto = conjunto_b.issuperset(conjunto_a)
print(f"¿Es conjunto_b un superconjunto de a?: {es_superconjunto})")

# Disconjuntos
son_disconjuntos = conjunto_a.isdisjoint(conjunto_c)
print(f"¿Es conjunto_a y c disjuntos?: {son_disconjuntos})")

# Simetría
simetria = conjunto_a.symmetric_difference(conjunto_b)
print(f"Diferencia simétrica entre conjunto_a y b: {simetria})")

# Unión update
conjunto_a.update(conjunto_b)
print(f"Conjunto a después de la unión con b: {conjunto_a})")

# Intersección update
conjunto_a.intersection_update(conjunto_b)
print(f"Conjunto_a después de la intersección con conjunto b: {conjunto_a}")

# Difference update
conjunto_a.difference_update(conjunto_b)
print(f"Conjunto a después de la intersección con conjunto b: {conjunto_a}")