set_a = {"col", "mex", "bol"}
set_b = {"pe", "bol"}

#UNION

# .union(): set function --> union de dos conjuntos
set_c = set_a.union(set_b)
print(f"La union entre set_a y set_b es: {set_c}")

# union de dos conjuntos usando el simbolo 'pipe' ( | )
# existe diferencia de sintaxis pero no de resultado
set_c = set_a | set_b
print(f"La union entre set_a y set_b es: {set_c}")

#INTERSECTION

# .intesection() : set function --> interseccion entre dos conjuntos
set_c = set_a.intersection(set_b)
print(f"La interseccion entre set_a y set_b es: {set_c}")

# interseccion usando el simbolo 'ampersand' ( & )

set_c = set_a & set_b
print(f"La interseccion entre set_a y set_b es: {set_c}")

# DIFFERENCE

# .difference(): set function --> diferencia entre el conjunto a del b
set_c = set_a.difference(set_b)
print(f"La diferencia entre set_a del set_b es: {set_c}")

# diferencia entre el conjunto a del b usando el simbolo 'minus' ( - )
set_c = set_a - set_b
print(f"La diferencia entre set_a del set_b es: {set_c}")

# DIFERENCIA SIMETRICA


# .symmetric_difference(): set function --> se obtiene los valores del conjunto sin la interseccion.
set_c = set_a.symmetric_difference(set_b)
print(f"La diferencia simetrica entre set_a y set_b es: {set_c}")

# symmetric difference usando el simbolo de intercalacion ( ^ )

set_c = set_a ^ set_b
print(f"La diferencia simetrica entre set_a y set_b es: {set_c}")


