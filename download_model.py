"""
Script para descargar el repositorio de Hugging Face:
carlosleao/FER-Facial-Expression-Recognition
"""

from huggingface_hub import snapshot_download
import os

# Configuración
REPOSITORY_ID = "mo-thecreator/vit-Facial-Expression-Recognition"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
OUTPUT_DIR = "./model"

def download_repository():
    """Descarga el repositorio completo de Hugging Face"""
    try:
        print(f"Descargando repositorio: {REPOSITORY_ID}")
        print(f"Guardando en: {OUTPUT_DIR}")
        
        # Crear directorio de salida si no existe
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        # Descargar el repositorio completo
        snapshot_download(
            repo_id=REPOSITORY_ID,
            token=ACCESS_TOKEN,
            local_dir=OUTPUT_DIR,
            local_dir_use_symlinks=False
        )
        
        print(f"\n✓ Descarga completada exitosamente!")
        print(f"Los archivos se encuentran en: {os.path.abspath(OUTPUT_DIR)}")
        
    except Exception as e:
        print(f"✗ Error al descargar el repositorio: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    download_repository()