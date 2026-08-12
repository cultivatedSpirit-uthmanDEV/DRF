from rest_framework import permissions
from .permission import IsStaffEditorPermission

class StaffEditorPermissionMixins():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]