from typing import TypedDict

from clients.http.client import HTTPClient
from httpx import Response


class IssueCardRequestDict(TypedDict):
    """
    Структура данных для создания новой виртуальной/физической карты.
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Выпуск новой виртуальной карты.

        :param request: Словарь с данными для создания новой виртуальной карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.client.post(url="/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Выпуск новой физической карты.

        :param request: Словарь с данными для создания новой физической карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.client.post(url="/api/v1/cards/issue-physical-card", json=request)
