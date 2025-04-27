from datetime import datetime

def build_index_html(articles, feeds):
    now_utc = datetime.utcnow().strftime("%d %b %Y, %H:%M UTC")

    # Prepare the sources list for the source filter
    source_filters_html = ""
    for feed in feeds:
        source_filters_html += f"""<label><input type="checkbox" class="sourceFilter" value="{feed['uniqueid']}" checked> {feed['source']}</label><br>"""

    # Prepare the initial table rows
    rows_html = ""
    for article in articles:
        date_display = article["date"] if article["date"] else ""
        row_class = "missing-date" if not article["date"] else ""
        rows_html += f"""<tr class="{row_class}" data-source="{article['source_id']}" data-date="{article['date']}" data-title="{article['title']}">
            <td>{date_display}</td>
            <td>{article['source']}</td>
            <td><a href="{article['link']}" target="_blank">{article['title']}</a></td>
        </tr>"""

    # Full HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>My News Feed</title>
<style>
  body {{ font-family: Arial, sans-serif; margin: 40px; }}
  table {{ border-collapse: collapse; width: 100%; }}
  th, td {{ text-align: left; padding: 8px; border-bottom: 1px solid #ddd; }}
  th {{ background-color: #f2f2f2; cursor: pointer; }}
  .missing-date td:first-child {{ color: gray; }}
  .filter-section {{ margin-bottom: 20px; }}
  .filter-group {{ margin-bottom: 10px; }}
</style>
</head>
<body>
<h2>My News Feed</h2>
<p><em>Page generated on {now_utc}</em></p>

<div class="filter-section">
  <div class="filter-group">
    <strong>Filter by source:</strong><br>
    {source_filters_html}
  </div>
  <div class="filter-group">
    <strong>Filter by time:</strong><br>
    <select id="timeFilter">
      <option value="all">All time</option>
      <option value="24h">Past 24 hours</option>
      <option value="48h" selected>Past 48 hours</option>
      <option value="7d">Past week</option>
    </select>
  </div>
  <div class="filter-group">
    <strong>Search titles:</strong><br>
    <input type="text" id="searchBox" placeholder="Type keywords..." />
  </div>
  <div class="filter-group">
    <button onclick="resetFilters()">Reset Filters</button>
  </div>
</div>

<table id="newsTable">
<thead>
<tr>
  <th onclick="sortTable(0)">Date ▲▼</th>
  <th onclick="sortTable(1)">Source ▲▼</th>
  <th>Title</th>
</tr>
</thead>
<tbody>
{rows_html}
</tbody>
</table>

<script>
// --- Helper Functions ---
function getUrlParams() {{
    const params = new URLSearchParams(window.location.search);
    return {{
        sources: params.get('sources') ? params.get('sources').split(',') : [],
        time: params.get('time') || '48h',
        search: params.get('search') || ''
    }};
}}

function updateUrlParams() {{
    const sources = Array.from(document.querySelectorAll('.sourceFilter:checked')).map(cb => cb.value);
    const time = document.getElementById('timeFilter').value;
    const search = document.getElementById('searchBox').value.trim();

    const params = new URLSearchParams();
    if (sources.length) params.set('sources', sources.join(','));
    if (time) params.set('time', time);
    if (search) params.set('search', search);

    const newUrl = window.location.pathname + '?' + params.toString();
    window.history.replaceState(null, '', newUrl);
}}

function parseBooleanSearch(query) {{
    query = query.trim();
    if (!query) return () => true;

    let terms = [];
    let current = '';
    let inQuotes = false;

    for (let i = 0; i < query.length; i++) {{
        const char = query[i];
        if (char === '"') {{
            inQuotes = !inQuotes;
            if (!inQuotes && current.length) {{
                terms.push({{ type: 'TERM', value: current.toLowerCase() }});
                current = '';
            }}
        }} else if (!inQuotes && /\s/.test(char)) {{
            if (current.length) {{
                if (current.toUpperCase() === 'AND' || current.toUpperCase() === 'OR') {{
                    terms.push({{ type: 'OP', value: current.toUpperCase() }});
                }} else {{
                    terms.push({{ type: 'TERM', value: current.toLowerCase() }});
                }}
                current = '';
            }}
        }} else {{
            current += char;
        }}
    }}
    if (current.length) {{
        terms.push({{ type: 'TERM', value: current.toLowerCase() }});
    }}

    if (!terms.length) return () => true;

    return function(title) {{
        title = title.toLowerCase();
        let result = null;
        let op = 'AND';
        for (const term of terms) {{
            if (term.type === 'OP') {{
                op = term.value;
            }} else {{
                const match = title.includes(term.value);
                if (result === null) {{
                    result = match;
                }} else if (op === 'AND') {{
                    result = result && match;
                }} else if (op === 'OR') {{
                    result = result || match;
                }}
            }}
        }}
        return result;
    }};
}}

// --- Filter and sort logic ---
function applyFilters() {{
    const params = getUrlParams();
    const sourceSet = new Set(params.sources);
    const filterTime = params.time;
    const searchFn = parseBooleanSearch(params.search);

    const now = new Date();

    document.querySelectorAll('#newsTable tbody tr').forEach(row => {{
        const source = row.getAttribute('data-source');
        const dateStr = row.getAttribute('data-date');
        const title = row.getAttribute('data-title');

        let show = true;

        if (params.sources.length && !sourceSet.has(source)) show = false;

        if (filterTime !== 'all' && dateStr) {{
            const articleDate = new Date(dateStr);
            let diffHours = (now - articleDate) / (1000 * 60 * 60);
            if ((filterTime === '24h' && diffHours > 24) ||
                (filterTime === '48h' && diffHours > 48) ||
                (filterTime === '7d' && diffHours > 168)) {{
                show = false;
            }}
        }}

        if (!searchFn(title)) show = false;

        row.style.display = show ? '' : 'none';
    }});
}}

function resetFilters() {{
    document.querySelectorAll('.sourceFilter').forEach(cb => cb.checked = true);
    document.getElementById('timeFilter').value = '48h';
    document.getElementById('searchBox').value = '';
    updateUrlParams();
    applyFilters();
}}

function setupEventListeners() {{
    document.querySelectorAll('.sourceFilter').forEach(cb => cb.addEventListener('change', () => {{
        updateUrlParams();
        applyFilters();
    }}));
    document.getElementById('timeFilter').addEventListener('change', () => {{
        updateUrlParams();
        applyFilters();
    }});
    document.getElementById('searchBox').addEventListener('input', () => {{
        updateUrlParams();
        applyFilters();
    }});
}}

function sortTable(colIndex) {{
    const tbody = document.querySelector('#newsTable tbody');
    let asc = true;
    const rows = Array.from(tbody.rows);
    rows.sort((a, b) => {{
        let valA = a.cells[colIndex].textContent.trim();
        let valB = b.cells[colIndex].textContent.trim();
        return asc ? valA.localeCompare(valB) : valB.localeCompare(valA);
    }});
    tbody.innerHTML = '';
    rows.forEach(r => tbody.appendChild(r));
}}

document.addEventListener('DOMContentLoaded', () => {{
    const params = getUrlParams();
    if (params.time) document.getElementById('timeFilter').value = params.time;
    if (params.search) document.getElementById('searchBox').value = params.search;
    if (params.sources.length) {{
        document.querySelectorAll('.sourceFilter').forEach(cb => {{
            cb.checked = params.sources.includes(cb.value);
        }});
    }}
    setupEventListeners();
    applyFilters();
}});
</script>

</body>
</html>"""
    return html
