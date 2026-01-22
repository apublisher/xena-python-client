from typing import Any, Dict, Optional
import requests

class ReportingApi:
    """API client for the Reporting domain of the Xena API."""
    def __init__(self, base_url: str, session: Optional[requests.Session] = None) -> None:
        self.base_url = base_url.rstrip('/')
        self.session = session or requests.Session()

    def api_report_email_setup__get_get__api__fiscal_fiscal_id__report_email_setup(self, fiscal_id: str, culture: str = None, report_module: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ReportEmailSetup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportEmailSetup"
        params: Dict[str, Any] = {}
        if culture is not None:
            params['culture'] = culture
        if report_module is not None:
            params['reportModule'] = report_module
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_email_setup__post_post__api__fiscal_fiscal_id__report_email_setup(self, report_email_setup: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ReportEmailSetup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportEmailSetup"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=report_email_setup, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_email_setup__get_get__api__fiscal_fiscal_id__report_email_setup_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ReportEmailSetup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportEmailSetup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_email_setup__put_put__api__fiscal_fiscal_id__report_email_setup_id(self, report_email_setup: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ReportEmailSetup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportEmailSetup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=report_email_setup, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_email_setup__delete_delete__api__fiscal_fiscal_id__report_email_setup_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ReportEmailSetup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportEmailSetup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_layout__get_get__api__fiscal_fiscal_id__report_layout(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ReportLayout"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportLayout"
        params: Dict[str, Any] = {}
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_layout__post_post__api__fiscal_fiscal_id__report_layout(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ReportLayout"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportLayout"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_layout__get_get__api__fiscal_fiscal_id__report_layout_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ReportLayout/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportLayout/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_layout__put_put__api__fiscal_fiscal_id__report_layout_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ReportLayout/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportLayout/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_layout__delete_delete__api__fiscal_fiscal_id__report_layout_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ReportLayout/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportLayout/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_layout__get_by_group_get__api__fiscal_fiscal_id__report_layout__group_group(self, group: str, fiscal_id: str, querystring: str = None, include_default: bool = None, use_standard: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ReportLayout/Group/{group}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportLayout/Group/{group}"
        params: Dict[str, Any] = {}
        if querystring is not None:
            params['querystring'] = querystring
        if include_default is not None:
            params['includeDefault'] = include_default
        if use_standard is not None:
            params['useStandard'] = use_standard
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_layout__post_default_reminder_steps_post__api__fiscal_fiscal_id__report_layout__default_reminder_steps(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ReportLayout/DefaultReminderSteps"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportLayout/DefaultReminderSteps"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_layout__get_order_report_get__api__fiscal_fiscal_id__report_layout__order_report(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ReportLayout/OrderReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportLayout/OrderReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_layout__get_modules_get__api__fiscal_fiscal_id__report_layout__modules(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ReportLayout/Modules"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportLayout/Modules"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_layout_text__get_get__api__fiscal_fiscal_id__report_layout_text_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ReportLayoutText/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportLayoutText/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_layout_text__put_put__api__fiscal_fiscal_id__report_layout_text_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ReportLayoutText/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportLayoutText/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_layout_text__delete_delete__api__fiscal_fiscal_id__report_layout_text_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ReportLayoutText/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportLayoutText/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_layout_text__post_post__api__fiscal_fiscal_id__report_layout_text(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ReportLayoutText"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportLayoutText"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_layout_text__get_by_report_layout_get__api__fiscal_fiscal_id__report_layout_id__text(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ReportLayout/{id}/Text"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportLayout/{id}/Text"
        params: Dict[str, Any] = {}
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_subscription__get_get__api__fiscal_fiscal_id__report_subscription(self, fiscal_id: str, report_module: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ReportSubscription"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportSubscription"
        params: Dict[str, Any] = {}
        if report_module is not None:
            params['reportModule'] = report_module
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_subscription__post_post__api__fiscal_fiscal_id__report_subscription(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ReportSubscription"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportSubscription"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_subscription__get_get__api__fiscal_fiscal_id__report_subscription_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ReportSubscription/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportSubscription/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_subscription__put_put__api__fiscal_fiscal_id__report_subscription_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ReportSubscription/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportSubscription/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_report_subscription__delete_delete__api__fiscal_fiscal_id__report_subscription_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ReportSubscription/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReportSubscription/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text
