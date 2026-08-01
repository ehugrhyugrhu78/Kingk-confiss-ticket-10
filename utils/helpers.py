import datetime



def now():

    return datetime.datetime.now().isoformat()



def clean(text):

    if not text:
        return ""

    return text.strip()
