import random


def splitClauses(text):
    return map(lambda x: x.strip(''),
               text.lower().replace(',','.').replace("'",'').split('.'))

def splitWords(text):
    return text.split(' ')

conversions = {
    'i': 'you',
    'you': 'i',
    'am': 'are',
    'are': 'am',
    'myself': 'yourself',
    'yourself': 'myself'
}

def transform(text):
    return map(lambda x: conversions[x] if x in conversions else x, text)

def matchWildCard(term, text, soFar=''):
    if len(text) == 0:
        return False, '', []
    
    if (isinstance(term, str) and text[0] == term) or\
         (not isinstance(term, str) and text[0] in term):
        return True, soFar, text
    
    return matchWildCard(term, text[1:], soFar + ' ' + text[0])

def matchPattern(pattern, text):
    matches = []

    for i in range(len(pattern)):
        if pattern[i] == 0:
            if i + 1 == len(pattern):
                matches.append(' '.join(text))
            else:
                success, match, text = matchWildCard(pattern[i+1], text)
                if not success:
                    return False, []
                else:
                    matches.append(match.strip())
        elif len(text) == 0:
            return False, []
        elif not isinstance(pattern[i], str):
            if text[0] == pattern[i]:
                matches.append(text[0])
                text = text[1:]
            else:
                return False, []
        elif pattern[i] == text[0]:
            matches.append(text[0])
            text = text[1:]
        else:
            return False, []
        
    return True, matches

while(True):
    text = input('? ')
    if len(text) == 0:
        break

    # Do something with the text

    for clause in splitClauses(text):
        print(splitWords(clause))