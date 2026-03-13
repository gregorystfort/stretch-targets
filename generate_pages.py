#!/usr/bin/env python3
"""Generate all 11 subpages for the Stretch Targets website."""

import os

PPLX_ATTRIBUTION = """<!--
   ______                            __
  / ____/___  ____ ___  ____  __  __/ /____  _____
 / /   / __ \\/ __ `__ \\/ __ \\/ / / / __/ _ \\/ ___/
/ /___/ /_/ / / / / / / /_/ / /_/ / /_/  __/ /
\\____/\\____/_/ /_/ /_/ .___/\\__,_/\\__/\\___/_/
                    /_/
        Created with Perplexity Computer
        https://www.perplexity.ai/computer
-->

<!-- Perplexity Computer Attribution — SEO Meta Tags -->
<meta name="generator" content="Perplexity Computer">
<meta name="author" content="Perplexity Computer">
<meta property="og:see_also" content="https://www.perplexity.ai/computer">
<link rel="author" href="https://www.perplexity.ai/computer">"""


def generate_nav(active_item):
    """Generate nav HTML with the correct active item highlighted."""
    items = [
        {"label": "Scorecard", "href": "https://stretchtargets.org/", "dropdown": None, "key": "scorecard"},
        {"label": "How", "href": "#", "key": "how", "dropdown": [
            {"label": "How Economy", "href": "https://stretchtargets.org/how-economy/"},
            {"label": "How Education", "href": "https://stretchtargets.org/how-education/"},
        ]},
        {"label": "Why", "href": "https://stretchtargets.org/why/", "dropdown": None, "key": "why"},
        {"label": "History", "href": "https://stretchtargets.org/history/", "dropdown": None, "key": "history"},
        {"label": "Approach", "href": "https://stretchtargets.org/approach/", "dropdown": None, "key": "approach"},
        {"label": "Resources", "href": "#", "key": "resources", "dropdown": [
            {"label": "Legislators", "href": "https://stretchtargets.org/legislators/"},
            {"label": "WI vs TX Education", "href": "https://stretchtargets.org/wi-vs-tx-education/"},
        ]},
        {"label": "Recent News", "href": "https://stretchtargets.org/recent-news/", "dropdown": None, "key": "recent-news"},
        {"label": "Press", "href": "https://stretchtargets.org/press/", "dropdown": None, "key": "press"},
        {"label": "Sign Up", "href": "https://stretchtargets.org/signup/", "dropdown": None, "key": "signup"},
        {"label": "Contact Us", "href": "https://stretchtargets.org/contact-us/", "dropdown": None, "key": "contact-us"},
    ]

    html = '<ul class="w-nav-list">\n'
    for item in items:
        classes = ["w-nav-item"]
        if item["key"] == active_item:
            classes.append("current-menu-item")
        if item.get("dropdown"):
            classes.append("has-dropdown")
        class_str = " ".join(classes)

        html += f'          <li class="{class_str}"><a class="w-nav-anchor" href="{item["href"]}">{item["label"]}</a>\n'
        if item.get("dropdown"):
            html += '            <ul class="w-nav-dropdown">\n'
            for sub in item["dropdown"]:
                html += f'              <li><a href="{sub["href"]}">{sub["label"]}</a></li>\n'
            html += '            </ul>\n'
        html += '          </li>\n'
    html += '        </ul>'
    return html


