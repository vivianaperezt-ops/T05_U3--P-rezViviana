# Declaración de uso de IA

| Herramienta | Fecha | Consulta / Propósito | Contenido incorporado | Comprobación independiente y decisión |
|---|---|---|---|---|
| Gemini | 2026-11-05 | Guía en la formulación analítica de u(x), cálculo de error en puntos medios y estructura de verificación. | Ecuación de la referencia cuadrática y función de interpolación lineal para `src/analisis.py`. | Verificación analítica manual del problema de contorno mediante integración directa y ejecución exitosa de `pytest` (2/2 pruebas aprobadas). Se adoptó la solución. |
| Gemini | 2026-11-05 | Interpretación del caso de contorno alterado u(L)=0 y balance de reacciones. | Explicación teórica de por qué el equilibrio axial cierra numéricamente a pesar de alterar el problema físico original. | Comprobación manual de sumatoria de fuerzas axiales (-10 kN - 30 kN + 20 kN + 20 kN = 0) y contraste con `resultados.csv`. |