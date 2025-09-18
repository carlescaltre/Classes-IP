# Exemple d'estructura d'un programa Python
# Autor: Professor SMR
# Aquest programa demana dades, calcula l'àrea d'un cercle i mostra resultats

# Importació de llibreries necessàries
import math

# Constants
PI = math.pi
MAX_ALUMNES = 30

# Variables globals
nom_programa = "Calculadora d'àrees"
autor = "Carles"
edat = 20  # variable d'exemple

# Funció per calcular l'àrea d'un cercle
def calcular_area_cercle(radi):
    """
    Rep el radi (float) i retorna l'àrea (float)
    """
    area = PI * radi ** 2  # Operadors i expressions
    return area    # Retorn de resultat

# Funció principal del programa (main)
def main():
    # Comentaris explicatius
    print(f"Benvingut/da al programa: {nom_programa}")
    print(f"Autor: {autor}")
    print("\n--- Dades d'entrada ---")
    radi = float(input("Indica el radi del cercle: "))  # Entrada de dades
    area = calcular_area_cercle(radi)                   # Crida a funció i processament

    # Sortida de resultats amb format
    print(f"\nL'àrea del cercle de radi {radi} és {area:.2f}")

    # Exemple de conversió de tipus
    radi_enter = int(radi)
    print(f"El radi enter, per exemple, és {radi_enter}")

    # Comentaris i finalització
    print("\nFinal del programa.")

# Bloc principal; s'executa quan el fitxer és el principal
if __name__ == "__main__":
    main()
