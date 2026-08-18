with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

icon_css = """
    /* ANIMATED ICON STYLES */
    .icon-pulse {
      animation: iconPulse 2s infinite ease-in-out;
      display: inline-block;
      vertical-align: middle;
    }

    .icon-bounce {
      animation: iconBounce 2s infinite ease-in-out;
      display: inline-block;
      vertical-align: middle;
    }

    .animated-icon-spin {
      animation: iconSpin 8s linear infinite;
      color: var(--neon-cyan);
    }

    .animated-icon-glow {
      animation: iconGlow 2s infinite alternate;
      color: var(--primary-purple);
    }

    .animated-icon-pulse {
      animation: iconPulse 1.5s infinite ease-in-out;
      color: #10b981;
    }

    @keyframes iconPulse {
      0%, 100% { transform: scale(1); filter: drop-shadow(0 0 2px rgba(157, 38, 255, 0.5)); }
      50% { transform: scale(1.15); filter: drop-shadow(0 0 8px rgba(0, 240, 255, 0.9)); }
    }

    @keyframes iconBounce {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-4px); }
    }

    @keyframes iconSpin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }

    @keyframes iconGlow {
      0% { filter: drop-shadow(0 0 2px var(--primary-purple)); }
      100% { filter: drop-shadow(0 0 12px var(--neon-cyan)); }
    }
"""

if '/* ANIMATED ICON STYLES */' not in html:
    html = html.replace('</style>', f'{icon_css}\n  </style>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Icon CSS added successfully!")
