import cmipld
from cmipld.utils.ldparse import name_entry

me = __file__.split('/')[-1].replace('.py','')

def run(io, whoami, path, name, **kwargs):
    # Get the main categories from src-data
    categories = [
        'area-label', 'cell-method', 'cmip6-mip-table', 
        'coordinate', 'data-request', 'dimension', 
        'horizontal-label', 'temporal-label', 'variable', 
        'variable-root', 'vertical-label'
    ]
    
    data = {category: f"{io}/{category}/" for category in categories}
    
    return f"{path}/{name}_{me}.json", me, data
