import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

from config.settings import (EMAIL_HOST, EMAIL_PORT, EMAIL_TEMPLATE_FILE,
                             EMAIL_USER, USERS_FILE)
from weather_notifier.visual_service import generate_html_report

load_dotenv()  # Carrega variáveis do .env
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def load_email_template():
    """Carregar o template de e-mail"""
    with open(EMAIL_TEMPLATE_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)


def load_users():
    """Carregar os usuários do arquivo JSON"""
    with open(USERS_FILE, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data["users"]


def htmls_aggregator(weather_data):
    """Agrega todos os visuais climaticos para as cidades selecionadas"""

    html_content = ""
    for i, city_data in enumerate(weather_data):
        # Gerar conteúdo HTML para cada cidade
        html_content += generate_html_report(city_data)
        # Adicionar um espaçamento entre cada cidade, exceto no último
        if i < len(weather_data) - 1:
            html_content += '<div style="margin: 20px 0;"></div>'

    return html_content


def send_email(weather_data):
    """Função para enviar e-mail"""

    # Carregar template e usuários
    template = load_email_template()
    users = load_users()
    date = weather_data[0]['date']

    html_content = htmls_aggregator(weather_data)

    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)

        for user in users:
            msg = MIMEMultipart()
            msg['From'] = EMAIL_USER
            msg['To'] = user["email"]
            msg['Subject'] = template["subject"].format(
                date=date)

            email_body = f"""
            <html>
                <body>
                    <h2>Olá, {user.get('nome')},</h2>
                    <h2>Previsão do clima para hoje, {date}:</h2>
                    {html_content}
                </body>
            </html>
            """

            # Anexar conteúdo HTML ao e-mail
            msg.attach(MIMEText(email_body, 'html'))

            # Enviar o e-mail
            server.send_message(msg)
            print(f"E-mail enviado para {user['nome']}({user['email']})\n")

        server.quit()
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
