import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Lucide script in <head> if not present
lucide_cdn = '<script src="https://unpkg.com/lucide@latest"></script>'
if lucide_cdn not in html:
    html = html.replace('</head>', f'  {lucide_cdn}\n</head>')

# 2. Upgrade Lucide init before </body>
lucide_init = '<script>lucide.createIcons();</script>'
if 'lucide.createIcons()' not in html:
    html = html.replace('</body>', f'  {lucide_init}\n</body>')

# Replacements for emojis with Lucide SVG markup
replacements = [
    ('⚡ DOWNLOAD APK', '<i data-lucide="zap" class="icon-pulse"></i> DOWNLOAD APK'),
    ('✨ Features', '<i data-lucide="sparkles"></i> Features'),
    ('🔥 Tournaments', '<i data-lucide="flame" class="icon-pulse"></i> Tournaments'),
    ('📱 App Preview', '<i data-lucide="smartphone"></i> App Preview'),
    ('❓ FAQ & Support', '<i data-lucide="help-circle"></i> FAQ & Support'),
    ('⚡ DOWNLOAD BOOYAH SPORTS APK (v1.0)', '<i data-lucide="download-cloud" class="icon-bounce"></i> DOWNLOAD BOOYAH SPORTS APK (v1.0)'),
    ('⚡ DOWNLOAD', '<i data-lucide="zap" class="icon-pulse"></i> DOWNLOAD'),
    ('📲 DOWNLOAD APK (v1.0)', '<i data-lucide="download" class="icon-bounce"></i> DOWNLOAD APK (v1.0)'),
    ('🎮 View Scrims', '<i data-lucide="gamepad-2"></i> View Scrims'),
    ('4.8 ★', '4.8 <i data-lucide="star" style="width:16px;height:16px;fill:#ffc107;color:#ffc107;display:inline;"></i>'),
    ('<div class="feature-icon">🤖</div>', '<div class="feature-icon"><i data-lucide="bot" class="animated-icon-spin"></i></div>'),
    ('<div class="feature-icon">⚡</div>', '<div class="feature-icon"><i data-lucide="zap" class="animated-icon-glow"></i></div>'),
    ('<div class="feature-icon">🛡️</div>', '<div class="feature-icon"><i data-lucide="shield-check" class="animated-icon-pulse"></i></div>'),
    ('<div class="feature-icon">🎯</div>', '<div class="feature-icon"><i data-lucide="crosshair" class="animated-icon-spin"></i></div>'),
    ('🔥 APNA GAME. APNA CASH. BOOYAH SPORTS PAR BOOYAH KARO!', '<i data-lucide="flame" style="color:#ff2660;display:inline;"></i> APNA GAME. APNA CASH. BOOYAH SPORTS PAR BOOYAH KARO!'),
    ('⚡ DOWNLOAD BOOYAH SPORTS APK NOW (v1.0)', '<i data-lucide="zap" class="icon-pulse"></i> DOWNLOAD BOOYAH SPORTS APK NOW (v1.0)'),
]

for old, new in replacements:
    html = html.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Icons updated successfully!")
