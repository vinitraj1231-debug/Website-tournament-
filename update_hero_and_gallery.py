with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace hero mockup image with real phone frame holding app_home.jpg
old_hero_mockup = '<img src="assets/mockup_hero.svg" alt="BOOYAH SPORTS App Mockup" class="hero-mockup-img">'
new_hero_mockup = """
        <div class="phone-frame-container">
          <div class="phone-notch"></div>
          <img src="assets/app_home.jpg" alt="BOOYAH SPORTS Android App Home Dashboard Screen" class="phone-screen-img">
          <div class="phone-reflection"></div>
        </div>
"""

if old_hero_mockup in html:
    html = html.replace(old_hero_mockup, new_hero_mockup)
    print("Hero phone frame updated!")

# Replace gallery section with 6 real screenshot showcase cards inside smartphone frames
old_gallery = """  <!-- 5. APP PREVIEW / GALLERY SECTION -->
  <section id="app-preview" class="gallery-section">
    <div class="container">
      <div class="section-title-area">
        <p>SLEEK & INTUITIVE UI</p>
        <h2>INSIDE BOOYAH SPORTS</h2>
      </div>

      <div class="gallery-grid">
        <div class="gallery-item">
          <img src="assets/app_screen1.svg" alt="Free Fire Tournament Lobby UI">
          <div class="gallery-caption">Tournament Match Lobby</div>
        </div>
        <div class="gallery-item">
          <img src="assets/app_screen2.svg" alt="Clash Squad 4v4 Match UI">
          <div class="gallery-caption">Clash Squad Custom Rooms</div>
        </div>
        <div class="gallery-item">
          <img src="assets/app_screen3.svg" alt="Instant UPI Wallet Payout UI">
          <div class="gallery-caption">Instant UPI Wallet Payouts</div>
        </div>
      </div>
    </div>
  </section>"""

new_gallery = """  <!-- 5. APP PREVIEW / GALLERY SECTION -->
  <section id="app-preview" class="gallery-section">
    <div class="container">
      <div class="section-title-area">
        <p>HIGH PERFORMANCE ANDROID APP</p>
        <h2>INSIDE BOOYAH SPORTS</h2>
      </div>

      <div class="gallery-grid-6">
        <!-- App Screen 1 -->
        <div class="app-card-showcase">
          <div class="mini-phone-frame">
            <div class="phone-notch"></div>
            <img src="assets/app_home.jpg" alt="Home Dashboard - BOOYAH SPORTS" class="phone-screen-img">
          </div>
          <div class="app-card-caption">
            <h4><i data-lucide="layout-dashboard" style="width:16px;height:16px;display:inline;color:var(--secondary-cyan);"></i> Main Dashboard</h4>
            <p>Live wallet balance, upcoming scrims & instant join buttons.</p>
          </div>
        </div>

        <!-- App Screen 2 -->
        <div class="app-card-showcase">
          <div class="mini-phone-frame">
            <div class="phone-notch"></div>
            <img src="assets/app_matches.jpg" alt="Match Lobby - BOOYAH SPORTS" class="phone-screen-img">
          </div>
          <div class="app-card-caption">
            <h4><i data-lucide="crosshair" style="width:16px;height:16px;display:inline;color:var(--secondary-cyan);"></i> Custom Scrim Lobbies</h4>
            <p>Clash Squad 4v4 & BR Full Map matches with live room codes.</p>
          </div>
        </div>

        <!-- App Screen 3 -->
        <div class="app-card-showcase">
          <div class="mini-phone-frame">
            <div class="phone-notch"></div>
            <img src="assets/app_tournaments.jpg" alt="Tournaments & Scrims - BOOYAH SPORTS" class="phone-screen-img">
          </div>
          <div class="app-card-caption">
            <h4><i data-lucide="trophy" style="width:16px;height:16px;display:inline;color:var(--secondary-cyan);"></i> Pro Tournament Hub</h4>
            <p>High-tier weekly esports leagues with big cash prizes.</p>
          </div>
        </div>

        <!-- App Screen 4 -->
        <div class="app-card-showcase">
          <div class="mini-phone-frame">
            <div class="phone-notch"></div>
            <img src="assets/app_wallet.jpg" alt="Instant UPI Wallet - BOOYAH SPORTS" class="phone-screen-img">
          </div>
          <div class="app-card-caption">
            <h4><i data-lucide="wallet" style="width:16px;height:16px;display:inline;color:var(--secondary-cyan);"></i> Instant UPI Wallet</h4>
            <p>Withdraw winnings in 60 seconds via UPI, Paytm, or PhonePe.</p>
          </div>
        </div>

        <!-- App Screen 5 -->
        <div class="app-card-showcase">
          <div class="mini-phone-frame">
            <div class="phone-notch"></div>
            <img src="assets/app_profile.jpg" alt="Gamer Profile - BOOYAH SPORTS" class="phone-screen-img">
          </div>
          <div class="app-card-caption">
            <h4><i data-lucide="user-check" style="width:16px;height:16px;display:inline;color:var(--secondary-cyan);"></i> Verified Gamer Profile</h4>
            <p>Track kill stats, match history & level progression.</p>
          </div>
        </div>

        <!-- App Screen 6 -->
        <div class="app-card-showcase">
          <div class="mini-phone-frame">
            <div class="phone-notch"></div>
            <img src="assets/app_support.jpg" alt="24x7 Helpdesk - BOOYAH SPORTS" class="phone-screen-img">
          </div>
          <div class="app-card-caption">
            <h4><i data-lucide="headphones" style="width:16px;height:16px;display:inline;color:var(--secondary-cyan);"></i> 24x7 In-App Support</h4>
            <p>Dedicated ticket desk for match queries & instant resolution.</p>
          </div>
        </div>
      </div>
    </div>
  </section>"""

