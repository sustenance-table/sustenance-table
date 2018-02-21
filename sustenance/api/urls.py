from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # ex: /webapp/category
    path('category', views.categories, name="categories"),
    # ex: /webapp/category/1/
    path('category/<int:category_id>', views.category, name='category'),
    # ex: /webapp/item/
    # path('item/', views.item, name="items"),
    # ex: /webapp/item/2
    # path('item/<int:item_id>/', views.item, name='item'),
    # ex: /webapp/nutrient/
    path('nutrient', views.nutrients, name="nutrients"),
    # ex: /webapp/nutrient/4/
    path('nutrient/<int:nutrient_id>', views.nutrient, name='nutrient'),
    # ex: /webapp/benefit/
    path('benefit', views.benefits, name='benefits'),
    # ex: /webapp/benefit/3/
    path('benefit/<int:benefit_id>', views.benefit, name='benefit'),
    # ex /api/category/2/items
    path('category/<int:category_id>/items', views.item_category, name="item_categories"),
    # ex /api/benefit/2/items
    path('benefit/<int:benefit_id>/items', views.item_benefit, name="item_benefits"),
    # ex /api/nutrient/2/items
    path('nutrient/<int:nutrient_id>/items', views.item_nutrient, name="item_nutrients"),
]
#     # ex: /webapp/
#     path('', views.index, name='index'),
#     # ex: /webapp/category
#     path('category/', views.categories, name="categories"),
#     # ex: /webapp/category/1/
#     path('category/<int:category_id>/', views.category, name='category'),
#     # ex: /webapp/item/
#     path('item/', views.items, name="items"),
#     # ex: /webapp/item/2
#     path('item/<int:item_id>/', views.item, name='item'),
#     # ex: /webapp/nutrient/
#     path('nutrient/', views.nutrients, name="nutrients"),
#     # ex: /webapp/nutrient/4/
#     path('nutrient/<int:nutrient_id>/', views.nutrient, name='nutrient'),
#     # ex: /webapp/benefit/
#     path('benefit/', views.benefits, name='benefits'),
#     # ex: /webapp/benefit/3/
#     path('benefit/<int:benefit_id>/', views.benefit, name='benefit'),
#     # ex: /webapp/season/
#     path('season/', views.seasons, name='seasons'),
#     # ex: /webapp/season/3/
#     path('season/<int:season_id>/', views.season, name='season'),
#     # ex: /webapp/recipe/
#     path('recipe/', views.recipes, name='recipes'),
#     # ex: /webapp/recipe/7/
#     path('recipe/<int:recipe_id>/', views.recipe, name='recipe'),
#     # ex: /webapp/remedy/
#     path('remedy/', views.remedies, name='remedies'),
#     # ex: /webapp/remedy/5
#     path('remedy/<int:remedy_id>/', views.remedy, name='remedy')
# ]