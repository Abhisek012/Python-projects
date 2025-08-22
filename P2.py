#social media Bio generator

import textwrap

name = input("Enter your name: ").strip()
profession = input("Enter your profession: ").strip()
passion = input("Enter your passion in one line: ").strip()
emoji = input("Enter your favorite emoji: ").strip()
website = input("Enter your website: ").strip()

print("\nChoose your style: ")
print("1. Simple line ")
print("2. Vertical lines ")
print("3. Emoji sandwich ")

style = input("Enter 1, 2, 3: ").strip()

def generate_bio(style):
    if style == "1":
        return f"{emoji} {name} | {profession} \n💡 {passion} \n {website}"
    
    elif style == "2":
        return f"{emoji} {name} \n {profession}🔥\n {passion}\n{website}🔥"
    elif style == "3":
        return f"{emoji*5} \n {name} - {profession} \n {passion}\n {website} \n {emoji*5}"

bio = generate_bio(style)

print("\nYOur stylish bio:\n")

print("*"*200)
print(textwrap.dedent(bio))
print("*"*200)

save = input("Do you want to save this bio to a text file? (y/n): ").lower()

if save == 'y':
    filename = f"{name.lower().replace(' ','_')}_bio.txt"
    with open(filename , "w" , encoding="utf-8") as f:
        f.write(bio)
    print("File saved!")