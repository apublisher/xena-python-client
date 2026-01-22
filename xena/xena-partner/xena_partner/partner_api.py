from typing import Any, Dict, Optional
import requests

class PartnerApi:
    """API client for the Partner domain of the Xena API."""
    def __init__(self, base_url: str, session: Optional[requests.Session] = None) -> None:
        self.base_url = base_url.rstrip('/')
        self.session = session or requests.Session()

    def api_partner__get_by_price_group_get__api__fiscal_fiscal_id__price_group_id__partner(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PriceGroup/{id}/Partner"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PriceGroup/{id}/Partner"
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

    def api_partner__get_get__api__fiscal_fiscal_id__partner(self, fiscal_id: str, query_string: str = None, excluded_id: int = None, include_default: bool = None, partner_context_type: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if excluded_id is not None:
            params['excludedId'] = excluded_id
        if include_default is not None:
            params['includeDefault'] = include_default
        if partner_context_type is not None:
            params['partnerContextType'] = partner_context_type
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

    def api_partner__post_post__api__fiscal_fiscal_id__partner(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Partner"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__get_get__api__fiscal_fiscal_id__partner_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__put_put__api__fiscal_fiscal_id__partner_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Partner/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__delete_delete__api__fiscal_fiscal_id__partner_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Partner/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__get_multiple_by_ids_get__api__fiscal_fiscal_id__partner__multiple(self, partner_ids: list, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/Multiple"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/Multiple"
        params: Dict[str, Any] = {}
        if partner_ids is not None:
            params['partnerIds'] = partner_ids
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

    def api_partner__get_by_account_number_get__api__fiscal_fiscal_id__partner__by_account_number_account_number(self, account_number: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/ByAccountNumber/{accountNumber}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/ByAccountNumber/{account_number}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__get_multiple_by_numbers_get__api__fiscal_fiscal_id__partner__by_multiple_account_numbers(self, account_numbers: list, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/ByMultipleAccountNumbers"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/ByMultipleAccountNumbers"
        params: Dict[str, Any] = {}
        if account_numbers is not None:
            params['accountNumbers'] = account_numbers
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

    def api_partner__get_search_get__api__fiscal_fiscal_id__partner__search(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, filter_partner_type: str = None, filter_name: str = None, filter_org_number: str = None, filter_g_ln_number: str = None, filter_attention: str = None, filter_street: str = None, filter_place_name: str = None, filter_zip: str = None, filter_city: str = None, filter_country_name: str = None, filter_phone_number: str = None, filter_email: str = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/Search"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/Search"
        params: Dict[str, Any] = {}
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        if filter_partner_type is not None:
            params['filter.partnerType'] = filter_partner_type
        if filter_name is not None:
            params['filter.name'] = filter_name
        if filter_org_number is not None:
            params['filter.orgNumber'] = filter_org_number
        if filter_g_ln_number is not None:
            params['filter.gLNNumber'] = filter_g_ln_number
        if filter_attention is not None:
            params['filter.attention'] = filter_attention
        if filter_street is not None:
            params['filter.street'] = filter_street
        if filter_place_name is not None:
            params['filter.placeName'] = filter_place_name
        if filter_zip is not None:
            params['filter.zip'] = filter_zip
        if filter_city is not None:
            params['filter.city'] = filter_city
        if filter_country_name is not None:
            params['filter.countryName'] = filter_country_name
        if filter_phone_number is not None:
            params['filter.phoneNumber'] = filter_phone_number
        if filter_email is not None:
            params['filter.email'] = filter_email
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__post_from_search_post__api__fiscal_fiscal_id__partner__search(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Partner/Search"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/Search"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__post_from_v_card_post__api__fiscal_fiscal_id_v_card_id__partner(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/VCard/{id}/Partner"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VCard/{id}/Partner"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__post_from_fiscal_setup_post__api__fiscal_fiscal_id__fiscal_setup_id__partner(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalSetup/{id}/Partner"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/{id}/Partner"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__get_partner_list_without_searcher_get__api__fiscal_fiscal_id__partner_id__search(self, id: int, fiscal_id: str, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/Search"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/Search"
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

    def api_partner__get_xena_fiscal_subscription_list_get__api__fiscal_fiscal_id__partner_id__xena_fiscal_subscription(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/XenaFiscalSubscription"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/XenaFiscalSubscription"
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

    def api_partner__get_history_entry_get__api__fiscal_fiscal_id__partner_id__partner_history_entry(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/PartnerHistoryEntry"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/PartnerHistoryEntry"
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

    def api_partner__get_partner_invite_history_entry_get__api__fiscal_fiscal_id__partner_id__partner_invite_history_entry(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/PartnerInviteHistoryEntry"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/PartnerInviteHistoryEntry"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__delete_partner_invite_history_entry_delete__api__fiscal_fiscal_id__partner_id__partner_invite_history_entry(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Partner/{id}/PartnerInviteHistoryEntry"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/PartnerInviteHistoryEntry"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__put_from_order_put__api__fiscal_fiscal_id__partner_id__from_order_order_id(self, id: int, order_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Partner/{id}/FromOrder/{orderId}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/FromOrder/{order_id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__delete_merge_into_delete__api__fiscal_fiscal_id__partner_partner_to_deactivate_id__merge_into_partner_to_keep_id(self, partner_to_keep_id: int, partner_to_deactivate_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Partner/{partnerToDeactivateId}/MergeInto/{partnerToKeepId}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{partner_to_deactivate_id}/MergeInto/{partner_to_keep_id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__get_history_get__api__fiscal_fiscal_id__partner__history(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/History"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/History"
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

    def api_partner__put_disconnect_put__api__fiscal_fiscal_id__partner_id__disconnect(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Partner/{id}/Disconnect"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/Disconnect"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__put_invite_put__api__fiscal_fiscal_id__partner_id__invite(self, id: int, invite_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Partner/{id}/Invite"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/Invite"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=invite_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__put_link_v_card_put__api__fiscal_fiscal_id__partner_id__link_v_card_v_card_id(self, id: int, v_card_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Partner/{id}/LinkVCard/{vCardId}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/LinkVCard/{v_card_id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__put_resend_partner_invitation_put__api__fiscal_fiscal_id__partner_id__resend_partner_invitation_partner_invitation_id(self, id: int, partner_invitation_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Partner/{id}/ResendPartnerInvitation/{partnerInvitationId}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/ResendPartnerInvitation/{partner_invitation_id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__get_balance_get__api__fiscal_fiscal_id__partner_id__balance(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/Balance"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/Balance"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__put_invoice_email_put__api__fiscal_fiscal_id__partner_id__invoice_email(self, id: int, email_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Partner/{id}/InvoiceEmail"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/InvoiceEmail"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=email_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__get_tag_get__api__fiscal_fiscal_id__partner__tag(self, fiscal_id: str, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/Tag"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/Tag"
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

    def api_partner__get_context_types_get__api__fiscal_fiscal_id__partner__context_types(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/ContextTypes"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/ContextTypes"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__get_schedule_methods_get__api__fiscal_fiscal_id__partner__schedule_methods(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/ScheduleMethods"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/ScheduleMethods"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__get_partner_type_get__api__fiscal_fiscal_id__partner__partner_type(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/PartnerType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/PartnerType"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__get_theme_get__api__fiscal_fiscal_id__partner__partner_context_type(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/PartnerContextType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/PartnerContextType"
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

    def api_partner__get_partner_post_get__api__fiscal_fiscal_id__partner__partner_post_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/PartnerPost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/PartnerPost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__put_partner_post_put__api__fiscal_fiscal_id__partner__partner_post_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Partner/PartnerPost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/PartnerPost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner__get_connection_data_for_partner_get__api__fiscal_fiscal_id__partner__partner_id__connection_data(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/Partner/{id}/ConnectionData"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/Partner/{id}/ConnectionData"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_context__get_get__api__fiscal_fiscal_id__partner_context_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PartnerContext/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerContext/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_context__put_put__api__fiscal_fiscal_id__partner_context_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/PartnerContext/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerContext/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_context__delete_delete__api__fiscal_fiscal_id__partner_context_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/PartnerContext/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerContext/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_context__post_post__api__fiscal_fiscal_id__partner_context(self, create_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/PartnerContext"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerContext"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=create_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_context__get_by_partner_get__api__fiscal_fiscal_id__partner_id__context(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/Context"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/Context"
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

    def api_partner_context__get_by_partner_and_context_type_get__api__fiscal_fiscal_id__partner_id__context_context_type(self, id: int, context_type: str, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/Context/{contextType}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/Context/{context_type}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_context_template__get_get__api__fiscal_fiscal_id__partner_context_template(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PartnerContextTemplate"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerContextTemplate"
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

    def api_partner_context_template__post_post__api__fiscal_fiscal_id__partner_context_template(self, partner_context_template: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/PartnerContextTemplate"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerContextTemplate"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=partner_context_template, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_context_template__get_get__api__fiscal_fiscal_id__partner_context_template_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PartnerContextTemplate/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerContextTemplate/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_context_template__put_put__api__fiscal_fiscal_id__partner_context_template_id(self, partner_context_template: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/PartnerContextTemplate/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerContextTemplate/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=partner_context_template, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_context_template__delete_delete__api__fiscal_fiscal_id__partner_context_template_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/PartnerContextTemplate/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerContextTemplate/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_delivery_address__get_by_partner_list_get__api__fiscal_fiscal_id__partner_id__delivery_address(self, id: int, fiscal_id: str, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/DeliveryAddress"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/DeliveryAddress"
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

    def api_partner_delivery_address__get_get__api__fiscal_fiscal_id__partner_delivery_address_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PartnerDeliveryAddress/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerDeliveryAddress/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_delivery_address__put_put__api__fiscal_fiscal_id__partner_delivery_address_id(self, address: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/PartnerDeliveryAddress/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerDeliveryAddress/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=address, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_delivery_address__delete_delete__api__fiscal_fiscal_id__partner_delivery_address_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/PartnerDeliveryAddress/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerDeliveryAddress/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_delivery_address__get_multiple_get__api__fiscal_fiscal_id__partner_delivery_address__multiple(self, ids: list, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PartnerDeliveryAddress/Multiple"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerDeliveryAddress/Multiple"
        params: Dict[str, Any] = {}
        if ids is not None:
            params['ids'] = ids
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

    def api_partner_delivery_address__post_post__api__fiscal_fiscal_id__partner_delivery_address(self, address: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/PartnerDeliveryAddress"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerDeliveryAddress"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=address, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_email_contact__get_by_partner_list_get__api__fiscal_fiscal_id__partner_id__email_contact(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/EmailContact"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/EmailContact"
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

    def api_partner_email_contact__get_get__api__fiscal_fiscal_id__partner_email_contact_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PartnerEmailContact/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerEmailContact/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_email_contact__put_put__api__fiscal_fiscal_id__partner_email_contact_id(self, article: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/PartnerEmailContact/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerEmailContact/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=article, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_email_contact__delete_delete__api__fiscal_fiscal_id__partner_email_contact_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/PartnerEmailContact/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerEmailContact/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_email_contact__post_post__api__fiscal_fiscal_id__partner_email_contact(self, article: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/PartnerEmailContact"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerEmailContact"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=article, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_gln_number__get_by_partner_list_get__api__fiscal_fiscal_id__partner_id_gln_number(self, id: int, fiscal_id: str, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/GLNNumber"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/GLNNumber"
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

    def api_partner_gln_number__get_get__api__fiscal_fiscal_id__partner_gln_number_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PartnerGLNNumber/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerGLNNumber/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_gln_number__put_put__api__fiscal_fiscal_id__partner_gln_number_id(self, article: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/PartnerGLNNumber/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerGLNNumber/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=article, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_gln_number__delete_delete__api__fiscal_fiscal_id__partner_gln_number_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/PartnerGLNNumber/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerGLNNumber/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_gln_number__post_post__api__fiscal_fiscal_id__partner_gln_number(self, article: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/PartnerGLNNumber"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerGLNNumber"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=article, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_location__get_get__api__fiscal_fiscal_id__partner_location(self, fiscal_id: str, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PartnerLocation"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerLocation"
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

    def api_partner_location__post_post__api__fiscal_fiscal_id__partner_location(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/PartnerLocation"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerLocation"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_location__get_get__api__fiscal_fiscal_id__partner_location_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PartnerLocation/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerLocation/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_location__put_put__api__fiscal_fiscal_id__partner_location_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/PartnerLocation/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerLocation/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_location__delete_delete__api__fiscal_fiscal_id__partner_location_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/PartnerLocation/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerLocation/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_location__get_by_partner_get__api__fiscal_fiscal_id__partner_id__location(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/Location"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/Location"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_note_history_entry__get_get__api__fiscal_fiscal_id__partner_note_history_entry_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PartnerNoteHistoryEntry/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerNoteHistoryEntry/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_note_history_entry__put_put__api__fiscal_fiscal_id__partner_note_history_entry_id(self, partner_note_history_entry: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/PartnerNoteHistoryEntry/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerNoteHistoryEntry/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=partner_note_history_entry, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_note_history_entry__delete_delete__api__fiscal_fiscal_id__partner_note_history_entry_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/PartnerNoteHistoryEntry/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerNoteHistoryEntry/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_note_history_entry__post_post__api__fiscal_fiscal_id__partner_note_history_entry(self, partner_note_history_entry: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/PartnerNoteHistoryEntry"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerNoteHistoryEntry"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=partner_note_history_entry, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_telephone_number__get_by_partner_list_get__api__fiscal_fiscal_id__partner_id__telephone_number(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/TelephoneNumber"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/TelephoneNumber"
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

    def api_partner_telephone_number__get_get__api__fiscal_fiscal_id__partner_telephone_number_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PartnerTelephoneNumber/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerTelephoneNumber/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_telephone_number__put_put__api__fiscal_fiscal_id__partner_telephone_number_id(self, article: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/PartnerTelephoneNumber/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerTelephoneNumber/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=article, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_telephone_number__delete_delete__api__fiscal_fiscal_id__partner_telephone_number_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/PartnerTelephoneNumber/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerTelephoneNumber/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_telephone_number__post_post__api__fiscal_fiscal_id__partner_telephone_number(self, article: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/PartnerTelephoneNumber"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerTelephoneNumber"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=article, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_reminder_step__get_get__api__fiscal_fiscal_id__reminder_step(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ReminderStep"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReminderStep"
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

    def api_reminder_step__post_post__api__fiscal_fiscal_id__reminder_step(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ReminderStep"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReminderStep"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_reminder_step__get_get__api__fiscal_fiscal_id__reminder_step_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ReminderStep/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReminderStep/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_reminder_step__put_put__api__fiscal_fiscal_id__reminder_step_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ReminderStep/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReminderStep/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_reminder_step__delete_delete__api__fiscal_fiscal_id__reminder_step_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ReminderStep/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReminderStep/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_reminder_step__put_execute_put__api__fiscal_fiscal_id__reminder_step__execute(self, execute_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ReminderStep/Execute"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ReminderStep/Execute"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=execute_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def partner_list__get_csv_get__api__fiscal_fiscal_id__report__partner_list_csv(self, fiscal_id: str, query_string: str = None, excluded_id: int = None, include_default: bool = None, partner_context_type: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Report/PartnerList/CSV"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Report/PartnerList/CSV"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if excluded_id is not None:
            params['excludedId'] = excluded_id
        if include_default is not None:
            params['includeDefault'] = include_default
        if partner_context_type is not None:
            params['partnerContextType'] = partner_context_type
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
