from django.shortcuts import render

projects_lsit = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'Website with my portfolio'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'Another Facebook killer'
    },

]


def projects(request):

    context = {'page': 'projects', 'number': '10', 'projects': projects_lsit}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    checkProjectList = [p for p in projects_lsit if p['id'] == pk]
    context = None
    if checkProjectList:
        context = checkProjectList[0]
    return render(request, 'projects/single-project.html', context)
