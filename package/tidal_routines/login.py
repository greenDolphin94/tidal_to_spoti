from ..common.logger import logErr, logInfo
from ..common.config import TIDAL_CREDENTIAL_FILE

def read_login_credentials()  -> list[str]:
    logInfo('Reading credentials file...')
    try:
        with open(TIDAL_CREDENTIAL_FILE, 'r') as file:
            content = file.read()
        return content.split(',')
    except Exception as err:
        logErr('Exception while reading credentials file. Error: ')
        logErr(err)

    return []

def store_login_credentials(session) -> None:
    logInfo('Storing new credentials...')
    with open(TIDAL_CREDENTIAL_FILE, 'w') as file:
        file.write(f"{session.token_type},"
                   f"{session.access_token},"
                   f"{session.refresh_token},"
                   f"{session.expiry_time.strftime('%d/%m/%y %H:%M:%S.%f')}")
        # file.write(session.token_type + ',')
        # file.write(session.access_token + ',')
        # file.write(session.refresh_token + ',')
        # file.write(session.expiry_time.strftime('%d/%m/%y %H:%M:%S.%f'))