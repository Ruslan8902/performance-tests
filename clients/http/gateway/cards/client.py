from typing import TypedDict

from clients.http.client import HTTPClient
from httpx import Response


class IssueVirtualCardRequestDict(TypedDict):
    """
    Структура данных для выпуска виртуальной карты.
    """
    userId: str
    accountId: str


class IssuePhysicalCardRequestDict(TypedDict):
    """
    Структура данных для выпуска физической карты.
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: IssueVirtualCardRequestDict) -> Response:
        """
        Выпуск новой виртуальной карты.

        :param request: Словарь с данными для создания новой виртуальной карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(url="/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssuePhysicalCardRequestDict) -> Response:
        """
        Выпуск новой физической карты.

        :param request: Словарь с данными для создания новой физической карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(url="/api/v1/cards/issue-physical-card", json=request)
