from typing import Any, Dict, Optional
import requests

class ChartApi:
    """API client for the Chart domain of the Xena API."""
    def __init__(self, base_url: str, session: Optional[requests.Session] = None) -> None:
        self.base_url = base_url.rstrip('/')
        self.session = session or requests.Session()

    def api_article_chart__get_average_price_developement_get__api__fiscal_fiscal_id__chart__article_id__average_price_developement(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Chart/Article/{id}/AveragePriceDevelopement"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Chart/Article/{id}/AveragePriceDevelopement"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_chart__get_historic_stock_get__api__fiscal_fiscal_id__chart__article_id__historic_stock(self, id: int, fiscal_period_id: int, fiscal_id: str, article_variant_id: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Chart/Article/{id}/HistoricStock"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Chart/Article/{id}/HistoricStock"
        params: Dict[str, Any] = {}
        if fiscal_period_id is not None:
            params['fiscalPeriodId'] = fiscal_period_id
        if article_variant_id is not None:
            params['articleVariantId'] = article_variant_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_chart__get_turnover_get__api__fiscal_fiscal_id__chart__article_id__turnover(self, id: int, fiscal_id: str, fiscal_period_id: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Chart/Article/{id}/Turnover"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Chart/Article/{id}/Turnover"
        params: Dict[str, Any] = {}
        if fiscal_period_id is not None:
            params['fiscalPeriodId'] = fiscal_period_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_group_chart__get_turnover_get__api__fiscal_fiscal_id__chart__article_group_id__turnover(self, id: int, fiscal_id: str, fiscal_period_id: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Chart/ArticleGroup/{id}/Turnover"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Chart/ArticleGroup/{id}/Turnover"
        params: Dict[str, Any] = {}
        if fiscal_period_id is not None:
            params['fiscalPeriodId'] = fiscal_period_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_period_chart__get_statistics_get__api__api__fiscal_fiscal_id__chart__fiscal_period_id__statistics(self, id: int, fiscal_id: str, department_id: int = None, bearer_id: int = None, purpose_id: int = None, limit_to_department: bool = None, limit_to_bearer: bool = None, limit_to_purpose: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Api/Fiscal/{fiscalId}/Chart/FiscalPeriod/{id}/Statistics"""
        url = f"{self.base_url}/Api/Api/Fiscal/{fiscal_id}/Chart/FiscalPeriod/{id}/Statistics"
        params: Dict[str, Any] = {}
        if department_id is not None:
            params['departmentId'] = department_id
        if bearer_id is not None:
            params['bearerId'] = bearer_id
        if purpose_id is not None:
            params['purposeId'] = purpose_id
        if limit_to_department is not None:
            params['limitToDepartment'] = limit_to_department
        if limit_to_bearer is not None:
            params['limitToBearer'] = limit_to_bearer
        if limit_to_purpose is not None:
            params['limitToPurpose'] = limit_to_purpose
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_period_chart__get_statistics_get__api__api__fiscal_fiscal_id__chart__fiscal_period_id__ledger_account_ledger_account__statistics(self, id: int, ledger_account: str, fiscal_id: str, department_id: int = None, bearer_id: int = None, purpose_id: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Api/Fiscal/{fiscalId}/Chart/FiscalPeriod/{id}/LedgerAccount/{ledgerAccount}/Statistics"""
        url = f"{self.base_url}/Api/Api/Fiscal/{fiscal_id}/Chart/FiscalPeriod/{id}/LedgerAccount/{ledger_account}/Statistics"
        params: Dict[str, Any] = {}
        if department_id is not None:
            params['departmentId'] = department_id
        if bearer_id is not None:
            params['bearerId'] = bearer_id
        if purpose_id is not None:
            params['purposeId'] = purpose_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_period_chart__get_dashboard_get__api__api__fiscal_fiscal_id__chart__fiscal_period_id__dashboard(self, id: int, fiscal_id: str, department_id: int = None, bearer_id: int = None, purpose_id: int = None, limit_to_department: bool = None, limit_to_bearer: bool = None, limit_to_purpose: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Api/Fiscal/{fiscalId}/Chart/FiscalPeriod/{id}/Dashboard"""
        url = f"{self.base_url}/Api/Api/Fiscal/{fiscal_id}/Chart/FiscalPeriod/{id}/Dashboard"
        params: Dict[str, Any] = {}
        if department_id is not None:
            params['departmentId'] = department_id
        if bearer_id is not None:
            params['bearerId'] = bearer_id
        if purpose_id is not None:
            params['purposeId'] = purpose_id
        if limit_to_department is not None:
            params['limitToDepartment'] = limit_to_department
        if limit_to_bearer is not None:
            params['limitToBearer'] = limit_to_bearer
        if limit_to_purpose is not None:
            params['limitToPurpose'] = limit_to_purpose
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag_chart__get_turnover_get__api__fiscal_fiscal_id__chart__ledger_tag_id__turnover(self, id: int, fiscal_id: str, fiscal_period_id: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Chart/LedgerTag/{id}/Turnover"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Chart/LedgerTag/{id}/Turnover"
        params: Dict[str, Any] = {}
        if fiscal_period_id is not None:
            params['fiscalPeriodId'] = fiscal_period_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_chart__get_cost_type_pie_get__api__fiscal_fiscal_id__chart__order_id__cost_type(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Chart/Order/{id}/CostType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Chart/Order/{id}/CostType"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_chart__get_revenue_pie_get__api__fiscal_fiscal_id__chart__order_id__revenue(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Chart/Order/{id}/Revenue"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Chart/Order/{id}/Revenue"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_chart__get_statistics_get__api__fiscal_fiscal_id__chart__partner_id__statistics(self, id: int, fiscal_period_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Chart/Partner/{id}/Statistics"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Chart/Partner/{id}/Statistics"
        params: Dict[str, Any] = {}
        if fiscal_period_id is not None:
            params['fiscalPeriodId'] = fiscal_period_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project_chart__get_totals_get__api__fiscal_fiscal_id__chart__project__totals(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Chart/Project/Totals"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Chart/Project/Totals"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project_chart__get_actual_get__api__fiscal_fiscal_id__chart__project_id__actual(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Chart/Project/{id}/Actual"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Chart/Project/{id}/Actual"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project_chart__get_budget_get__api__fiscal_fiscal_id__chart__project_id__budget(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Chart/Project/{id}/Budget"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Chart/Project/{id}/Budget"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_subscription_chart__get_totals_by_article_group_get__api__fiscal_fiscal_id__chart__subscription__article_group_totals(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Chart/Subscription/ArticleGroupTotals"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Chart/Subscription/ArticleGroupTotals"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_subscription_chart__get_forecast_get__api__fiscal_fiscal_id__chart__subscription__forecast(self, fiscal_id: str, fiscal_period_id: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Chart/Subscription/Forecast"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Chart/Subscription/Forecast"
        params: Dict[str, Any] = {}
        if fiscal_period_id is not None:
            params['fiscalPeriodId'] = fiscal_period_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_subscription_chart__get_development_get__api__fiscal_fiscal_id__chart__subscription__development(self, fiscal_id: str, fiscal_period_id: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Chart/Subscription/Development"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Chart/Subscription/Development"
        params: Dict[str, Any] = {}
        if fiscal_period_id is not None:
            params['fiscalPeriodId'] = fiscal_period_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text