def generate_page(page_title, breadcrumb_text, active_nav_item, main_content_html, og_url=""):
    """Generate a complete HTML page."""
    nav_html = generate_nav(active_nav_item)

    return f'''<!DOCTYPE html>
<html lang="en-US">
<head>
{PPLX_ATTRIBUTION}
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page_title} - Wisconsin Global Scorecard</title>
<meta property="og:locale" content="en_US">
<meta property="og:type" content="website">
<meta property="og:title" content="{page_title} - Wisconsin Global Scorecard">
<meta property="og:url" content="https://stretchtargets.org/{og_url}">
<meta property="og:site_name" content="Wisconsin Global Scorecard">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap" rel="stylesheet">
<style>
/* ===== RESET ===== */
*, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}

/* ===== BASE ===== */
body {{
  font-family: 'Open Sans', sans-serif;
  font-size: 14px;
  line-height: 24px;
  color: #333;
  background: #fff;
  -webkit-font-smoothing: antialiased;
}}
a {{ text-decoration: none; color: inherit; }}
img {{ max-width: 100%; height: auto; display: block; }}
strong {{ color: #ff0000; }}

/* ===== HEADER ===== */
.l-header {{
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 111;
  background: #fff;
  box-shadow: 0 1px 0 rgba(0,0,0,0.08);
}}

.l-subheader.at_middle {{
  height: 100px;
  background: #fff;
  transition: height 0.3s;
}}
.l-header.sticky .l-subheader.at_middle {{
  height: 50px;
}}
.l-subheader-h {{
  max-width: 1300px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  height: inherit;
  padding: 0 20px;
}}
.header-logo img {{
  height: 50px;
  width: auto;
}}

.l-subheader.at_bottom {{
  height: 50px;
  background: #1e73be;
  box-shadow: 0 1px 0 rgba(0,0,0,0.08);
}}
.l-subheader.at_bottom .l-subheader-h {{
  padding: 0;
  justify-content: space-between;
}}

/* ===== NAVIGATION ===== */
.w-nav-list {{
  list-style: none;
  display: flex;
  align-items: stretch;
  height: 50px;
  margin: 0;
  padding: 0;
}}
.w-nav-item {{
  position: relative;
}}
.w-nav-anchor {{
  display: flex;
  align-items: center;
  height: 50px;
  padding: 0 15px;
  color: #fff;
  font-size: 14px;
  font-weight: 700;
  line-height: 50px;
  white-space: nowrap;
  transition: background 0.2s;
}}
.w-nav-anchor:hover {{
  color: #ff0000;
}}
.w-nav-item.current-menu-item .w-nav-anchor {{
  background: #ff0000;
  color: #fff;
}}
.w-nav-item.current-menu-item .w-nav-anchor:hover {{
  color: #fff;
}}

.w-nav-item.has-dropdown > .w-nav-anchor::after {{
  content: '';
  display: inline-block;
  width: 0;
  height: 0;
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-top: 4px solid #fff;
  margin-left: 6px;
}}
.w-nav-item.has-dropdown:hover > .w-nav-anchor::after {{
  border-top-color: #ff0000;
}}
.w-nav-item.current-menu-item.has-dropdown:hover > .w-nav-anchor::after {{
  border-top-color: #fff;
}}

.w-nav-dropdown {{
  display: none;
  position: absolute;
  top: 50px;
  left: 0;
  background: #1e73be;
  min-width: 180px;
  z-index: 100;
  list-style: none;
  padding: 0;
  box-shadow: 0 3px 5px rgba(0,0,0,0.15);
}}
.w-nav-item.has-dropdown:hover .w-nav-dropdown {{
  display: block;
}}
.w-nav-dropdown li a {{
  display: block;
  padding: 10px 20px;
  color: #fff;
  font-size: 14px;
  font-weight: 400;
  white-space: nowrap;
}}
.w-nav-dropdown li a:hover {{
  background: rgba(255,255,255,0.1);
  color: #ff0000;
}}

.nav-right {{
  display: flex;
  align-items: center;
  height: 50px;
}}
.search-icon {{
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50px;
  height: 50px;
  color: #fff;
  cursor: pointer;
  font-size: 16px;
}}
.search-icon:hover {{
  color: #ff0000;
}}

.search-overlay {{
  display: none;
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: #fff;
  z-index: 999;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}}
.search-overlay.active {{
  display: flex;
}}
.search-overlay input {{
  font-size: 30px;
  border: none;
  border-bottom: 2px solid #ccc;
  outline: none;
  text-align: center;
  width: 50%;
  padding: 10px;
  font-family: 'Open Sans', sans-serif;
  color: #999;
}}
.search-overlay .close-btn {{
  position: absolute;
  top: 20px;
  right: 30px;
  font-size: 30px;
  cursor: pointer;
  color: #333;
}}

/* ===== PAGE TITLE SECTION ===== */
.page-title-section {{
  background: #f5f5f5;
  padding: 25px 0;
  border-bottom: 1px solid #eee;
}}
.page-title-section .l-section-h {{
  max-width: 1300px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}}
.page-title-section h1 {{
  font-size: 24px;
  font-weight: 700;
  color: #333;
  font-family: 'Open Sans', sans-serif;
}}
.page-title-section h1 strong {{
  color: #333;
}}
.breadcrumbs {{
  font-size: 13px;
  color: #777;
}}
.breadcrumbs a {{
  color: #1e73be;
}}
.breadcrumbs a:hover {{
  text-decoration: underline;
}}

/* ===== SECTIONS ===== */
.l-section {{
  padding: 25px 0;
}}
.l-section-h {{
  max-width: 1300px;
  margin: 0 auto;
  padding: 0 20px;
}}

/* ===== MAIN CONTENT ===== */
.main-content {{
  padding: 30px 0;
  background: #fff;
}}
.main-content .l-section-h {{
  max-width: 1300px;
  margin: 0 auto;
  padding: 0 20px;
}}
.main-content p {{
  font-size: 14px;
  line-height: 24px;
  color: #333;
  margin-bottom: 15px;
}}
.main-content h2 {{
  font-size: 20px;
  font-weight: 700;
  color: #333;
  margin-bottom: 15px;
}}
.main-content h2 strong {{
  color: #ff0000;
}}
.main-content h3 {{
  font-size: 16px;
  font-weight: 700;
  color: #333;
  margin-bottom: 10px;
}}
.main-content a.read-more {{
  color: #1e73be;
  font-weight: 700;
}}
.main-content a.read-more:hover {{
  text-decoration: underline;
}}
.main-content ul {{
  margin-bottom: 15px;
  padding-left: 20px;
}}
.main-content ul li {{
  margin-bottom: 8px;
  font-size: 14px;
  line-height: 24px;
}}
.main-content ul li a {{
  color: #1e73be;
}}
.main-content ul li a:hover {{
  text-decoration: underline;
}}

/* Grid layouts */
.grid-row {{
  display: flex;
  gap: 30px;
  margin-bottom: 30px;
}}
.grid-col {{
  flex: 1;
  background: #f9f9f9;
  padding: 20px;
  border: 1px solid #eee;
}}
.grid-col h3 {{
  color: #333;
  margin-bottom: 8px;
}}
.grid-col h3 strong {{
  color: #ff0000;
}}
.grid-col p {{
  font-size: 14px;
  line-height: 24px;
  color: #333;
}}

/* Two column layout */
.two-col-row {{
  display: flex;
  gap: 30px;
  align-items: flex-start;
  margin-bottom: 20px;
}}
.two-col-left {{
  flex: 1;
}}
.two-col-right {{
  flex: 1;
}}

/* Legislators blue banner */
.legislators-banner {{
  background: #1e73be;
  color: #fff;
  padding: 40px 0;
  margin-bottom: 0;
}}
.legislators-banner .l-section-h {{
  display: flex;
  gap: 30px;
  align-items: center;
}}
.legislators-banner h2 {{
  color: #fff;
  font-size: 22px;
  margin-bottom: 10px;
}}
.legislators-banner p {{
  color: #fff;
  font-size: 14px;
  line-height: 24px;
}}
.btn-download {{
  display: inline-block;
  background: #ff4400;
  color: #fff;
  padding: 15px 30px;
  font-size: 16px;
  font-weight: 700;
  border: none;
  cursor: pointer;
  font-family: 'Open Sans', sans-serif;
  white-space: nowrap;
}}
.btn-download:hover {{
  opacity: 0.9;
}}

/* Video wrapper */
.video-wrapper {{
  position: relative;
  padding-bottom: 56.25%;
  height: 0;
  overflow: hidden;
  margin-bottom: 20px;
}}
.video-wrapper iframe {{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 0;
}}

/* Slideshare embed */
.slideshare-wrapper {{
  margin: 20px 0;
}}
.slideshare-wrapper iframe {{
  width: 100%;
  height: 500px;
  border: 1px solid #eee;
}}

/* Fact statements */
.fact-statement {{
  font-size: 15px;
  line-height: 26px;
  margin-bottom: 20px;
  padding: 15px 20px;
  background: #f9f9f9;
  border-left: 4px solid #1e73be;
}}
.fact-statement strong {{
  color: #ff0000;
}}

/* ===== SIGN-UP SECTION ===== */
.section-signup {{
  background: #f4f4f4;
  padding: 30px 0;
}}
.section-signup h1 {{
  font-size: 30px;
  font-weight: 700;
  color: #1e73be;
  margin-bottom: 15px;
  font-family: 'Open Sans', sans-serif;
  text-align: left;
}}
.section-signup > .l-section-h > p {{
  font-size: 14px;
  line-height: 24px;
  color: #333;
  margin-bottom: 15px;
  text-align: left;
}}
.signup-form label {{
  font-weight: 700;
  font-size: 14px;
  color: #333;
  display: block;
  margin-bottom: 5px;
}}
.signup-form-row {{
  display: flex;
  gap: 15px;
  align-items: stretch;
}}
.signup-form-row input[type="email"] {{
  flex: 2.5;
  padding: 8px 12px;
  border: 1px solid #ccc;
  font-size: 14px;
  font-family: 'Open Sans', sans-serif;
  background: #fff;
  outline: none;
}}
.signup-form-row input[type="submit"] {{
  flex: 1;
  background: #1e73be;
  color: #fff;
  border: none;
  padding: 8px 20px;
  font-size: 14px;
  font-weight: 700;
  font-family: 'Open Sans', sans-serif;
  cursor: pointer;
  text-transform: uppercase;
}}
.signup-form-row input[type="submit"]:hover {{
  opacity: 0.9;
}}

/* ===== FOOTER ===== */
.l-footer {{
  background: #1e73be;
  color: #fff;
  padding: 30px 0;
  font-size: 0.9rem;
  line-height: 1.5rem;
  text-align: center;
}}
.footer-fb {{
  margin-bottom: 15px;
}}
.footer-fb img {{
  width: 59px;
  height: 59px;
  display: inline-block;
}}
.footer-copyright {{
  margin-bottom: 15px;
  font-size: 0.9rem;
}}
.footer-copyright a {{
  color: #ffff00;
}}
.footer-copyright a:hover {{
  text-decoration: underline;
}}
.footer-info {{
  font-size: 0.85rem;
  line-height: 1.5rem;
  padding: 0 40px;
}}
.footer-info b {{
  color: #fff;
}}
.pplx-footer {{
  margin-top: 15px;
  font-size: 0.75rem;
  opacity: 0.7;
}}
.pplx-footer a {{
  color: #ffff00;
}}

/* ===== BODY OFFSET ===== */
.l-main {{
  padding-top: 150px;
}}
.l-header.sticky + .l-main,
.l-header.sticky ~ .l-main {{
  padding-top: 100px;
}}

/* ===== RESPONSIVE ===== */
@media (max-width: 900px) {{
  .l-main {{
    padding-top: 100px;
  }}
  .l-subheader.at_middle {{
    height: 60px;
  }}
  .header-logo img {{
    height: 35px;
  }}
  .w-nav-list {{
    flex-wrap: wrap;
    height: auto;
  }}
  .w-nav-anchor {{
    height: auto;
    padding: 8px 12px;
    font-size: 13px;
    line-height: normal;
  }}
  .l-subheader.at_bottom {{
    height: auto;
  }}
  .grid-row,
  .two-col-row,
  .legislators-banner .l-section-h {{
    flex-direction: column;
  }}
  .signup-form-row {{
    flex-direction: column;
  }}
  .page-title-section .l-section-h {{
    flex-direction: column;
    gap: 5px;
  }}
}}
</style>
</head>
<body>

<!-- ===== HEADER ===== -->
<header class="l-header" id="site-header">
  <div class="l-subheader at_middle">
    <div class="l-subheader-h">
      <div class="header-logo">
        <a href="/"><img src="../assets/logo.jpg" alt="Stretch Targets" width="935" height="176"></a>
      </div>
    </div>
  </div>
  <div class="l-subheader at_bottom">
    <div class="l-subheader-h">
      <nav>
        {nav_html}
      </nav>
      <div class="nav-right">
        <div class="search-icon" onclick="document.getElementById('searchOverlay').classList.add('active')">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        </div>
      </div>
    </div>
  </div>
</header>

<!-- Search Overlay -->
<div class="search-overlay" id="searchOverlay">
  <span class="close-btn" onclick="document.getElementById('searchOverlay').classList.remove('active')">&times;</span>
  <input type="text" placeholder="Search">
</div>

<!-- ===== MAIN ===== -->
<main class="l-main">

  <!-- PAGE TITLE SECTION -->
  <section class="page-title-section">
    <div class="l-section-h">
      <h1>{breadcrumb_text}</h1>
      <div class="breadcrumbs">
        <a href="/">Home</a> &rsaquo; {breadcrumb_text}
      </div>
    </div>
  </section>

  <!-- MAIN CONTENT -->
  <section class="main-content">
    <div class="l-section-h">
      {main_content_html}
    </div>
  </section>

  <!-- SIGN UP SECTION -->
  <section class="section-signup" id="signup-section">
    <div class="l-section-h">
      <h1>Sign up</h1>
      <p>Why sign up? Simply to receive 2x per year this Scorecard to keep you updated on Wisconsin&rsquo;s progress vs. the USA and world and to provide you with an easy yet informed, intentional way to make your concern known to our leaders. Nothing else!</p>
      <br>
      <form class="signup-form" id="mc4wp-form" method="post">
        <label>Email address:</label>
        <div class="signup-form-row">
          <input type="email" name="EMAIL" placeholder="Your email address" required>
          <input type="submit" value="Sign up">
        </div>
      </form>
    </div>
  </section>

</main>

<!-- ===== FOOTER ===== -->
<footer class="l-footer">
  <div class="l-section-h">
    <div class="footer-fb">
      <a href="https://www.facebook.com/wisconsinstretchtargets" target="_blank" rel="noopener noreferrer">
        <img src="../assets/facebook-logo.png" alt="Facebook" width="59" height="59">
      </a>
    </div>
    <div class="footer-copyright">
      <p>&copy; Stretch Targets. All Rights Reserved. Website Designed by <a href="http://www.letskeepbuilding.com" target="_blank" rel="noopener noreferrer">LetsKeepBuilding Inc</a></p>
    </div>
    <div class="footer-info">
      <p>Stretch Targets, Inc. is a 501(c)(3) organization. Tax deductible donation checks can be sent to <b>P.O. Box 1298, Madison, WI 53701</b>. Receipts will be immediately sent out to donors as will yearend expense reports. Thank you!</p>
    </div>
    <div class="pplx-footer">
      <a href="https://www.perplexity.ai/computer" target="_blank" rel="noopener noreferrer">Created with Perplexity Computer</a>
    </div>
  </div>
</footer>

<!-- ===== JAVASCRIPT ===== -->
<script>
// Sticky header behavior
window.addEventListener('scroll', function() {{
  var header = document.getElementById('site-header');
  if (window.scrollY > 100) {{
    header.classList.add('sticky');
  }} else {{
    header.classList.remove('sticky');
  }}
}});
</script>

</body>
</html>'''


