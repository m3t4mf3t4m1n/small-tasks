import random
import nltk

BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': ['привет!', 'хай', 'Здравствуйте!!'],
            'responses': ['Добрый день', 'Здравия желаю!', 'Добрый вечер']
        },
        'bye': {
            'examples': ['пОкА!', 'до свидания', 'Увидимся!'],
            'responses': ['До связи', 'Саонара!!', 'Покеда']
        },
        'howdoyoudo': {
            'examples': ['как дела?', 'как жизнь?'],
            'responses': ['не жалуюсь!!']
        }
    },
    'not_found': {
        'responses': ['Извините, не удалось определить интент', 'Я пока еще глупый бот, ничего не понимаю!!']
    }
}

def clean(text):
    cleaned_text = ''
    for ch in text.lower():
        if ch in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя ':
            cleaned_text = cleaned_text + ch
    return cleaned_text

def get_intent(text):
    for intent in BOT_CONFIG['intents'].keys():
        for example in BOT_CONFIG['intents'][intent]['examples']:
            cleaned_example = clean(example)
            cleaned_text = clean(text)
            if nltk.edit_distance(cleaned_example, cleaned_text) / max(len(cleaned_example), len(cleaned_text)) < 0.4:
                return intent
    return 'not_found'

def bot(text):
    intent = get_intent(text)
    if intent != 'not_found':
        return random.choice(BOT_CONFIG['intents'][intent]['responses'])
    return random.choice(BOT_CONFIG['not_found']['responses'])

input_text = ''
while input_text != 'exit':
    input_text = input()
    response = bot(input_text)
    print(response)
