def handle_request(request):
    # Validation
    if not isinstance(request, str):
        return {"error": "Invalid request type"}

    # Processing
    processed = request.upper()

    # Response
    response = {
        "original": request,
        "processed": processed
    }

    return response


# Simulate a request
req = "hello ai system"
res = handle_request(req)

print("Response:", res)

def handle_request(request):
    if not isinstance(request, str):
        return {"error": "Invalid request type"}

    processed = request.upper()

    return {
        "original": request,
        "processed": processed
    }

# Failure test: invalid input
bad_request = 123
result = handle_request(bad_request)

print("Failure Test Result:", result)