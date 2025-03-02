from django.shortcuts import render, get_object_or_404  
from django.contrib.auth.decorators import permission_required  
from .models import Article  

@permission_required('your_app_name.can_view', raise_exception=True)  
def article_list(request):  
    articles = Article.objects.all()  
    return render(request, 'article_list.html', {'articles': articles})  

@permission_required('your_app_name.can_create', raise_exception=True)  
def article_create(request):  
    if request.method == 'POST':  
        # Handle form submission for new article  
        pass  
    return render(request, 'article_form.html')  

@permission_required('your_app_name.can_edit', raise_exception=True)  
def article_edit(request, article_id):  
    article = get_object_or_404(Article, id=article_id)  
    if request.method == 'POST':  
        # Handle form submission for editing article  
        pass  
    return render(request, 'article_form.html', {'article': article})  

@permission_required('your_app_name.can_delete', raise_exception=True)  
def article_delete(request, article_id):  
    article = get_object_or_404(Article, id=article_id)  
    if request.method == 'POST':  
        article.delete()  
        # Redirect after deletion  
        pass  
    return render(request, 'article_confirm_delete.html', {'article': article})
