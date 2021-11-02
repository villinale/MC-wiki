from django.shortcuts import render


# 该文件直接访问templates
def main_interface(request):
    return render(request, './web/main.html')


def item_interface(request):
    return render(request, './web/mc_item.html')


def item_weapon(request, item_id):
    path = './web/item/weapon/' + str(item_id) + '.html'
    return render(request, path)


def item_nature(request, item_id):
    path = './web/item/nature/' + str(item_id) + '.html'
    return render(request, path)


def item_block(request, item_id):
    path = './web/item/block/' + str(item_id) + '.html'
    return render(request, path)


def item_decorate(request, item_id):
    path = './web/item/decorate/' + str(item_id) + '.html'
    return render(request, path)
