# NLP-information-extractor

## Introdução

Projeto criado com o intuito de extrair e classificar informações de acórdãos jurídicos em arquivos PDF, utilizando python, regex, a library Spacy para a formação de entidades customizadas e para a criação e treinamento de modelos de classificação. A interface com o usuário é feita em Django. 

Os dados extraídos foram: 
- ementa de cada acórdão;
- número do processo;
- nome do órgão;
- restante do texto;

O projeto está em fase de desenvolvimento, e uma parte dele se encontra em uma aplicação feita em Django: O usuário submete um arquivo em PDF contendo um acórdão, no qual palavras chaves são extraídas e o número de suas ocorrências no texto são apresentadas em uma tabela.

As palavras chaves serão utilizadas para a classificação dos acórdãos por meio do reconhecimento de entidades.  


## 🚀 Comandos básicos da aplicação:

- Build: 

```bash
docker-compose build
```

- Deploy:

```bash
docker-compose up
```

- Logs:

```bash
docker-compose logs
```
