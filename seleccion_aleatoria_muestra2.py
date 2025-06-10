import random
import hashlib

# Lista de vinos candidatos
vinos = [
    "Abadía de San Quirce Finca Helena ’22",
    "Alión ’21",
    "Amancio ’21",
    "Ausàs Interpretación ’22",
    "Barón de Chirel ’19",
    "Clos Mogador ’22",
    "Cuentaviñas El Tiznado ’22",
    "Do Ferreiro Cepas Vellas ’23",
    "Gaudium ’20",
    "L’Ermita ’22",
    "Lalomba Finca Valhonta ’20",
    "Les Aubaguettes ’22",
    "Mirto ’18",
    "Pago de Valtarreña ’20",
    "Pingus ’22",
    "Pujanza Cisma ’20",
    "Pujanza Norte ’21",
    "Quiñón de Valmira ’22",
    "San Vicente ’21",
    "Sierra Cantabria Mágico ’21",
    "Sorte O Soro ’22",
    "Tapias del Marqués de Riscal ’21",
    "Tío Pepe Tres Palmas",
    "Torre de Oña El Camino ’21",
    "Viña El Pisón ’22",
    "Viña Sastre Pesus ’18"
]

# Semilla fija para replicabilidad
random.seed(20250610)

# Selección aleatoria
seleccion = random.sample(vinos, 8)

# Mostrar selección
print("Selección aleatoria:")
for i, vino in enumerate(seleccion, start=1):
    print(f"{i}. {vino}")

# Crear hash SHA-256
resultado = ",".join(seleccion).encode()
hash_verificacion = hashlib.sha256(resultado).hexdigest()

print("\nHash SHA-256 del resultado:")
print(hash_verificacion)
