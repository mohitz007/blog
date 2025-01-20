


from django.http import JsonResponse
import json
from common.models import Token


def authenticated(fun):
    def wrapper(request, *args, **kwargs):
        # Implement logic to validate authentication token
        token = request.headers.get("Authorization")
        if not token:
            return JsonResponse(data={"message": "Authentication token is required"}, status=401)
        try:
            token_obj = Token.objects.get(token=token)
            if not token_obj.user:
                return JsonResponse(data={"message": "Invalid authentication token"}, status=401)
            request.body = json.loads(request.body)
            request.body["user"] = token_obj.user_id
        except Token.DoesNotExist:
            return JsonResponse(data={"message": "Invalid authentication token"}, status=401)
        return fun(request, *args, **kwargs)
    return wrapper