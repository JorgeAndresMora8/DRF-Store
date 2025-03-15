# from django.shortcuts import render
# from watchlist_app.models import Product
# from django.http import JsonResponse

# # Create your views here.
# def view_list(request): 
#     product_list = Product.objects.all()
#     product_list_dict = list(product_list.values())
#     data = {
#         "Products": product_list_dict
#     }
#     return JsonResponse(data)
    
    
# def view_detail(request, pk):  
#     product = Product.objects.get(pk=pk)
#     data = { 
#         'name': product.name,    
#         'description': product.description,    
#         'price': product.price,    
#             }
    
#     return JsonResponse(data)