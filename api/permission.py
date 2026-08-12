from rest_framework import permissions

# custom_permission
# for 'GET' request
class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        perms_map = {
                'GET': ['%(app_label)s.view_%(model_name)s'],
                'OPTIONS': [],
                'HEAD': [],
                'POST': ['%(app_label)s.add_%(model_name)s'],
                'PUT': ['%(app_label)s.change_%(model_name)s'],
                'PATCH': ['%(app_label)s.change_%(model_name)s'],
                'DELETE': ['%(app_label)s.delete_%(model_name)s'],
            }
       
        user = request.user
        if not user.is_staff:
           return False
        return super().has_permission(request, view)
       







       # print(user.get_all_permissions())
             # if user.is_staff:
                 # if user.has_perm("products.add_product"): # app_name.verb_model name
                 #         return True
                 # if user.has_perm("products.delete_product"): 
                         # return True
                #  if user.has_perm("products.change_product"): 
                         # return True
                 # if user.has_perm("products.view_product"): 
                         # return True
                  #return False
            
             # return False
