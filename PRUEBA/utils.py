import os
import logger
#region ######## VALIDATION ########
def is_mail(text):
    """
    Returns True if the string is a mail\n
    is_mail(string) -> bool
    """
    return '@' in text and '.' in text
        
def has_number(text):
    """
    Returns True if the string has a number\n
    word_has_number(string) -> bool
    """
    for char in text:
        if char.isdigit():
            return True

def is_url_or_filename(text):
    """
    Returns True if the string is an URL or filename\n
    is_url(string) -> bool
    """
    return '.' in text or '/' in text or '\\' in text 

#endregion

#region ########## ERRORS ##########

def check_folders(LOG_DIRECTORY, DIRECTORI_ENTRADA, DIRECTORI_SORTIDA):
    directoris= os.listdir('.')
    if LOG_DIRECTORY not in directoris:
        print('ERROR, NO ES POT COMENÇAR PERQUÈ NO ES TROBA EL DIRECTORI DEL LOG')
    elif DIRECTORI_ENTRADA not in directoris:
        logger.error("NO ES POT COMENÇAR: NO ES POT TROBAR EL DIRECTORI D'ENTRADA")
    elif DIRECTORI_SORTIDA not in directoris:
        logger.error("NO ES POT COMENÇAR: NO ES POT TROBAR EL DIRECTORI DE SORTIDA")
    else:
        return True
