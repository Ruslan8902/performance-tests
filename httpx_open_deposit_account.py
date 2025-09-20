import httpx
import time

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
create_account_payload = {
  "userId": user_id
}
# Выполняем POST-запрос к эндпоинту /api/v1/accounts
create_deposit_account_response = httpx.post(f"{baseUrl}/accounts/open-deposit-account",
                              json=create_account_payload)
print(create_deposit_account_response.json())
print(create_deposit_account_response.status_code)


