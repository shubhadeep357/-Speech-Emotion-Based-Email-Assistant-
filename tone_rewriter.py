from textblob import TextBlob

def rewrite_email(text, emotion):
    if emotion in ["angry", "fearful", "disgust"]:
        polite_prefix = "Dear Sir/Madam,\n\nI hope this message finds you well. I would like to bring to your attention the following matter in a respectful tone:\n\n"
        polite_suffix = "\n\nThank you for your understanding and time.\n\nBest regards."
        text = TextBlob(text).correct()
        return polite_prefix + str(text) + polite_suffix
    elif emotion in ["happy", "calm", "neutral"]:
        friendly_prefix = "Hello,\n\nJust wanted to say:\n\n"
        return friendly_prefix + text + "\n\nCheers!"
    elif emotion == "sad":
        soft_prefix = "Hello,\n\nI wanted to share something on my mind:\n\n"
        return soft_prefix + text + "\n\nThanks for hearing me out."
    else:
        return "Here is your message: \n\n" + text
