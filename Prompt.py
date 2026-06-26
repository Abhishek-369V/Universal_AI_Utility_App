def create_prompt(task, text, option):
    if task == "Summarize":
        return f"Summarize {text} in consise buttet points."
    elif task == "Translate":
        return f"Translate {text} into {option}."
    elif task == "Explain":
        return f"Explain {text} use beginner language."
    elif task == "Generate Email":
        return f"Generate an Email of purpose:{text}."
    else:
        return f"Rewrite {text} Professional tone."