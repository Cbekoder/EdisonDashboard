from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *

class NodeGroupView(View):
    def get(self, request):
        if request.user.is_authenticated:
            context = {
                "user": request.user,
                'groups': NodeGroups.objects.filter(user_id=request.user.id)
            }
            return render(request, 'tables.html', context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            folder = NodeGroups.objects.create(
                title=request.POST.get('title').title(),
                user_id=request.user
            )
            return redirect('folders')
        return redirect('login')


class TreeNode(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            folder = NodeGroups.objects.get(id=pk)
            context = {
                "user": request.user,
                "scripts": Script.objects.filter(folder_id=folder)
            }
            return render(request, 'tree_node.html', context)
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            if request.POST.get('forma') == 'f1':
                node = Script.objects.get(id=request.POST.get("node_id"))
                node.question_uz = request.POST.get('question_uz')
                node.answer_uz = request.POST.get('answer_uz')
                node.question_ru = request.POST.get('question_ru')
                node.answer_ru = request.POST.get('answer_ru')
                node.save()

            elif request.POST.get('forma') == 'f2':
                script = Script.objects.create(
                    folder_id = NodeGroups.objects.get(id=pk),
                    question_uz = request.POST.get('question_uz'),
                    question_ru = request.POST.get('question_ru'),
                    answer_uz = request.POST.get('answer_uz'),
                    answer_ru = request.POST.get('answer_ru'),
                    parent_id = Script.objects.get(id=request.POST.get('parent_id'))
                )


            return redirect(f'/edit/groups/{pk}')
        return redirect('login')

class DefaultAdd(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            folder = NodeGroups.objects.get(id=pk)
            if Script.objects.filter(folder_id=folder).count() == 0 and folder.user_id == request.user:
                script = Script.objects.create(
                    folder_id= folder,
                    question_uz="Robot",
                    answer_uz="Assalomu alaykum",
                    question_ru="Робот",
                    answer_ru="Привет",
                    parent_id=None
                )
                return redirect(f'/edit/groups/{pk}')
        return redirect('login')

def delete_group(request, pk):
    group = get_object_or_404(NodeGroups, id=pk)
    if request.user.is_authenticated and group.user_id == request.user:
        group.delete()
        return redirect('/edit/groups/')
    return redirect('login')

def delete_script(request, pk):
    script = get_object_or_404(Script, id=pk)
    group_id = script.folder_id
    if request.user.is_authenticated and group_id.user_id == request.user:
        script.delete()
        return redirect(f'/edit/groups/{group_id.id}')
    return redirect('login')

