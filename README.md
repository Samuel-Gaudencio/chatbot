# Stream Chat

Este projeto consiste em um chatbot utilizando Streamlit e a API Gemini para gerar respostas automáticas baseadas em entrada do usuário.

## Tecnologias Utilizadas

- Python
- Streamlit
- Google Gemini API
- Dotenv para gerenciamento de variáveis de ambiente

## Como Executar o Projeto

### 1. Clone o Repositório

```bash
git clone https://github.com/samuel-gaudencio/chatbot
cd chatbot
```

### 2. Crie um Ambiente Virtual (Opcional, mas Recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a Chave da API

Crie um arquivo `.env` na raiz do projeto e adicione a chave da API:

```env
key=SUA_CHAVE_DA_API
```

### 5. Execute o Projeto

```bash
streamlit run app.py
```

## Funcionalidades

- Interface interativa com Streamlit
- Input do usuário via chat
- Respostas geradas pela API Gemini
- Histórico de mensagens armazenado na sessão

## Contribuição

Sinta-se à vontade para contribuir enviando pull requests ou abrindo issues no repositório.

## Licença

Este projeto está sob a licença MIT.

