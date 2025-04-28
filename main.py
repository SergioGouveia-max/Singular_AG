from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import telebot
import time
from keep_alive import keep_alive

# Dados do teu bot (VAI CONFIGURAR ISSO DEPOIS NAS VARIÁVEIS DO RAILWAY)
API_TOKEN = 'SEU_TOKEN_AQUI'
CHAT_ID = 'SEU_CHAT_ID_AQUI'

bot = telebot.TeleBot(API_TOKEN)

def setup_driver():
    options = Options()
    options.headless = True  # Roda navegador sem abrir tela
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver

def enviar_mensagem(texto):
    bot.send_message(CHAT_ID, texto)

def analisa_resultado(driver):
    try:
        # Aqui você deve ajustar para o local exato do número do resultado no Bac Bo da BantuBet
        placar = driver.find_element(By.CLASS_NAME, "SUA_CLASSE_AQUI").text
        return placar
    except Exception as e:
        print(f"Erro ao capturar resultado: {e}")
        return None

def main():
    keep_alive()
    enviar_mensagem("❤️ Coração Bac Bo ativo!\nAnalisando BantuBet...")

    driver = setup_driver()
    driver.get('https://www.bantubet.co.ao/')

    time.sleep(5)  # Aguarda o site carregar
    
    while True:
        resultado = analisa_resultado(driver)
        if resultado:
            print(f"Resultado capturado: {resultado}")
            
            # Lógica para decidir se é aposta segura
            # (Aqui você pode montar tua estratégia!)
            # Exemplo fictício:
            if "Player" in resultado:
                enviar_mensagem(f"✅ Aposta segura em Player! Resultado: {resultado}")
            elif "Banker" in resultado:
                enviar_mensagem(f"✅ Aposta segura em Banker! Resultado: {resultado}")
            else:
                enviar_mensagem(f"⚠️ Resultado diferente: {resultado}")

        time.sleep(10)  # Espera antes de buscar novo resultado

if __name__ == "__main__":
    main()
