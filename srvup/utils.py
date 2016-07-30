def jwt_response_payload_handler(token, user=None, *args, **kwargs):
    return {
        "token": token,
        "user": str(user.username),
        "active": user.is_active
    }
# 만약에 결제 모듈을 붙인다면, 여기다가 token을 처음로그인 할 때 받아내야 한다.