from typing import Any, Dict, Optional
import requests

class AccountantApi:
    """API client for the Accountant domain of the Xena API."""
    def __init__(self, base_url: str, session: Optional[requests.Session] = None) -> None:
        self.base_url = base_url.rstrip('/')
        self.session = session or requests.Session()

    def api_accountant_admin__get_client_list_get__api__fiscal_fiscal_id__accountant_admin__client(self, fiscal_id: str, query_string: str = None, accountant_department_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/AccountantAdmin/Client"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantAdmin/Client"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if accountant_department_id is not None:
            params['accountantDepartmentId'] = accountant_department_id
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

    def api_accountant_admin__delete_client_delete__api__fiscal_fiscal_id__accountant_admin__client_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/AccountantAdmin/Client/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantAdmin/Client/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_accountant_admin__get_accountant_list_get__api__fiscal_fiscal_id__accountant_admin__accountant(self, fiscal_id: str, query_string: str = None, accountant_department_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/AccountantAdmin/Accountant"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantAdmin/Accountant"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if accountant_department_id is not None:
            params['accountantDepartmentId'] = accountant_department_id
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

    def api_accountant_admin__get_accountant_by_client_list_get__api__fiscal_fiscal_id__accountant_admin__client_client_id__accountant(self, client_id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/AccountantAdmin/Client/{clientId}/Accountant"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantAdmin/Client/{client_id}/Accountant"
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

    def api_accountant_admin__get_client_by_accountant_list_get__api__fiscal_fiscal_id__accountant_admin__accountant_accountant_id__client(self, accountant_id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/AccountantAdmin/Accountant/{accountantId}/Client"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantAdmin/Accountant/{accountant_id}/Client"
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

    def api_accountant_admin__post_accountant_post__api__fiscal_fiscal_id__accountant_admin__client_client_id__accountant_accountant_id(self, client_id: int, accountant_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/AccountantAdmin/Client/{clientId}/Accountant/{accountantId}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantAdmin/Client/{client_id}/Accountant/{accountant_id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_accountant_admin__delete_accountant_delete__api__fiscal_fiscal_id__accountant_admin__client_client_id__accountant_accountant_id(self, client_id: int, accountant_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/AccountantAdmin/Client/{clientId}/Accountant/{accountantId}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantAdmin/Client/{client_id}/Accountant/{accountant_id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_accountant_admin__get_accountant_security_role_list_get__api__fiscal_fiscal_id__accountant_admin__accountant_security_roles(self, fiscal_id: str, list_option_show_deactivated: bool = None, list_option_page: int = None, list_option_page_size: int = None, list_option_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/AccountantAdmin/AccountantSecurityRoles"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantAdmin/AccountantSecurityRoles"
        params: Dict[str, Any] = {}
        if list_option_show_deactivated is not None:
            params['listOption.showDeactivated'] = list_option_show_deactivated
        if list_option_page is not None:
            params['listOption.page'] = list_option_page
        if list_option_page_size is not None:
            params['listOption.pageSize'] = list_option_page_size
        if list_option_force_no_paging is not None:
            params['listOption.forceNoPaging'] = list_option_force_no_paging
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_accountant_admin__get_get__api__fiscal_fiscal_id__accountant_admin_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/AccountantAdmin/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantAdmin/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_accountant_admin__post_partner_from_client_post__api__fiscal_fiscal_id__accountant_admin__client_client_id__partner(self, client_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/AccountantAdmin/Client/{clientId}/Partner"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantAdmin/Client/{client_id}/Partner"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_accountant_admin__get_accountant_temp_access_get__api__fiscal_fiscal_id__accountant_admin__accountant_resource_temp_access(self, fiscal_id: str, accountant_id: int = None, client_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/AccountantAdmin/AccountantResourceTempAccess"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantAdmin/AccountantResourceTempAccess"
        params: Dict[str, Any] = {}
        if accountant_id is not None:
            params['accountantId'] = accountant_id
        if client_id is not None:
            params['clientId'] = client_id
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

    def api_accountant_client__get_get__api__fiscal_fiscal_id__accountant_client_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/AccountantClient/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantClient/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_accountant_client__put_put__api__fiscal_fiscal_id__accountant_client_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/AccountantClient/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantClient/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_accountant_department__get_get__api__fiscal_fiscal_id__accountant_department(self, fiscal_id: str, query_string: str = None, include_default: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/AccountantDepartment"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantDepartment"
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

    def api_accountant_department__post_post__api__fiscal_fiscal_id__accountant_department(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/AccountantDepartment"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantDepartment"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_accountant_department__get_get__api__fiscal_fiscal_id__accountant_department_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/AccountantDepartment/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantDepartment/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_accountant_department__put_put__api__fiscal_fiscal_id__accountant_department_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/AccountantDepartment/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantDepartment/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_accountant_department__delete_delete__api__fiscal_fiscal_id__accountant_department_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/AccountantDepartment/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantDepartment/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_accountant_resource__get_get__api__fiscal_fiscal_id__accountant_resource_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/AccountantResource/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantResource/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_accountant_resource__put_put__api__fiscal_fiscal_id__accountant_resource_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/AccountantResource/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AccountantResource/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text
