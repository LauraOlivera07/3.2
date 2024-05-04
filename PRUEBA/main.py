import data_source, write_words, logger, config, utils, time

def main():
    puede_empezar= utils.check_folders(config.LOG_DIRECTORY, config.DIRECTORI_ENTRADA, config.DIRECTORI_SORTIDA)
    if puede_empezar== True:
        start=time.time()
        logger.info('======================================================')
        logger.info('Program started')

        contingut_directori = data_source.get_dir_content(config.DIRECTORI_ENTRADA)
        if contingut_directori:
            write_words.write_mixed_content(config.DIRECTORI_ENTRADA, contingut_directori)
        else:
            logger.error("Not able to read directory content")
        logger.info(f'Program ended. TIME ELAPSED: {utils.calculate_time(start)}')

if __name__ == '__main__':

    main()
