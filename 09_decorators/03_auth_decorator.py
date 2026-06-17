from functools import wraps

def require_admin(func):
  @wraps(func)
  def wrapper(user_role):
    if user_role != "admin":
      print("Access denied: Only Admins are allowed")
      return None
    else:
      return func(user_role)
  return wrapper

@require_admin
def access_dashboard(role):
  print("Access granted to dashboard")

access_dashboard("user")
access_dashboard("admin")