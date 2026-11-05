# Bitácora

| Fecha | Predicción / decisión | Cambio | Prueba y evidencia | Commit |
|---|---|---|---|---|
| 2026-11-05 | Predicción: u(L)=0.30 mm exacto en nodos para todas las mallas por superconvergencia 1D; el error en puntos medios decae como O(h^2); u(L)=0 altera el problema físico pero mantiene equilibrio numérico. | Registro de hipótesis previas antes de correr el código en BITACORA.md. | Deducción analítica manual: u(L)=0.30 mm, R_0=-40000 N. | 5d42f9b |
| 2026-11-05 | Implementar referencia analítica cuadrática e interpolación lineal de u_h en puntos medios de cada elemento. | Edición de src/analisis.py completando desplazamiento_referencia y error_puntos_medios. | pytest ejecutado: 2 pruebas pasadas exitosamente (100%). | 5d42f9b |
| 2026-11-05 | Ejecutar convergencia para mallas de 2, 4 y 8 elementos, más caso con contorno alterado u(L)=0. | Ejecución de python src/ejecutar.py. | Se genera salidas/resultados.csv y figura convergencia.png. u(L)=0.30 mm constante, error medio pasa de 0.00625 a 0.00039 mm (tasa 4.0), R_izq+R_der+P+qL=0. | 5d42f9b |