if old_gallery in html:
    html = html.replace(old_gallery, new_gallery)
    print("Gallery grid updated!")

# CSS for Phone Frame
phone_css = """
    /* PHONE FRAME & SHOWCASE STYLES */
    .phone-frame-container {
      position: relative;
      width: 290px;
      height: 580px;
      background: #000;
      border-radius: 40px;
      border: 4px solid #3b2a68;
      box-shadow: 0 0 35px rgba(157, 38, 255, 0.6), inset 0 0 10px rgba(0,0,0,0.8);
      overflow: hidden;
      margin: 0 auto;
      transition: transform 0.4s ease, box-shadow 0.4s ease;
    }

    .phone-frame-container:hover {
      transform: translateY(-8px) scale(1.02);
      box-shadow: 0 0 50px rgba(0, 240, 255, 0.8), 0 0 20px rgba(157, 38, 255, 0.9);
      border-color: var(--neon-cyan);
    }

    .phone-notch {
      position: absolute;
      top: 10px;
      left: 50%;
      transform: translateX(-50%);
      width: 90px;
      height: 18px;
      background: #000;
      border-radius: 10px;
      z-index: 10;
    }

    .phone-screen-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .gallery-grid-6 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 30px;
      margin-top: 40px;
    }

    .app-card-showcase {
      background: rgba(24, 17, 46, 0.75);
      border: 1px solid rgba(157, 38, 255, 0.25);
      border-radius: 20px;
      padding: 24px;
      text-align: center;
      backdrop-filter: blur(10px);
      transition: all 0.3s ease;
    }

    .app-card-showcase:hover {
      border-color: var(--neon-cyan);
      transform: translateY(-5px);
      box-shadow: 0 10px 30px rgba(157, 38, 255, 0.3);
    }

    .mini-phone-frame {
      position: relative;
      width: 220px;
      height: 440px;
      background: #000;
      border-radius: 30px;
      border: 3px solid #3b2a68;
      box-shadow: 0 0 20px rgba(157, 38, 255, 0.4);
      overflow: hidden;
      margin: 0 auto 18px auto;
    }

    .app-card-caption h4 {
      font-family: var(--font-subheading);
      font-size: 1.15rem;
      color: #fff;
      margin-bottom: 6px;
    }

    .app-card-caption p {
      font-size: 0.88rem;
      color: var(--soft-lavender);
    }
"""

if '/* PHONE FRAME & SHOWCASE STYLES */' not in html:
    html = html.replace('</style>', f'{phone_css}\n  </style>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Hero and App Preview updated successfully!")
