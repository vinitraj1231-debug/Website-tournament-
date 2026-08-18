with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

legal_links = """
        <div class="footer-col">
          <h4>LEGAL & SECURITY</h4>
          <ul>
            <li><a href="privacy-policy.html" style="color:var(--metallic-silver);"><i data-lucide="shield" style="width:14px;height:14px;display:inline;"></i> Privacy Policy</a></li>
            <li><a href="terms-of-service.html" style="color:var(--metallic-silver);"><i data-lucide="file-text" style="width:14px;height:14px;display:inline;"></i> Terms of Service</a></li>
            <li><a href="security-compliance.html" style="color:var(--metallic-silver);"><i data-lucide="lock" style="width:14px;height:14px;display:inline;"></i> Security & Compliance</a></li>
            <li><a href="fair-play-anti-cheat.html" style="color:var(--metallic-silver);"><i data-lucide="crosshair" style="width:14px;height:14px;display:inline;"></i> Fair Play & Anti-Cheat</a></li>
            <li><a href="disclaimer.html" style="color:var(--metallic-silver);"><i data-lucide="alert-circle" style="width:14px;height:14px;display:inline;"></i> Disclaimer</a></li>
            <li><a href="contact-support.html" style="color:var(--metallic-silver);"><i data-lucide="headphones" style="width:14px;height:14px;display:inline;"></i> Contact Support</a></li>
          </ul>
        </div>
"""

# Replace the existing static LEGAL links block in footer
old_legal_block = """        <div class="footer-col">
          <h4>LEGAL</h4>
          <ul>
            <li><a href="#">Privacy Policy</a></li>
            <li><a href="#">Terms of Service</a></li>
            <li><a href="#">Fair Play Policy</a></li>
            <li><a href="#">Refund Policy</a></li>
          </ul>
        </div>"""

if old_legal_block in html:
    html = html.replace(old_legal_block, legal_links)
    print("Footer legal links updated!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
