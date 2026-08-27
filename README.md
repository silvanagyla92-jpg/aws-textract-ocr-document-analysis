# AWS Textract OCR Document Analysis

Projeto prático de estudo sobre extração de texto em imagens utilizando **Amazon Textract**, **Python** e uma alternativa de OCR local.

## 1. Objetivo

Demonstrar, em uma versão **educacional e documental**, os conceitos e a estrutura necessários para trabalhar com reconhecimento óptico de caracteres (OCR) em imagens e documentos, utilizando o Amazon Textract como referência de serviço em nuvem.

O projeto não representa uma execução produtiva nem uma validação real do serviço Amazon Textract em ambiente AWS. O código de integração foi preparado para fins de estudo e demonstração técnica.

## 2. Tecnologias utilizadas

- Python
- Amazon Textract
- Amazon Web Services (AWS)
- Boto3
- OCR (Optical Character Recognition)
- Tesseract OCR
- Pillow
- Git e GitHub

## 3. Estrutura do projeto

```text
aws-textract-ocr-document-analysis/
├── src/
│   ├── main.py
│   └── ocr_local.py
├── imagens/
├── resultados/
├── README.md
├── requirements.txt
└── .gitignore
```

## 4. Fluxo conceitual da solução

```text
Imagem
   ↓
Python + Boto3
   ↓
Amazon Textract
   ↓
Reconhecimento de texto
   ↓
Processamento da resposta
   ↓
Texto extraído
```

Como alternativa para estudo sem dependência de uma conta AWS, o projeto também contém uma implementação de OCR local com Tesseract.

## 5. Implementação

O arquivo `src/main.py` apresenta uma implementação preparada para enviar uma imagem ao Amazon Textract por meio do Boto3 e recuperar os blocos de texto reconhecidos.

O arquivo `src/ocr_local.py` fornece uma alternativa local utilizando Tesseract OCR, Pillow e Python. Essa alternativa permite estudar o fluxo de OCR sem necessidade de autenticação ou consumo do serviço AWS.

## 6. Limitações da versão

Esta versão deve ser interpretada exclusivamente como **versão educacional/documental**.

- A integração com o Amazon Textract está implementada em código, mas não foi validada mediante execução real no serviço AWS.
- Não foram incluídas credenciais ou chaves de acesso da AWS.
- Não há evidências de uma execução real do Amazon Textract nesta versão.
- O OCR local é disponibilizado como alternativa para estudo e testes sem utilização da AWS.

## 7. Segurança

Nenhuma credencial da AWS deve ser armazenada neste repositório. Para uma eventual execução em ambiente AWS, devem ser utilizadas práticas seguras de gerenciamento de credenciais e permissões.

## 8. Finalidade do projeto

O projeto foi desenvolvido como atividade prática de estudos em Inteligência Artificial, OCR, processamento de documentos e integração com serviços de IA em nuvem.

Seu objetivo é demonstrar compreensão conceitual, organização de código e capacidade de estruturar uma solução de OCR, sem afirmar uma execução do Amazon Textract que não foi realizada.

## 9. Contato

**Autor:** Nágyla Silva

**Projeto:** AWS Textract OCR Document Analysis

**Desafio:** Análise Avançada de Imagens e Texto com IA na AWS

**GitHub:** [silvanagyla92-jpg](https://github.com/silvanagyla92-jpg)

**LinkedIn:** [Nágyla Silva](https://www.linkedin.com/in/n%C3%A1gyla-silva-215aba35/)

---

**Projeto:** AWS Textract OCR Document Analysis

Projeto integrante do portfólio prático em Inteligência Artificial, desenvolvido para demonstrar competências em treinamento e avaliação de sistemas de IA, análise crítica de respostas e anotação de dados, aplicadas às funções de AI Trainer, AI Response Evaluator e Data Annotator, com base em experiência em QA e Auditoria.
