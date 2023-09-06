from django.db.models import Count
from .models import Category, Post

#using context processor to find the trending posts
def trending_posts(request):
    trending_posts = Post.objects.order_by('-views')[:5]
    context = {
        'trending_posts': trending_posts,
    }
    return context

#using context processor to find top posts by category
def top_posts_by_category(request):
    top_posts = []
    categories = Category.objects.all()
    for category in categories:
        posts = Post.objects.filter(category=category).annotate(num_views=Count('views')).order_by('-num_views')[:3]
        top_posts.append({'category': category, 'posts': posts})
    return {'top_posts_by_category': top_posts}