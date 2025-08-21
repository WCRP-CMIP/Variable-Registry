# Branded Variable Builder

This interactive tool helps you construct CMIP branded identifiers by selecting components from standardized vocabularies.

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
    gap: 15px;
    margin-bottom: 20px;
    align-items: flex-start;
}

.component-group {
    flex: 1;
    min-width: 200px;
    background: #f8f9fa;
    border-radius: 8px;
    padding: 15px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.component-group h3 {
    margin: 0 0 10px 0;
    color: #2c3e50;
    font-size: 1.1em;
}

select {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 14px;
    background: white;
}

select:focus {
    outline: none;
    border-color: #007bff;
    box-shadow: 0 0 5px rgba(0,123,255,0.3);
}

.description-box {
    margin-top: 10px;
    padding: 10px;
    background: white;
    border-radius: 4px;
    min-height: 60px;
    font-size: 13px;
    color: #555;
    border-left: 4px solid #e9ecef;
}

.description-box.filled {
    border-left-color: #28a745;
}

.result-section {
    margin-top: 30px;
    padding: 20px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 10px;
    color: white;
    text-align: center;
}

.branded-identifier {
    font-size: 24px;
    font-weight: bold;
    margin: 15px 0;
    padding: 15px;
    background: rgba(255,255,255,0.1);
    border-radius: 5px;
    font-family: 'Courier New', monospace;
    letter-spacing: 1px;
}

.interpretation {
    font-size: 16px;
    font-style: italic;
    margin-top: 15px;
}

.component-colors {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin: 15px 0;
    justify-content: center;
}

.color-legend {
    padding: 5px 10px;
    border-radius: 15px;
    font-size: 12px;
    font-weight: bold;
}

.root { background: #e1f5fe; color: #01579b; }
.temporal { background: #f3e5f5; color: #4a148c; }
.area { background: #e8f5e8; color: #1b5e20; }
.horizontal { background: #fff3e0; color: #e65100; }
.vertical { background: #fce4ec; color: #880e4f; }

.reset-button {
    margin-top: 15px;
    padding: 10px 20px;
    background: rgba(255,255,255,0.2);
    color: white;
    border: 2px solid rgba(255,255,255,0.3);
    border-radius: 5px;
    cursor: pointer;
    font-size: 14px;
    transition: all 0.3s;
}

.reset-button:hover {
    background: rgba(255,255,255,0.3);
}
</style>

<div class="builder-container">
    <div class="component-row">
        <div class="component-group">
            <h3>🌡️ Variable Root</h3>
            <select id="variableRoot">
                <option value="">Select variable root...</option>
                <option value="tas" data-description="Near-surface air temperature">tas - Air Temperature</option>
                <option value="tos" data-description="Sea surface temperature">tos - Sea Surface Temperature</option>
                <option value="pr" data-description="Precipitation flux">pr - Precipitation</option>
                <option value="huss" data-description="Specific humidity at surface">huss - Specific Humidity</option>
                <option value="ta" data-description="Air temperature at various levels">ta - Air Temperature (3D)</option>
                <option value="ua" data-description="Eastward component of wind">ua - Eastward Wind</option>
                <option value="clt" data-description="Total cloud area fraction">clt - Cloud Fraction</option>
                <option value="mrso" data-description="Total water content of soil layer">mrso - Soil Moisture</option>
                <option value="siconc" data-description="Sea ice area fraction">siconc - Sea Ice Concentration</option>
            </select>
            <div class="description-box" id="rootDesc">Select a variable root to see its description...</div>
        </div>

        <div class="component-group">
            <h3>⏰ Temporal Label</h3>
            <select id="temporalLabel">
                <option value="">Select temporal...</option>
                <option value="tavg" data-description="Mean over time">tavg - Mean</option>
                <option value="tclm" data-description="Annual cycle climatology">tclm - Annual Climatology</option>
                <option value="tclmdc" data-description="Diurnal cycle climatology">tclmdc - Diurnal Climatology</option>
                <option value="ti" data-description="Time independent data">ti - Time Independent</option>
                <option value="tmaxstat" data-description="Maximum or mean of daily maxima">tmaxstat - Maximum</option>
                <option value="tmin" data-description="Minimum or mean of daily minima">tmin - Minimum</option>
                <option value="tpt" data-description="Point in time">tpt - Point in Time</option>
                <option value="tsum" data-description="Sum over time">tsum - Sum</option>
            </select>
            <div class="description-box" id="temporalDesc">Select a temporal method to see its description...</div>
        </div>
    </div>

    <div class="component-row">
        <div class="component-group">
            <h3>🌍 Area Label</h3>
            <select id="areaLabel">
                <option value="">Select area...</option>
                <option value="air" data-description="Over air region">air - Air</option>
                <option value="sea" data-description="Over sea region">sea - Sea</option>
                <option value="lnd" data-description="Over land region">lnd - Land</option>
                <option value="si" data-description="Over sea ice region">si - Sea Ice</option>
                <option value="cl" data-description="Over cloud region">cl - Cloud</option>
                <option value="veg" data-description="Over vegetation region">veg - Vegetation</option>
                <option value="sn" data-description="Over snow region">sn - Snow</option>
                <option value="u" data-description="Unmasked (no area restriction)">u - Unmasked</option>
                <option value="tree" data-description="Over tree region">tree - Trees</option>
                <option value="crp" data-description="Over crop region">crp - Crops</option>
            </select>
            <div class="description-box" id="areaDesc">Select an area type to see its description...</div>
        </div>

        <div class="component-group">
            <h3>🗺️ Horizontal Label</h3>
            <select id="horizontalLabel">
                <option value="">Select horizontal...</option>
                <option value="hxy" data-description="Gridded horizontal data">hxy - Gridded</option>
                <option value="hm" data-description="Horizontal mean">hm - Horizontal Mean</option>
                <option value="hy" data-description="Zonal mean">hy - Zonal Mean</option>
                <option value="ht" data-description="Mean along a line or across areas">ht - Line/Area Mean</option>
                <option value="hxys" data-description="Site-specific values">hxys - Site Values</option>
                <option value="hybs" data-description="Zonal mean within a basin">hybs - Basin Zonal Mean</option>
            </select>
            <div class="description-box" id="horizontalDesc">Select a horizontal averaging to see its description...</div>
        </div>
    </div>

    <div class="component-row">
        <div class="component-group">
            <h3>📏 Vertical Label</h3>
            <select id="verticalLabel">
                <option value="">Select vertical...</option>
                <option value="u" data-description="Unspecified vertical dimension">u - Unspecified</option>
                <option value="h2m" data-description="At 2 meter height">h2m - 2m Height</option>
                <option value="h10m" data-description="At 10 meter height">h10m - 10m Height</option>
                <option value="d0m" data-description="At surface level">d0m - Surface</option>
                <option value="al" data-description="Atmospheric model levels">al - Atmosphere Levels</option>
                <option value="ol" data-description="Ocean model levels">ol - Ocean Levels</option>
                <option value="sl" data-description="Model soil levels">sl - Soil Levels</option>
                <option value="500hPa" data-description="At 500 hPa pressure level">500hPa - 500hPa Level</option>
                <option value="850hPa" data-description="At 850 hPa pressure level">850hPa - 850hPa Level</option>
                <option value="d100m" data-description="At 100 meter depth">d100m - 100m Depth</option>
            </select>
            <div class="description-box" id="verticalDesc">Select a vertical level to see its description...</div>
        </div>
    </div>

    <div class="result-section">
        <h2>🎯 Branded Identifier Result</h2>
        <div class="component-colors">
            <span class="color-legend root">Variable Root</span>
            <span class="color-legend temporal">Temporal</span>
            <span class="color-legend area">Area</span>
            <span class="color-legend horizontal">Horizontal</span>
            <span class="color-legend vertical">Vertical</span>
        </div>
        <div class="branded-identifier" id="result">Select components above to build your identifier...</div>
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

const descriptions = {
    variableRoot: document.getElementById('rootDesc'),
    temporalLabel: document.getElementById('temporalDesc'),
    areaLabel: document.getElementById('areaDesc'),
    horizontalLabel: document.getElementById('horizontalDesc'),
    verticalLabel: document.getElementById('verticalDesc')
};

const resultElement = document.getElementById('result');
const interpretationElement = document.getElementById('interpretation');

function updateDescription(selectorName, element) {
    const selectedOption = element.options[element.selectedIndex];
    const description = selectedOption.getAttribute('data-description');
    const descBox = descriptions[selectorName];
    
    if (description && element.value !== '') {
        descBox.textContent = description;
        descBox.classList.add('filled');
    } else {
        descBox.textContent = `Select a ${selectorName.replace(/([A-Z])/g, ' $1').toLowerCase()} to see its description...`;
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
        const rootOption = selectors.variableRoot.options[selectors.variableRoot.selectedIndex];
        interpretation = rootOption.getAttribute('data-description') || values.root;
    }

    if (values.temporal) {
        identifier += '_' + values.temporal;
        const tempOption = selectors.temporalLabel.options[selectors.temporalLabel.selectedIndex];
        interpretation += ', ' + (tempOption.getAttribute('data-description') || values.temporal);
    }

    if (values.area) {
        identifier += '-' + values.area;
        const areaOption = selectors.areaLabel.options[selectors.areaLabel.selectedIndex];
        interpretation += ', over ' + (areaOption.getAttribute('data-description') || values.area);
    }

    if (values.horizontal) {
        identifier += '-' + values.horizontal;
        const horizOption = selectors.horizontalLabel.options[selectors.horizontalLabel.selectedIndex];
        interpretation += ', ' + (horizOption.getAttribute('data-description') || values.horizontal);
    }

    if (values.vertical) {
        identifier += '-' + values.vertical;
        const vertOption = selectors.verticalLabel.options[selectors.verticalLabel.selectedIndex];
        interpretation += ', at ' + (vertOption.getAttribute('data-description') || values.vertical);
    }

    // Update display
    if (identifier) {
        resultElement.textContent = identifier;
        interpretationElement.textContent = interpretation;
    } else {
        resultElement.textContent = 'Select components above to build your identifier...';
        interpretationElement.textContent = 'Your selection will be interpreted here...';
    }

    // Color-code the identifier
    if (identifier && values.root) {
        let coloredIdentifier = `<span class="root">${values.root}</span>`;
        if (values.temporal) coloredIdentifier += `_<span class="temporal">${values.temporal}</span>`;
        if (values.area) coloredIdentifier += `-<span class="area">${values.area}</span>`;
        if (values.horizontal) coloredIdentifier += `-<span class="horizontal">${values.horizontal}</span>`;
        if (values.vertical) coloredIdentifier += `-<span class="vertical">${values.vertical}</span>`;
        
        resultElement.innerHTML = coloredIdentifier;
    }
}

function resetBuilder() {
    Object.values(selectors).forEach(selector => {
        selector.selectedIndex = 0;
        updateDescription(selector.id, selector);
    });
    updateResult();
}

// Add event listeners
Object.entries(selectors).forEach(([name, selector]) => {
    selector.addEventListener('change', () => updateDescription(name, selector));
});

// Initialize
updateResult();
</script>

</div>

## Example Branded Identifiers

Here are some common examples:

- **`tas_tavg-u-hxy-h2m`** - Near-surface air temperature, time-averaged, unmasked, gridded, at 2m height
- **`tos_tavg-sea-hxy-d0m`** - Sea surface temperature, time-averaged, over sea, gridded, at surface
- **`pr_tsum-u-hxy-u`** - Precipitation, time-summed, unmasked, gridded, unspecified vertical
- **`ua_tavg-air-hy-500hPa`** - Eastward wind, time-averaged, over air, zonal mean, at 500hPa

## How to Use This Builder

1. **Start with Variable Root** - Choose what physical quantity you want to describe
2. **Select Temporal Method** - How the data is averaged or sampled in time  
3. **Choose Area Type** - Which region or surface type the data covers
4. **Pick Horizontal Processing** - How data is spatially averaged or gridded
5. **Define Vertical Level** - At what height, depth, or pressure level

The tool will automatically construct your branded identifier and provide a human-readable interpretation!
