from typing import Any, Dict, Optional
import requests

class ProjectApi:
    """API client for the Project domain of the Xena API."""
    def __init__(self, base_url: str, session: Optional[requests.Session] = None) -> None:
        self.base_url = base_url.rstrip('/')
        self.session = session or requests.Session()

    def api_cost_type__get_get__api__fiscal_fiscal_id__cost_type(self, fiscal_id: str, query_string: str = None, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/CostType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/CostType"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if include_defaults is not None:
            params['includeDefaults'] = include_defaults
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

    def api_cost_type__post_post__api__fiscal_fiscal_id__cost_type(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/CostType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/CostType"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_cost_type__get_get__api__fiscal_fiscal_id__cost_type_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/CostType/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/CostType/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_cost_type__put_put__api__fiscal_fiscal_id__cost_type_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/CostType/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/CostType/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_cost_type__delete_delete__api__fiscal_fiscal_id__cost_type_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/CostType/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/CostType/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_cost_type__post_create_standard_post__api__fiscal_fiscal_id__cost_type__standard(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/CostType/Standard"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/CostType/Standard"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_cost_type__get_export_type_list_get__api__fiscal_fiscal_id__cost_type__cost_type_group(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/CostType/CostTypeGroup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/CostType/CostTypeGroup"
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

    def api_project__get_get__api__fiscal_fiscal_id__project(self, fiscal_id: str, query_string: str = None, include_defaults: bool = None, order_by_asc: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Project"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if include_defaults is not None:
            params['includeDefaults'] = include_defaults
        if order_by_asc is not None:
            params['orderByAsc'] = order_by_asc
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

    def api_project__post_post__api__fiscal_fiscal_id__project(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Project"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project__get_get__api__fiscal_fiscal_id__project_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Project/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project__put_put__api__fiscal_fiscal_id__project_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Project/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project__delete_delete__api__fiscal_fiscal_id__project_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Project/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project__get_by_number_get__api__fiscal_fiscal_id__project__by_number(self, project_number: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Project/ByNumber"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/ByNumber"
        params: Dict[str, Any] = {}
        if project_number is not None:
            params['projectNumber'] = project_number
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project__get_open_get__api__fiscal_fiscal_id__project__open(self, fiscal_id: str, query_string: str = None, include_defaults: bool = None, order_by_asc: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Project/Open"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/Open"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if include_defaults is not None:
            params['includeDefaults'] = include_defaults
        if order_by_asc is not None:
            params['orderByAsc'] = order_by_asc
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

    def api_project__get_closed_get__api__fiscal_fiscal_id__project__closed(self, fiscal_id: str, query_string: str = None, include_defaults: bool = None, order_by_asc: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Project/Closed"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/Closed"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if include_defaults is not None:
            params['includeDefaults'] = include_defaults
        if order_by_asc is not None:
            params['orderByAsc'] = order_by_asc
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

    def api_project__get_summary_get__api__fiscal_fiscal_id__project_id__summary(self, id: int, fiscal_id: str, show_invoiced: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Project/{id}/Summary"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/{id}/Summary"
        params: Dict[str, Any] = {}
        if show_invoiced is not None:
            params['showInvoiced'] = show_invoiced
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project__get_cost_type_statistics_get__api__fiscal_fiscal_id__project__statistics__cost_type(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Project/Statistics/CostType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/Statistics/CostType"
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

    def api_project__get_closed_project_statistics_get__api__fiscal_fiscal_id__project__statistics__closed(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Project/Statistics/Closed"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/Statistics/Closed"
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

    def api_project__get_resource_inbox_statistics_data_get__api__fiscal_fiscal_id__project__statistics__inbox(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Project/Statistics/Inbox"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/Statistics/Inbox"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project__get_projects_for_status_get__api__fiscal_fiscal_id__project__projects_for_status_id(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, filter_query_string: str = None, filter_responsible_id: int = None, filter_limit_to_responsible: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Project/ProjectsForStatus/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/ProjectsForStatus/{id}"
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
        if filter_responsible_id is not None:
            params['filter.responsibleId'] = filter_responsible_id
        if filter_limit_to_responsible is not None:
            params['filter.limitToResponsible'] = filter_limit_to_responsible
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project__get_project_statistics_data_get__api__fiscal_fiscal_id__project_id__get_project_statistics_data(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Project/{id}/GetProjectStatisticsData"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/{id}/GetProjectStatisticsData"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project__get_history_get__api__fiscal_fiscal_id__project__history(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Project/History"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/History"
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

    def api_project__get_favorite_get__api__fiscal_fiscal_id__project__favorite(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Project/Favorite"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/Favorite"
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

    def api_project__put_mark_favorite_put__api__fiscal_fiscal_id__project_id__mark_favorite(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Project/{id}/MarkFavorite"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/{id}/MarkFavorite"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project__delete_mark_favorite_delete__api__fiscal_fiscal_id__project_id__remove_favorite(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Project/{id}/RemoveFavorite"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/{id}/RemoveFavorite"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project__put_bookkeep_invoice_put__api__fiscal_fiscal_id__project_id__bookkeep_invoice(self, id: int, project_bookkeep_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Project/{id}/BookkeepInvoice"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/{id}/BookkeepInvoice"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=project_bookkeep_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project__put_pay_on_account_put__api__fiscal_fiscal_id__project_id__pay_on_account(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Project/{id}/PayOnAccount"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/{id}/PayOnAccount"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project__get_budget_types_get__api__fiscal_fiscal_id__project__budget_types(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Project/BudgetTypes"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/BudgetTypes"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project_calculation_post__get_by_project_get__api__fiscal_fiscal_id__project_calculation_post(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ProjectCalculationPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProjectCalculationPost"
        params: Dict[str, Any] = {}
        if id is not None:
            params['id'] = id
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

    def api_project_calculation_post__post_post__api__fiscal_fiscal_id__project_calculation_post(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ProjectCalculationPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProjectCalculationPost"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project_calculation_post__get_get__api__fiscal_fiscal_id__project_calculation_post_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ProjectCalculationPost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProjectCalculationPost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project_calculation_post__put_put__api__fiscal_fiscal_id__project_calculation_post_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ProjectCalculationPost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProjectCalculationPost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project_calculation_post__delete_delete__api__fiscal_fiscal_id__project_calculation_post_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ProjectCalculationPost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProjectCalculationPost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project_calculation_post__post_create_default_post__api__fiscal_fiscal_id__project_project_id__project_calculation_post__standard(self, project_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Project/{projectId}/ProjectCalculationPost/Standard"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/{project_id}/ProjectCalculationPost/Standard"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project_group__get_get__api__fiscal_fiscal_id__project_group(self, fiscal_id: str, query_string: str = None, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ProjectGroup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProjectGroup"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if include_defaults is not None:
            params['includeDefaults'] = include_defaults
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

    def api_project_group__post_post__api__fiscal_fiscal_id__project_group(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ProjectGroup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProjectGroup"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project_group__get_get__api__fiscal_fiscal_id__project_group_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ProjectGroup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProjectGroup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project_group__put_put__api__fiscal_fiscal_id__project_group_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ProjectGroup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProjectGroup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project_group__delete_delete__api__fiscal_fiscal_id__project_group_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ProjectGroup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProjectGroup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project_group__post_create_standard_post__api__fiscal_fiscal_id__project_group__standard(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ProjectGroup/Standard"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProjectGroup/Standard"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project_status__get_get__api__fiscal_fiscal_id__project_status(self, fiscal_id: str, query_string: str = None, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ProjectStatus"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProjectStatus"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if include_defaults is not None:
            params['includeDefaults'] = include_defaults
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

    def api_project_status__post_post__api__fiscal_fiscal_id__project_status(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ProjectStatus"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProjectStatus"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project_status__get_get__api__fiscal_fiscal_id__project_status_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ProjectStatus/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProjectStatus/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project_status__put_put__api__fiscal_fiscal_id__project_status_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ProjectStatus/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProjectStatus/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project_status__delete_delete__api__fiscal_fiscal_id__project_status_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ProjectStatus/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProjectStatus/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_project_status__post_create_standard_post__api__fiscal_fiscal_id__project_status__standard(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ProjectStatus/Standard"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProjectStatus/Standard"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_work_in_progress_detail__get_list_get__api__fiscal_fiscal_id__work_in_progress_detail(self, fiscal_id: str, filter_is_closed: bool = None, filter_date_from: int = None, filter_date_to: int = None, filter_posting_date_from: int = None, filter_posting_date_to: int = None, filter_statement_date: int = None, filter_project_status_id: int = None, filter_limit_to_project_status: bool = None, filter_project_id: int = None, filter_limit_to_project: bool = None, filter_project_group_id: int = None, filter_limit_to_project_group: bool = None, filter_responsible_id: int = None, filter_limit_to_responsible: bool = None, filter_partner_id: int = None, filter_limit_to_partner: bool = None, filter_department_id: int = None, filter_limit_to_department: bool = None, filter_bearer_id: int = None, filter_limit_to_bearer: bool = None, filter_purpose_id: int = None, filter_limit_to_purpose: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/WorkInProgressDetail"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/WorkInProgressDetail"
        params: Dict[str, Any] = {}
        if filter_is_closed is not None:
            params['filter.isClosed'] = filter_is_closed
        if filter_date_from is not None:
            params['filter.dateFrom'] = filter_date_from
        if filter_date_to is not None:
            params['filter.dateTo'] = filter_date_to
        if filter_posting_date_from is not None:
            params['filter.postingDateFrom'] = filter_posting_date_from
        if filter_posting_date_to is not None:
            params['filter.postingDateTo'] = filter_posting_date_to
        if filter_statement_date is not None:
            params['filter.statementDate'] = filter_statement_date
        if filter_project_status_id is not None:
            params['filter.projectStatusId'] = filter_project_status_id
        if filter_limit_to_project_status is not None:
            params['filter.limitToProjectStatus'] = filter_limit_to_project_status
        if filter_project_id is not None:
            params['filter.projectId'] = filter_project_id
        if filter_limit_to_project is not None:
            params['filter.limitToProject'] = filter_limit_to_project
        if filter_project_group_id is not None:
            params['filter.projectGroupId'] = filter_project_group_id
        if filter_limit_to_project_group is not None:
            params['filter.limitToProjectGroup'] = filter_limit_to_project_group
        if filter_responsible_id is not None:
            params['filter.responsibleId'] = filter_responsible_id
        if filter_limit_to_responsible is not None:
            params['filter.limitToResponsible'] = filter_limit_to_responsible
        if filter_partner_id is not None:
            params['filter.partnerId'] = filter_partner_id
        if filter_limit_to_partner is not None:
            params['filter.limitToPartner'] = filter_limit_to_partner
        if filter_department_id is not None:
            params['filter.departmentId'] = filter_department_id
        if filter_limit_to_department is not None:
            params['filter.limitToDepartment'] = filter_limit_to_department
        if filter_bearer_id is not None:
            params['filter.bearerId'] = filter_bearer_id
        if filter_limit_to_bearer is not None:
            params['filter.limitToBearer'] = filter_limit_to_bearer
        if filter_purpose_id is not None:
            params['filter.purposeId'] = filter_purpose_id
        if filter_limit_to_purpose is not None:
            params['filter.limitToPurpose'] = filter_limit_to_purpose
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
