from django.shortcuts import render, redirect,get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from .models import Comment
from .forms import CommentForm
from django.http import Http404
# Create your views here.

def add(request):

    if (request.method == 'POST'):

        form = CommentForm(request.POST)
        form.save() # puede no ser una variable comment, xd?, si 
        # print(comment)

        #guardar
        return redirect('comments:index')


    else:
            form = CommentForm()

            print('El campo esta vacio')


    return render(request,'comments/add.html', {'form': form})


# def add(request):

#     if (request.method == 'GET'):

#         pass
    
#     if (request.method == 'POST'):

#         #guardar

#         if request.POST.get('text') != '':
            
#             comment = Comment() #objeto

#             comment.text = request.POST.get('text')

#             comment.save()
#         else:
#             print('El campo esta vacio')


#     return render(request,'add.html', {'data': 'Content'})





def index(request):
        
    # comments = Comment.objects.all()
    comments  = get_list_or_404(Comment) #no es el comportamiento tipico cuando no hay elemetos
    paginator = Paginator(comments,5)

    page_number = request.GET.get('page')
    comments_page = paginator.get_page(page_number)


    return render(request,'comments/index.html',{'comments':comments_page})

def update (request,pk):


    #hace todo lo q hace el try juas juas 
    comment = get_object_or_404(Comment,pk=pk)


    #Try Catch para la respuesta 404 not found
    #try:
    #    comment = Comment.objects.get(pk=pk)
    #except Comment.DoesNotExist:
    #    raise Http404
        
    
    if request.method == 'POST':

        form = CommentForm(request.POST, instance= comment)

        if form.is_valid():
            form.save()  ##POR DIOS SANTO SEBASTIAN COMO VAS A PONER UNA FUNCION SIN PARENTESIS AHUEVADO DE PUTA MIERDA XDDDDDDDDDDD
            return redirect('comments:index') #luego del guardado
        
    else:

        form = CommentForm(instance=comment) 
        
    return render(request,'comments/add.html', {'form': form})

def delete (request,pk):
    
    comment = get_object_or_404(Comment,pk=pk)

    if request.method == 'POST':

        comment.delete()
        return redirect('comments:index') #obligatorio
    

