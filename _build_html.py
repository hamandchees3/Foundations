#!/usr/bin/env python3
"""Convert AI_Foundations_Summer2026.md to print-friendly HTML matching the style of AI_Foundations_Print.html.

Run from the Foundations directory:
    python3 _build_html.py
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "AI_Foundations_Summer2026.md"
DST = HERE / "AI_Foundations_Summer2026.html"

CSS = """        /* Print-optimized styles */
        @page {
            size: letter;
            margin: 0.75in 0.85in;
        }

        @media print {
            body {
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }

            .no-print {
                display: none !important;
            }

            h2.chapter {
                page-break-before: always;
            }

            h2, h3 {
                page-break-after: avoid;
            }

            ul, ol {
                page-break-inside: avoid;
            }
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Georgia', 'Times New Roman', Times, serif;
            font-size: 11pt;
            line-height: 1.65;
            color: #333;
            max-width: 7in;
            margin: 0 auto;
            padding: 0.5in;
            background: white;
        }

        h1 {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            font-size: 26pt;
            font-weight: 600;
            color: #1e3a5f;
            text-align: center;
            margin-top: 1.5in;
            margin-bottom: 0.3em;
            letter-spacing: -0.02em;
        }

        h1 + p {
            text-align: center;
            font-size: 11pt;
            color: #666;
            font-style: italic;
            margin-bottom: 0.5in;
        }

        h2 {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            font-size: 16pt;
            font-weight: 600;
            color: #1e3a5f;
            margin-top: 1.5em;
            margin-bottom: 0.6em;
            border-bottom: 1.5px solid #ddd;
            padding-bottom: 0.2em;
        }

        h2.chapter {
            margin-top: 0;
            padding-top: 0.5in;
            border-bottom: 2px solid #1e3a5f;
        }

        h2.chapter .chapter-num {
            display: block;
            font-size: 10pt;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.15em;
            color: #8b2942;
            margin-bottom: 0.15em;
        }

        h2.chapter .chapter-title {
            display: block;
        }

        h3 {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            font-size: 12pt;
            font-weight: 600;
            color: #374151;
            margin-top: 1.25em;
            margin-bottom: 0.4em;
        }

        p {
            margin-top: 0;
            margin-bottom: 0.85em;
            text-align: justify;
            hyphens: auto;
            -webkit-hyphens: auto;
        }

        a {
            color: #1e3a5f;
            text-decoration: none;
        }

        @media print {
            a {
                text-decoration: underline;
                text-decoration-color: #ccc;
            }
        }

        strong {
            font-weight: 600;
            color: #1e3a5f;
        }

        em {
            font-style: italic;
        }

        ul, ol {
            margin-top: 0;
            margin-left: 1.25em;
            margin-bottom: 0.85em;
        }

        li {
            margin-bottom: 0.4em;
            line-height: 1.65;
        }

        li > ul, li > ol {
            margin-top: 0.4em;
            margin-bottom: 0;
        }

        h2 + p, h3 + p {
            margin-top: 0;
        }

        h2 + ul, h3 + ul {
            margin-top: 0;
        }

        p + ul {
            margin-top: -0.4em;
        }

        hr {
            border: none;
            border-top: 1px solid #e5e7eb;
            margin: 1.5em 0;
        }

        .title-page {
            text-align: center;
            page-break-after: always;
        }

        .title-page h1 {
            margin-top: 2.5in;
        }

        h2:first-of-type {
            margin-top: 0;
        }

        h2 + ul {
            list-style: none;
            margin-left: 0;
            padding-left: 0;
        }

        h2 + ul li {
            margin-bottom: 0.4em;
            padding-left: 0;
        }

        h2 + ul li a {
            color: #1e3a5f;
            text-decoration: none;
        }

        h2 + ul li a:hover {
            text-decoration: underline;
        }

        .print-btn {
            position: fixed;
            top: 20px;
            right: 20px;
            background: #1e3a5f;
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 14px;
            font-weight: 500;
            border-radius: 6px;
            cursor: pointer;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
            z-index: 1000;
        }

        .print-btn:hover {
            background: #2d4a6f;
        }

        @media print {
            .print-btn {
                display: none;
            }
        }

        /* ===== Sidebar TOC (scroll-spy) ===== */
        .toc-sidebar {
            position: fixed;
            top: 0;
            left: 0;
            width: 220px;
            height: 100vh;
            overflow-y: auto;
            background: #fafaf7;
            border-right: 1px solid #e5e7eb;
            padding: 32px 18px 32px 24px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            font-size: 11.5px;
            line-height: 1.4;
            z-index: 500;
            box-sizing: border-box;
            transform: translateX(-100%);
            transition: transform 0.2s ease-out, box-shadow 0.2s;
        }

        .toc-sidebar-heading {
            font-size: 10px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.15em;
            color: #8b2942;
            margin-bottom: 1em;
            padding-bottom: 0.6em;
            border-bottom: 1px solid #e5e7eb;
            font-family: inherit;
        }

        .toc-sidebar-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .toc-sidebar-list li {
            margin-bottom: 0.15em;
            border-left: 2px solid transparent;
            transition: border-color 0.15s, background 0.15s;
        }

        .toc-sidebar-list li a {
            color: #5b6478;
            text-decoration: none;
            display: block;
            padding: 6px 0 6px 10px;
            transition: color 0.15s;
        }

        .toc-sidebar-list li a:hover {
            color: #1e3a5f;
        }

        .toc-sidebar-list li.active {
            border-left-color: #8b2942;
            background: rgba(139, 41, 66, 0.05);
        }

        .toc-sidebar-list li.active a {
            color: #1e3a5f;
            font-weight: 600;
        }

        .toc-num {
            display: inline-block;
            width: 1.6em;
            color: #999;
            font-variant-numeric: tabular-nums;
            font-size: 10px;
        }

        .toc-sidebar-list li.active .toc-num {
            color: #8b2942;
        }

        .toc-toggle {
            position: fixed;
            bottom: 20px;
            left: 20px;
            background: #1e3a5f;
            color: white;
            border: none;
            padding: 10px 18px;
            font-size: 13px;
            font-weight: 500;
            border-radius: 24px;
            cursor: pointer;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            box-shadow: 0 2px 12px rgba(0,0,0,0.18);
            z-index: 1000;
            display: none;
        }

        .toc-toggle:hover {
            background: #2d4a6f;
        }

        .toc-backdrop {
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.3);
            z-index: 499;
        }

        .toc-backdrop.open {
            display: block;
        }

        /* Desktop: sidebar visible, no toggle */
        @media (min-width: 1100px) {
            .toc-sidebar {
                transform: translateX(0);
            }
        }

        /* Narrow viewports: sidebar becomes a drawer triggered by the toggle */
        @media (max-width: 1099px) {
            .toc-toggle {
                display: block;
            }
            .toc-sidebar.open {
                transform: translateX(0);
                box-shadow: 4px 0 20px rgba(0,0,0,0.15);
            }
        }

        @media print {
            .toc-sidebar,
            .toc-toggle,
            .toc-backdrop {
                display: none !important;
            }
        }
