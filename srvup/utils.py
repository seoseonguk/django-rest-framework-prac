def jwt_response_payload_handler(token, user=None, *args, **kwargs):
    return {
        "token": token,
        "user": str(user.username),
        "active": user.is_active
    }