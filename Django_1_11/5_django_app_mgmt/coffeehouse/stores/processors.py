

def onsale(request):
    # Create fixed data structures to pass to template
    # data could equally come from database queries
    # web services or social APIs
    sale_items = {'Monday':'Mocha 2x1','Tuesday':'Latte 2x1'}
    return {'SALE_ITEMS': sale_items}
