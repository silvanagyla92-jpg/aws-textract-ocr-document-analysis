# AWS Textract OCR Document Analysis

Projeto prático de extração de texto em imagens utilizando **AWS Textract** e **Python**.

## Objetivo

Demonstrar, de forma prática, como utilizar recursos de reconhecimento óptico de caracteres (OCR) da AWS para identificar e extrair textos presentes em imagens e documentos.

## Tecnologias utilizadas

- Python
- AWS Textract
- Amazon Web Services (AWS)
- Boto3
- OCR (Optical Character Recognition)
- Git e GitHub

## Estrutura do projeto

```text
aws-textract-ocr-document-analysis/
├── src/
├── imagens/
├── resultados/
├── evidencias/
├── README.md
├── requirements.txt
└── .gitignore
```

## Fluxo da solução

```text
Imagem
   ↓
Python + Boto3
   ↓
AWS Textract
   ↓
Reconhecimento de texto
   ↓
Processamento da resposta
   ↓
Texto extraído
```

## Próximas etapas

- Implementar o código de integração com o AWS Textract.
- Adicionar uma imagem de teste sem dados pessoais.
- Registrar o resultado da extração.
- Documentar evidências com prints.
- Analisar os resultados, insights e possibilidades de aplicação.

## Segurança

Nenhuma credencial da AWS deve ser armazenada neste repositório. Utilize as configurações seguras recomendadas pela AWS para autenticação.

## Projeto de portfólio

Este projeto foi desenvolvido como atividade prática de estudos em Inteligência Artificial, reconhecimento de documentos e processamento de informações, com foco em demonstrar aprendizado aplicado e documentação técnica.
