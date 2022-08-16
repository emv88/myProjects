from collections import Counter

# Text taken from Python para Todos from Charles Severance
text =  "Escribir programas (o programar) es una actividad muy creativa y gratificante."\
        "Puedes escribir programas por muchas razones, que pueden ir desde mantenerte activo resolviendo un problema de "\
        "análisis de datos complejo hasta hacerlo por pura diversión ayudando a otros a resolver un enigma."\
        "Este libro asume que todo el mundo necesita saber programar, y que una vez que aprendas a programar ya encontrarás "\
        "qué quieres hacer con esas habilidades recién adquiridas"

# Convert text to list
split_it = text.split()

# Class Counter
Counter = Counter(split_it)

# Show Top 3 words
most_occur = Counter.most_common(3)
print(most_occur)
