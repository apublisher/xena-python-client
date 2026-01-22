from typing import Any, Dict, Optional
import requests

class ProviderApi:
    """API client for the Provider domain of the Xena API."""
    def __init__(self, base_url: str, session: Optional[requests.Session] = None) -> None:
        self.base_url = base_url.rstrip('/')
        self.session = session or requests.Session()

    def api_account_plan_template__get_list_get__api__fiscal_fiscal_id__account_plan_template(self, fiscal_id: str, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/AccountPlanTemplate"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountPlanTemplate"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
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

    def api_account_plan_template__post_post__api__fiscal_fiscal_id__account_plan_template(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/AccountPlanTemplate"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountPlanTemplate"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_account_plan_template__get_provider_list_get__api__fiscal_fiscal_id__account_plan_template__provider(self, fiscal_id: str, provider_id: int = None, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/AccountPlanTemplate/Provider"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountPlanTemplate/Provider"
        params: Dict[str, Any] = {}
        if provider_id is not None:
            params['providerId'] = provider_id
        if query_string is not None:
            params['queryString'] = query_string
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

    def api_account_plan_template__get_get__api__fiscal_fiscal_id__account_plan_template_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/AccountPlanTemplate/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountPlanTemplate/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_account_plan_template__put_put__api__fiscal_fiscal_id__account_plan_template_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/AccountPlanTemplate/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountPlanTemplate/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_account_plan_template__delete_delete__api__fiscal_fiscal_id__account_plan_template_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/AccountPlanTemplate/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountPlanTemplate/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_account_plan_template__post_copy_post__api__fiscal_fiscal_id__account_plan_template_id__copy(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/AccountPlanTemplate/{id}/Copy"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountPlanTemplate/{id}/Copy"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_account_plan_template__post_apply_post__api__fiscal_fiscal_id__account_plan_template_id__apply(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/AccountPlanTemplate/{id}/Apply"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountPlanTemplate/{id}/Apply"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_default_provider_report_layout__get_list_get__api__fiscal_fiscal_id__default_provider_report_layout(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/DefaultProviderReportLayout"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DefaultProviderReportLayout"
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

    def api_default_provider_report_layout__post_post__api__fiscal_fiscal_id__default_provider_report_layout(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/DefaultProviderReportLayout"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DefaultProviderReportLayout"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_default_provider_report_layout__put_put__api__fiscal_fiscal_id__default_provider_report_layout_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/DefaultProviderReportLayout/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DefaultProviderReportLayout/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_default_provider_report_layout__delete_delete__api__fiscal_fiscal_id__default_provider_report_layout_id(self, report_group: str, fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/DefaultProviderReportLayout/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DefaultProviderReportLayout/{id}"
        params: Dict[str, Any] = {}
        if report_group is not None:
            params['reportGroup'] = report_group
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_discount_code__get_get__api__fiscal_fiscal_id__discount_code(self, fiscal_id: str, show_used: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/DiscountCode"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DiscountCode"
        params: Dict[str, Any] = {}
        if show_used is not None:
            params['showUsed'] = show_used
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

    def api_discount_code__post_post__api__fiscal_fiscal_id__discount_code(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/DiscountCode"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DiscountCode"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_discount_code__get_get__api__fiscal_fiscal_id__discount_code_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/DiscountCode/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DiscountCode/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_discount_code__delete_delete__api__fiscal_fiscal_id__discount_code_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/DiscountCode/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DiscountCode/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_discount_code__post_create_multiple_post__api__fiscal_fiscal_id__discount_code__create_multiple(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/DiscountCode/CreateMultiple"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DiscountCode/CreateMultiple"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_discount_code__change_end_date_post__api__fiscal_fiscal_id__discount_code_id__change_expiration_date(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/DiscountCode/{id}/ChangeExpirationDate"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DiscountCode/{id}/ChangeExpirationDate"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_accepted_terms__get_get__api__fiscal_fiscal_id__fiscal_accepted_terms(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalAcceptedTerms"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalAcceptedTerms"
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

    def api_fiscal_accepted_terms__get_get__api__fiscal_fiscal_id__fiscal_accepted_terms_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalAcceptedTerms/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalAcceptedTerms/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup_provider_context__get_by_fiscal_setup_get__api__fiscal_fiscal_id__fiscal_setup_provider_context(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetupProviderContext"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetupProviderContext"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup_provider_context__post_post__api__fiscal_fiscal_id__fiscal_setup_provider_context(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalSetupProviderContext"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetupProviderContext"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup_provider_context__get_get__api__fiscal_fiscal_id__fiscal_setup_provider_context_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetupProviderContext/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetupProviderContext/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup_provider_context__put_put__api__fiscal_fiscal_id__fiscal_setup_provider_context_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/FiscalSetupProviderContext/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetupProviderContext/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup_provider_context__delete_delete__api__fiscal_fiscal_id__fiscal_setup_provider_context_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/FiscalSetupProviderContext/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetupProviderContext/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup_provider_context__get_onboarding_types_list_get__api__fiscal_fiscal_id__fiscal_setup_provider_context__get_onboarding_types_list(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetupProviderContext/GetOnboardingTypesList"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetupProviderContext/GetOnboardingTypesList"
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

    def api_ledger_tag_template__get_list_get__api__fiscal_fiscal_id__ledger_tag_template(self, account_plan_template_id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTagTemplate"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTagTemplate"
        params: Dict[str, Any] = {}
        if account_plan_template_id is not None:
            params['accountPlanTemplateId'] = account_plan_template_id
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

    def api_ledger_tag_template__post_post__api__fiscal_fiscal_id__ledger_tag_template(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/LedgerTagTemplate"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTagTemplate"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag_template__get_get__api__fiscal_fiscal_id__ledger_tag_template_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTagTemplate/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTagTemplate/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag_template__put_put__api__fiscal_fiscal_id__ledger_tag_template_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/LedgerTagTemplate/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTagTemplate/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag_template__delete_delete__api__fiscal_fiscal_id__ledger_tag_template_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/LedgerTagTemplate/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTagTemplate/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_provider__get_provided_fiscal_setups_get__api__fiscal_fiscal_id__provider__provided_fiscal_setups(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, filter_query_string: str = None, filter_created_from_date: int = None, filter_created_to_date: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Provider/ProvidedFiscalSetups"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Provider/ProvidedFiscalSetups"
        params: Dict[str, Any] = {}
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        if filter_query_string is not None:
            params['filter.queryString'] = filter_query_string
        if filter_created_from_date is not None:
            params['filter.createdFromDate'] = filter_created_from_date
        if filter_created_to_date is not None:
            params['filter.createdToDate'] = filter_created_to_date
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_provider__put_put__api__fiscal_fiscal_id__provider__update_sproom_account(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Provider/UpdateSproomAccount"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Provider/UpdateSproomAccount"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_provider_culture_layout__get_by_report_layout_list_get__api__fiscal_fiscal_id__provider_report_layout_id__cultures(self, id: int, fiscal_id: str, query_string: str = None, include_default: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ProviderReportLayout/{id}/Cultures"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderReportLayout/{id}/Cultures"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if include_default is not None:
            params['includeDefault'] = include_default
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

    def api_provider_culture_layout__get_get__api__fiscal_fiscal_id__provider_culture_layout_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ProviderCultureLayout/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderCultureLayout/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_provider_culture_layout__put_put__api__fiscal_fiscal_id__provider_culture_layout_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ProviderCultureLayout/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderCultureLayout/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_provider_culture_layout__delete_delete__api__fiscal_fiscal_id__provider_culture_layout_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ProviderCultureLayout/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderCultureLayout/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_provider_culture_layout__post_post__api__fiscal_fiscal_id__provider_culture_layout(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ProviderCultureLayout"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderCultureLayout"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_provider_email_setup__get_list_get__api__fiscal_fiscal_id__provider_email_setup_culture(self, culture: str, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ProviderEmailSetup/{culture}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderEmailSetup/{culture}"
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

    def api_provider_email_setup__get_get__api__fiscal_fiscal_id__provider_email_setup_culture_email_part_constant(self, culture: str, email_part_constant: str, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ProviderEmailSetup/{culture}/{emailPartConstant}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderEmailSetup/{culture}/{email_part_constant}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_provider_email_setup__put_put__api__fiscal_fiscal_id__provider_email_setup_culture_email_part_constant(self, culture: str, email_part_constant: str, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ProviderEmailSetup/{culture}/{emailPartConstant}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderEmailSetup/{culture}/{email_part_constant}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_provider_email_setup__post_post__api__fiscal_fiscal_id__provider_email_setup_culture_email_part_constant(self, culture: str, email_part_constant: str, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ProviderEmailSetup/{culture}/{emailPartConstant}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderEmailSetup/{culture}/{email_part_constant}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_provider_email_setup__delete_delete__api__fiscal_fiscal_id__provider_email_setup_culture_email_part_constant(self, culture: str, email_part_constant: str, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ProviderEmailSetup/{culture}/{emailPartConstant}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderEmailSetup/{culture}/{email_part_constant}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_provider_report_layout__get_list_get__api__fiscal_fiscal_id__provider_report_layout(self, fiscal_id: str, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ProviderReportLayout"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderReportLayout"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
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

    def api_provider_report_layout__post_post__api__fiscal_fiscal_id__provider_report_layout(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ProviderReportLayout"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderReportLayout"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_provider_report_layout__get_get__api__fiscal_fiscal_id__provider_report_layout_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ProviderReportLayout/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderReportLayout/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_provider_report_layout__put_put__api__fiscal_fiscal_id__provider_report_layout_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ProviderReportLayout/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderReportLayout/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_provider_report_layout__delete_delete__api__fiscal_fiscal_id__provider_report_layout_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ProviderReportLayout/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderReportLayout/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_terms__get_get__api__fiscal_fiscal_id__terms(self, fiscal_id: str, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Terms"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Terms"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
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

    def api_terms__post_post__api__fiscal_fiscal_id__terms(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Terms"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Terms"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_terms__get_get__api__fiscal_fiscal_id__terms_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Terms/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Terms/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_terms__put_put__api__fiscal_fiscal_id__terms_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Terms/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Terms/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_terms__delete_delete__api__fiscal_fiscal_id__terms_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Terms/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Terms/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_terms__put_activate_put__api__fiscal_fiscal_id__terms_id__activate(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Terms/{id}/Activate"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Terms/{id}/Activate"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_terms__put_set_active_to_put__api__fiscal_fiscal_id__terms_id__set_active_to(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Terms/{id}/SetActiveTo"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Terms/{id}/SetActiveTo"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_terms__get_terms_type_list_get__api__fiscal_fiscal_id__terms__types(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Terms/Types"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Terms/Types"
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

    def api_terms_culture__get_by_terms_get__api__fiscal_fiscal_id__terms_id__culture(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Terms/{id}/Culture"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Terms/{id}/Culture"
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

    def api_terms_culture__get_get__api__fiscal_fiscal_id__terms_culture_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/TermsCulture/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/TermsCulture/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_terms_culture__put_put__api__fiscal_fiscal_id__terms_culture_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/TermsCulture/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/TermsCulture/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_terms_culture__delete_delete__api__fiscal_fiscal_id__terms_culture_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/TermsCulture/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/TermsCulture/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_terms_culture__post_post__api__fiscal_fiscal_id__terms_culture(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/TermsCulture"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/TermsCulture"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text
