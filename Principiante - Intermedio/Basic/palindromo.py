def palindormo(text: str):
    text = text.replace(' ', '').lower()
    return text == text[::-1]

print(palindormo("ana"))
