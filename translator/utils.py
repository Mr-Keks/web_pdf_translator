import re

from googletrans import Translator


def drop_spaces(input_field):
    

    c = 0
    res = ['']
    # drop all '-' in the and of sentence
    input_field = re.sub(r'-(?=\s*$)', '', input_field)
    
    # drop all of 'enters'
    print(input_field.split('\n'))
    for i in input_field.split('\n'):
        if i == '\r':
            c +=1
            res.append('')
            continue 
        res[c] += i.strip() + ' '
    print(res)
    input_field = '\n'.join(res)
    # find all smile symbols and replace for '-'
    input_field = re.sub(chr(2), "", input_field)

    return input_field

def translate_text(input_field):
    # translate the text
    translator = Translator()
    return translator.translate(input_field, dest='uk').text