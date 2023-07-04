import re

from googletrans import Translator


def drop_spaces(input_field):
    c = 0
    res = ['']
    # drop all '-' in the and of sentence
    input_field = re.sub(r'-(?=\s*$)', '', input_field)
    
    # drop all of 'enters'
    for i in input_field.split('\n'):
        if i == '\r':
            c +=1
            res.append('')
            continue 
        res[c] += i.strip() + ' '
    input_field = '\n'.join(res)
    # find all smile symbols and replace for '-'
    input_field = re.sub(chr(2), "", input_field)

    return input_field

def translate_text(input_field, translate_lang):
    # translate the text
    translator = Translator()
    check_lang = translator.detect(input_field).lang
    translate = translator.translate(input_field, src=check_lang, dest=translate_lang).text
    return check_lang, translate 