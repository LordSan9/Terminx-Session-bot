import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres://eyrknkbc:4H3Dv2ccbBTmqwTKIJmfMnohhwrq3Mcf@tyke.db.elephantsql.com/eyrknkbc", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 9033689
    API_HASH = "c8d9ff692d165ac1a3b57fbe9a087809"
    BOT_TOKEN = "5579008234:AAHdM14epeHOSq863QLmhGT3zs_16VcP4Wk"
    DATABASE_URL = "postgres://eyrknkbc:4H3Dv2ccbBTmqwTKIJmfMnohhwrq3Mcf@tyke.db.elephantsql.com/eyrknkbc"
    DATABASE_URL = DATABASE_URL.replace("postgres://eyrknkbc:4H3Dv2ccbBTmqwTKIJmfMnohhwrq3Mcf@tyke.db.elephantsql.com/eyrknkbc", "postgresql")
    MUST_JOIN = ""
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
