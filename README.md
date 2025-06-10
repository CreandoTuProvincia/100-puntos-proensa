# Selección aleatoria de vinos con 100 puntos – Muestra 2 (JCR-ready)

Este repositorio documenta una segunda selección aleatoria de 8 vinos entre una lista de 26 candidatos con puntuaciones de 100 puntos por críticos internacionales.

## Metodología

- Lenguaje: Python 3.11  
- Método: `random.sample()` (selección sin reemplazo)  
- Semilla fija: `20250610` para asegurar replicabilidad  
- Verificación: Hash SHA-256 del resultado final

## Resultado

Lista seleccionada:
1. Sorte O Soro ’22  
2. Pago de Valtarreña ’20  
3. Ausàs Interpretación ’22  
4. Pujanza Cisma ’20  
5. Pingus ’22  
6. Abadía de San Quirce Finca Helena ’22  
7. Do Ferreiro Cepas Vellas ’23  
8. Gaudium ’20

Hash SHA-256 del resultado:  
`384df7fcf916fb38d16e4e0e9c1ab7986fcb23b32a83d94ff65a42348cdc0d9d`

## Reproducibilidad

Ejecuta el script `seleccion_aleatoria_muestra2.py` en cualquier entorno Python 3.x para comprobar la selección y validar el hash.

