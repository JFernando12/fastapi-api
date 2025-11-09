def success_response(data=None, message="Operation successful"):
    return {
        "status": "success",
        "message": message,
        "data": data
    }