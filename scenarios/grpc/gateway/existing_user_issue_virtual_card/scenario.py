from locust import task
from locust import task, events
from locust.env import Environment

from clients.grpc.gateway.locust import GatewayGRPCTaskSet
from seeds.scenarios.existing_user_issue_virtual_card import ExistingUserIssueVirtualCardSeedsScenario
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountResponse
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser


@events.init.add_listener
def init(environment: Environment, **kwargs):
    # Создаем экземпляр сидинг-сценария
    seeds_scenario = ExistingUserIssueVirtualCardSeedsScenario()

    # Выполняем генерацию данных, если они ещё не созданы
    seeds_scenario.build()

    # Загружаем сгенерированных пользователей в окружение Locust
    environment.seeds = seeds_scenario.load()


# Класс сценария: описывает последовательный флоу нового пользователя
class IssueVirtualCardTaskSet(GatewayGRPCTaskSet):
    seed_user: SeedUserResult

    # Метод вызывается при запуске каждой сессии пользователя (до начала задач)
    def on_start(self) -> None:
        super().on_start()

        # Получаем следующего пользователя из списка (по порядку!)
        self.seed_user = self.user.environment.seeds.get_next_user()

    @task(3)
    def get_accounts(self):
        # Запрашиваем список счетов
        self.accounts_gateway_client.get_accounts(user_id=self.seed_user.user_id)

    @task(1)
    def issue_virtual_card_operation(self):
        self.cards_gateway_client.issue_virtual_card(
            user_id=self.seed_user.user_id,
            account_id=self.seed_user.debit_card_accounts[0].account_id,
        )


# Класс пользователя — связывает TaskSet со средой исполнения Locust
class IssueVirtualCardScenarioUser(LocustBaseUser):
    # Назначаем сценарий, который будет выполняться этим пользователем
    tasks = [IssueVirtualCardTaskSet]
