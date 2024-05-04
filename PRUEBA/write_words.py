import logging
import config
import data_source
import utils
import mix_content
import logger
def write_in_file(contingut_exit, fitxer_sortida):
    with open(fitxer_sortida, mode='wt', encoding='utf-8') as exit_file:
        exit_file.write(contingut_exit)

def write_mixed_content(DIRECTORI, contingut_directori):
    try:
        for fitxer in contingut_directori:
            ruta_fitxer_sortida, ruta_fitxer_entrada= data_source.get_file_path(config.DIRECTORI_ENTRADA, config.DIRECTORI_SORTIDA, fitxer)
            contingut_exit=mix_content.mix_file_content(ruta_fitxer_entrada, fitxer)
            if contingut_exit:
                write_in_file(contingut_exit, ruta_fitxer_sortida)

    except UnicodeDecodeError:
       logger.error(f"Not able to process {ruta_fitxer_entrada}")