"""


def escape_html(text: str) -> str:
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;"))


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
ITALIC_RE = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")
INLINE_CODE_RE = re.compile(r"`([^`]+)`")


def render_inline(text: str) -> str:
    """Convert markdown inline syntax to HTML.

    Note: the source markdown uses raw '<' and '>' characters in some places
    (e.g. '>70%'), so we cannot blanket-escape HTML. We instead process
    markdown constructs in a known-safe order and only escape user-visible
    angle brackets that are NOT part of HTML tags we emit.
    """
    # Inline code -> <code>
    text = INLINE_CODE_RE.sub(lambda m: f"<code>{escape_html(m.group(1))}</code>", text)

    # Links: [label](url) -> <a href="url">label</a>
    def link_repl(m):
        label = m.group(1)
        url = m.group(2)
        # Allow markdown inside label
        label = BOLD_RE.sub(r"<strong>\1</strong>", label)
        label = ITALIC_RE.sub(r"<em>\1</em>", label)
        return f'<a href="{url}">{label}</a>'

    text = LINK_RE.sub(link_repl, text)

    # Bold
    text = BOLD_RE.sub(r"<strong>\1</strong>", text)
    # Italic (single *)
    text = ITALIC_RE.sub(r"<em>\1</em>", text)

    return text


CHAPTER_RE = re.compile(r"^## Chapter (\d+): (.+)$")


def is_chapter_heading(line: str):
    m = CHAPTER_RE.match(line)
    if not m:
        return None
    return int(m.group(1)), m.group(2)


def convert(md: str) -> str:
    lines = md.split("\n")
    out = []

    # Skip past the H1 title block — we render it manually for the title page.
    # The markdown starts with "# AI Foundations for Policymakers" then a blank
    # line, then a "## AI Foundations for Policymakers" intro section.
    i = 0
    # Find and skip the H1 line
    while i < len(lines) and not lines[i].startswith("# "):
        i += 1
    # Now lines[i] is the H1 — skip it
    i += 1

    # Emit the title page
    out.append('<div class="title-page">')
    out.append('<h1>AI Foundations for Policymakers</h1>')
    out.append('<p>Conservative AI Policy Fellowship – Summer 2026 Edition</p>')
    out.append('</div>')
    out.append('')

    # Now walk the remaining content. Track state: are we in a list, paragraph buffer, etc.
    in_list = False
    list_buf = []

    def flush_list():
        nonlocal in_list, list_buf
        if in_list and list_buf:
            out.append("<ul>")
            for item in list_buf:
                out.append(f"<li>{render_inline(item)}</li>")
            out.append("</ul>")
            out.append("")
        in_list = False
        list_buf = []

    para_buf = []

    def flush_para():
        nonlocal para_buf
        if para_buf:
            text = " ".join(para_buf).strip()
            if text:
                out.append(f"<p>{render_inline(text)}</p>")
                out.append("")
        para_buf = []

    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip()

        # Blank line
        if stripped == "":
            flush_para()
            flush_list()
            i += 1
            continue

        # Horizontal rule
        if stripped == "---":
            flush_para()
            flush_list()
            out.append("<hr>")
            out.append("")
            i += 1
            continue

        # Chapter heading
        ch = is_chapter_heading(stripped)
        if ch:
            flush_para()
            flush_list()
            num, title = ch
            out.append(
                f'<h2 id="chapter-{num}" class="chapter">'
                f'<span class="chapter-num">Chapter {num}</span>'
                f'<span class="chapter-title">{render_inline(title)}</span></h2>'
            )
            out.append("")
            i += 1
            continue

        # Other H2
        if stripped.startswith("## "):
            flush_para()
            flush_list()
            heading = stripped[3:]
            out.append(f"<h2>{render_inline(heading)}</h2>")
            out.append("")
            i += 1
            continue

        # H3
        if stripped.startswith("### "):
            flush_para()
            flush_list()
            heading = stripped[4:]
            out.append(f"<h3>{render_inline(heading)}</h3>")
            out.append("")
            i += 1
            continue

        # List item
        if stripped.startswith("- "):
            flush_para()
            if not in_list:
                in_list = True
                list_buf = []
            # Capture this item; handle continuation lines
            item_text = stripped[2:]
            # Look ahead for continuation (indented or wrap) lines until blank or new bullet
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if nxt.strip() == "":
                    break
                if nxt.startswith("- ") or nxt.startswith("## ") or nxt.startswith("### "):
                    break
                # Continuation line — append with a space
                item_text += " " + nxt.strip()
                j += 1
            list_buf.append(item_text)
            i = j
            continue

        # Paragraph text
        flush_list()
        para_buf.append(stripped)
        i += 1

    flush_para()
    flush_list()

    return "\n".join(out)


CHAPTERS = [
    (1, "What Is Computation?"),
    (2, "Machine Learning"),
    (3, "What Is Learning, Anyway? (Optimization and Training Dynamics)"),
    (4, "Semantic Understanding and Generative AI"),
    (5, "Emergent Abilities and the Power of Scale"),
    (6, "Reasoning Models – Chain-of-Thought and Advanced Prompting"),
    (7, "The Alignment Problem – Ensuring AI Systems Reflect Human Values"),
    (8, "Safety Beyond Misalignment"),
    (9, "The AI Industry Landscape (Who's Leading and What They're Doing)"),
    (10, "US AI Policy"),
    (11, "China and AI Competition"),
    (12, "AI and the Labor Market"),
    (13, "AI and Scientific Discovery"),
]

# Compact titles for the sidebar TOC (the full titles are too long for a 220px rail).
SIDEBAR_TITLES = {
    1: "What Is Computation?",
    2: "Machine Learning",
    3: "What Is Learning, Anyway?",
    4: "Semantic Understanding & GenAI",
    5: "Emergent Abilities & Scale",
    6: "Reasoning Models",
    7: "The Alignment Problem",
    8: "Safety Beyond Misalignment",
    9: "The AI Industry Landscape",
    10: "US AI Policy",
    11: "China and AI Competition",
    12: "AI and the Labor Market",
    13: "AI and Scientific Discovery",
}


def build_toc():
    """Build the in-document (printable) table of contents block."""
    lines = ['<h2>AI Foundations for Policymakers - Table of Contents</h2>', '', '<ul>']
    for n, title in CHAPTERS:
        lines.append(f'<li><a href="#chapter-{n}">Chapter {n}: {title}</a></li>')
    lines.append('</ul>')
    lines.append('')
    return "\n".join(lines)


def build_sidebar():
    """Build the fixed-position scroll-spy sidebar (hidden in print)."""
    lines = [
        '<nav class="toc-sidebar no-print" id="toc-sidebar" aria-label="Table of contents">',
        '    <div class="toc-sidebar-heading">Contents</div>',
        '    <ol class="toc-sidebar-list">',
    ]
    for n, _ in CHAPTERS:
        short = SIDEBAR_TITLES[n]
        lines.append(
            f'        <li data-chapter-id="chapter-{n}">'
            f'<a href="#chapter-{n}"><span class="toc-num">{n}</span>{short}</a></li>'
        )
    lines.append('    </ol>')
    lines.append('</nav>')
    lines.append('<div class="toc-backdrop no-print" id="toc-backdrop"></div>')
    lines.append(
        '<button class="toc-toggle no-print" id="toc-toggle" '
        'aria-label="Open table of contents" aria-expanded="false">☰ Contents</button>'
    )
    return "\n".join(lines)


SCROLLSPY_JS = """<script>
(function() {
    var chapters = Array.prototype.slice.call(document.querySelectorAll('h2.chapter'));
    var items = Array.prototype.slice.call(document.querySelectorAll('.toc-sidebar-list li'));
    var idToLi = {};
    items.forEach(function(li) { idToLi[li.getAttribute('data-chapter-id')] = li; });

    var sidebar = document.getElementById('toc-sidebar');
    var toggle = document.getElementById('toc-toggle');
    var backdrop = document.getElementById('toc-backdrop');

    function updateActive() {
        if (!chapters.length) return;
        var scrollPos = window.scrollY + window.innerHeight * 0.25;
        var active = chapters[0];
        for (var i = 0; i < chapters.length; i++) {
            if (chapters[i].offsetTop <= scrollPos) {
                active = chapters[i];
            } else {
                break;
            }
        }
        items.forEach(function(li) { li.classList.remove('active'); });
        var activeLi = idToLi[active.id];
        if (activeLi) {
            activeLi.classList.add('active');
            // Keep the active item in view inside a scrollable sidebar.
            var sidebarRect = sidebar.getBoundingClientRect();
            var liRect = activeLi.getBoundingClientRect();
            if (liRect.top < sidebarRect.top || liRect.bottom > sidebarRect.bottom) {
                activeLi.scrollIntoView({ block: 'center' });
            }
        }
    }

    var pending = false;
    function onScroll() {
        if (!pending) {
            pending = true;
            window.requestAnimationFrame(function() {
                updateActive();
                pending = false;
            });
        }
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    updateActive();

    // ---- Drawer behavior (narrow viewports) ----
    function isNarrow() { return window.matchMedia('(max-width: 1099px)').matches; }

    function openDrawer() {
        sidebar.classList.add('open');
        backdrop.classList.add('open');
        toggle.setAttribute('aria-expanded', 'true');
    }
    function closeDrawer() {
        sidebar.classList.remove('open');
        backdrop.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
    }

    toggle.addEventListener('click', function() {
        if (sidebar.classList.contains('open')) closeDrawer();
        else openDrawer();
    });
    backdrop.addEventListener('click', closeDrawer);

    // Escape key closes the drawer
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && sidebar.classList.contains('open')) closeDrawer();
    });

    // Smooth-scroll on chapter link clicks; close drawer on mobile after navigation.
    document.querySelectorAll('a[href^="#chapter-"]').forEach(function(a) {
        a.addEventListener('click', function(e) {
            var id = a.getAttribute('href').slice(1);
            var el = document.getElementById(id);
            if (el) {
                e.preventDefault();
                el.scrollIntoView({ behavior: 'smooth', block: 'start' });
                if (history.pushState) history.pushState(null, '', '#' + id);
            }
            if (isNarrow()) closeDrawer();
        });
    });
})();
</script>
"""


def build_intro():
    """Build the executive summary / preface block."""
    return (
        '<h2>About this handbook</h2>\n\n'
        '<p>This handbook introduces the fundamentals of AI, explains how modern AI systems '
        'like neural networks learn and make decisions, and surveys the most consequential '
        'developments through mid-2026 — from reasoning models and autonomous coding agents '
        'to differential-access governance experiments like Project Glasswing, the H200 '
        'export-license regime, and the unfolding AI IPO wave. By the end you should have a '
        'working understanding of how AI works, what it can (and can\'t) do, who the major '
        'players are, and which policy questions are on the near horizon.</p>\n'
    )


def main():
    md = SRC.read_text()
    body = convert(md)

    # Strip the markdown source's TOC (we'll insert our own structured one),
    # plus the intro <h2> section that the converter emitted as a normal h2.
    # The structure produced by convert() begins with:
    #   title-page div, then "## AI Foundations for Policymakers" intro
    #   then "## AI Foundations for Policymakers - Table of Contents" with bullets
    #   then "<hr>", then Chapter 1 etc.
    # We'll surgically replace those first two sections with our intro + TOC.

    # Find the index of "<h2>AI Foundations for Policymakers - Table of Contents</h2>"
    # and the next <hr>, and replace the block from after title-page through that <hr>.
    title_end = body.find("</div>") + len("</div>")
    after_title = body[title_end:]

    # Find first chapter h2
    chapter1_pos = after_title.find('<h2 id="chapter-1"')
    if chapter1_pos < 0:
        sys.exit("Could not locate Chapter 1 heading in converted body.")
    head_block = body[:title_end]
    rest_block = after_title[chapter1_pos:]

    middle = "\n\n" + build_intro() + "\n<hr>\n\n" + build_toc() + "\n<hr>\n\n"

    body = head_block + middle + rest_block

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Foundations for Policymakers — Summer 2026</title>
    <style>
{CSS}    </style>
</head>
<body>
{build_sidebar()}
    <button class="print-btn no-print" onclick="window.print()">Print / Save as PDF</button>

{body}

{SCROLLSPY_JS}
</body>
</html>
"""

    DST.write_text(html)
    print(f"Wrote {DST}")
    print(f"Source: {len(md):,} chars -> Output: {len(html):,} chars")


if __name__ == "__main__":
    main()
