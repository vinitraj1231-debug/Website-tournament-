with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

org_schema = """      {
        "@type": "Organization",
        "name": "BOOYAH SPORTS Technologies",
        "url": "https://booyahsports.in",
        "logo": "https://booyahsports.in/assets/logo.jpg",
        "sameAs": [
          "https://t.me/BooyahSportsOfficial"
        ],
        "contactPoint": {
          "@type": "ContactPoint",
          "email": "support@booyahsports.in",
          "contactType": "customer service",
          "areaServed": "IN",
          "availableLanguage": ["en", "hi"]
        }
      },"""

if '"@type": "Organization"' not in html:
    html = html.replace('"@graph": [', f'"@graph": [\n{org_schema}')
    print("Organization schema added!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
