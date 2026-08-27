"""Extração de texto em imagens utilizando o Amazon Textract."""

from pathlib import Path

import boto3
from botocore.exceptions import BotoCoreError, ClientError


IMAGE_PATH = Path(__file__).resolve().parent.parent / "imagens" / "documento_exemplo.png"
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "resultados" / "texto_extraido.txt"
AWS_REGION = "us-east-1"


def extract_text(image_path: Path) -> str:
    """Envia uma imagem ao Textract e retorna as linhas de texto reconhecidas."""
    if not image_path.exists():
        raise FileNotFoundError(f"Imagem não encontrada: {image_path}")

    textract = boto3.client("textract", region_name=AWS_REGION)

    with image_path.open("rb") as image_file:
        response = textract.detect_document_text(Document={"Bytes": image_file.read()})

    lines = [
        block["Text"]
        for block in response.get("Blocks", [])
        if block.get("BlockType") == "LINE" and "Text" in block
    ]

    return "\n".join(lines)


def main() -> None:
    """Executa a extração e salva o texto reconhecido."""
    try:
        extracted_text = extract_text(IMAGE_PATH)
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_PATH.write_text(extracted_text + "\n", encoding="utf-8")

        print("Texto extraído com sucesso:")
        print(extracted_text)
        print(f"\nResultado salvo em: {OUTPUT_PATH}")

    except FileNotFoundError as error:
        print(f"Erro: {error}")
    except (BotoCoreError, ClientError) as error:
        print(f"Erro ao acessar o AWS Textract: {error}")


if __name__ == "__main__":
    main()
