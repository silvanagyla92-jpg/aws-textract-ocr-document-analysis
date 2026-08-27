"""OCR local para testes sem necessidade de uma conta AWS."""

from pathlib import Path

import pytesseract
from PIL import Image


IMAGE_PATH = Path(__file__).resolve().parent.parent / "imagens" / "documento_exemplo.png"
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "resultados" / "texto_extraido_local.txt"


def extract_text(image_path: Path) -> str:
    """Extrai texto de uma imagem usando Tesseract OCR localmente."""
    if not image_path.exists():
        raise FileNotFoundError(f"Imagem não encontrada: {image_path}")

    with Image.open(image_path) as image:
        return pytesseract.image_to_string(image, lang="por+eng").strip()


def main() -> None:
    """Executa o OCR local e salva o texto reconhecido."""
    try:
        extracted_text = extract_text(IMAGE_PATH)
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_PATH.write_text(extracted_text + "\n", encoding="utf-8")

        print("Texto extraído com OCR local:")
        print(extracted_text)
        print(f"\nResultado salvo em: {OUTPUT_PATH}")
    except FileNotFoundError as error:
        print(f"Erro: {error}")
    except Exception as error:
        print(f"Erro durante o OCR local: {error}")


if __name__ == "__main__":
    main()
