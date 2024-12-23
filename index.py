from src.databases.db_conexion import SessionLocal
from src.databases.db_queries import obtener_animales, insertar_medicion, registrar_evento

def main():
    # Crear una sesión
    db = SessionLocal()
    
    try:
        # Obtener todos los animales
        print("Animales registrados:")
        animales = obtener_animales(db)
        for animal in animales:
            print(animal)
        
        # Insertar una medición
        print("\nInsertando una nueva medición...")
        insertar_medicion(db, animal_id=1, peso=2.5, imagen_base64="imagen_base64_aqui", fecha_medicion="2024-12-23")
        print("Medición registrada con éxito.")
        
        # Registrar un evento
        print("\nRegistrando un nuevo evento...")
        registrar_evento(db, animal_id=1, tipo_evento="Peso capturado", descripcion="Se registró una medición de peso.", fecha_evento="2024-12-23")
        print("Evento registrado con éxito.")
    
    except Exception as e:
        print(f"Error durante la ejecución: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
