#!/usr/bin/env python3
"""Write the text in copy.md into every page. Run: python3 build.py"""
import html
import re
import sys
from pathlib import Path

here = Path(__file__).parent


def parse(md):
    """`## name` starts a text. A `# ` line ends it, so it works as a divider."""
    copy, key = {}, None
    for line in md.splitlines():
        if line.startswith("## "):
            key = line.split()[1]  # anything after the name is a note for the writer
            if key in copy:
                sys.exit(f"copy.md has {key} twice")
            copy[key] = ""
        elif line.startswith("# "):
            key = None
        elif key:
            copy[key] = " ".join(f"{copy[key]} {line}".split())
    return copy


def render(text):
    """Escape the text, then turn `x` into code and *x* into em."""
    parts = html.escape(text, quote=False).split("`")
    for i, part in enumerate(parts):  # odd parts sit between backticks
        parts[i] = f"<code>{part}</code>" if i % 2 else re.sub(r"\*(.+?)\*", r"<em>\1</em>", part)
    return "".join(parts)


assert render("a `b*` *c* & d") == "a <code>b*</code> <em>c</em> &amp; d"

copy = parse((here / "copy.md").read_text())
used = set()


def text(key):
    if not copy.get(key):
        sys.exit(f"copy.md has no text for {key}")
    used.add(key)
    return copy[key]


# ponytail: a regex, not an HTML parser. A data-t element must not hold
# another element of its own tag. Use a real parser if that ever gets in the way.
slot = re.compile(r'(<(\w+)\b[^>]*\bdata-t="([\w-]+)"[^>]*>)(.*?)(</\2>)', re.S)
# One page per product: Sunriser at the root, then Nightstar. All take their text from copy.md.
pages = ["index.html", "nightstar/index.html"]
outs = {}
for name in pages:
    out = slot.sub(lambda m: m[1] + render(text(m[3])) + m[5], (here / name).read_text())
    # The description lives in an attribute, so it has its own rule.
    meta = r'(<meta name="description" data-t="([\w-]+)" content=")[^"]*'
    outs[name] = re.sub(meta, lambda m: m[1] + html.escape(text(m[2])), out)

if extra := sorted(copy.keys() - used):
    sys.exit(f"copy.md has names the page does not use: {', '.join(extra)}")
for name, out in outs.items():
    (here / name).write_text(out)
print(f"{len(used)} texts written to {len(pages)} pages")
