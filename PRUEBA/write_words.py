import config, data_source, utils, mix_content, logger, os

def write_in_file(contingut_exit, fitxer_sortida):
    directorios, _ = os.path.split(fitxer_sortida)
    if not os.path.exists(directorios):
        os.mkdir(directorios)

    try:
        with open(fitxer_sortida, mode='wt', encoding='utf-8') as exit_file:
            exit_file.write(contingut_exit)
    except:
        logger.error(f'Cannot open or write in {fitxer_sortida}! Skipping...')

def write_mixed_content(DIRECTORI, contingut_directori):
    for fitxer in contingut_directori:
        try:
            print(fitxer)
            ruta_fitxer_sortida, ruta_fitxer_entrada= data_source.get_file_path(config.DIRECTORI_ENTRADA, config.DIRECTORI_SORTIDA, fitxer)
            contingut_exit=mix_content.mix_file_content(ruta_fitxer_entrada, fitxer)
            if contingut_exit:
                write_in_file(contingut_exit, ruta_fitxer_sortida)
        except UnicodeDecodeError:
            logger.error(f"Not able to process {ruta_fitxer_entrada}! Skipping...")
