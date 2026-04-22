class DeviceTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user_agent.is_mobile:
            request.device_type = 'mobile'
        elif request.user_agent.is_pc:
            request.device_type = 'pc'
        else:
            request.device_type = 'unknown'

        response = self.get_response(request)
        return response