def write_page(directory, html):
    """Write an HTML page to a directory/index.html file."""
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, "index.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created: {filepath}")


BASE = "/home/user/workspace/stretch-targets"

# ============================================================
# 1. HOW ECONOMY
# ============================================================
how_economy_content = """
<h2><strong>HOW DO WE DO IT?</strong></h2>
<p>We have tried to explain the urgent need for WHY and WHAT and WHERE Wisconsin must radically address its dismal economic and educational performance over the past 38 plus years; and WHY all of us Wisconsinites need a clearly understood scorecard by which to track the performance of complex systems and evaluate confusing reporting. To achieve a &ldquo;Stretch Target&rdquo;, people and institutions have to invent new HOW strategies and incentives and implementations-entirely new ways often fused with past and current &ldquo;successful&rdquo; initiatives and programs to achieve their purpose (Harvard Kennedy School, Baskerville).</p>

<h2><strong>HOW WISCONSIN CAN IN THE NEXT 20 YEARS CATCH UP ECONOMICALLY WITH MINNESOTA (&amp; THE NATION)</strong></h2>
<p>We are not delineating any alternative, concrete economic growth plan in addition to the many already proposed.** Rather, based on the experience from &ldquo;successful&rdquo; projects and initiatives in Wisconsin, elsewhere in the United States, and Overseas, we are suggesting that the following elements be considered in any HOW strategy, i.e., the serious effort to implement a dramatic 20-year Target to economically overtake Minnesota. Our approach will be different than their very successful run. But local business leaders, investors, entrepreneurs and skilled workers will also lead the way with the overall direction of state government.</p>
<p>** = Though we have attached on the home page one specific proposal for Legislators or other Public Servants to consider.</p>

<div class="grid-row">
  <div class="grid-col">
    <h3><strong>THE &ldquo;STRETCH&rdquo;</strong></h3>
    <p>Get our leaders to think BIG!</p>
    <a class="read-more" href="http://stretchtargets.letskeepbuilding.com/the-stretch/">Read more</a>
  </div>
  <div class="grid-col">
    <h3><strong>THE IMPLEMENTATION</strong></h3>
    <p>Gather expeditiously the best and broadest input from many quarters before developing concrete plans.</p>
    <a class="read-more" href="http://stretchtargets.letskeepbuilding.com/the-implementation/">Read more</a>
  </div>
  <div class="grid-col">
    <h3><strong>THE STATE GOVERNMENT</strong></h3>
    <p>Recognize limited state resources will not do it. Rather an all court 20 year press in an integrative state effort will.</p>
    <a class="read-more" href="http://stretchtargets.letskeepbuilding.com/the-state-government/">Read more</a>
  </div>
</div>

<div class="grid-row">
  <div class="grid-col">
    <h3><strong>THE TACTICS</strong></h3>
    <p>Increase the capital to fund growth!</p>
    <a class="read-more" href="http://stretchtargets.letskeepbuilding.com/the-tactics/">Read more</a>
  </div>
  <div class="grid-col">
    <h3><strong>THE QUALITY OF LIFE</strong></h3>
    <p>Excitement matters!</p>
    <a class="read-more" href="http://stretchtargets.letskeepbuilding.com/the-quality-of-life/">Read more</a>
  </div>
</div>
"""

