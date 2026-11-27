document.querySelectorAll(".copy").forEach(b => b.onclick = async () => {
  try { await navigator.clipboard.writeText(b.closest(".panel").querySelector("code").innerText); b.textContent = "Copied"; } catch { b.textContent = "Select to copy"; }
  setTimeout(() => b.textContent = "Copy", 1400);
});

// Each step has its own tabs, so a click only changes the step it is in.
document.querySelectorAll("[data-tab]").forEach(t => t.onclick = () => {
  const step = t.closest(".setup");
  step.querySelectorAll("[data-tab]").forEach(x => x.setAttribute("aria-selected", x === t));
  step.querySelectorAll("[data-panel]").forEach(p => p.hidden = p.dataset.panel !== t.dataset.tab);
});

const trace = document.getElementById("trace-card");
const traceToggle = document.getElementById("trace-toggle");
if (trace && traceToggle) traceToggle.onclick = () => {
  const paused = trace.classList.toggle("is-paused");
  traceToggle.setAttribute("aria-pressed", paused);
  traceToggle.querySelector("span").textContent = paused ? "Play" : "Pause";
};

// ASCII sunrise: density falls off with distance from a sun below the bottom edge.
const pre = document.getElementById("ascii");
function draw() {
  const cols = Math.ceil(pre.clientWidth / 7.2), rows = Math.ceil(pre.clientHeight / 14);
  const cx = cols * .72, cy = rows * 1.05, chars = " .-->>00";
  let out = "";
  for (let y = 0; y < rows; y++) {
    for (let x = 0; x < cols; x++) {
      const d = Math.hypot((x - cx) / 2.1, y - cy) / rows;
      const ray = Math.sin(Math.atan2(y - cy, x - cx) * 14) * .06;
      const v = 1.15 - d + ray;
      out += chars[Math.max(0, Math.min(chars.length - 1, Math.floor(v * chars.length)))];
    }
    out += "\n";
  }
  pre.textContent = out;
}
if (pre) { draw(); addEventListener("resize", draw); }
