import httpx
import time
import pprint

baseUrl = "http://localhost:8003/api/v1"

# Инициализируем JSON-данные, которые будем отправлять в API
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
# Выполняем POST-запрос к эндпоинту /api/v1/users
create_user_response = httpx.post(f"{baseUrl}/users", json=create_user_payload)
user_id = create_user_response.json()["user"]["id"]

# Инициализируем JSON-данные, которые будем отправлять в API
create_credit_card_account_payload = {
    "userId": user_id
}
# Выполняем POST-запрос к эндпоинту /api/v1/accounts
create_credit_card_account_response = httpx.post(f"{baseUrl}/accounts/open-credit-card-account",
                                                 json=create_credit_card_account_payload)
account_id = create_credit_card_account_response.json()["account"]["id"]
card_id = create_credit_card_account_response.json()["account"]["cards"][0]["id"]

# Инициализируем JSON-данные, которые будем отправлять в API
make_purchase_operation_payload = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "cardId": card_id,
    "accountId": account_id,
    "category": "taxi"
}
# Выполняем POST-запрос к эндпоинту /api/v1/operations
make_purchase_operation_response = httpx.post(f"{baseUrl}/operations/make-purchase-operation",
                                              json=make_purchase_operation_payload)
operation_id = make_purchase_operation_response.json()["operation"]["id"]

# Выполняем GET-запрос к эндпоинту /api/v1/operations
get_operation_receipt_response = httpx.get(
    f"{baseUrl}/operations/operation-receipt/{operation_id}")
operation_id = make_purchase_operation_response.json()["operation"]["id"]
pprint.pp(get_operation_receipt_response.json())