write_page(
    os.path.join(BASE, "how-economy"),
    generate_page("How Economy", "How Economy", "how", how_economy_content, "how-economy/"),
)

# ============================================================
# 2. HOW EDUCATION
# ============================================================
how_education_content = """
<h2><strong>HOW WISCONSIN KIDS CAN CATCH UP IN THE NEXT 20 YEARS TO THE &lsquo;WORLD&rsquo;</strong></h2>
<h2><strong>IN MATH (SINGAPORE), SCIENCE (JAPAN), AND READING (CANADA)</strong></h2>

<p>Again, no formula or concrete plans are being suggested per se.** There will be many different ways for the 426 school districts of Wisconsin to reach the same, very difficult but urgent &ldquo;Stretch Targets&rdquo; in 20 years. The following elements are some that many experts and &ldquo;successful practitioners&rdquo; and international business people have found essential:</p>
<p>** = Though we have attached on the home page one specific proposal for Legislators &amp; other Public Servants to consider.</p>

<div class="grid-row">
  <div class="grid-col">
    <h3><strong>CRITICAL</strong></h3>
    <p>Bi-partisan long term-targets.</p>
    <a class="read-more" href="http://stretchtargets.letskeepbuilding.com/critical/">Read more</a>
  </div>
  <div class="grid-col">
    <h3><strong>THE CLASSROOM</strong></h3>
    <p>High student expectations and goals for all nonspecial education students.</p>
    <a class="read-more" href="http://stretchtargets.letskeepbuilding.com/the-classroom/">Read more</a>
  </div>
  <div class="grid-col">
    <h3><strong>THE TEACHING</strong></h3>
    <p>Teacher preparation</p>
    <a class="read-more" href="http://stretchtargets.letskeepbuilding.com/the-teaching/">Read more</a>
  </div>
</div>

<div class="grid-row">
  <div class="grid-col">
    <h3><strong>THE STRATEGY</strong></h3>
    <p>Strategic upgrading.</p>
    <a class="read-more" href="http://stretchtargets.letskeepbuilding.com/the-strategy/">Read more</a>
  </div>
  <div class="grid-col">
    <h3><strong>OTHER</strong></h3>
    <p>Overcoming poverty and family breakdown.</p>
    <a class="read-more" href="http://stretchtargets.letskeepbuilding.com/other/">Read more</a>
  </div>
</div>
"""

