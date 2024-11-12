# weather_notifier/visual_service.py


from jinja2 import Template

from config.settings import FILE_HTML


def read_html_template(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_template = file.read()
        return html_template
    except FileNotFoundError:
        print(f"Erro: O arquivo {file_path} não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return None


def generate_html_report(weather_data):
    """
    Gera o relatório HTML formatado com os dados do clima.

    Parameters:
        weather_data (dict): Dicionário contendo os dados do clima para a \
            cidade.

    Returns:
        str: Código HTML formatado com os dados do clima.
    """

    # Template HTML com CSS embutido para visualização de clima
    HTML_TEMPLATE = read_html_template(FILE_HTML)

    # Carregar dados do clima no template HTML
    template = Template(HTML_TEMPLATE)

    # print(weather_data)

    html_content = template.render(
        city=weather_data['city'],
        date=weather_data['date'],
        time=weather_data['time'],
        temp=weather_data['temp'],
        max_temp=weather_data['max'],
        min_temp=weather_data['min'],
        currently=weather_data['currently'],
        condition_slug=weather_data['condition_slug'],
        description=weather_data['description'],
        humidity=weather_data['humidity'],
        rain=weather_data['rain'],
        rain_probability=weather_data['rain_probability'],
        wind_speed=weather_data['wind_speedy'],
        wind_cardinal=weather_data['wind_cardinal'],
        cloudiness=weather_data['cloudiness'],
        sunrise=weather_data['sunrise'],
        sunset=weather_data['sunset']
    )

    return html_content
