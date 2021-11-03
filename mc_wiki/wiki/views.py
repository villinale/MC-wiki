from django.shortcuts import render
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = BASE_DIR.replace('\\', '/')
BASE_DIR += '/templates'
# 该文件直接访问templates
def main_interface(request):
    return render(request, './web/main.html')


def topography(request):
    return render(request, './web/topography.html')


def item_interface(request):
    return render(request, './web/mc_item.html')


def item_weapon(request, item_id):
    path = './web/item/weapon/' + str(item_id) + '.html'
    if not os.path.exists(BASE_DIR+path[1:]):
        return render(request, './web/item/introduce_not_find.html')

    return render(request, path)



def item_nature(request, item_id):
    path = './web/item/nature/' + str(item_id) + '.html'
    if not os.path.exists(BASE_DIR+path[1:]):
        return render(request, './web/item/introduce_not_find.html')

    return render(request, path)


def item_block(request, item_id):
    path = './web/item/block/' + str(item_id) + '.html'
    if not os.path.exists(BASE_DIR+path[1:]):
        return render(request, './web/item/introduce_not_find.html')

    return render(request, path)


def item_decorate(request, item_id):
    path = './web/item/decorate/' + str(item_id) + '.html'
    if not os.path.exists(BASE_DIR+path[1:]):
        return render(request, './web/item/introduce_not_find.html')

    return render(request, path)


# 默认处理与错误处理
def default_solve(request, type):
    if type == "introduce":
        return render(request, './web/item/introduce_default.html')

    pass
