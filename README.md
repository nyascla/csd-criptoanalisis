## Descripción de Algoritmos de Ataque a Claves Públicas

### Baby-Step Giant-Step
Baby-Step Giant-Step es un algoritmo de fuerza bruta optimizado para calcular logaritmos discretos. Divide el espacio de búsqueda en dos partes:
- **Baby steps**: Genera una tabla de valores precomputados.
- **Giant steps**: Busca coincidencias usando pasos más grandes.
Esto reduce la complejidad del algoritmo a \(O(\\sqrt{n})\), donde \(n\) es el tamaño del grupo.

### Pollard's Rho
Pollard's Rho es un algoritmo probabilístico para resolver el problema del logaritmo discreto. Utiliza funciones pseudoaleatorias para recorrer el grupo, detectando colisiones (cuando dos cálculos producen el mismo resultado). Su complejidad esperada es \(O(\\sqrt{n})\), lo que lo hace eficiente tanto en tiempo como en memoria.

### Index Calculus
Index Calculus es un método diseñado para resolver problemas de logaritmos discretos en grupos finitos grandes. Aprovecha propiedades algebraicas para expresar el logaritmo como una combinación de factores conocidos, resolviendo luego el sistema de ecuaciones resultante. Es particularmente eficiente contra sistemas basados en logaritmos discretos.


## Video Clases
### 15 noviembre
- https://upvedues.sharepoint.com/:v:/r/sites/PFT_DOC_34876_2024-Csd/Documentos%20compartidos/General/Recordings/Solo%20vista/Clase%20semanal%20de%20CSD-20241113_153949-Grabaci%C3%B3n%20de%20la%20reuni%C3%B3n.mp4?csf=1&web=1&e=kLlbHJ

### 20 noviembre (BSGS)
- https://engage.videoapuntes.upv.es/play/b796d1c0-a0c9-11ef-bcb1-cd3fbeb0d606

### 22 noviembre (BSGS practica)
- https://upvedues.sharepoint.com/:v:/r/sites/PFT_DOC_34876_2024-Csd/Documentos%20compartidos/General/Recordings/Solo%20vista/Clase%20semanal%20CSD-20241122_150230-Grabaci%C3%B3n%20de%20la%20reuni%C3%B3n.mp4?csf=1&web=1&e=2GqN4g

### 27 noviembre (Pollard-rho)
- https://upvedues.sharepoint.com/:v:/r/sites/PFT_DOC_34876_2024-Csd/Documentos%20compartidos/General/Recordings/Solo%20vista/Clase%20semanal%20de%20CSD-20241127_151640-Grabaci%C3%B3n%20de%20la%20reuni%C3%B3n%201.mp4?csf=1&web=1&e=drS9VH

### 29 noviembre (Index-calculus)
- https://upvedues.sharepoint.com/:v:/r/sites/PFT_DOC_34876_2024-Csd/Documentos%20compartidos/General/Recordings/Solo%20vista/Clase%20semanal%20CSD-20241129_153135-Grabaci%C3%B3n%20de%20la%20reuni%C3%B3n%201.mp4?csf=1&web=1&e=jncfeF
