from typing import Any, Dict, Optional
import requests

class AppstoreApi:
    """API client for the AppStore domain of the Xena API."""
    def __init__(self, base_url: str, session: Optional[requests.Session] = None) -> None:
        self.base_url = base_url.rstrip('/')
        self.session = session or requests.Session()

    def api_xena_app_subscriber__get_by_xena_app_list_get__api__fiscal_fiscal_id__xena_app_id__subscriber(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaApp/{id}/Subscriber"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp/{id}/Subscriber"
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

    def api_xena_app_subscriber__get_users_for_xena_app_list_get__api__fiscal_fiscal_id__xena_app_id__users(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaApp/{id}/Users"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp/{id}/Users"
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

    def api_xena_app_subscriber__get_list_get__api__fiscal_fiscal_id__xena_app_subscriber(self, membership_id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaAppSubscriber"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppSubscriber"
        params: Dict[str, Any] = {}
        if membership_id is not None:
            params['membershipId'] = membership_id
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

    def api_xena_app_subscriber__put_subscribe_put__api__fiscal_fiscal_id__xena_app_id__subscribe(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/XenaApp/{id}/Subscribe"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp/{id}/Subscribe"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_subscriber__delete_unsubscribe_delete__api__fiscal_fiscal_id__xena_app_id__unsubscribe(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/XenaApp/{id}/Unsubscribe"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp/{id}/Unsubscribe"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_subscriber__put_remove_app_expire_date_put__api__fiscal_fiscal_id__xena_app_id__remove_app_expire_date(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/XenaApp/{id}/RemoveAppExpireDate"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp/{id}/RemoveAppExpireDate"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text