write_page(
    os.path.join(BASE, "how-education"),
    generate_page("How Education", "How Education", "how", how_education_content, "how-education/"),
)

# ============================================================
# 3. WHY
# ============================================================
why_content = """
<h2><strong>WHY DO WE NEED RADICAL CHANGE AND &ldquo;TARGETS&rdquo; IN OUR WISCONSIN ECONOMY AND EDUCATION?</strong></h2>
<p>Three reasons seem to stand out. (But we solicit your input for other motivations)</p>

<h2><strong>ONE. BUSINESS/JOBS AND QUALITY OF WORK</strong></h2>
<p>American and global companies invest in locations where there is much &lsquo;welcome&rsquo;, tax incentives, a growing industrial or enterprise base, a quality of life style for employees and their families to match their economic interests, and most always a quality work force. Despite our low WI unemployment numbers, there are not only over three million jobs at every national level, including at least 180,000 in Wisconsin, which are not being filled due to lack of qualified workers (Pres. Ray Cross, UW System, 1/15). It is as true in Watertown, WI as in Silicon Valley!</p>

<p>Business (and our advanced schools) today desperately need skilled workers (and graduate students) with fundamental tools that are globally competitive. If our Wisconsin economy begins to catch up with Minnesota, that will be even more so! With the momentous advances in technology now and in the future, one thing is certain. We may not know whether more welders or more futuristic 3-D manufacturing &lsquo;foreman&rsquo; are most needed in the next 10~20 years. (65% of careers in fifteen years likely don&rsquo;t exist yet!) But whatever, we do know that basic reading, writing and counting performance with the best in the world will be a fundamental MUST for all STEM and &lsquo;blue collar&rsquo; jobs of the future!</p>

<p>In addition, if a growing segment of our State&rsquo;s population due to poor skills and low paying jobs fall below the poverty line, Wisconsin companies will experience smaller markets/less demand/fewer retail consumers for their products and services.</p>

<h2><strong>TWO. REAL SOCIAL JUSTICE.</strong></h2>
<p>True, this educational &ldquo;Stretch Target&rdquo; is needed not only for &lsquo;slow learners&rsquo; but for all of our Wisconsin K-12 students who are not in special education. But our poorest students are the most undereducated among the poorest of all First World Countries (OECD Report). Furthermore, the educational achievement gaps between rich and poor students as well as the income gaps continue to grow in most Wisconsin communities. As important as short term welfare and nutrition programs are for children, the only way, with rare exceptions, for people to move out of poverty and into the middle class, is the traditional American route of excellent education. Global &ldquo;Targets&rdquo; where preparation begins at ages 4~5! If we wish to have smaller economic divisions in our Wisconsin society where many more people contribute, it will not happen because of mediocre, slightly improving K-12 education&hellip; or even Affirmative Action or the War on Poverty, as important as some of these programs have been during past eras. It WILL BE demanding, rigorous accountable education for all!</p>

<p>The Hebrew-Christian tradition of serving and feeding &ldquo;the widow and the orphan&rdquo; has for generations rightly been a driving force for social passion and movements in Wisconsin. Good! Let&rsquo;s keep that up! Yet, another biblical side to this issue which most Christian churches and synagogues pay far less attention to is &lsquo;getting the poor <em>out of</em> poverty&rsquo; and into jobs that can sustain a better, more dignified life style. The Psalmist says not only to feed the poor, but to &ldquo;<em>raise</em> the poor from the dust and <em>lift</em> the needy from the trash heap&rdquo; {Ps. 113:7}. Not just feed and free them, but give them back their families and dignity and the resources to regain self-sufficiency above the poverty line. In the New Testament <em>Magnificat</em> (Luke 1), Mary sings about &ldquo;&hellip;<em>lifting up</em> the lowly and filling the hungry with good things&rdquo; (not only food but&hellip;education&hellip; ample work preparation&hellip; jobs that support families). A reversal of fortunes! Let&rsquo;s address the <em>real</em> sources of the gaps, not just keep people alive and enabled!</p>

<p>In America and hopefully in Wisconsin, as our Declaration of Independence states: &ldquo;&hellip;all men (people) are created equal&hellip;and endowed with certain unalienable rights&hellip;&rdquo; Is not the right to &ldquo;the pursuit of happiness&rdquo;, among other things, to have equal access to very high quality education, like in many other countries? This has always been the main ladder of mobility for millions of Wisconsin immigrants/other ethnic groups over our history.</p>

<h2><strong>THREE. SECURITY FOR THE NATION.</strong></h2>
<p>If one looks at history, there are both domestic and international factors that &lsquo;bring down great nations&rsquo;. Domestically, Wisconsin and the nation must have sound, honest, moral government and institutions as well a high degree of well educated citizenry participation and a high quality, globally competitive economy. Internationally, we must develop the globally most advanced technology and military to survive as a leader. If our K-12 and advanced system is not able to develop the interest, enthusiasm, and knowledge of math and science, eventually we will succumb to other more powerful nations. In 2015, for example, in our world renowned UW-Madison in most strategic majors, the overwhelming number of graduate and professional students are not only not from Wisconsin, but not from the United States as well. (64% of Computer Science graduate students in 2015 were non-American, 89% in mechanical engineering; 80% in electrical engineering; 76% in statistics, 60% in mathematics; 79% in economics. Many non-Americans came from China.) Welcome! And they should be very welcome to long-term living/working in Wisconsin after graduation! Still, sooner or later, this domestic advanced education STEM &ldquo;gap&rsquo; also will catch up with the Republic. Don&rsquo;t let it happen, Wisconsin!</p>

<p>And if a nation can not read well, even in this digital age, its ability to know history, literature and politics will sadly be lacking; and citizen preparation for &lsquo;global participation&rsquo; and political and business and church leadership will be inadequate!</p>
"""

