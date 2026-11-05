"""Complete las dos funciones antes de ejecutar el estudio."""
import numpy as np

def desplazamiento_referencia(x, L, E, A, P, q):
    """u(0)=0, EA*u'(L)=P, q uniforme. Devuelve un array en mm."""
    x = np.asarray(x, dtype=float)
    return (1.0 / (E * A)) * ((P + q * L) * x - 0.5 * q * (x**2))

def error_puntos_medios(resultado, L, E, A, P, q):
    """Devuelve el maximo error absoluto de u_h frente a u_ref en puntos medios.
    No basta comparar los nodos: interpole u_h linealmente en cada elemento.
    """
    # Extraer las coordenadas nodales (x) y los desplazamientos calculados (u)
    # Compatible si resultado es un diccionario o un objeto con atributos
    if isinstance(resultado, dict):
        x_nodos = np.asarray(resultado.get("x", resultado.get("nodos", [])))
        u_nodos = np.asarray(resultado.get("u", resultado.get("desplazamientos", [])))
    else:
        x_nodos = np.asarray(getattr(resultado, "x", getattr(resultado, "nodos", [])))
        u_nodos = np.asarray(getattr(resultado, "u", getattr(resultado, "desplazamientos", [])))

    # Puntos medios geométricos de cada elemento
    x_medios = 0.5 * (x_nodos[:-1] + x_nodos[1:])
    
    # Desplazamiento aproximado MEF interpolado linealmente en el punto medio
    u_h_medios = 0.5 * (u_nodos[:-1] + u_nodos[1:])
    
    # Solución analítica exacta evaluada en los puntos medios
    u_ref_medios = desplazamiento_referencia(x_medios, L, E, A, P, q)
    
    # Error absoluto máximo entre nodos
    error_max = np.max(np.abs(u_h_medios - u_ref_medios))
    return float(error_max)
