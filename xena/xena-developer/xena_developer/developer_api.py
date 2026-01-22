from typing import Any, Dict, Optional
import requests

class DeveloperApi:
    """API client for the Developer domain of the Xena API."""
    def __init__(self, base_url: str, session: Optional[requests.Session] = None) -> None:
        self.base_url = base_url.rstrip('/')
        self.session = session or requests.Session()

    def api_web_hook__get_get__api__fiscal_fiscal_id__web_hook(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/WebHook"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/WebHook"
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

    def api_web_hook__post_post__api__fiscal_fiscal_id__web_hook(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/WebHook"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/WebHook"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_web_hook__get_get__api__fiscal_fiscal_id__web_hook_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/WebHook/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/WebHook/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_web_hook__put_put__api__fiscal_fiscal_id__web_hook_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/WebHook/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/WebHook/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_web_hook__delete_delete__api__fiscal_fiscal_id__web_hook_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/WebHook/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/WebHook/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_web_hook__get_webhook_failures_get__api__fiscal_fiscal_id__web_hook_id__web_hook_failures(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/WebHook/{id}/WebHookFailures"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/WebHook/{id}/WebHookFailures"
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

    def api_xena_app__get_get__api__fiscal_fiscal_id__xena_app(self, fiscal_id: str, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaApp"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp"
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

    def api_xena_app__post_post__api__fiscal_fiscal_id__xena_app(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/XenaApp"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app__get_get__api__fiscal_fiscal_id__xena_app_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaApp/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app__put_put__api__fiscal_fiscal_id__xena_app_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/XenaApp/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app__delete_xena_app_delete__api__fiscal_fiscal_id__xena_app_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/XenaApp/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app__get_subscriber_fiscal_list_get__api__fiscal_fiscal_id__xena_app_xena_app_id__subscriber_fiscal(self, xena_app_id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaApp/{xenaAppId}/SubscriberFiscal"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp/{xena_app_id}/SubscriberFiscal"
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

    def api_xena_app__put_request_approval_put__api__fiscal_fiscal_id__xena_app_id__request_approval(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/XenaApp/{id}/RequestApproval"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp/{id}/RequestApproval"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app__delete_request_approval_delete__api__fiscal_fiscal_id__xena_app_id__request_approval(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/XenaApp/{id}/RequestApproval"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp/{id}/RequestApproval"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app__put_request_unapproval_put__api__fiscal_fiscal_id__xena_app_id__request_unapproval(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/XenaApp/{id}/RequestUnapproval"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp/{id}/RequestUnapproval"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app__delete_take_down_delete__api__fiscal_fiscal_id__xena_app_id__take_down(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/XenaApp/{id}/TakeDown"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp/{id}/TakeDown"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app__get_app_category_get__api__fiscal_fiscal_id__xena_app__category(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaApp/Category"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp/Category"
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

    def api_xena_app__get_app_visibility_get__api__fiscal_fiscal_id__xena_app__visibility(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaApp/Visibility"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp/Visibility"
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

    def api_xena_app_bundle__get_list_get__api__fiscal_fiscal_id__xena_app_bundle(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaAppBundle"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppBundle"
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

    def api_xena_app_bundle__post_post__api__fiscal_fiscal_id__xena_app_bundle(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/XenaAppBundle"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppBundle"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_bundle__get_get__api__fiscal_fiscal_id__xena_app_bundle_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaAppBundle/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppBundle/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_bundle__put_put__api__fiscal_fiscal_id__xena_app_bundle_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/XenaAppBundle/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppBundle/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_bundle__delete_xena_app_bundle_delete__api__fiscal_fiscal_id__xena_app_bundle_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/XenaAppBundle/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppBundle/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_bundle__put_request_approval_put__api__fiscal_fiscal_id__xena_app_bundle_id__request_approval(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/XenaAppBundle/{id}/RequestApproval"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppBundle/{id}/RequestApproval"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_bundle__delete_request_approval_delete__api__fiscal_fiscal_id__xena_app_bundle_id__request_approval(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/XenaAppBundle/{id}/RequestApproval"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppBundle/{id}/RequestApproval"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_bundle__put_request_unapproval_put__api__fiscal_fiscal_id__xena_app_bundle_id__request_unapproval(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/XenaAppBundle/{id}/RequestUnapproval"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppBundle/{id}/RequestUnapproval"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_bundle__delete_take_down_delete__api__fiscal_fiscal_id__xena_app_bundle_id__take_down(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/XenaAppBundle/{id}/TakeDown"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppBundle/{id}/TakeDown"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_bundle_item__get_by_xena_app_list_get__api__fiscal_fiscal_id__xena_app_bundle_id__bundle_item(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaAppBundle/{id}/BundleItem"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppBundle/{id}/BundleItem"
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

    def api_xena_app_bundle_item__get_get__api__fiscal_fiscal_id__xena_app_bundle_item_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaAppBundleItem/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppBundleItem/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_bundle_item__put_put__api__fiscal_fiscal_id__xena_app_bundle_item_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/XenaAppBundleItem/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppBundleItem/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_bundle_item__delete_xena_app_bundle_item_delete__api__fiscal_fiscal_id__xena_app_bundle_item_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/XenaAppBundleItem/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppBundleItem/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_bundle_item__post_post__api__fiscal_fiscal_id__xena_app_bundle_item(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/XenaAppBundleItem"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppBundleItem"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_bundle_price__get_by_xena_app_bundle_list_get__api__fiscal_fiscal_id__xena_app_bundle_id__price(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaAppBundle/{id}/Price"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppBundle/{id}/Price"
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

    def api_xena_app_bundle_price__get_get__api__fiscal_fiscal_id__xena_app_bundle_price_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaAppBundlePrice/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppBundlePrice/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_bundle_price__put_put__api__fiscal_fiscal_id__xena_app_bundle_price_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/XenaAppBundlePrice/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppBundlePrice/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_bundle_price__delete_xena_app_bundle_price_delete__api__fiscal_fiscal_id__xena_app_bundle_price_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/XenaAppBundlePrice/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppBundlePrice/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_bundle_price__post_post__api__fiscal_fiscal_id__xena_app_bundle_price(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/XenaAppBundlePrice"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppBundlePrice"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_plugin__get_get__api__fiscal_fiscal_id__xena_app_id__plugin(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaApp/{id}/Plugin"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp/{id}/Plugin"
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

    def api_xena_app_plugin__get_get__api__fiscal_fiscal_id__xena_app_plugin_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaAppPlugin/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppPlugin/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_plugin__put_put__api__fiscal_fiscal_id__xena_app_plugin_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/XenaAppPlugin/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppPlugin/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_plugin__delete_delete__api__fiscal_fiscal_id__xena_app_plugin_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/XenaAppPlugin/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppPlugin/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_plugin__post_post__api__fiscal_fiscal_id__xena_app_plugin(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/XenaAppPlugin"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppPlugin"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_plugin__get_plugin_type_get__api__fiscal_fiscal_id__xena_app_plugin__plugin_type(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaAppPlugin/PluginType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppPlugin/PluginType"
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

    def api_xena_app_plugin__get_parent_plugins_get__api__fiscal_fiscal_id__xena_app_id__parent_plugins(self, id: int, fiscal_id: str, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaApp/{id}/ParentPlugins"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp/{id}/ParentPlugins"
        params: Dict[str, Any] = {}
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

    def api_xena_app_price__get_by_xena_app_list_get__api__fiscal_fiscal_id__xena_app_id__price(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaApp/{id}/Price"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaApp/{id}/Price"
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

    def api_xena_app_price__get_get__api__fiscal_fiscal_id__xena_app_price_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaAppPrice/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppPrice/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_price__put_put__api__fiscal_fiscal_id__xena_app_price_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/XenaAppPrice/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppPrice/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_price__delete_xena_app_price_delete__api__fiscal_fiscal_id__xena_app_price_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/XenaAppPrice/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppPrice/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_app_price__post_post__api__fiscal_fiscal_id__xena_app_price(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/XenaAppPrice"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaAppPrice"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text
