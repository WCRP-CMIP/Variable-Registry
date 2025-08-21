# Branded Variable Builder

This interactive tool helps you construct CMIP branded identifiers by selecting components from standardized vocabularies loaded dynamically from the Variable Registry.

## Structure: `[Variable Root]_[Temporal Label]-[Area Label]-[Horizontal Label]-[Vertical Label]`

<div id="variable-builder">
<style>
.builder-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.component-row {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    margin-bottom: 25px;
    align-items: flex-start;
}

.component-group {
    flex: 1;
    min-width: 280px;
    background: #f8f9fa;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    transition: transform 0.2s, box-shadow 0.2s;
}

.component-group:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(0,0,0,0.1);
}

.component-group h3 {
    margin: 0 0 15px 0;
    color: #2c3e50;
    font-size: 1.2em;
    display: flex;
    align-items: center;
    gap: 8px;
}

input[type="text"] {
    width: 100%;
    padding: 12px;
    border: 2px solid #e9ecef;
    border-radius: 8px;
    font-size: 14px;
    background: white;
    transition: all 0.3s;
}

input[type="text"]:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 10px rgba(102,126,234,0.2);
}

input[type="text"]:hover {
    border-color: #ced4da;
}

.autocomplete-container {
    position: relative;
}

.autocomplete-suggestions {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    border: 2px solid #667eea;
    border-top: none;
    border-radius: 0 0 8px 8px;
    max-height: 200px;
    overflow-y: auto;
    z-index: 1000;
    display: none;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.autocomplete-suggestion {
    padding: 10px 12px;
    cursor: pointer;
    border-bottom: 1px solid #f0f0f0;
    transition: background 0.2s;
}

.autocomplete-suggestion:hover,
.autocomplete-suggestion.highlighted {
    background: #f0f8ff;
}

.autocomplete-suggestion:last-child {
    border-bottom: none;
}

.autocomplete-suggestion strong {
    color: #667eea;
}

.source-link {
    font-size: 11px;
    margin-top: 8px;
    text-align: center;
}

.source-link a {
    color: #667eea;
    text-decoration: none;
    font-weight: 500;
}

.source-link a:hover {
    text-decoration: underline;
}

.description-box {
    margin-top: 12px;
    padding: 12px;
    background: white;
    border-radius: 6px;
    min-height: 70px;
    font-size: 13px;
    color: #6c757d;
    border-left: 4px solid #e9ecef;
    transition: all 0.3s;
    line-height: 1.4;
}

.description-box.filled {
    border-left-color: #28a745;
    color: #495057;
    background: #f8fff9;
}

.result-section {
    margin-top: 40px;
    padding: 30px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 12px;
    color: white;
    text-align: center;
}

.result-section h2 {
    font-size: 1.8em;
    margin-bottom: 20px;
}

.branded-identifier {
    font-size: 28px;
    font-weight: bold;
    margin: 20px 0;
    padding: 20px;
    background: rgba(255,255,255,0.15);
    border-radius: 8px;
    font-family: 'Courier New', monospace;
    letter-spacing: 1px;
    border: 2px solid rgba(255,255,255,0.2);
    transition: all 0.3s;
}

.interpretation {
    font-size: 16px;
    font-style: italic;
    margin: 20px 0;
    line-height: 1.5;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}

.component-colors {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin: 20px 0;
    justify-content: center;
}

.color-legend {
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
    transition: transform 0.2s;
}

.root { background: #e1f5fe; color: #01579b; }
.temporal { background: #f3e5f5; color: #4a148c; }
.area { background: #e8f5e8; color: #1b5e20; }
.horizontal { background: #fff3e0; color: #e65100; }
.vertical { background: #fce4ec; color: #880e4f; }

.reset-button {
    margin-top: 20px;
    padding: 12px 24px;
    background: rgba(255,255,255,0.2);
    color: white;
    border: 2px solid rgba(255,255,255,0.3);
    border-radius: 25px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 600;
    transition: all 0.3s;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.reset-button:hover {
    background: rgba(255,255,255,0.3);
    border-color: rgba(255,255,255,0.5);
    transform: translateY(-1px);
}

.status-indicator {
    font-size: 12px;
    padding: 5px 10px;
    border-radius: 15px;
    margin-top: 10px;
    font-weight: bold;
    text-align: center;
}

.status-loading {
    background: #e3f2fd;
    color: #1976d2;
}

.status-loaded {
    background: #e8f5e8;
    color: #1b5e20;
}

.status-error {
    background: #ffebee;
    color: #c62828;
}
</style>

<div class="builder-container">
    <div class="component-row">
        <div class="component-group">
            <h3>🌡️ Variable Root</h3>
            <div class="autocomplete-container">
                <input type="text" id="variableRoot" placeholder="Type to search variable roots...">
                <div class="autocomplete-suggestions" id="variableRootSuggestions"></div>
            </div>
            <div class="source-link">
                <a href="https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/variable-root/" target="_blank">
                    All possible values can be found here
                </a>
            </div>
            <div class="description-box" id="rootDesc">Type to search and select a variable root...</div>
            <div class="status-indicator status-loading" id="rootStatus">Loading from Variable Registry...</div>
        </div>

        <div class="component-group">
            <h3>⏰ Temporal Label</h3>
            <div class="autocomplete-container">
                <input type="text" id="temporalLabel" placeholder="Type to search temporal methods...">
                <div class="autocomplete-suggestions" id="temporalLabelSuggestions"></div>
            </div>
            <div class="source-link">
                <a href="https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/temporal-label/" target="_blank">
                    All possible values can be found here
                </a>
            </div>
            <div class="description-box" id="temporalDesc">Type to search and select a temporal method...</div>
            <div class="status-indicator status-loading" id="temporalStatus">Loading from Variable Registry...</div>
        </div>
    </div>

    <div class="component-row">
        <div class="component-group">
            <h3>🌍 Area Label</h3>
            <div class="autocomplete-container">
                <input type="text" id="areaLabel" placeholder="Type to search area types...">
                <div class="autocomplete-suggestions" id="areaLabelSuggestions"></div>
            </div>
            <div class="source-link">
                <a href="https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/area-label/" target="_blank">
                    All possible values can be found here
                </a>
            </div>
            <div class="description-box" id="areaDesc">Type to search and select an area type...</div>
            <div class="status-indicator status-loading" id="areaStatus">Loading from Variable Registry...</div>
        </div>

        <div class="component-group">
            <h3>🗺️ Horizontal Label</h3>
            <div class="autocomplete-container">
                <input type="text" id="horizontalLabel" placeholder="Type to search horizontal processing...">
                <div class="autocomplete-suggestions" id="horizontalLabelSuggestions"></div>
            </div>
            <div class="source-link">
                <a href="https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/horizontal-label/" target="_blank">
                    All possible values can be found here
                </a>
            </div>
            <div class="description-box" id="horizontalDesc">Type to search and select horizontal processing...</div>
            <div class="status-indicator status-loading" id="horizontalStatus">Loading from Variable Registry...</div>
        </div>
    </div>

    <div class="component-row">
        <div class="component-group">
            <h3>📏 Vertical Label</h3>
            <div class="autocomplete-container">
                <input type="text" id="verticalLabel" placeholder="Type to search vertical levels...">
                <div class="autocomplete-suggestions" id="verticalLabelSuggestions"></div>
            </div>
            <div class="source-link">
                <a href="https://github.com/WCRP-CMIP/Variable-Registry/tree/main/src-data/vertical-label/" target="_blank">
                    All possible values can be found here
                </a>
            </div>
            <div class="description-box" id="verticalDesc">Type to search and select a vertical level...</div>
            <div class="status-indicator status-loading" id="verticalStatus">Loading from Variable Registry...</div>
        </div>
    </div>

    <div class="result-section">
        <h2>🎯 Your Branded Identifier</h2>
        <div class="component-colors">
            <span class="color-legend root">Variable Root</span>
            <span class="color-legend temporal">Temporal</span>
            <span class="color-legend area">Area</span>
            <span class="color-legend horizontal">Horizontal</span>
            <span class="color-legend vertical">Vertical</span>
        </div>
        <div class="branded-identifier" id="result">Type in the fields above to build your identifier...</div>
        <div class="interpretation" id="interpretation">Your selection will be interpreted here...</div>
        <button class="reset-button" onclick="resetBuilder()">🔄 Reset All</button>
    </div>
</div>

<script>
const selectors = {
    variableRoot: document.getElementById('variableRoot'),
    temporalLabel: document.getElementById('temporalLabel'),
    areaLabel: document.getElementById('areaLabel'),
    horizontalLabel: document.getElementById('horizontalLabel'),
    verticalLabel: document.getElementById('verticalLabel')
};

const suggestions = {
    variableRoot: document.getElementById('variableRootSuggestions'),
    temporalLabel: document.getElementById('temporalLabelSuggestions'),
    areaLabel: document.getElementById('areaLabelSuggestions'),
    horizontalLabel: document.getElementById('horizontalLabelSuggestions'),
    verticalLabel: document.getElementById('verticalLabelSuggestions')
};

const descriptions = {
    variableRoot: document.getElementById('rootDesc'),
    temporalLabel: document.getElementById('temporalDesc'),
    areaLabel: document.getElementById('areaDesc'),
    horizontalLabel: document.getElementById('horizontalDesc'),
    verticalLabel: document.getElementById('verticalDesc')
};

const statusElements = {
    variableRoot: document.getElementById('rootStatus'),
    temporalLabel: document.getElementById('temporalStatus'),
    areaLabel: document.getElementById('areaStatus'),
    horizontalLabel: document.getElementById('horizontalStatus'),
    verticalLabel: document.getElementById('verticalStatus')
};

const resultElement = document.getElementById('result');
const interpretationElement = document.getElementById('interpretation');

// Store loaded data for autocomplete
let componentData = {};

// API endpoints for component data
const dataEndpoints = {
    variableRoot: 'https://wcrp-cmip.github.io/Variable-Registry/variable-root/graph.jsonld',
    temporalLabel: 'https://wcrp-cmip.github.io/Variable-Registry/temporal-label/graph.jsonld',
    areaLabel: 'https://wcrp-cmip.github.io/Variable-Registry/area-label/graph.jsonld',
    horizontalLabel: 'https://wcrp-cmip.github.io/Variable-Registry/horizontal-label/graph.jsonld',
    verticalLabel: 'https://wcrp-cmip.github.io/Variable-Registry/vertical-label/graph.jsonld'
};

// Load data from endpoints
async function loadComponentData() {
console.log('Starting to load component data...');

// Load all data in parallel
const promises = Object.entries(dataEndpoints).map(async ([component, url]) => {
const statusEl = statusElements[component];
try {
console.log(`[${component}] Loading from:`, url);
statusEl.textContent = 'Loading from Variable Registry...';
statusEl.className = 'status-indicator status-loading';

const response = await fetch(url);
console.log(`[${component}] Response status:`, response.status);

if (!response.ok) {
throw new Error(`HTTP ${response.status}: ${response.statusText}`);
}
const data = await response.json();
console.log(`[${component}] Raw data:`, data);
console.log(`[${component}] Data keys:`, Object.keys(data));

// Handle different possible JSON-LD structures
let items = [];
if (data['@graph']) {
    console.log(`[${component}] Found @graph with ${data['@graph'].length} items`);
    items = data['@graph'];
} else if (Array.isArray(data)) {
    console.log(`[${component}] Data is array with ${data.length} items`);
    items = data;
} else if (data.items) {
        console.log(`[${component}] Found items property with ${data.items.length} items`);
    items = data.items;
} else {
    console.log(`[${component}] Checking for direct component data...`);
    // Check if it's the older JSON format with component name as key
        const componentKey = component.replace('Label', '-label');
            if (data[componentKey]) {
                            console.log(`[${component}] Found component key: ${componentKey}`);
                items = Object.entries(data[componentKey]).map(([key, value]) => ({
                    '@id': key,
                    'rdfs:label': value['ui-label'] || value.description || key,
                    'rdfs:comment': value.description || value['ui-label'] || key
                }));
        }
}

console.log(`[${component}] Items found:`, items.length);
console.log(`[${component}] Sample items:`, items.slice(0, 3));

if (items.length > 0) {
    const validItems = items.filter(item => 
        (item['@id'] || item.id) && (item['rdfs:label'] || item.label || item['ui-label'])
    );

console.log(`[${component}] Valid items: ${validItems.length}`);

componentData[component] = validItems.map(item => ({
        id: item['@id'] || item.id,
        label: item['rdfs:label'] || item.label || item['ui-label'],
        description: item['rdfs:comment'] || item.description || item['rdfs:label'] || item.label,
            searchText: `${item['@id'] || item.id} ${item['rdfs:label'] || item.label || item['ui-label']}`.toLowerCase()
    }));
    
    statusEl.textContent = `Loaded ${validItems.length} items`;
    statusEl.className = 'status-indicator status-loaded';
    } else {
            throw new Error('No valid items found');
        }
        
            return { component, data, success: true };
                } catch (error) {
                    console.error(`[${component}] Failed to load data:`, error);
                    statusEl.textContent = 'Failed to load - using fallback';
                    statusEl.className = 'status-indicator status-error';
                    componentData[component] = getFallbackData(component);
                    return { component, data: null, success: false };
                }
            });

            const results = await Promise.all(promises);
            console.log('All API calls completed:', results);
            console.log('Final componentData structure:', Object.keys(componentData));
        }

function getFallbackData(component) {
    const fallbackOptions = {
        variableRoot: [
            { id: 'tas', label: 'Air Temperature', description: 'Near-surface air temperature' },
            { id: 'tos', label: 'Sea Surface Temperature', description: 'Sea surface temperature' },
            { id: 'pr', label: 'Precipitation', description: 'Precipitation flux' },
            { id: 'huss', label: 'Specific Humidity', description: 'Specific humidity at surface' }
        ],
        temporalLabel: [
            { id: 'tavg', label: 'Mean', description: 'Mean over time' },
            { id: 'tclm', label: 'Annual Climatology', description: 'Annual cycle climatology' },
            { id: 'tpt', label: 'Point in Time', description: 'Point in time' }
        ],
        areaLabel: [
            { id: 'air', label: 'Air', description: 'Over air region' },
            { id: 'sea', label: 'Sea', description: 'Over sea region' },
            { id: 'lnd', label: 'Land', description: 'Over land region' },
            { id: 'u', label: 'Unmasked', description: 'Unmasked (no area restriction)' }
        ],
        horizontalLabel: [
            { id: 'hxy', label: 'Gridded', description: 'Gridded horizontal data' },
            { id: 'hm', label: 'Horizontal Mean', description: 'Horizontal mean' },
            { id: 'hy', label: 'Zonal Mean', description: 'Zonal mean' }
        ],
        verticalLabel: [
            { id: 'u', label: 'Unspecified', description: 'Unspecified vertical dimension' },
            { id: 'h2m', label: '2m Height', description: 'At 2 meter height' },
            { id: 'd0m', label: 'Surface', description: 'At surface level' }
        ]
    };

    return (fallbackOptions[component] || []).map(opt => ({
        id: opt.id,
        label: opt.label,
        description: opt.description,
        searchText: `${opt.id} ${opt.label}`.toLowerCase()
    }));
}

function setupAutocomplete(component, input, suggestionsDiv) {
console.log(`[${component}] Setting up autocomplete...`);
            console.log(`[${component}] Input element:`, input);
console.log(`[${component}] Suggestions div:`, suggestionsDiv);
console.log(`[${component}] Component data:`, componentData[component]);

let highlightedIndex = -1;

input.addEventListener('input', function() {
const query = input.value.toLowerCase().trim();
console.log(`[${component}] Input changed to:`, query);

// Check if current value matches exactly any component
const exactMatch = componentData[component]?.find(item => item.id === input.value);
if (exactMatch) {
    console.log(`[${component}] Exact match found:`, exactMatch);
    input.setAttribute('data-description', exactMatch.description);
} else {
input.removeAttribute('data-description');
}
                
updateDescription(component, input);

if (query.length === 0) {
                    suggestionsDiv.style.display = 'none';
    return;
}

const matches = componentData[component]?.filter(item => 
                    item.searchText.includes(query)
) || [];

console.log(`[${component}] Matches found:`, matches.length, matches);

if (matches.length === 0) {
suggestionsDiv.style.display = 'none';
return;
}

suggestionsDiv.innerHTML = '';
matches.slice(0, 10).forEach((item) => {
const div = document.createElement('div');
    div.className = 'autocomplete-suggestion';
                    div.innerHTML = `<strong>${item.id}</strong> - ${item.label}`;
    div.addEventListener('click', function() {
        console.log(`[${component}] Suggestion clicked:`, item.id);
            input.value = item.id;
                        input.setAttribute('data-description', item.description);
            suggestionsDiv.style.display = 'none';
        updateDescription(component, input);
    });
    suggestionsDiv.appendChild(div);
});

console.log(`[${component}] Showing suggestions div`);
suggestionsDiv.style.display = 'block';
highlightedIndex = -1;
});

input.addEventListener('keydown', function(e) {
const suggestionElements = suggestionsDiv.querySelectorAll('.autocomplete-suggestion');

if (e.key === 'ArrowDown') {
e.preventDefault();
    highlightedIndex = Math.min(highlightedIndex + 1, suggestionElements.length - 1);
updateHighlight(suggestionElements);
} else if (e.key === 'ArrowUp') {
    e.preventDefault();
        highlightedIndex = Math.max(highlightedIndex - 1, -1);
                    updateHighlight(suggestionElements);
    } else if (e.key === 'Enter') {
    e.preventDefault();
if (highlightedIndex >= 0 && suggestionElements[highlightedIndex]) {
        suggestionElements[highlightedIndex].click();
        }
                } else if (e.key === 'Escape') {
        suggestionsDiv.style.display = 'none';
    highlightedIndex = -1;
}
});

input.addEventListener('blur', function() {
setTimeout(function() {
    suggestionsDiv.style.display = 'none';
    }, 200);
    });

            function updateHighlight(suggestionElements) {
                suggestionElements.forEach((sugg, index) => {
                    if (index === highlightedIndex) {
                        sugg.classList.add('highlighted');
                    } else {
                        sugg.classList.remove('highlighted');
                    }
                });
            }
            
            console.log(`[${component}] Autocomplete setup complete`);
        }

function updateDescription(component, input) {
    const description = input.getAttribute('data-description');
    const descBox = descriptions[component];
    
    if (description && input.value !== '') {
        descBox.textContent = description;
        descBox.classList.add('filled');
    } else {
        const defaultText = {
            variableRoot: 'Type to search and select a variable root...',
            temporalLabel: 'Type to search and select a temporal method...',
            areaLabel: 'Type to search and select an area type...',
            horizontalLabel: 'Type to search and select horizontal processing...',
            verticalLabel: 'Type to search and select a vertical level...'
        };
        descBox.textContent = defaultText[component];
        descBox.classList.remove('filled');
    }
    updateResult();
}

function updateResult() {
    const values = {
        root: selectors.variableRoot.value,
        temporal: selectors.temporalLabel.value,
        area: selectors.areaLabel.value,
        horizontal: selectors.horizontalLabel.value,
        vertical: selectors.verticalLabel.value
    };

    // Build the identifier
    let identifier = '';
    let interpretation = '';
    
    if (values.root) {
        identifier = values.root;
        interpretation = selectors.variableRoot.getAttribute('data-description') || values.root;
    }

    if (values.temporal) {
        identifier += '_' + values.temporal;
        const tempDesc = selectors.temporalLabel.getAttribute('data-description') || values.temporal;
        interpretation += ', ' + tempDesc.toLowerCase();
    }

    if (values.area) {
        identifier += '-' + values.area;
        const areaDesc = selectors.areaLabel.getAttribute('data-description') || values.area;
        interpretation += ', ' + areaDesc.toLowerCase();
    }

    if (values.horizontal) {
        identifier += '-' + values.horizontal;
        const horizDesc = selectors.horizontalLabel.getAttribute('data-description') || values.horizontal;
        interpretation += ', ' + horizDesc.toLowerCase();
    }

    if (values.vertical) {
        identifier += '-' + values.vertical;
        const vertDesc = selectors.verticalLabel.getAttribute('data-description') || values.vertical;
        interpretation += ', ' + vertDesc.toLowerCase();
    }

    // Update display
    if (identifier) {
        interpretationElement.textContent = interpretation;
        
        // Color-code the identifier
        let coloredIdentifier = `<span class="root">${values.root}</span>`;
        if (values.temporal) coloredIdentifier += `_<span class="temporal">${values.temporal}</span>`;
        if (values.area) coloredIdentifier += `-<span class="area">${values.area}</span>`;
        if (values.horizontal) coloredIdentifier += `-<span class="horizontal">${values.horizontal}</span>`;
        if (values.vertical) coloredIdentifier += `-<span class="vertical">${values.vertical}</span>`;
        
        resultElement.innerHTML = coloredIdentifier;
    } else {
        resultElement.textContent = 'Type in the fields above to build your identifier...';
        interpretationElement.textContent = 'Your selection will be interpreted here...';
    }
}

function resetBuilder() {
    Object.values(selectors).forEach(input => {
        input.value = '';
        input.removeAttribute('data-description');
        updateDescription(input.id, input);
    });
    Object.values(suggestions).forEach(div => {
        div.style.display = 'none';
    });
    updateResult();
}

// Initialize by loading data
console.log('Starting initialization...');

loadComponentData().then(() => {
console.log('Data loading complete. Setting up autocomplete...');
console.log('Available component data:', Object.keys(componentData));

    // Setup autocomplete for each component
            Object.entries(selectors).forEach(([component, input]) => {
                console.log(`Setting up ${component}:`, !!input, !!suggestions[component]);
                setupAutocomplete(component, input, suggestions[component]);
            });
            
            console.log('All autocomplete setup complete');
            updateResult();
        }).catch(error => {
            console.error('Initialization failed:', error);
        });
        
        // Add a test function to verify everything is working
        window.testAutocomplete = function() {
            console.log('=== AUTOCOMPLETE TEST ===');
            console.log('Selectors:', selectors);
            console.log('Suggestions:', suggestions);
            console.log('Component data:', componentData);
            
            // Test first input
            const firstInput = selectors.variableRoot;
            console.log('First input element:', firstInput);
            console.log('First input has event listeners:', firstInput._events || 'No _events property');
            
            // Simulate typing in first input
            if (firstInput) {
                console.log('Simulating input event...');
                firstInput.value = 'ta';
                firstInput.dispatchEvent(new Event('input', { bubbles: true }));
            }
            
            return 'Test complete - check console for details';
        };
        
        // Verify page rendered correctly
        setTimeout(() => {
            console.log('=== PAGE RENDER CHECK ===');
            console.log('All input elements found:', Object.keys(selectors).map(k => !!selectors[k]));
            console.log('All suggestion divs found:', Object.keys(suggestions).map(k => !!suggestions[k]));
            console.log('Status elements found:', Object.keys(statusElements).map(k => !!statusElements[k]));
            console.log('Result elements:', !!resultElement, !!interpretationElement);
            console.log('Page render check complete');
        }, 100);
</script>

</div>

## Data Sources

This tool dynamically loads component definitions from the CMIP Variable Registry:

- **Variable Roots**: [graph.jsonld](https://wcrp-cmip.github.io/Variable-Registry/variable-root/graph.jsonld)
- **Temporal Labels**: [graph.jsonld](https://wcrp-cmip.github.io/Variable-Registry/temporal-label/graph.jsonld)  
- **Area Labels**: [graph.jsonld](https://wcrp-cmip.github.io/Variable-Registry/area-label/graph.jsonld)
- **Horizontal Labels**: [graph.jsonld](https://wcrp-cmip.github.io/Variable-Registry/horizontal-label/graph.jsonld)
- **Vertical Labels**: [graph.jsonld](https://wcrp-cmip.github.io/Variable-Registry/vertical-label/graph.jsonld)

## How to Use This Builder

1. **Wait for data to load** - Status indicators show loading progress
2. **Type in any field** - Autocomplete suggestions appear as you type
3. **Use arrow keys** to navigate suggestions or click to select
4. **Watch the identifier build** automatically with color coding
5. **See descriptions** update in real-time as you make selections

The tool will automatically construct your branded identifier and provide a human-readable interpretation using the latest definitions from the Variable Registry!-Registry/variable-root/graph.jsonld)
- **Temporal Labels**: [graph.jsonld](https://wcrp-cmip.github.io/Variable-Registry/temporal-label/graph.jsonld)  
- **Area Labels**: [graph.jsonld](https://wcrp-cmip.github.io/Variable-Registry/area-label/graph.jsonld)
- **Horizontal Labels**: [graph.jsonld](https://wcrp-cmip.github.io/Variable-Registry/horizontal-label/graph.jsonld)
- **Vertical Labels**: [graph.jsonld](https://wcrp-cmip.github.io/Variable-Registry/vertical-label/graph.jsonld)

## How to Use This Builder

1. **Wait for data to load** - Status indicators show loading progress
2. **Type in any field** - Autocomplete suggestions appear as you type
3. **Use arrow keys** to navigate suggestions or click to select
4. **Watch the identifier build** automatically with color coding
5. **See descriptions** update in real-time as you make selections

The tool will automatically construct your branded identifier and provide a human-readable interpretation using the latest definitions from the Variable Registry!