write_page(
    os.path.join(BASE, "why"),
    generate_page("Why", "Why", "why", why_content, "why/"),
)

# ============================================================
# 4. HISTORY
# ============================================================
history_content = """
<h2><strong>THE HISTORY OF</strong></h2>
<h2><strong>THIS &ldquo;STRETCH TARGET&rdquo; ENDEAVOR</strong></h2>

<p>When the Green Bay Packers work to accomplish a long term &ldquo;Stretch Target&rdquo;, a Super Bowl win, the challenge is very complex and the endeavor difficult. Without a well understood, simple scorecard/weekly NFL standings for this complex game we fans would not be able to track Packer progress or hold them &ldquo;accountable&rdquo;. The same applies for businesses and nonprofits with complex challenges and a need for radical change. Do these targets &amp; a scorecard not also apply to the economy and education of our great state? Please read on.</p>

<p>SO, WHO IS THIS GUY WHO STARTED THE ENDEAVOR? I, DAVE BASKERVILLE, am not a politician, economist, educator or activist. My votes over the past 55 plus years have been very &lsquo;independent&rsquo;. A native of Madison, Wisconsin, I have spent over forty years in international business, mainly for two USA companies. Since 1993, I retired with my wife back to our hometown, Madison, where for another twenty-two years, my post retirement work has been consulting for companies headquartered around the United States {<a href="http://www.baskervilleinternational.com/" style="color:#1e73be;">BaskervilleInternational.com</a>}. I have lived twenty years in East Asia, and on both coasts of America. I have traveled to over 100 countries for work and also for church/NGO-related volunteer activities. I have observed literally hundreds of offices and factories in many countries; and eventually looked into the education backgrounds of those entering the work force.. Closer to home, for many years my work took me to the Twin Cities, and I sensed there was a major difference between the Minnesota and Wisconsin economic climates.</p>

<p>A check of the data consistently confirmed that our beloved Wisconsin indeed was economically doing very poorly with slow good job growth vis a vis our neighbor to the north and other states. The data also confirmed my observations that American workers at most levels were ill prepared vis a vis their counterparts elsewhere in the world. In math, science and reading, problem solving. American kids at every level were behind their First World peers as they entered the workforce or higher education. I was very aware that such basic skills related very directly to where companies invest and create good paying jobs&hellip; and to how social justice and equality of opportunity in Wisconsin can be improved!</p>

<p>I have also noted that most fellow Wisconsinites that I have interacted with do not believe that our great State has long term direction or goals. Nor can citizens readily evaluate over time the impact of complex policies proposed or implemented with considerable rhetoric by both political parties. Does not Wisconsin need a sense of direction and a couple of critical long-term goals that will greatly improve our lot? And, yes, a scorecard that will allow their progress (or lack thereof) to be easily measured&hellip; much like a Green Bay Packer Scorecard?</p>

<p>I, needless to say, am not leading this endeavor alone. Retired UW-Madison Professor and advisor on education for several Governors, Jim Zellmer, who dogs us daily on the need for radical change and the will to &lsquo;stay the course&rsquo;. JIM ZELLMER, entrepreneur and long time operator of the blog, <a href="http://www.schoolinfosystem.org/" style="color:#1e73be;">schoolinfosystem.org</a>, is the main reason, I, Baskerville, began devoting a major share of my time to &ldquo;Stretch Targets&rdquo;. (The endeavor would not have happened without Jim!) PETER GASCOYNE is a Berkeley-trained economist and Senior Analyst who doggedly assures the numbers and analysis that we use are well documented and the most reliable. CHAN STROMAN, prominent real estate lawyer with a passion for &lsquo;much better&rsquo; Wisconsin education supports and critiques our efforts at every turn. CURT FUSZARD, retired bank executive and financial advisor, is a constant developer of contacts around the State. GREGORY ST. FORT, who is the CEO of <a href="http://www.letskeepbuilding.com/" style="color:#1e73be;">LetsKeepBuilding Inc and Executive Director of 100 State</a> is responsible for marketing and for this excellent Web page, and assures that the endeavor remains very relevant to his fellow Millennials. MARNIE GINSBERG of marnie@readingsimplified.com, a specialist in special education and KERRYANN DILORETO, senior analyst at the UW Survey Center have also been most helpful, especially with the launching and managing of Facebook!</p>

<p>If enough Wisconsinites buy into these bipartisan &ldquo;Targets&rdquo;, and read the Scorecard, AND persistently relay it and their concerns to their families and colleagues, the Governor, other political candidates, our local School Board Members, educators and the teachers unions&hellip;finally we WILL see, under our Statewide pressure, policies/focus/results that will in the long term enable us to reverse our 38 year economic slide vis a vis Minnesota&hellip;and allow us to again become one of America&rsquo;s top education states&hellip;and in the top 10 among the nations!</p>

<p>MANY OTHERS are stepping forward to volunteer their time and talents during this &lsquo;do or die&rsquo; 2018 year&hellip;or just signing up to read/pass on the Scorecard and the &ldquo;Stretch&rdquo; challenge. They include school teachers, students, business executives, economists, legislators, craftsman, construction workers and civil rights advocates. Some are Republicans and/or &lsquo;far Right&rsquo;. Some are Democrats and/or &lsquo;far Left&rsquo;. Most are politically somewhere &lsquo;in between&rsquo;. But increasingly, they are Wisconsin PEOPLE OF ALL WALKS OF LIFE who simply want much more from our great state. i.e. very significant but doable positive change! A long shot? Indeed&hellip;POSSIBLE? You bet!</p>
"""

