import tidalapi

import os

from ..common.logger import logInfo
from ..common.config import TIDAL_AUTH_TOKENS_FILE_PATH

def _read_tokens()  -> list[str]:
    logInfo('Reading credentials file...')
    with open(TIDAL_AUTH_TOKENS_FILE_PATH, 'r') as file:
        content = file.read()
    return content.split(',')

def _store_login_credentials(session) -> None:
    logInfo('Storing new credentials...')
    with open(TIDAL_AUTH_TOKENS_FILE_PATH, 'w') as file:
        file.write(f"{session.token_type},"
                   f"{session.access_token},"
                   f"{session.refresh_token},"
                   f"{session.expiry_time.strftime('%d/%m/%y %H:%M:%S.%f')}")

def tidal_login_session(session: tidalapi.Session) -> None:
    token_info = []
    if os.path.exists(TIDAL_AUTH_TOKENS_FILE_PATH): 
        token_info = _read_tokens()
    if len(token_info) == 4 and session.load_oauth_session(token_info[0], token_info[1], token_info[2], token_info[3]):
                logInfo('Login successful for user  ' + session.user.email)
    else:
        # Will run until you visit the printed url and link your account
        session.login_oauth_simple()
        _store_login_credentials(session)

    if not session.check_login():
        raise RuntimeError('Tidal login failed') 