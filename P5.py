# simple emoji enhancer

# get a dictionary 
emoji_map_fun = {
    "love":"💗",
    "happy":"😊",
    "code":"💻",
    "tea":"☕",
    "music":"🎵",
    "food":"🍕"
}

#get user message 
message = input("Enter your message: ")

#process each word 
updated_words = []

for word in message.split():
    cleaned = word.lower().strip(".,!?")
    emoji = emoji_map_fun.get(cleaned, "")
    if emoji:
        updated_words.append(f"{word} {emoji}")
    else:
        updated_words.append(word)

updated_message = " ".join(updated_words)
print("\n Enhanced message:\n")
print(updated_message)

# if we use only {emoji} by removing {word} in the line 23 instead of (f"{word} {emoji}") it'll eventually replace thee word with the emoji . 