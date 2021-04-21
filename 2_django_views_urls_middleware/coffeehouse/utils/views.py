from django.shortcuts import render

def bad_request(request, exception):
    # Dict to pass to template, data could come from DB query
    context = {'view':'bad_request'}
    return render(request,'400.html', context, status=400)

def permission_denied(request, exception):
    # Dict to pass to template, data could come from DB query
    context = {'view':'permission_denied'}
    return render(request,'403.html', context, status=403)

def page_not_found(request, exception):
    # Dict to pass to template, data could come from DB query
    context = {'view':'page_not_found'}
    return render(request,'404.html', context, status=404)

def server_error(request):
    # Dict to pass to template, data could come from DB query
    context = {'view':'server_error'}
    return render(request,'500.html', context, status=500)
