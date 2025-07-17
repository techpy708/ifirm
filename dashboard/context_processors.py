from .models import EmployeeMaster

from .models import EmployeeMaster

def role_flags(request):
    is_admin = False
    is_partner = False
    is_team_leader = False

    if request.user.is_authenticated:
        full_name = f"{request.user.first_name} {request.user.last_name}"
        is_admin = EmployeeMaster.objects.filter(Admin=full_name).exists()
        is_partner = EmployeeMaster.objects.filter(Partner=full_name).exists()
        is_team_leader = EmployeeMaster.objects.filter(audit_manager=full_name).exists()

    return {
        'is_admin': is_admin,
        'is_partner': is_partner,
        'is_team_leader': is_team_leader,
    }

