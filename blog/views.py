from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import PostForm, UpdateForm, CommentForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Category, Comment

# Home view function to render all posts
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# View to display all posts in a list with pagination
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

# View to display all posts by a specific user with pagination
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

# View to display a single post with its details
class PostDetailView(DetailView):
    model = Post

    # Increment the view count when the post is viewed
    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.views += 1
        post.save()
        return super().get(request, *args, **kwargs)
    
    # Add comments to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(post=self.object)
        context['comments'] = comments
        return context

# View to create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.header_image = self.request.FILES.get('header_image')
        return super().form_valid(form)

# View to update an existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = UpdateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# View to delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# View to display top posts based on views
class TopPostsListView(ListView):
    model = Post
    template_name = 'blog/top_posts.html' 
    context_object_name = 'trending_posts'
    ordering = ['-views']
    paginate_by = 5

    def get_queryset(self):
        # Get the posts with the most page views in the last 30 days
        start_date = timezone.now() - timezone.timedelta(days=30)
        return Post.objects.filter(date_posted__gte=start_date).order_by('-views')[:5]
    
    
# View to display a list of all categories
class CategoryListView(ListView):
    model = Category
    template_name = 'blog/discover.html'
    context_object_name = 'categories'

# View to render the 'About Us' page
def info(request):
    return render(request, 'blog/blog-info.html', {'title': 'About Us'})

# View to render the 'Discover' page
def discover(request):
    return render(request, 'blog/discover.html', {'title': 'Discover'})

# View to display all posts in a specific category
def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats)
    return render(request, 'blog/categories.html', {'cats': cats, 'category_post': category_post})

# View to add a comment to a specific post
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Check if the request method is POST, and if the comment form is valid
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Create a new comment and save it
            comment = Comment(
                post=post,
                name=form.cleaned_data['name'],
                body=form.cleaned_data['body']
            )
            comment.save()
            # Redirect to the post detail page after the comment is saved
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()

    # Render the 'add_comment' template with the post and form as context
    return render(request, 'blog/add_comment.html', {'post': post, 'form': form})