write_page(
    os.path.join(BASE, "history"),
    generate_page("History", "History", "history", history_content, "history/"),
)

# ============================================================
# 5. APPROACH
# ============================================================
approach_content = """
<p>In the national comparisons with Minnesota and the international comparisons, we have used experienced, highly qualified academics and economists who have been most conscientious in making the difficult but reliable, trackable quantitative comparisons. For the economic comparison with Minnesota, the Survey of Current Business of the U.S. Department of Commerce: Bureau of Economic Analysis is used. In our education benchmarking, the Programme for International Student Assessment (PISA) from OECD which is updated every three years is used to show how the USA as a nation compares with some 70 other First World and Emerging Nations. The National Assessment of Education Progress test (NAEP), administered every other year, is used to compare Wisconsin with the rest of the USA states. (And please note our demographic desegregation that breaks down and enlightens the Wisconsin vs. Texas comparison on the &lsquo;RESOURCES&rsquo; page.) The State of Wisconsin, unlike at least nine other states does not offer as a state either the international PISA or the other international test, The Trends in International Mathematics and Science Study (TIMSS). Only currently Massachusetts and North Carolina offer PISA on a statewide basis. This is one reason that we in Wisconsin, with the exception of a few school districts that have taken at least one time the PISA test, are not aware of where the job skill competition takes place. For we do not have available the direct achievement comparison yet between the State and Other Countries.</p>

<p><strong>There is considerable misunderstanding within Wisconsin education circles regarding these tests.</strong> Unlike some thirty years ago, most leading countries including Singapore, Japan and Canada have more, not less 15 year olds taking these international tests than the United States. In the 2007 TIMSS tests, the United States had an exclusion rate of 9.2%, the highest of any country taking the test. Most were below 3%. (TIMSS 2007 Technical Report. More recent test data is likely the same.) And for PISA tests, a set, identical sampling method is used in all countries.</p>

<p><strong>And because our Wisconsin &ldquo;Best and the Brightest&rdquo; students no longer have the math, science and reading skills of their counterparts around the world (Ripley,. 2011, OECD) at age 15, the K-12 education problem is not one just for immigrants, the poor and certain minorities.</strong> As referred to in the HOW EDUCATION page, most recent OECD data (2012) tested 15 year old students in First World Countries and separately targeted three groups, the top socio-economic performers, a middle group, and the economically poorest and lowest achieving students in each country. The USA&rsquo;s &lsquo;Best and the Brightest&rsquo; vis a vis their peers came in # 30. Last place! AND problem solving and critical thinking are the key factors in these tests. There is no reason also to believe Wisconsin&rsquo;s groups would score differently. In the GMAT tests for acceptance into American MBA programs. Recent test scores of Americans students in the quantitative portion of the GMAT have fallen woefully below the scores of test takers worldwide (<em>WSJ</em> 11/5/14, Lindsay Gellman).</p>

<p>Incidentally, our <strong>Founding Fathers</strong> came from many walks of life, but were generally literate, well educated leaders. And the <strong>Original Wisconsin Progressives of Fighting Bob La Follette, Sr. and Young Bob</strong> were most concerned about improving the lot of the <strong>Common Man</strong>. How do you really raise up the Common Man and Woman in Wisconsin today? It seems a &lsquo;no brainer&rsquo; to say that the only way out of the current descending morale and material quality of life is via a world class K-12 education and many more available high value &lsquo;blue collar&rsquo; and STEM jobs. With most all K-12 Wisconsin students academically behind their international peers, the &lsquo;lifting up&rsquo; of the poor AND Common Folks via &ldquo;Stretch Targets&rdquo; is an effort that positively impacts <em>all</em> students and future workers. <strong>It thus deserves the support of <em>all</em> Wisconsinites!</strong></p>
"""

write_page(
    os.path.join(BASE, "approach"),
    generate_page("Approach", "Approach", "approach", approach_content, "approach/"),
)

# ============================================================
# 6. LEGISLATORS
# ============================================================
legislators_content = """
</div>
  </section>

  <!-- LEGISLATORS BLUE BANNER -->
  <section class="legislators-banner">
    <div class="l-section-h">
      <div style="flex:2;">
        <h2>Share This With Legislators &amp; Other Public Servants</h2>
        <p>We have a set of concrete action points that you now can put in the hands of your candidates &amp; Legislators &amp; Governor when asked: &ldquo;Well, what do you want me to do with this Stretch Targets?&rdquo;</p>
      </div>
      <div style="flex:1; display:flex; align-items:center; justify-content:center;">
        <a class="btn-download" href="http://bit.ly/2BA5M7v">DOWNLOAD PDF</a>
      </div>
    </div>
  </section>

  <section class="main-content" style="display:none;">
    <div class="l-section-h">
"""

write_page(
    os.path.join(BASE, "legislators"),
    generate_page("Legislators", "Legislators", "resources", legislators_content, "legislators/"),
)

