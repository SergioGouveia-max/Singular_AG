# 🎯 Singular_AG - Bot de Sinais para Aviator (BantuBet)

O **Singular_AG** é um bot inteligente que monitora o jogo **Aviator** na plataforma **BantuBet** em tempo real, analisa padrões de baixa performance e envia **sinais automáticos via Telegram** com **entrada e saída pré-definidas**.

## Estratégia
- Entrada após **3 rodadas abaixo de 1.50x**
- Saída sempre em **2.00x**

## Como usar

### 1. Configuração local

```bash
pip install -r requirements.txt
```

Crie um `.env` com:

```
TELEGRAM_BOT_TOKEN=seu_token_aqui
TELEGRAM_CHAT_ID=seu_chat_id
```

Execute:

```bash
python main.py
```

### 2. Deploy no Render

- Tipo: Background Worker
- Start command: `python main.py`
- Variáveis de ambiente: `TELEGRAM_BOT_TOKEN` e `TELEGRAM_CHAT_ID`

## Feito com ❤️