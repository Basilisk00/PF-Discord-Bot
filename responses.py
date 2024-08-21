from random import choice, randint
import firefox_scraper

def get_response(user_input:str) -> str:
    lowered: str = user_input.lower()
    percentFull = 0
    if lowered == '':
        return 'Well, you\'re awfully silent'
    elif 'pf' in lowered:
        percentFull = firefox_scraper.scrape()
        if percentFull < 0:
            return 'Could not find crowd meter data'
        if percentFull < 10:
            percentFull = percentFull * 10
        return f'Planet Fitness is {percentFull}% full'
    
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return choice(['I do not understand...',
                       'What are you talking about?',
                       'Do you mind rephrasing that?'])