# ============================================================
# 7. WI vs TX Education
# ============================================================
wi_vs_tx_content = """
<div class="two-col-row">
  <div class="two-col-left">
    <div class="fact-statement">
      <p>Per OECD testing, the <strong>&lsquo;Best &amp; Brightest&rsquo;</strong> in America (&amp; Wisconsin) are dead last in math/reading vs. all 15 of their First World counterpart &ldquo;Best &amp; Brightest&rdquo;!</p>
    </div>
    <div class="fact-statement">
      <p>The USA is #35 in <strong>world math scores</strong>!</p>
    </div>
    <div class="fact-statement">
      <p>In Finland, only one in ten applicants are admitted to <strong>teacher training</strong>, in South Korea 5%!</p>
    </div>
    <div class="fact-statement">
      <p>Texas spends $3,103 less <strong>per K-12 child</strong> than Wisconsin, yet their math and reading scores are substantially better!</p>
    </div>
    <div class="fact-statement">
      <p>Unlike at least eleven other states, Wisconsin does not take any tests that <strong>compare directly with scores of foreign countries</strong>!</p>
    </div>
  </div>
  <div class="two-col-right">
    <div class="slideshare-wrapper">
      <iframe src="https://www.slideshare.net/slideshow/embed_code/key/bGCaJkGpZKMPUa" width="100%" height="500" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" allowfullscreen></iframe>
      <p style="font-size:13px; color:#666; margin-top:8px;"><strong>How are we doing 2015 short version</strong> from <a href="https://www.slideshare.net/letskeepbuilding" style="color:#1e73be;">letskeepbuilding</a></p>
    </div>
  </div>
</div>
"""

write_page(
    os.path.join(BASE, "wi-vs-tx-education"),
    generate_page("WI vs TX Education", "WI vs TX Education", "resources", wi_vs_tx_content, "wi-vs-tx-education/"),
)

# ============================================================
# 8. RECENT NEWS
# ============================================================
recent_news_content = """
<p style="text-align:center; padding: 40px 0; color:#666; font-size:16px;">No recent news at this time. Please check back later.</p>
"""

write_page(
    os.path.join(BASE, "recent-news"),
    generate_page("Recent News", "Recent News", "recent-news", recent_news_content, "recent-news/"),
)

# ============================================================
# 9. PRESS
# ============================================================
press_content = """
<p>Thanks to everyone that has featured this movement. For press inquiries contact us <a href="https://stretchtargets.org/contact-us/" style="color:#1e73be;">here</a>.</p>

<ul>
  <li>Aug 3 2017 <a href="https://youtu.be/vI2EQHyBWxc">Channel 3000 For the Record</a></li>
  <li>July 26 2017 <a href="http://www.channel3000.com/madison-magazine/opinion/neil-heinen/heinen-stretching-a-little-for-long-term-changes/590081576">Madison Magazine &ndash; Heinen: Stretching a little for long-term changes</a></li>
  <li>May 24 2017 <a href="http://www.beloitdailynews.com/article/20170524/ARTICLE/170529905">Grassroots organizer addresses Wisconsin&rsquo;s future at Rotary Club</a></li>
  <li>April 2017 <a href="http://www.ibmadison.com/In-Business-Madison/April-2017/For-Baskerville-economic-progress-is-a-real-stretch/">Inbusiness: For Baskerville, economic progress is a real stretch</a></li>
  <li>Nov 4 2015 <a href="http://host.madison.com/wsj/news/opinion/column/guest/david-baskerville-madison-schools-need-global-goals/article_308b2c99-eafe-56f5-b299-8db147a0e1a4.html">Wisconsin State Journal: David Baskerville: Madison schools need global goal</a></li>
</ul>

<div class="grid-row">
  <div class="grid-col" style="background:#fff; border:none; padding:0;">
    <div class="video-wrapper">
      <iframe src="https://www.youtube.com/embed/iMZssS46DK0" title="For The Record" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
    <p style="text-align:center; font-size:13px; color:#666;">For The Record: Stretching for a more competitive state, smarter kids</p>
  </div>
  <div class="grid-col" style="background:#fff; border:none; padding:0;">
    <div class="video-wrapper">
      <iframe src="https://player.vimeo.com/video/138755286?portrait=0&color=00adef" title="Wisconsin's Scorecard" allow="autoplay; fullscreen" allowfullscreen></iframe>
    </div>
    <p style="text-align:center; font-size:13px; color:#666;">Wisconsin&rsquo;s Scorecard</p>
  </div>
  <div class="grid-col" style="background:#fff; border:none; padding:0;">
    <div class="video-wrapper">
      <iframe src="https://www.youtube.com/embed/WpzPV8-LBRg" title="Morning Minute" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
    <p style="text-align:center; font-size:13px; color:#666;">Morning Minute: Madison Rotary Club - Dave Baskerville on Wisconsin Stretch Targets</p>
  </div>
</div>
"""

write_page(
    os.path.join(BASE, "press"),
    generate_page("Press", "Press", "press", press_content, "press/"),
)

# ============================================================
# 10. SIGN UP
# ============================================================
signup_content = """
<p>Why sign up? Simply to receive 2x per year this Scorecard plus bi-monthly one liners to keep you updated on Wisconsin&rsquo;s progress vs. the USA and world and to provide you with an easy yet informed, intentional way to make your concern known to our leaders. Nothing else!</p>
"""

write_page(
    os.path.join(BASE, "signup"),
    generate_page("Sign Up", "Sign Up", "signup", signup_content, "signup/"),
)

# ============================================================
# 11. CONTACT US
# ============================================================
contact_us_content = """
<p>Email <a href="mailto:donna@stretchtargets.org" style="color:#1e73be; font-weight:700;">donna@stretchtargets.org</a> or use the below contact form.</p>

<p>You can also like our Facebook Page &ndash; <a href="https://www.facebook.com/wisconsinstretchtargets" style="color:#1e73be;">https://www.facebook.com/wisconsinstretchtargets</a></p>
"""

write_page(
    os.path.join(BASE, "contact-us"),
    generate_page("Contact Us", "Contact Us", "contact-us", contact_us_content, "contact-us/"),
)

print("\n=== All 11 pages generated successfully! ===")
