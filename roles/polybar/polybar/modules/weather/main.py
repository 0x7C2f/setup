import os
import parser
import openweather
from util import get_city

# Get your API KEY here https://openweathermap.org/api,
# and set an environment variable for OPENWEATHER_API_KEY with your API KEY.
OPENWEATHER_API_KEY = "428e6f14cc62af5274df9d53896ffd26"
API_KEY = os.environ.get("OPENWEATHER_API_KEY", OPENWEATHER_API_KEY)


def main() -> None:
    args = parser.args
    api_key = args.api_key[0] if args.api_key else API_KEY
    city = args.city if args.city else get_city()
    lang = args.lang[0] if args.lang else "en"
    unit = args.unit[0] if args.unit else "standard"

    weather = openweather.get_weather(city, lang, unit, api_key)
    if weather:
        temp, desc = weather.values()
        if args.verbose:
            print(f"{temp}, {desc}")
        else:
            print(f"{temp} & {desc}")


if __name__ == "__main__":
    main()
