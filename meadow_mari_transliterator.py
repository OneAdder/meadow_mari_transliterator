#!/usr/bin/python3
author = 'Michael Voronov'
year = '2019'

import re

mapping = {
    'e': 'е',
    'r': 'р',
    't': 'т',
    'u': 'у',
    'i': 'и',
    'o': 'о',
    'p': 'п',
    'a': 'а',
    's': 'с',
    'd': 'д',
    'f': 'ф',
    'g': 'г',
    'j': 'й',
    'k': 'к',
    'l': 'л',
    'z': 'з',
    'c': 'ц',
    'v': 'в',
    'b': 'б',
    'n': 'н',
    'm': 'м',
    'ə': 'ы',
    'š': 'ш',
    'č': 'ч',
    'ŋ': 'ҥ',
    'ö': 'ӧ',
    'ü': 'ӱ',
    'ž': 'ж',
}
escape = ''' \n\r-",.;:()[]{}*?\\/!@#№$%~`'''
ignore = "'"

def remove_j(cyr):
    cyr = re.sub('й[у]', 'ю', cyr)
    cyr = re.sub('й[а]', 'я', cyr)
    return cyr

def vlak(cyr):
    return ' '.join(
        [word[:-4] + '-влак' if word.endswith('влак') else word \
            for word in cyr.split()]
    )

def capitalize(cyr):
    if cyr:
        if not cyr[-1] in '!?.,;:':
            cyr = cyr + '.'
    return cyr.capitalize()

def latin_to_cyrillic(lat):
    cyr = ''
    for sym in lat:
        try:
            cyr += mapping[sym]
        except KeyError:
            if not sym in ignore:
                cyr += sym
            if not sym in escape and not sym in ignore:
                print('The symbol {} is not recognised, skipping.'.format(sym))
    return capitalize(vlak(remove_j(cyr)))

if __name__ == '__main__':
    with open('text', 'r', encoding='utf-8') as f:
        text = f.read()
    if len(text) > 5:
        result = '\n'.join([latin_to_cyrillic(sent) for sent in text.split('.')])
        print(result)
            
