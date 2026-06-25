// Self-hosted GPT-Vis-SSR render endpoint for the AntV `chart` MCP server.
//
// The MCP server (configured with VIS_REQUEST_SERVER) POSTs a chart spec here and
// expects { success, resultObj } back, where resultObj is an image URL/data-URI.
// We render with @antv/gpt-vis-ssr and inject the repo design tokens so MCP-generated
// charts match the matplotlib/D2/ECharts pack.
//
// Brand colors/fonts come from ../brand-theme.json (regenerate with
//   PYTHONPATH=. python3 -m scripts.visuals.brand_theme
// so tokens.py stays the single source of truth).
//
// Run:
//   cd scripts/visuals/charts_js/ssr && npm install && npm start
//   export VIS_REQUEST_SERVER="http://localhost:3000/api/gpt-vis"
//
// CommonJS on purpose: @antv/gpt-vis-ssr transitively `require()`s .css files, which
// Node cannot parse. We stub the .css extension before loading the package.

const path = require('node:path');
const { readFileSync } = require('node:fs');

// Stub CSS (and other style) requires so the SSR dependency tree loads under Node.
for (const ext of ['.css', '.less', '.scss']) {
  require.extensions[ext] = () => {};
}

const express = require('express');
const { render } = require('@antv/gpt-vis-ssr');

const PORT = Number(process.env.PORT) || 3000;
const brand = JSON.parse(
  readFileSync(path.resolve(__dirname, '../brand-theme.json'), 'utf-8'),
);

// Apply the brand palette/background/font to a chart spec when the caller left them unset.
function applyBrand(spec) {
  const out = { ...spec };
  if (out.palette == null) out.palette = brand.palette;
  if (out.theme == null) out.theme = 'default';
  if (out.background == null) out.background = brand.backgroundColor;
  if (out.texture == null) out.texture = 'default';
  return out;
}

const app = express();
app.use(express.json({ limit: '4mb' }));

app.get('/healthz', (_req, res) => {
  res.json({ ok: true, theme: brand.name });
});

app.post('/api/gpt-vis', async (req, res) => {
  try {
    const spec = applyBrand(req.body || {});
    const vis = await render(spec);
    const dataUri = `data:image/png;base64,${vis.toBuffer().toString('base64')}`;
    res.json({ success: true, resultObj: dataUri });
  } catch (err) {
    res.json({ success: false, errorMessage: String((err && err.message) || err) });
  }
});

app.listen(PORT, () => {
  console.log(`gpt-vis-ssr (${brand.name}) listening on http://localhost:${PORT}/api/gpt-vis`);
});
