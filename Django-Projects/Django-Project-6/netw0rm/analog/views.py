from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, CommentForm
from .models import Post, Comment



class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-created_at']
    form_class = PostForm

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        context['current_category'] = self.request.GET.get('category')
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object).order_by('created_at')
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return redirect(reverse('post_detail', kwargs={'pk': self.object.pk}))

        context = self.get_context_data()
        context['comment_form'] = form
        return self.render_to_response(context)