from typing import Any, Dict, Optional
import requests

class CoreApi:
    """API client for the Core domain of the Xena API."""
    def __init__(self, base_url: str, session: Optional[requests.Session] = None) -> None:
        self.base_url = base_url.rstrip('/')
        self.session = session or requests.Session()

    def actuator__get_health_get__api_actuator_health(self, **kwargs) -> Any:
        """Auto-generated method for GET /Api/actuator/health"""
        url = f"{self.base_url}/Api/actuator/health"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_audit_trail__get_list_get__api__fiscal_fiscal_id__audit_trail_type_id(self, id: int, type: str, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/AuditTrail/{type}/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AuditTrail/{type}/{id}"
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

    def api_available_provider_report_layout__get_list_get__api__fiscal_fiscal_id__available_provider_report_layout(self, report_module: str, fiscal_id: str, query_string: str = None, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/AvailableProviderReportLayout"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AvailableProviderReportLayout"
        params: Dict[str, Any] = {}
        if report_module is not None:
            params['reportModule'] = report_module
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

    def api_country__get_get__api__country(self, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Country"""
        url = f"{self.base_url}/Api/Country"
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

    def api_culture__get_profile_cultures_get__api__culture__profiles(self, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Culture/Profiles"""
        url = f"{self.base_url}/Api/Culture/Profiles"
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

    def api_culture__get_get__api__culture(self, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Culture"""
        url = f"{self.base_url}/Api/Culture"
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

    def api_default_report_layout__get_list_get__api__fiscal_fiscal_id__default_report_layout(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/DefaultReportLayout"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DefaultReportLayout"
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

    def api_default_report_layout__post_post__api__fiscal_fiscal_id__default_report_layout(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/DefaultReportLayout"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DefaultReportLayout"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_default_report_layout__put_put__api__fiscal_fiscal_id__default_report_layout_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/DefaultReportLayout/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DefaultReportLayout/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_default_report_layout__delete_delete__api__fiscal_fiscal_id__default_report_layout_id(self, report_group: str, fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/DefaultReportLayout/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DefaultReportLayout/{id}"
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

    def api_email__get_get__api__fiscal_fiscal_id__email(self, fiscal_id: str, partner_id: int = None, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Email"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Email"
        params: Dict[str, Any] = {}
        if partner_id is not None:
            params['partnerId'] = partner_id
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

    def api_email__post_send_mail_post__api__fiscal_fiscal_id__email__send(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Email/Send"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Email/Send"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_entity_template__get_get__api__fiscal_fiscal_id__entity_template(self, entity_type: str, fiscal_id: str, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/EntityTemplate"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/EntityTemplate"
        params: Dict[str, Any] = {}
        if entity_type is not None:
            params['entityType'] = entity_type
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

    def api_entity_template__post_post__api__fiscal_fiscal_id__entity_template(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/EntityTemplate"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/EntityTemplate"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_entity_template__get_get__api__fiscal_fiscal_id__entity_template_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/EntityTemplate/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/EntityTemplate/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_entity_template__put_put__api__fiscal_fiscal_id__entity_template_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/EntityTemplate/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/EntityTemplate/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_entity_template__delete_delete__api__fiscal_fiscal_id__entity_template_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/EntityTemplate/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/EntityTemplate/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_entity_template__post_apply_post__api__fiscal_fiscal_id__entity_template_id__apply(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/EntityTemplate/{id}/Apply"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/EntityTemplate/{id}/Apply"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_entity_template__put_save_put__api__fiscal_fiscal_id__entity_template_id__save(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/EntityTemplate/{id}/Save"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/EntityTemplate/{id}/Save"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_external__get_danish_company_by_cvr_list_get__api__external_data__danish_company_by_cvr(self, query_string: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/ExternalData/DanishCompanyByCVR"""
        url = f"{self.base_url}/Api/ExternalData/DanishCompanyByCVR"
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

    def api_fiscal_notification__get_get__api__fiscal_fiscal_id__notification(self, notification_types: str, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Notification"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Notification"
        params: Dict[str, Any] = {}
        if notification_types is not None:
            params['notificationTypes'] = notification_types
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

    def api_fiscal_notification__put_execute_put__api__fiscal_fiscal_id__notification_id__execute(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Notification/{id}/Execute"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Notification/{id}/Execute"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_notification__get_notification_count_get__api__fiscal_fiscal_id__notification__fiscal_notification_count(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Notification/FiscalNotificationCount"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Notification/FiscalNotificationCount"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_home__get_fiscal_setup_get__api__home__fiscal_setup(self, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Home/FiscalSetup"""
        url = f"{self.base_url}/Api/Home/FiscalSetup"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_home__post_fiscal_setup_post__api__home__fiscal_setup(self, dto: Dict[str, Any], **kwargs) -> Any:
        """Auto-generated method for POST /Api/Home/FiscalSetup"""
        url = f"{self.base_url}/Api/Home/FiscalSetup"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_home__delete_subscription_ticket_delete__api__home__subscription_ticket_id(self, id: int, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Home/SubscriptionTicket/{id}"""
        url = f"{self.base_url}/Api/Home/SubscriptionTicket/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_home__post_accept_partner_invitation_post__api__home__partner_invitation__accept(self, invited_partner_dto: Dict[str, Any], **kwargs) -> Any:
        """Auto-generated method for POST /Api/Home/PartnerInvitation/Accept"""
        url = f"{self.base_url}/Api/Home/PartnerInvitation/Accept"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=invited_partner_dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_home__get_accountant_list_get__api__home__accountant(self, querystring: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Home/Accountant"""
        url = f"{self.base_url}/Api/Home/Accountant"
        params: Dict[str, Any] = {}
        if querystring is not None:
            params['querystring'] = querystring
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

    def api_home__get_provider_list_get__api__home__provider(self, querystring: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Home/Provider"""
        url = f"{self.base_url}/Api/Home/Provider"
        params: Dict[str, Any] = {}
        if querystring is not None:
            params['querystring'] = querystring
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

    def api_home__get_accountant_department_list_get__api__home__accountant_accountant_id__department(self, accountant_id: int, querystring: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Home/Accountant/{accountantId}/Department"""
        url = f"{self.base_url}/Api/Home/Accountant/{accountant_id}/Department"
        params: Dict[str, Any] = {}
        if querystring is not None:
            params['querystring'] = querystring
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

    def api_home__post_epay_data_for_online_user_payment_post__api__home__epay_data_for_online_user_payment(self, payment_data: Dict[str, Any], **kwargs) -> Any:
        """Auto-generated method for POST /Api/Home/EpayDataForOnlineUserPayment"""
        url = f"{self.base_url}/Api/Home/EpayDataForOnlineUserPayment"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=payment_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_home__get_default_currency_list_get__api__home__get_default_currency_list(self, querystring: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Home/GetDefaultCurrencyList"""
        url = f"{self.base_url}/Api/Home/GetDefaultCurrencyList"
        params: Dict[str, Any] = {}
        if querystring is not None:
            params['querystring'] = querystring
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

    def api_home__get_sasha_url_get__api__home__get_sasha_url(self, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Home/GetSashaUrl"""
        url = f"{self.base_url}/Api/Home/GetSashaUrl"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_provider_release_notes_link__get_get__api__fiscal_fiscal_id__provider_release_notes_link_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ProviderReleaseNotesLink/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderReleaseNotesLink/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_provider_release_notes_link__put_put__api__fiscal_fiscal_id__provider_release_notes_link_id(self, link: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ProviderReleaseNotesLink/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderReleaseNotesLink/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=link, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_provider_release_notes_link__delete_delete__api__fiscal_fiscal_id__provider_release_notes_link_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ProviderReleaseNotesLink/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderReleaseNotesLink/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_provider_release_notes_link__get_get__api__fiscal_fiscal_id__provider_release_notes_link(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ProviderReleaseNotesLink"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderReleaseNotesLink"
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

    def api_provider_release_notes_link__post_post__api__fiscal_fiscal_id__provider_release_notes_link(self, link: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ProviderReleaseNotesLink"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ProviderReleaseNotesLink"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=link, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_public__get_active_terms_get__api__public__terms(self, terms_type: str = None, provider_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Public/Terms"""
        url = f"{self.base_url}/Api/Public/Terms"
        params: Dict[str, Any] = {}
        if terms_type is not None:
            params['termsType'] = terms_type
        if provider_id is not None:
            params['providerId'] = provider_id
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

    def api_public__get_v_card_by_fiscal_get__api__public__fiscal_id_v_card(self, id: int, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Public/Fiscal/{id}/VCard"""
        url = f"{self.base_url}/Api/Public/Fiscal/{id}/VCard"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_public__get_v_card_by_user_get__api__public__user_id_v_card(self, id: int, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Public/User/{id}/VCard"""
        url = f"{self.base_url}/Api/Public/User/{id}/VCard"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_public__get_resource_v_card_by_fiscal_get__api__public__fiscal_id__resource_v_card(self, id: int, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Public/Fiscal/{id}/Resource/VCard"""
        url = f"{self.base_url}/Api/Public/Fiscal/{id}/Resource/VCard"
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

    def api_public__get_get__api__public__app(self, query_string: str = None, include_xena: bool = None, include_bundles: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Public/App"""
        url = f"{self.base_url}/Api/Public/App"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if include_xena is not None:
            params['includeXena'] = include_xena
        if include_bundles is not None:
            params['includeBundles'] = include_bundles
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

    def api_public__get_get__api__public__app_id(self, id: int, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Public/App/{id}"""
        url = f"{self.base_url}/Api/Public/App/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_public__get_xena_app_for_discount_code_list_get__api__public__xena_app_for_discount_code_list(self, id: int, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Public/XenaAppForDiscountCodeList"""
        url = f"{self.base_url}/Api/Public/XenaAppForDiscountCodeList"
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

    def api_public__get_app_category_get__api__public__app__category(self, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Public/App/Category"""
        url = f"{self.base_url}/Api/Public/App/Category"
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

    def api_smtp_setting__get_get__api__fiscal_fiscal_id__smtp_setting(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/SmtpSetting"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/SmtpSetting"
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

    def api_smtp_setting__post_post__api__fiscal_fiscal_id__smtp_setting(self, smtp_setting: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/SmtpSetting"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/SmtpSetting"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=smtp_setting, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_smtp_setting__get_get__api__fiscal_fiscal_id__smtp_setting_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/SmtpSetting/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/SmtpSetting/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_smtp_setting__put_put__api__fiscal_fiscal_id__smtp_setting_id(self, smtp_setting: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/SmtpSetting/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/SmtpSetting/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=smtp_setting, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_smtp_setting__delete_delete__api__fiscal_fiscal_id__smtp_setting_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/SmtpSetting/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/SmtpSetting/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_smtp_setting__post_send_test_mail_post__api__fiscal_fiscal_id__smtp_setting__send_test_mail(self, setting_dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/SmtpSetting/SendTestMail"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/SmtpSetting/SendTestMail"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=setting_dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_terms_culture_handling__get_active_term_get__api__xena_terms_culture_id(self, id: int, **kwargs) -> Any:
        """Auto-generated method for GET /Api/XenaTermsCulture/{id}"""
        url = f"{self.base_url}/Api/XenaTermsCulture/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_terms_culture_handling__put_accept_put__api__xena_terms_culture_id__accept(self, id: int, data: Dict[str, Any], **kwargs) -> Any:
        """Auto-generated method for PUT /Api/XenaTermsCulture/{id}/Accept"""
        url = f"{self.base_url}/Api/XenaTermsCulture/{id}/Accept"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_terms_handling__get_unhandled_terms_get__api__xena_terms__unhandled(self, fiscal_setup_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/XenaTerms/Unhandled"""
        url = f"{self.base_url}/Api/XenaTerms/Unhandled"
        params: Dict[str, Any] = {}
        if fiscal_setup_id is not None:
            params['fiscalSetupId'] = fiscal_setup_id
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

    def api_terms_handling__get_get__api__xena_terms(self, fiscal_setup_id: int = None, terms_type: str = None, provider_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/XenaTerms"""
        url = f"{self.base_url}/Api/XenaTerms"
        params: Dict[str, Any] = {}
        if fiscal_setup_id is not None:
            params['fiscalSetupId'] = fiscal_setup_id
        if terms_type is not None:
            params['termsType'] = terms_type
        if provider_id is not None:
            params['providerId'] = provider_id
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

    def api_terms_handling__put_reject_put__api__xena_terms_id__reject(self, id: int, data: Dict[str, Any], **kwargs) -> Any:
        """Auto-generated method for PUT /Api/XenaTerms/{id}/Reject"""
        url = f"{self.base_url}/Api/XenaTerms/{id}/Reject"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_user__get_xena_user_partner_post_list_for_subscription_get__api__user__subscription_id__xena_user_partner_post(self, id: int, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/User/Subscription/{id}/XenaUserPartnerPost"""
        url = f"{self.base_url}/Api/User/Subscription/{id}/XenaUserPartnerPost"
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

    def api_user__get_shared_document_get__api__user__fiscal_setup_id__shared_document(self, id: int, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/User/FiscalSetup/{id}/SharedDocument"""
        url = f"{self.base_url}/Api/User/FiscalSetup/{id}/SharedDocument"
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

    def api_user__delete_delete__api__user_id(self, id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/User/{id}"""
        url = f"{self.base_url}/Api/User/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_user__get_xena_user_partner_post_for_fiscal_setup_get__api__user__fiscal_setup_id__xena_user_partner_post(self, id: int, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/User/FiscalSetup/{id}/XenaUserPartnerPost"""
        url = f"{self.base_url}/Api/User/FiscalSetup/{id}/XenaUserPartnerPost"
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

    def api_user__get_xena_user_subscription_for_fiscal_setup_get__api__user__fiscal_setup_id__xena_user_subscription(self, id: int, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/User/FiscalSetup/{id}/XenaUserSubscription"""
        url = f"{self.base_url}/Api/User/FiscalSetup/{id}/XenaUserSubscription"
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

    def api_user__get_xena_user_subscription_line_get__api__user__xena_user_subscription_id__xena_user_subscription_line(self, id: int, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/User/XenaUserSubscription/{id}/XenaUserSubscriptionLine"""
        url = f"{self.base_url}/Api/User/XenaUserSubscription/{id}/XenaUserSubscriptionLine"
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

    def api_user__get_v_card_for_user_get__api__user_v_card_for_user(self, **kwargs) -> Any:
        """Auto-generated method for GET /Api/User/VCardForUser"""
        url = f"{self.base_url}/Api/User/VCardForUser"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_user__get_v_card_get__api__user_v_card_id(self, id: int, **kwargs) -> Any:
        """Auto-generated method for GET /Api/User/VCard/{id}"""
        url = f"{self.base_url}/Api/User/VCard/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_user__put_v_card_put__api__user_v_card_id(self, dto: Dict[str, Any], id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/User/VCard/{id}"""
        url = f"{self.base_url}/Api/User/VCard/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_user__delete_v_card_delete__api__user_v_card_id(self, id: int, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/User/VCard/{id}"""
        url = f"{self.base_url}/Api/User/VCard/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_user__post_v_card_post__api__user_v_card(self, **kwargs) -> Any:
        """Auto-generated method for POST /Api/User/VCard"""
        url = f"{self.base_url}/Api/User/VCard"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_user__get_xena_user_partner_get__api__user__xena_user_partner(self, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/User/XenaUserPartner"""
        url = f"{self.base_url}/Api/User/XenaUserPartner"
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

    def api_user__available_emails_get__api__user__authenticated_emails(self, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/User/AuthenticatedEmails"""
        url = f"{self.base_url}/Api/User/AuthenticatedEmails"
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

    def api_user__get_xena_user_subscription_ticket_get__api__user__xena_user_subscription_ticket(self, id: int, **kwargs) -> Any:
        """Auto-generated method for GET /Api/User/XenaUserSubscriptionTicket"""
        url = f"{self.base_url}/Api/User/XenaUserSubscriptionTicket"
        params: Dict[str, Any] = {}
        if id is not None:
            params['id'] = id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_user__get_subscription_ticket_get__api__user__subscription_id__subscription_ticket(self, id: int, **kwargs) -> Any:
        """Auto-generated method for GET /Api/User/Subscription/{id}/SubscriptionTicket"""
        url = f"{self.base_url}/Api/User/Subscription/{id}/SubscriptionTicket"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_user__get_fiscal_setup_get__api__user__fiscal_setup(self, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/User/FiscalSetup"""
        url = f"{self.base_url}/Api/User/FiscalSetup"
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

    def api_user__get_user_notification_count_get__api__user__user_notification_count(self, **kwargs) -> Any:
        """Auto-generated method for GET /Api/User/UserNotificationCount"""
        url = f"{self.base_url}/Api/User/UserNotificationCount"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_user__get_xena_user_membership_list_get__api__user__xena_user_membership(self, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/User/XenaUserMembership"""
        url = f"{self.base_url}/Api/User/XenaUserMembership"
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

    def api_user__get_id_s_membership_list_get__api__user__ids_user_membership(self, **kwargs) -> Any:
        """Auto-generated method for GET /Api/User/IdsUserMembership"""
        url = f"{self.base_url}/Api/User/IdsUserMembership"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_user__get_history_get__api__user__history(self, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/User/History"""
        url = f"{self.base_url}/Api/User/History"
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

    def api_user__get_connection_data_for_fiscal_get__api__user__fiscal_id__connection_data(self, id: int, **kwargs) -> Any:
        """Auto-generated method for GET /Api/User/Fiscal/{id}/ConnectionData"""
        url = f"{self.base_url}/Api/User/Fiscal/{id}/ConnectionData"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_user__post_epay_ticket_for_existing_user_subscription_post__api__user__epay_ticket_for_existing_user_subscription(self, data: Dict[str, Any], **kwargs) -> Any:
        """Auto-generated method for POST /Api/User/EpayTicketForExistingUserSubscription"""
        url = f"{self.base_url}/Api/User/EpayTicketForExistingUserSubscription"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_user_notification__get_get__api__notification(self, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Notification"""
        url = f"{self.base_url}/Api/Notification"
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

    def api_user_notification__put_execute_put__api__notification_id__execute(self, id: int, data: Dict[str, Any], **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Notification/{id}/Execute"""
        url = f"{self.base_url}/Api/Notification/{id}/Execute"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_user_settings__get_get__api__api__user_settings(self, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Api/UserSettings"""
        url = f"{self.base_url}/Api/Api/UserSettings"
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

    def api_user_settings__get_bool_get__api__api__user_settings__bool_setting(self, setting: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Api/UserSettings/Bool/{setting}"""
        url = f"{self.base_url}/Api/Api/UserSettings/Bool/{setting}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_user_settings__put_bool_put__api__api__user_settings__bool_setting(self, setting: str, data: Dict[str, Any], **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Api/UserSettings/Bool/{setting}"""
        url = f"{self.base_url}/Api/Api/UserSettings/Bool/{setting}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_value_template__get_get__api__fiscal_fiscal_id__value_template(self, key: str, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ValueTemplate"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ValueTemplate"
        params: Dict[str, Any] = {}
        if key is not None:
            params['key'] = key
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

    def api_value_template__post_post__api__fiscal_fiscal_id__value_template(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ValueTemplate"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ValueTemplate"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_value_template__get_get__api__fiscal_fiscal_id__value_template_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ValueTemplate/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ValueTemplate/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_value_template__put_put__api__fiscal_fiscal_id__value_template_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ValueTemplate/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ValueTemplate/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_value_template__delete_delete__api__fiscal_fiscal_id__value_template_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ValueTemplate/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ValueTemplate/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_v_card__get_by_partner_get__api__fiscal_fiscal_id_v_card__by_partner_partner_id(self, partner_id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VCard/ByPartner/{partnerId}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VCard/ByPartner/{partner_id}"
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

    def api_v_card__get_by_type_get__api__fiscal_fiscal_id_v_card__by_type(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, filter_partner_type: str = None, filter_name: str = None, filter_org_number: str = None, filter_g_ln_number: str = None, filter_attention: str = None, filter_street: str = None, filter_place_name: str = None, filter_zip: str = None, filter_city: str = None, filter_country_name: str = None, filter_phone_number: str = None, filter_email: str = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VCard/ByType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VCard/ByType"
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

    def api_v_card__get_user_search_get__api__fiscal_fiscal_id_v_card__user_search(self, fiscal_id: str, query_string: str = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VCard/UserSearch"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VCard/UserSearch"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_fiscal_app__get_installed_get__api__fiscal_fiscal_id__xena_fiscal_app__installed(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaFiscalApp/Installed"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaFiscalApp/Installed"
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

    def api_xena_fiscal_app__get_installed_fiscal_apps_get__api__fiscal_fiscal_id__xena_fiscal_app__installed_fiscal_apps(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaFiscalApp/InstalledFiscalApps"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaFiscalApp/InstalledFiscalApps"
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

    def api_xena_fiscal_app__delete_unsubscribe_delete__api__fiscal_fiscal_id__xena_fiscal_app_app_id__unsubscribe(self, app_id: int, delete_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/XenaFiscalApp/{appId}/Unsubscribe"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaFiscalApp/{app_id}/Unsubscribe"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, json=delete_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_price__get_xena_user_price_get__api__fiscal_fiscal_id__xena_user_price_article(self, article: str, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaUserPrice/{article}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaUserPrice/{article}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_price__get_user_price_info_get__api__fiscal_fiscal_id__xena_user_price__get_user_price_info(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/XenaUserPrice/GetUserPriceInfo"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/XenaUserPrice/GetUserPriceInfo"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_xena_price__get_subscription_consequence_for_deletion_get__api__fiscal_fiscal_id__membership_membership_id__deletion_consequence(self, fiscal_id: int, membership_id: int, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Membership/{membershipId}/DeletionConsequence"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Membership/{membership_id}/DeletionConsequence"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_zip__get_by_zip_get__api__fiscal_fiscal_id__zip(self, zip: str, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Zip"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Zip"
        params: Dict[str, Any] = {}
        if zip is not None:
            params['zip'] = zip
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_zip__get_by_zip_get__api__zip(self, zip: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Zip"""
        url = f"{self.base_url}/Api/Zip"
        params: Dict[str, Any] = {}
        if zip is not None:
            params['zip'] = zip
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text
