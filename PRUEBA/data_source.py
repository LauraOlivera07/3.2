#region ############ IMPORTS & CONSTANTS ############
import utils
import os
import crazy_words

def get_dir_content(DIRECTORI):
    if os.path.isdir(DIRECTORI):
        contingut_directori = os.listdir(DIRECTORI)
        contingut_directori.sort()
    return contingut_directori

def mix_file_content(contingut_directori):
    try:
        for fitxer in contingut_directori:
            fitxer_sortida=os.path.join('sortida', f'{fitxer}_boges.txt')
            ruta_fitxer = os.path.join(DIRECTORI, fitxer)
            print(ruta_fitxer)

            if os.path.isfile(ruta_fitxer) and '.txt' in fitxer:
                with open(ruta_fitxer, mode='rt', encoding='utf-8') as f:
                    contingut_boig=[]
                    contingut_fitxer= f.readlines()
                    for line in contingut_fitxer:
                        linea_boja=crazy_words.crazy_text(line).strip()
                        contingut_boig.append(linea_boja + '\n')

                        with open(fitxer_sortida, mode='wt', encoding='utf-8') as exit_file:
                            exit_file.write("".join([str(elem) for elem in contingut_boig]))
                            exit_file.

    except UnicodeDecodeError:
        print(f"Error! No s'ha pogut processar el fitxer {ruta_fitxer})

DIRECTORI = "entrada"
contingut_directori=get_dir_content(DIRECTORI)
mix_file_content(contingut_directori)

