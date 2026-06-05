from playwright.sync_api import Playwright


def test_fakestore_api(playwright: Playwright):
    """
    API test for https://fakestoreapi.com/products/1 using Playwright MCP (request API)
    Steps:
    1. Create a request context
    2. Send GET to the endpoint
    3. Verify status code == 200
    4. Validate JSON contains required keys
    5. Validate specific expected values
    6. Log full response body
    """

    url = "https://fakestoreapi.com/products/1"

    # 1. Create a request context
    request = playwright.request.new_context()

    # 2. Send GET request
    response = request.get(url)

    # 3. Verify the response status code
    status = response.status
    print(f"Response status: {status}")
    assert status == 200, f"Expected status 200 but got {status}"

    # 4. Parse JSON and validate keys
    body = response.json()
    print("Full response JSON:")
    print(body)

    required_keys = ["id", "title", "price", "category", "description"]
    for key in required_keys:
        assert key in body, f"Missing expected key in response JSON: {key}"

    # 5. Validate expected values
    assert body.get("id") == 1, f"Expected id 1, got {body.get('id')}"
    # Use tolerance for float comparison
    assert abs(float(body.get("price", 0)) - 109.95) < 0.001, f"Expected price 109.95, got {body.get('price')}"
    assert body.get("category") == "men's clothing", f"Expected category ""men's clothing"" but got {body.get('category')}"

    # 6. Cleanup
    request.dispose()

