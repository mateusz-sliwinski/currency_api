# Currency Exchange API

This project is a REST API for a basic currency exchange database, which interacts with an external API to fetch
currency data.
It allows users to retrieve information about currencies and their historical exchange rates.
The project is implemented in Django and uses a local database to store currency and exchange rate data.

## Installation and Usage

1. Clone this repository to your local machine.

```bash
git clone https://github.com/mateusz-sliwinski/currency_api.git
```
I used python 3.11 so I recommend using it

2. Install project dependencies.

```bash
pip install -r requirements.txt
pip install -r requirements_dev.txt
```

3. Run database migrations.

During the migration, an administrator with the nickname 'admin' and password 'admin' is created. Additionally, data is downloaded from an external database, and this process should conclude with three iterations.```bash
python manage.py migrate

4. Start the development server.

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`.
