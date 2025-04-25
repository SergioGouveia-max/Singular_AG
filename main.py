import time
import requests
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, ESTRATEGIA

url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

def enviar_sinal(entrada, saida):
    mensagem = f"🎯 SINAL - SINGULAR_AG\n📥 Entrada confirmada\n🎯 Saída: {saida:.2f}x"
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": mensagem})

def iniciar_bot():
    options = uc.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = uc.Chrome(options=options)
    driver.get("https://bantubet.com.ao/aviator")

    historico = []

    while True:
        try:
            time.sleep(1.5)
            elementos = driver.find_elements(By.CLASS_NAME, 'coefficient__value')
            multiplicadores = [float(e.text.replace('x', '').strip()) for e in elementos if e.text.endswith('x')]

            if multiplicadores:
                ultimo = multiplicadores[0]
                historico.insert(0, ultimo)
                historico = historico[:10]

                ruins = [m for m in historico[:ESTRATEGIA["min_sequencia_ruim"]] if m < 1.50]

                if len(ruins) == ESTRATEGIA["min_sequencia_ruim"]:
                    print(f"🚀 ENTRADA! Últimos: {historico[:5]}")
                    enviar_sinal(entrada=True, saida=ESTRATEGIA["ponto_entrada"])
                    time.sleep(15)
        except Exception as e:
            print(f"Erro: {e}")
            continue

if __name__ == "__main__":
    iniciar_bot()