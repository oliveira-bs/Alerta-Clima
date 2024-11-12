# main.py

from weather_notifier.email_service import send_email
from weather_notifier.weather_service import get_weather_data


def main():
    # Obtém os dados do clima para as cidades listadas
    weather_data = get_weather_data()

    # Envia o e-mail com as informações de clima para todos os usuários
    send_email(weather_data)


if __name__ == "__main__":
    main()
