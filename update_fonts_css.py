with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace font import
old_font = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Orbitron:wght@500;700;800;900&family=Rajdhani:wght@500;600;700&display=swap" rel="stylesheet">'
new_font = '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Orbitron:wght@600;700;800;900&family=Rajdhani:wght@600;700&display=swap" rel="stylesheet">'

html = html.replace(old_font, new_font)

# Update CSS variables
html = html.replace("--font-body: 'Inter', sans-serif;", "--font-body: 'Outfit', sans-serif;")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Typography updated!")
