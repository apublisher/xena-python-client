"""Xena Client - Unified client for all Xena API packages."""

import json
import requests
from pathlib import Path
from typing import Optional
from .auth import BearerTokenAuth

# Import all API packages
from xena_accountant import AccountantApi
from xena_appstore import AppstoreApi
from xena_archive import ArchiveApi
from xena_article import ArticleApi
from xena_bank import BankApi
from xena_chart import ChartApi
from xena_core import CoreApi
from xena_developer import DeveloperApi
from xena_document import DocumentApi
from xena_finance import FinanceApi
from xena_order import OrderApi
from xena_partner import PartnerApi
from xena_price import PriceApi
from xena_project import ProjectApi
from xena_provider import ProviderApi
from xena_reporting import ReportingApi
from xena_scheduling import SchedulingApi
from xena_subscription import SubscriptionApi


class XenaClient:
    """
    Unified client for Xena API.
    
    Automatically loads credentials from config.json and provides
    access to all Xena API domains.
    
    Example:
        client = XenaClient()
        partners = client.partner.api_partner__get_get__api__fiscal_fiscal_id__partner(
            fiscal_id=client.fiscal_id
        )
    """
    
    BASE_URL = "https://my.xena.biz"
    
    def __init__(self, config_path: Optional[str] = None, api_key: Optional[str] = None, 
                 fiscal_id: Optional[str] = None, *, access_token: Optional[str] = None) -> None:
        """
        Initialize Xena Client.
        
        Args:
            config_path: Path to config.json (default: looks in current directory)
            api_key: API key (overrides config file)
            fiscal_id: Fiscal ID (overrides config file)
            access_token: Existing OAuth access token, without the Bearer prefix.
                Mutually exclusive with api_key. No automatic login or refresh.
        """
        # Load config if not provided via parameters
        if config_path is not None or (access_token is None and (api_key is None or fiscal_id is None)):
            config = self._load_config(config_path)
            if api_key is None and access_token is None:
                api_key = config.get('api_key') or None
                access_token = config.get('access_token') or None
            if fiscal_id is None:
                fiscal_id = config.get('fiscal_id', '')
        
        if api_key is not None and access_token is not None:
            raise ValueError("Provide either api_key or access_token, not both")
        if not api_key and access_token is None:
            raise ValueError("API key or OAuth access token is required. Provide via parameter or config.json")
        
        self.api_key = api_key
        self.fiscal_id = fiscal_id if fiscal_id is not None else ''
        
        # Create authenticated session
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        if access_token is not None:
            self.set_access_token(access_token)
        else:
            self.session.headers['XenaAPIKey'] = api_key
        
        # Initialize all API clients (lazy loading)
        self._accountant = None
        self._appstore = None
        self._archive = None
        self._article = None
        self._bank = None
        self._chart = None
        self._core = None
        self._developer = None
        self._document = None
        self._finance = None
        self._order = None
        self._partner = None
        self._price = None
        self._project = None
        self._provider = None
        self._reporting = None
        self._scheduling = None
        self._subscription = None
    
    def set_access_token(self, access_token: str) -> None:
        """Use a new access token on all domain clients, including existing ones.

        Call after a new login or an external refresh. Tokens are never persisted.
        A rejected/expired token raises the normal requests.HTTPError on an API
        call; requests are not automatically retried or switched to API-key auth.
        """
        auth = BearerTokenAuth(access_token)
        self.session.headers.pop('XenaAPIKey', None)
        self.session.headers.pop('Authorization', None)
        self.session.auth = auth
        self.api_key = None

    def _load_config(self, config_path: Optional[str] = None) -> dict:
        """Load configuration from config.json."""
        if config_path:
            config_file = Path(config_path)
        else:
            # Look for config.json in current directory
            config_file = Path('config.json')
            if not config_file.exists():
                # Try in user's home directory
                config_file = Path.home() / '.xena' / 'config.json'
        
        if not config_file.exists():
            return {}
        
        with open(config_file, 'r') as f:
            return json.load(f)
    
    @property
    def accountant(self) -> AccountantApi:
        """Access Accountant API."""
        if self._accountant is None:
            self._accountant = AccountantApi(base_url=self.BASE_URL, session=self.session)
        return self._accountant
    
    @property
    def appstore(self) -> AppstoreApi:
        """Access AppStore API."""
        if self._appstore is None:
            self._appstore = AppstoreApi(base_url=self.BASE_URL, session=self.session)
        return self._appstore
    
    @property
    def archive(self) -> ArchiveApi:
        """Access Archive API."""
        if self._archive is None:
            self._archive = ArchiveApi(base_url=self.BASE_URL, session=self.session)
        return self._archive
    
    @property
    def article(self) -> ArticleApi:
        """Access Article API."""
        if self._article is None:
            self._article = ArticleApi(base_url=self.BASE_URL, session=self.session)
        return self._article
    
    @property
    def bank(self) -> BankApi:
        """Access Bank API."""
        if self._bank is None:
            self._bank = BankApi(base_url=self.BASE_URL, session=self.session)
        return self._bank
    
    @property
    def chart(self) -> ChartApi:
        """Access Chart API."""
        if self._chart is None:
            self._chart = ChartApi(base_url=self.BASE_URL, session=self.session)
        return self._chart
    
    @property
    def core(self) -> CoreApi:
        """Access Core API."""
        if self._core is None:
            self._core = CoreApi(base_url=self.BASE_URL, session=self.session)
        return self._core
    
    @property
    def developer(self) -> DeveloperApi:
        """Access Developer API."""
        if self._developer is None:
            self._developer = DeveloperApi(base_url=self.BASE_URL, session=self.session)
        return self._developer
    
    @property
    def document(self) -> DocumentApi:
        """Access Document API."""
        if self._document is None:
            self._document = DocumentApi(base_url=self.BASE_URL, session=self.session)
        return self._document
    
    @property
    def finance(self) -> FinanceApi:
        """Access Finance API."""
        if self._finance is None:
            self._finance = FinanceApi(base_url=self.BASE_URL, session=self.session)
        return self._finance
    
    @property
    def order(self) -> OrderApi:
        """Access Order API."""
        if self._order is None:
            self._order = OrderApi(base_url=self.BASE_URL, session=self.session)
        return self._order
    
    @property
    def partner(self) -> PartnerApi:
        """Access Partner API."""
        if self._partner is None:
            self._partner = PartnerApi(base_url=self.BASE_URL, session=self.session)
        return self._partner
    
    @property
    def price(self) -> PriceApi:
        """Access Price API."""
        if self._price is None:
            self._price = PriceApi(base_url=self.BASE_URL, session=self.session)
        return self._price
    
    @property
    def project(self) -> ProjectApi:
        """Access Project API."""
        if self._project is None:
            self._project = ProjectApi(base_url=self.BASE_URL, session=self.session)
        return self._project
    
    @property
    def provider(self) -> ProviderApi:
        """Access Provider API."""
        if self._provider is None:
            self._provider = ProviderApi(base_url=self.BASE_URL, session=self.session)
        return self._provider
    
    @property
    def reporting(self) -> ReportingApi:
        """Access Reporting API."""
        if self._reporting is None:
            self._reporting = ReportingApi(base_url=self.BASE_URL, session=self.session)
        return self._reporting
    
    @property
    def scheduling(self) -> SchedulingApi:
        """Access Scheduling API."""
        if self._scheduling is None:
            self._scheduling = SchedulingApi(base_url=self.BASE_URL, session=self.session)
        return self._scheduling
    
    @property
    def subscription(self) -> SubscriptionApi:
        """Access Subscription API."""
        if self._subscription is None:
            self._subscription = SubscriptionApi(base_url=self.BASE_URL, session=self.session)
        return self._subscription
