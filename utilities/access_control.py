from flask import request

from utilities.variables import unauthorized_list


def request_authorization():
    """
    Returns True if incoming_request passes security checks. Else False.
    """
    incoming_request = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    if not user_agent:
        return False
    if unauthorized_list.get(incoming_request):
        return False
    return True
