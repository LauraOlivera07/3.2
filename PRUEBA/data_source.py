import logging
import os
import config
def get_dir_content(DIRECTORI):
    if os.path.isdir(DIRECTORI):
        contingut_directori = os.listdir(DIRECTORI)
        contingut_directori.sort()
        return contingut_directori


def get_file_path(DIRECTORI_ENTRADA, DIRECTORI_SORTIDA, fitxer):
        fitxer_sortida=os.path.join(DIRECTORI_SORTIDA, f'{fitxer}_boges.txt')
        ruta_fitxer = os.path.join(DIRECTORI_ENTRADA, fitxer)
        logging.info(f'PROCESSING: {ruta_fitxer}')
        return fitxer_sortida, ruta_fitxer


