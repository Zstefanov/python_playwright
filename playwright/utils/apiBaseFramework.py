from playwright.sync_api import Playwright

ordersPayLoad = {"orders": [{"country": "India", "productOrderedId": "67a8dde5c0d3e6622a297cc8"}]}


class APIUtils:

    def getToken(self, playwright: Playwright, user_credentials):
        user_email = user_credentials["userEmail"]
        user_password = user_credentials["userPassword"]
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data={"userEmail": user_email,
                                                  "userPassword": user_password })
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]

    def createOrder(self, playwright: Playwright, user_credentials):
        token = self.getToken(playwright, user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                            data=ordersPayLoad,
                                            headers={"Authorization": token,
                                                     "Content-Type": "application/json"
                                                     })
        print(response.json())
        response_body = response.json()
        orderId = response_body["orders"][0]
        return orderId