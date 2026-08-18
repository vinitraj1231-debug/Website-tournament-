with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = """        <div class="footer-col">
          <h4>PAYMENT MODES</h4>"""

replacement = """        <div class="footer-col">
          <h4>LEGAL & SECURITY</h4>
          <ul>
            <li><a href="privacy-policy.html"><i data-lucide="shield" style="width:13px;height:13px;display:inline;"></i> Privacy Policy</a></li>
            <li><a href="terms-of-service.html"><i data-lucide="file-text" style="width:13px;height:13px;display:inline;"></i> Terms of Service</a></li>
            <li><a href="security-compliance.html"><i data-lucide="lock" style="width:13px;height:13px;display:inline;"></i> Security & Compliance</a></li>
            <li><a href="fair-play-anti-cheat.html"><i data-lucide="crosshair" style="width:13px;height:13px;display:inline;"></i> Fair Play</a></li>
            <li><a href="disclaimer.html"><i data-lucide="alert-circle" style="width:13px;height:13px;display:inline;"></i> Disclaimer</a></li>
            <li><a href="contact-support.html"><i data-lucide="headphones" style="width:13px;height:13px;display:inline;"></i> Contact Support</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>PAYMENT MODES</h4>"""

if target in html:
    html = html.replace(target, replacement)
    print("Legal column injected into footer!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
