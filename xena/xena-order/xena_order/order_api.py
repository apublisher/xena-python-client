from typing import Any, Dict, Optional
import requests

class OrderApi:
    """API client for the Order domain of the Xena API."""
    def __init__(self, base_url: str, session: Optional[requests.Session] = None) -> None:
        self.base_url = base_url.rstrip('/')
        self.session = session or requests.Session()

    def api_order__get_validate_order_for_electronic_invoicing_get__api__fiscal_fiscal_id__order_id__can_be_sent_electronically(self, id: int, fiscal_id: str, electronic_invoice_type: str = None, tasks_ids: list = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{id}/CanBeSentElectronically"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/CanBeSentElectronically"
        params: Dict[str, Any] = {}
        if electronic_invoice_type is not None:
            params['electronicInvoiceType'] = electronic_invoice_type
        if tasks_ids is not None:
            params['tasksIds'] = tasks_ids
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_get__api__fiscal_fiscal_id__order(self, fiscal_id: str, filter_query_string: str = None, filter_context_type: str = None, filter_deliver_filter: str = None, filter_partner_id: int = None, filter_order_status_id: int = None, filter_responsible_id: int = None, filter_limit_to_responsible: bool = None, filter_limit_to_department: bool = None, filter_limit_to_bearer: bool = None, filter_limit_to_purpose: bool = None, filter_department_id: int = None, filter_bearer_id: int = None, filter_purpose_id: int = None, filter_date_from: int = None, filter_date_to: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order"
        params: Dict[str, Any] = {}
        if filter_query_string is not None:
            params['filter.queryString'] = filter_query_string
        if filter_context_type is not None:
            params['filter.contextType'] = filter_context_type
        if filter_deliver_filter is not None:
            params['filter.deliverFilter'] = filter_deliver_filter
        if filter_partner_id is not None:
            params['filter.partnerId'] = filter_partner_id
        if filter_order_status_id is not None:
            params['filter.orderStatusId'] = filter_order_status_id
        if filter_responsible_id is not None:
            params['filter.responsibleId'] = filter_responsible_id
        if filter_limit_to_responsible is not None:
            params['filter.limitToResponsible'] = filter_limit_to_responsible
        if filter_limit_to_department is not None:
            params['filter.limitToDepartment'] = filter_limit_to_department
        if filter_limit_to_bearer is not None:
            params['filter.limitToBearer'] = filter_limit_to_bearer
        if filter_limit_to_purpose is not None:
            params['filter.limitToPurpose'] = filter_limit_to_purpose
        if filter_department_id is not None:
            params['filter.departmentId'] = filter_department_id
        if filter_bearer_id is not None:
            params['filter.bearerId'] = filter_bearer_id
        if filter_purpose_id is not None:
            params['filter.purposeId'] = filter_purpose_id
        if filter_date_from is not None:
            params['filter.dateFrom'] = filter_date_from
        if filter_date_to is not None:
            params['filter.dateTo'] = filter_date_to
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

    def api_order__post_post__api__fiscal_fiscal_id__order(self, create_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Order"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=create_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_get__api__fiscal_fiscal_id__order_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__put_put__api__fiscal_fiscal_id__order_id(self, order_dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Order/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=order_dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__delete_delete__api__fiscal_fiscal_id__order_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Order/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_multiple_by_ids_get__api__fiscal_fiscal_id__order__multiple(self, order_ids: list, search_term: str, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/Multiple"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/Multiple"
        params: Dict[str, Any] = {}
        if order_ids is not None:
            params['orderIds'] = order_ids
        if search_term is not None:
            params['searchTerm'] = search_term
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

    def api_order__post_multiple_post__api__fiscal_fiscal_id__order__multiple(self, orders_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Order/Multiple"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/Multiple"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=orders_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_undelivered_orders_get__api__fiscal_fiscal_id__order__undelivered(self, fiscal_id: str, filter_query_string: str = None, filter_context_type: str = None, filter_deliver_filter: str = None, filter_partner_id: int = None, filter_order_status_id: int = None, filter_responsible_id: int = None, filter_limit_to_responsible: bool = None, filter_limit_to_department: bool = None, filter_limit_to_bearer: bool = None, filter_limit_to_purpose: bool = None, filter_department_id: int = None, filter_bearer_id: int = None, filter_purpose_id: int = None, filter_date_from: int = None, filter_date_to: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/Undelivered"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/Undelivered"
        params: Dict[str, Any] = {}
        if filter_query_string is not None:
            params['filter.queryString'] = filter_query_string
        if filter_context_type is not None:
            params['filter.contextType'] = filter_context_type
        if filter_deliver_filter is not None:
            params['filter.deliverFilter'] = filter_deliver_filter
        if filter_partner_id is not None:
            params['filter.partnerId'] = filter_partner_id
        if filter_order_status_id is not None:
            params['filter.orderStatusId'] = filter_order_status_id
        if filter_responsible_id is not None:
            params['filter.responsibleId'] = filter_responsible_id
        if filter_limit_to_responsible is not None:
            params['filter.limitToResponsible'] = filter_limit_to_responsible
        if filter_limit_to_department is not None:
            params['filter.limitToDepartment'] = filter_limit_to_department
        if filter_limit_to_bearer is not None:
            params['filter.limitToBearer'] = filter_limit_to_bearer
        if filter_limit_to_purpose is not None:
            params['filter.limitToPurpose'] = filter_limit_to_purpose
        if filter_department_id is not None:
            params['filter.departmentId'] = filter_department_id
        if filter_bearer_id is not None:
            params['filter.bearerId'] = filter_bearer_id
        if filter_purpose_id is not None:
            params['filter.purposeId'] = filter_purpose_id
        if filter_date_from is not None:
            params['filter.dateFrom'] = filter_date_from
        if filter_date_to is not None:
            params['filter.dateTo'] = filter_date_to
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

    def api_order__get_by_number_get__api__fiscal_fiscal_id__order__by_number(self, order_number: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/ByNumber"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/ByNumber"
        params: Dict[str, Any] = {}
        if order_number is not None:
            params['orderNumber'] = order_number
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__create_purchase_order_from_sales_order_post__api__fiscal_fiscal_id__order_id__create_purchase_order_from_sales_order(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Order/{id}/CreatePurchaseOrderFromSalesOrder"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/CreatePurchaseOrderFromSalesOrder"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_order_offer_get__api__fiscal_fiscal_id__order__offer(self, fiscal_id: str, query_string: str = None, responsible_id: int = None, limit_to_responsible: bool = None, context_type: str = None, order_status_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/Offer"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/Offer"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if responsible_id is not None:
            params['responsibleId'] = responsible_id
        if limit_to_responsible is not None:
            params['limitToResponsible'] = limit_to_responsible
        if context_type is not None:
            params['contextType'] = context_type
        if order_status_id is not None:
            params['orderStatusId'] = order_status_id
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

    def api_order__put_pay_put__api__fiscal_fiscal_id__order__pay(self, pay_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Order/Pay"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/Pay"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=pay_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__put_cancel_multiple_order_invoice_put__api__fiscal_fiscal_id__order__invoice__cancel(self, cancel_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Order/Invoice/Cancel"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/Invoice/Cancel"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=cancel_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__put_send_electronic_invoices_put__api__fiscal_fiscal_id__order__invoice__send_electronic_invoice(self, invoice_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Order/Invoice/SendElectronicInvoice"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/Invoice/SendElectronicInvoice"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=invoice_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__put_send_mobile_pay_invoices_put__api__fiscal_fiscal_id__order__invoice__send_mobile_pay_invoice(self, invoice_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Order/Invoice/SendMobilePayInvoice"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/Invoice/SendMobilePayInvoice"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=invoice_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_invoice_get__api__fiscal_fiscal_id__order__invoice(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, filter_query_string: str = None, filter_context_type: str = None, filter_deliver_filter: str = None, filter_is_settled: bool = None, filter_partner_id: int = None, filter_order_status_id: int = None, filter_responsible_id: int = None, filter_limit_to_responsible: bool = None, filter_date_from: int = None, filter_date_to: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/Invoice"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/Invoice"
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
        if filter_context_type is not None:
            params['filter.contextType'] = filter_context_type
        if filter_deliver_filter is not None:
            params['filter.deliverFilter'] = filter_deliver_filter
        if filter_is_settled is not None:
            params['filter.isSettled'] = filter_is_settled
        if filter_partner_id is not None:
            params['filter.partnerId'] = filter_partner_id
        if filter_order_status_id is not None:
            params['filter.orderStatusId'] = filter_order_status_id
        if filter_responsible_id is not None:
            params['filter.responsibleId'] = filter_responsible_id
        if filter_limit_to_responsible is not None:
            params['filter.limitToResponsible'] = filter_limit_to_responsible
        if filter_date_from is not None:
            params['filter.dateFrom'] = filter_date_from
        if filter_date_to is not None:
            params['filter.dateTo'] = filter_date_to
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_invoice_by_partner_get__api__fiscal_fiscal_id__partner_id__invoice(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/Invoice"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/Invoice"
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

    def api_order__get_history_get__api__fiscal_fiscal_id__order__history(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/History"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/History"
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

    def api_order__get_by_article_get__api__fiscal_fiscal_id__article_id__order(self, id: int, fiscal_id: str, context_type: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/{id}/Order"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/Order"
        params: Dict[str, Any] = {}
        if context_type is not None:
            params['contextType'] = context_type
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

    def api_order__get_by_project_get__api__fiscal_fiscal_id__project_id__order(self, id: int, fiscal_id: str, show_invoiced: bool = None, newest_first: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Project/{id}/Order"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/{id}/Order"
        params: Dict[str, Any] = {}
        if show_invoiced is not None:
            params['showInvoiced'] = show_invoiced
        if newest_first is not None:
            params['newestFirst'] = newest_first
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

    def api_order__get_open_orders_by_article_get__api__fiscal_fiscal_id__article_id__open_order(self, id: int, context_type: str, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/{id}/OpenOrder"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/OpenOrder"
        params: Dict[str, Any] = {}
        if context_type is not None:
            params['contextType'] = context_type
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

    def api_order__get_confirmed_by_article_get__api__fiscal_fiscal_id__article_id__confirmed_order(self, id: int, context_type: str, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/{id}/ConfirmedOrder"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/ConfirmedOrder"
        params: Dict[str, Any] = {}
        if context_type is not None:
            params['contextType'] = context_type
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

    def api_order__get_order_article_reservations_by_article_get__api__fiscal_fiscal_id__article_id__order_article_reservations(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/{id}/OrderArticleReservations"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/OrderArticleReservations"
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

    def api_order__get_offer_by_partner_get__api__fiscal_fiscal_id__partner_id__offer(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/Offer"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/Offer"
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

    def api_order__get_by_partner_get__api__fiscal_fiscal_id__partner_id__order(self, id: int, fiscal_id: str, context_type: str = None, query_string: str = None, date_from: int = None, date_to: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/Order"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/Order"
        params: Dict[str, Any] = {}
        if context_type is not None:
            params['contextType'] = context_type
        if query_string is not None:
            params['queryString'] = query_string
        if date_from is not None:
            params['dateFrom'] = date_from
        if date_to is not None:
            params['dateTo'] = date_to
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

    def api_order__get_not_invoiced_get__api__fiscal_fiscal_id__order__not_invoiced(self, fiscal_id: str, filter_query_string: str = None, filter_context_type: str = None, filter_deliver_filter: str = None, filter_partner_id: int = None, filter_order_status_id: int = None, filter_responsible_id: int = None, filter_limit_to_responsible: bool = None, filter_limit_to_department: bool = None, filter_limit_to_bearer: bool = None, filter_limit_to_purpose: bool = None, filter_department_id: int = None, filter_bearer_id: int = None, filter_purpose_id: int = None, filter_date_from: int = None, filter_date_to: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/NotInvoiced"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/NotInvoiced"
        params: Dict[str, Any] = {}
        if filter_query_string is not None:
            params['filter.queryString'] = filter_query_string
        if filter_context_type is not None:
            params['filter.contextType'] = filter_context_type
        if filter_deliver_filter is not None:
            params['filter.deliverFilter'] = filter_deliver_filter
        if filter_partner_id is not None:
            params['filter.partnerId'] = filter_partner_id
        if filter_order_status_id is not None:
            params['filter.orderStatusId'] = filter_order_status_id
        if filter_responsible_id is not None:
            params['filter.responsibleId'] = filter_responsible_id
        if filter_limit_to_responsible is not None:
            params['filter.limitToResponsible'] = filter_limit_to_responsible
        if filter_limit_to_department is not None:
            params['filter.limitToDepartment'] = filter_limit_to_department
        if filter_limit_to_bearer is not None:
            params['filter.limitToBearer'] = filter_limit_to_bearer
        if filter_limit_to_purpose is not None:
            params['filter.limitToPurpose'] = filter_limit_to_purpose
        if filter_department_id is not None:
            params['filter.departmentId'] = filter_department_id
        if filter_bearer_id is not None:
            params['filter.bearerId'] = filter_bearer_id
        if filter_purpose_id is not None:
            params['filter.purposeId'] = filter_purpose_id
        if filter_date_from is not None:
            params['filter.dateFrom'] = filter_date_from
        if filter_date_to is not None:
            params['filter.dateTo'] = filter_date_to
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

    def api_order__post_copy_post__api__fiscal_fiscal_id__order_id__copy(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Order/{id}/Copy"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/Copy"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__put_split_order_lines_put__api__fiscal_fiscal_id__order_id__split_lines(self, id: int, split_order_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Order/{id}/SplitLines"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/SplitLines"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=split_order_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__post_from_order_lines_post__api__fiscal_fiscal_id__order_partner_id__from_lines(self, partner_id: int, split_order_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Order/{partnerId}/FromLines"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{partner_id}/FromLines"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=split_order_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__put_deliver_put__api__fiscal_fiscal_id__order_id__deliver(self, id: int, deliver_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Order/{id}/Deliver"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/Deliver"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=deliver_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_delivery_data_get__api__fiscal_fiscal_id__order_id__delivery_data(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{id}/DeliveryData"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/DeliveryData"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_supplier_order_data_by_order_get__api__fiscal_fiscal_id__order_id__supplier_order_data_by_order(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{id}/SupplierOrderDataByOrder"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/SupplierOrderDataByOrder"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_pay_on_account_data_get__api__fiscal_fiscal_id__order_id__pay_on_account_data(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{id}/PayOnAccountData"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/PayOnAccountData"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_order_budget_data_get__api__fiscal_fiscal_id__order_id__get_order_budget_data(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{id}/GetOrderBudgetData"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/GetOrderBudgetData"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_order_task_statistics_data_get__api__fiscal_fiscal_id__order_id__get_order_task_statistics_data(self, id: int, fiscal_id: str, show_deactivated: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{id}/GetOrderTaskStatisticsData"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/GetOrderTaskStatisticsData"
        params: Dict[str, Any] = {}
        if show_deactivated is not None:
            params['showDeactivated'] = show_deactivated
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__put_offer_put__api__fiscal_fiscal_id__order_id__offer(self, id: int, create_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Order/{id}/Offer"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/Offer"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=create_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__put_confirmation_put__api__fiscal_fiscal_id__order_id__confirmation(self, id: int, create_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Order/{id}/Confirmation"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/Confirmation"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=create_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__put_pay_on_account_put__api__fiscal_fiscal_id__order_id__pay_on_account(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Order/{id}/PayOnAccount"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/PayOnAccount"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__put_bookkeep_put__api__fiscal_fiscal_id__order_id__bookkeep(self, id: int, bookkeep_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Order/{id}/Bookkeep"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/Bookkeep"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=bookkeep_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_partner_has_open_orders_get__api__fiscal_fiscal_id__partner_id__has_open_order(self, id: int, fiscal_id: str, context_type: str = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/HasOpenOrder"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/HasOpenOrder"
        params: Dict[str, Any] = {}
        if context_type is not None:
            params['contextType'] = context_type
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_open_by_partner_get__api__fiscal_fiscal_id__partner_id__open_order(self, id: int, fiscal_id: str, context_type: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/OpenOrder"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/OpenOrder"
        params: Dict[str, Any] = {}
        if context_type is not None:
            params['contextType'] = context_type
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

    def api_order__get_order_journal_get__api__fiscal_fiscal_id__order_id__journal(self, id: int, fiscal_id: str, only_invoices: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{id}/Journal"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/Journal"
        params: Dict[str, Any] = {}
        if only_invoices is not None:
            params['onlyInvoices'] = only_invoices
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

    def api_order__put_from_context_put__api__fiscal_fiscal_id__partner_context_id__update_order(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/PartnerContext/{id}/UpdateOrder"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerContext/{id}/UpdateOrder"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__put_from_partner_put__api__fiscal_fiscal_id__partner_id__update_order(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Partner/{id}/UpdateOrder"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/UpdateOrder"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_context_type_get__api__fiscal_fiscal_id__order__context_type(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/ContextType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/ContextType"
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

    def api_order__get_recipient_address_types_get__api__fiscal_fiscal_id__order__recipient_address_types(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/RecipientAddressTypes"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/RecipientAddressTypes"
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

    def api_order__get_partner_post_get__api__fiscal_fiscal_id__order_id__partner_post(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{id}/PartnerPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/PartnerPost"
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

    def api_order__get_due_type_get__api__fiscal_fiscal_id__order__due_type(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/DueType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/DueType"
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

    def api_order__get_summary_get__api__fiscal_fiscal_id__order_id__summary(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{id}/Summary"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/Summary"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_invoice_summary_get__api__fiscal_fiscal_id__order_id__invoice_summary(self, id: int, fiscal_id: str, tasks_ids: list = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{id}/InvoiceSummary"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/InvoiceSummary"
        params: Dict[str, Any] = {}
        if tasks_ids is not None:
            params['tasksIds'] = tasks_ids
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_default_electronic_invoice_data_get__api__fiscal_fiscal_id__order__default_electronic_invoice_data(self, journal_ids: list, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/DefaultElectronicInvoiceData"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/DefaultElectronicInvoiceData"
        params: Dict[str, Any] = {}
        if journal_ids is not None:
            params['journalIds'] = journal_ids
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_default_mobile_pay_invoice_data_get__api__fiscal_fiscal_id__order__default_mobile_pay_invoice_data(self, journal_ids: list, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/DefaultMobilePayInvoiceData"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/DefaultMobilePayInvoiceData"
        params: Dict[str, Any] = {}
        if journal_ids is not None:
            params['journalIds'] = journal_ids
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_electronic_invoice_journal_events_get__api__fiscal_fiscal_id__order__electronic_invoice_journal_id__events(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/ElectronicInvoiceJournal/{id}/Events"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/ElectronicInvoiceJournal/{id}/Events"
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

    def api_order__get_orders_for_status_get__api__fiscal_fiscal_id__order__orders_for_status_id(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, filter_query_string: str = None, filter_responsible_id: int = None, filter_limit_to_responsible: bool = None, filter_date_from: int = None, filter_date_to: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/OrdersForStatus/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/OrdersForStatus/{id}"
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
        if filter_date_from is not None:
            params['filter.dateFrom'] = filter_date_from
        if filter_date_to is not None:
            params['filter.dateTo'] = filter_date_to
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__put_update_with_barcodes_put__api__fiscal_fiscal_id__order_id__barcodes(self, id: int, scanned_barcode_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Order/{id}/Barcodes"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/Barcodes"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=scanned_barcode_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__put_process_mass_put__api__fiscal_fiscal_id__order__process__bulk(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Order/Process/Bulk"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/Process/Bulk"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_undelivered_orders_by_article_get__api__fiscal_fiscal_id__order__undelivered__article_id(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/Undelivered/Article/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/Undelivered/Article/{id}"
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

    def api_order__get_has_order_journal_articles_with_inventory_management_get__api__fiscal_fiscal_id__order__order_journal_entry_id__has_articles_with_inventory_management(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/OrderJournalEntry/{id}/HasArticlesWithInventoryManagement"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/OrderJournalEntry/{id}/HasArticlesWithInventoryManagement"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order__get_closed_order_statistics_get__api__fiscal_fiscal_id__order__statistics__closed(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/Statistics/Closed"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/Statistics/Closed"
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

    def api_order_budget_post__get_get__api__fiscal_fiscal_id__order_budget_post(self, fiscal_id: str, order_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderBudgetPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderBudgetPost"
        params: Dict[str, Any] = {}
        if order_id is not None:
            params['orderId'] = order_id
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

    def api_order_budget_post__post_post__api__fiscal_fiscal_id__order_budget_post(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderBudgetPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderBudgetPost"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_budget_post__get_get__api__fiscal_fiscal_id__order_budget_post_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderBudgetPost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderBudgetPost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_budget_post__put_put__api__fiscal_fiscal_id__order_budget_post_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/OrderBudgetPost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderBudgetPost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_budget_post__delete_delete__api__fiscal_fiscal_id__order_budget_post_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/OrderBudgetPost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderBudgetPost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_budget_post__post_create_default_post__api__fiscal_fiscal_id__order_order_id__order_budget_post__standard(self, order_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Order/{orderId}/OrderBudgetPost/Standard"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{order_id}/OrderBudgetPost/Standard"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_delivery_transaction__get_get__api__fiscal_fiscal_id__order_id__delivery_transaction(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{id}/DeliveryTransaction"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/DeliveryTransaction"
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

    def api_order_delivery_transaction__delete_multiple_deliveries_delete__api__fiscal_fiscal_id__order_delivery_transaction__delete_multiple_deliveries(self, delete_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/OrderDeliveryTransaction/DeleteMultipleDeliveries"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderDeliveryTransaction/DeleteMultipleDeliveries"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, json=delete_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_invoice_transaction__get_get__api__fiscal_fiscal_id__order_invoice_transaction_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderInvoiceTransaction/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderInvoiceTransaction/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_journal_entry__get_get__api__fiscal_fiscal_id__order_journal_entry_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderJournalEntry/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderJournalEntry/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_line__get_linked_lines_get__api__fiscal_fiscal_id__order_line_id__linked_lines(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderLine/{id}/LinkedLines"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderLine/{id}/LinkedLines"
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

    def api_order_line__get_by_order_task_get__api__fiscal_fiscal_id__order_task_id__order_line(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTask/{id}/OrderLine"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTask/{id}/OrderLine"
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

    def api_order_line__get_get__api__fiscal_fiscal_id__order_line_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderLine/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderLine/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_line__put_put__api__fiscal_fiscal_id__order_line_id(self, line_dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/OrderLine/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderLine/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=line_dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_line__delete_delete__api__fiscal_fiscal_id__order_line_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/OrderLine/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderLine/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_line__get_get__api__fiscal_fiscal_id__order_line__old_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderLine/Old/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderLine/Old/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_line__put_obsolete_put__api__fiscal_fiscal_id__order_line__old_id(self, line_dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/OrderLine/Old/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderLine/Old/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=line_dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_line__delete_delete__api__fiscal_fiscal_id__order_line__old_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/OrderLine/Old/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderLine/Old/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_line__put_bulk_put__api__fiscal_fiscal_id__order_line__bulk(self, dtos: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/OrderLine/Bulk"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderLine/Bulk"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dtos, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_line__post_bulk_create_order_line_post__api__fiscal_fiscal_id__order_line__bulk(self, line_dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderLine/Bulk"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderLine/Bulk"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=line_dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_line__post_post__api__fiscal_fiscal_id__order_line(self, line_dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderLine"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderLine"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=line_dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_line__post_obsolete_post__api__fiscal_fiscal_id__order_line__old(self, line_dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderLine/Old"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderLine/Old"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=line_dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_line_bundle_item__get_list_get__api__fiscal_fiscal_id__order_line_id__bundle_item(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderLine/{id}/BundleItem"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderLine/{id}/BundleItem"
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

    def api_order_line_bundle_item__get_get__api__fiscal_fiscal_id__order_line_bundle_item_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderLineBundleItem/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderLineBundleItem/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_line_bundle_item__put_put__api__fiscal_fiscal_id__order_line_bundle_item_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/OrderLineBundleItem/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderLineBundleItem/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_line_reception_draft__get_get__api__fiscal_fiscal_id__order_reception_draft_id__order_line_reception_draft(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderReceptionDraft/{id}/OrderLineReceptionDraft"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderReceptionDraft/{id}/OrderLineReceptionDraft"
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

    def api_order_line_reception_draft__get_get__api__fiscal_fiscal_id__order_line_reception_draft_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderLineReceptionDraft/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderLineReceptionDraft/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_line_reception_draft__put_put__api__fiscal_fiscal_id__order_line_reception_draft_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/OrderLineReceptionDraft/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderLineReceptionDraft/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_line_reception_draft__delete_delete__api__fiscal_fiscal_id__order_line_reception_draft_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/OrderLineReceptionDraft/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderLineReceptionDraft/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_line_reception_draft__post_post__api__fiscal_fiscal_id__order_line_reception_draft(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderLineReceptionDraft"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderLineReceptionDraft"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_reception_draft__get_get__api__fiscal_fiscal_id__order_reception_draft(self, responsible_id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderReceptionDraft"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderReceptionDraft"
        params: Dict[str, Any] = {}
        if responsible_id is not None:
            params['responsibleId'] = responsible_id
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

    def api_order_reception_draft__post_post__api__fiscal_fiscal_id__order_reception_draft(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderReceptionDraft"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderReceptionDraft"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_reception_draft__get_get__api__fiscal_fiscal_id__order_reception_draft_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderReceptionDraft/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderReceptionDraft/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_reception_draft__put_put__api__fiscal_fiscal_id__order_reception_draft_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/OrderReceptionDraft/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderReceptionDraft/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_reception_draft__delete_delete__api__fiscal_fiscal_id__order_reception_draft_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/OrderReceptionDraft/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderReceptionDraft/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_status__get_get__api__fiscal_fiscal_id__order_status(self, context_type: str, fiscal_id: str, query_string: str = None, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderStatus"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderStatus"
        params: Dict[str, Any] = {}
        if context_type is not None:
            params['contextType'] = context_type
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

    def api_order_status__post_post__api__fiscal_fiscal_id__order_status(self, order_status: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderStatus"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderStatus"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=order_status, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_status__get_get__api__fiscal_fiscal_id__order_status_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderStatus/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderStatus/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_status__put_put__api__fiscal_fiscal_id__order_status_id(self, order_status: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/OrderStatus/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderStatus/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=order_status, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_status__delete_delete__api__fiscal_fiscal_id__order_status_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/OrderStatus/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderStatus/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_status__post_create_standard_sales_post__api__fiscal_fiscal_id__order_status__standard_sales(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderStatus/StandardSales"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderStatus/StandardSales"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_status__post_create_standard_purchasing_post__api__fiscal_fiscal_id__order_status__standard_purchasing(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderStatus/StandardPurchasing"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderStatus/StandardPurchasing"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task__get_get__api__fiscal_fiscal_id__order_task(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, filter_query_string: str = None, filter_order_task_status_ids: list = None, filter_is_invoiced: bool = None, filter_is_delivered: bool = None, filter_project_closed: bool = None, filter_for_bookkeeping: bool = None, filter_include_default: bool = None, filter_order_id: int = None, filter_context_type: str = None, filter_created_after: str = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTask"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTask"
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
        if filter_order_task_status_ids is not None:
            params['filter.orderTaskStatusIds'] = filter_order_task_status_ids
        if filter_is_invoiced is not None:
            params['filter.isInvoiced'] = filter_is_invoiced
        if filter_is_delivered is not None:
            params['filter.isDelivered'] = filter_is_delivered
        if filter_project_closed is not None:
            params['filter.projectClosed'] = filter_project_closed
        if filter_for_bookkeeping is not None:
            params['filter.forBookkeeping'] = filter_for_bookkeeping
        if filter_include_default is not None:
            params['filter.includeDefault'] = filter_include_default
        if filter_order_id is not None:
            params['filter.orderId'] = filter_order_id
        if filter_context_type is not None:
            params['filter.contextType'] = filter_context_type
        if filter_created_after is not None:
            params['filter.createdAfter'] = filter_created_after
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task__post_post__api__fiscal_fiscal_id__order_task(self, task_dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderTask"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTask"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=task_dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task__get_get__api__fiscal_fiscal_id__order_task_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTask/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTask/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task__put_put__api__fiscal_fiscal_id__order_task_id(self, task_dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/OrderTask/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTask/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=task_dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task__delete_delete__api__fiscal_fiscal_id__order_task_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/OrderTask/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTask/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task__get_get__api__fiscal_fiscal_id__order_id__order_task__non_invoiced(self, id: int, fiscal_id: str, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{id}/OrderTask/NonInvoiced"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/OrderTask/NonInvoiced"
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

    def api_order_task__get_latest_get__api__fiscal_fiscal_id__order_task__latest(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, filter_query_string: str = None, filter_order_task_status_ids: list = None, filter_is_invoiced: bool = None, filter_is_delivered: bool = None, filter_project_closed: bool = None, filter_for_bookkeeping: bool = None, filter_include_default: bool = None, filter_order_id: int = None, filter_context_type: str = None, filter_created_after: str = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTask/Latest"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTask/Latest"
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
        if filter_order_task_status_ids is not None:
            params['filter.orderTaskStatusIds'] = filter_order_task_status_ids
        if filter_is_invoiced is not None:
            params['filter.isInvoiced'] = filter_is_invoiced
        if filter_is_delivered is not None:
            params['filter.isDelivered'] = filter_is_delivered
        if filter_project_closed is not None:
            params['filter.projectClosed'] = filter_project_closed
        if filter_for_bookkeeping is not None:
            params['filter.forBookkeeping'] = filter_for_bookkeeping
        if filter_include_default is not None:
            params['filter.includeDefault'] = filter_include_default
        if filter_order_id is not None:
            params['filter.orderId'] = filter_order_id
        if filter_context_type is not None:
            params['filter.contextType'] = filter_context_type
        if filter_created_after is not None:
            params['filter.createdAfter'] = filter_created_after
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task__get_multiple_by_ids_get__api__fiscal_fiscal_id__order_task__multiple(self, order_ids: list, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTask/Multiple"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTask/Multiple"
        params: Dict[str, Any] = {}
        if order_ids is not None:
            params['orderIds'] = order_ids
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

    def api_order_task__get_list_for_filtered_order_status_get__api__fiscal_fiscal_id__order_task__get_list_for_filtered_order_status(self, fiscal_id: str, is_invoiced: bool = None, order_status_id: int = None, department_id: int = None, bearer_id: int = None, purpose_id: int = None, responsible_id: int = None, limit_to_responsible: bool = None, limit_to_order_status: bool = None, limit_to_department: bool = None, limit_to_bearer: bool = None, limit_to_purpose: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTask/GetListForFilteredOrderStatus"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTask/GetListForFilteredOrderStatus"
        params: Dict[str, Any] = {}
        if is_invoiced is not None:
            params['isInvoiced'] = is_invoiced
        if order_status_id is not None:
            params['orderStatusId'] = order_status_id
        if department_id is not None:
            params['departmentId'] = department_id
        if bearer_id is not None:
            params['bearerId'] = bearer_id
        if purpose_id is not None:
            params['purposeId'] = purpose_id
        if responsible_id is not None:
            params['responsibleId'] = responsible_id
        if limit_to_responsible is not None:
            params['limitToResponsible'] = limit_to_responsible
        if limit_to_order_status is not None:
            params['limitToOrderStatus'] = limit_to_order_status
        if limit_to_department is not None:
            params['limitToDepartment'] = limit_to_department
        if limit_to_bearer is not None:
            params['limitToBearer'] = limit_to_bearer
        if limit_to_purpose is not None:
            params['limitToPurpose'] = limit_to_purpose
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

    def api_order_task__get_by_order_get__api__fiscal_fiscal_id__order_id__order_task(self, id: int, fiscal_id: str, created_after: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{id}/OrderTask"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/OrderTask"
        params: Dict[str, Any] = {}
        if created_after is not None:
            params['createdAfter'] = created_after
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

    def api_order_task__post_copy_post__api__fiscal_fiscal_id__order_task_id__copy(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderTask/{id}/Copy"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTask/{id}/Copy"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task__delete_all_lines_delete__api__fiscal_fiscal_id__order_task_id__delete_all_lines(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/OrderTask/{id}/DeleteAllLines"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTask/{id}/DeleteAllLines"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task__delete_confirmation_delete__api__fiscal_fiscal_id__order_task_id__confirmation(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/OrderTask/{id}/Confirmation"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTask/{id}/Confirmation"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task__get_journal_get__api__fiscal_fiscal_id__order_task_id__journal(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTask/{id}/Journal"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTask/{id}/Journal"
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

    def api_order_task__post_subscription_post__api__fiscal_fiscal_id__order_task_id__subscription(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderTask/{id}/Subscription"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTask/{id}/Subscription"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task__get_order_task_for_partner_get__api__fiscal_fiscal_id__order_task__get_order_task_for_partner_id(self, id: int, context_type: str, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTask/GetOrderTaskForPartner/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTask/GetOrderTaskForPartner/{id}"
        params: Dict[str, Any] = {}
        if context_type is not None:
            params['contextType'] = context_type
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task__get_by_numbers_get__api__fiscal_fiscal_id__order_task__by_numbers(self, order_task_numbers: list, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTask/ByNumbers"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTask/ByNumbers"
        params: Dict[str, Any] = {}
        if order_task_numbers is not None:
            params['orderTaskNumbers'] = order_task_numbers
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_ledger__get_list_get__api__fiscal_fiscal_id__order_task_ledger(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTaskLedger"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskLedger"
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

    def api_order_task_ledger__post_post__api__fiscal_fiscal_id__order_task_ledger(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderTaskLedger"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskLedger"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_ledger__get_get__api__fiscal_fiscal_id__order_task_ledger_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTaskLedger/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskLedger/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_ledger__put_put__api__fiscal_fiscal_id__order_task_ledger_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/OrderTaskLedger/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskLedger/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_ledger__delete_delete__api__fiscal_fiscal_id__order_task_ledger_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/OrderTaskLedger/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskLedger/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_line__get_list_get__api__fiscal_fiscal_id__order_task_line(self, fiscal_period_id: int, fiscal_id: str, project_ledger_id: int = None, filter_order_task_id: int = None, filter_resource_id: int = None, filter_responsible_id: int = None, filter_entry_by_id: int = None, limit_to_order_task: bool = None, limit_to_resource: bool = None, limit_to_responsible: bool = None, limit_to_entry_by: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTaskLine"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskLine"
        params: Dict[str, Any] = {}
        if fiscal_period_id is not None:
            params['fiscalPeriodId'] = fiscal_period_id
        if project_ledger_id is not None:
            params['projectLedgerId'] = project_ledger_id
        if filter_order_task_id is not None:
            params['filterOrderTaskId'] = filter_order_task_id
        if filter_resource_id is not None:
            params['filterResourceId'] = filter_resource_id
        if filter_responsible_id is not None:
            params['filterResponsibleId'] = filter_responsible_id
        if filter_entry_by_id is not None:
            params['filterEntryById'] = filter_entry_by_id
        if limit_to_order_task is not None:
            params['limitToOrderTask'] = limit_to_order_task
        if limit_to_resource is not None:
            params['limitToResource'] = limit_to_resource
        if limit_to_responsible is not None:
            params['limitToResponsible'] = limit_to_responsible
        if limit_to_entry_by is not None:
            params['limitToEntryBy'] = limit_to_entry_by
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

    def api_order_task_line__post_post__api__fiscal_fiscal_id__order_task_line(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderTaskLine"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskLine"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_line__get_by_approver_get__api__fiscal_fiscal_id__partner_resource_context__order_task_line(self, fiscal_id: str, project_ledger_id: int = None, filter_order_task_id: int = None, filter_resource_id: int = None, filter_responsible_id: int = None, filter_entry_by_id: int = None, filter_order_id: int = None, limit_to_order_task: bool = None, limit_to_resource: bool = None, limit_to_responsible: bool = None, limit_to_entry_by: bool = None, limit_to_order: bool = None, fiscal_date_from: int = None, fiscal_date_to: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PartnerResourceContext/OrderTaskLine"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerResourceContext/OrderTaskLine"
        params: Dict[str, Any] = {}
        if project_ledger_id is not None:
            params['projectLedgerId'] = project_ledger_id
        if filter_order_task_id is not None:
            params['filterOrderTaskId'] = filter_order_task_id
        if filter_resource_id is not None:
            params['filterResourceId'] = filter_resource_id
        if filter_responsible_id is not None:
            params['filterResponsibleId'] = filter_responsible_id
        if filter_entry_by_id is not None:
            params['filterEntryById'] = filter_entry_by_id
        if filter_order_id is not None:
            params['filterOrderId'] = filter_order_id
        if limit_to_order_task is not None:
            params['limitToOrderTask'] = limit_to_order_task
        if limit_to_resource is not None:
            params['limitToResource'] = limit_to_resource
        if limit_to_responsible is not None:
            params['limitToResponsible'] = limit_to_responsible
        if limit_to_entry_by is not None:
            params['limitToEntryBy'] = limit_to_entry_by
        if limit_to_order is not None:
            params['limitToOrder'] = limit_to_order
        if fiscal_date_from is not None:
            params['fiscalDateFrom'] = fiscal_date_from
        if fiscal_date_to is not None:
            params['fiscalDateTo'] = fiscal_date_to
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

    def api_order_task_line__get_by_order_task_get__api__fiscal_fiscal_id__order_task_order_task_id__line(self, order_task_id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTask/{orderTaskId}/Line"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTask/{order_task_id}/Line"
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

    def api_order_task_line__get_by_order_get__api__fiscal_fiscal_id__order_order_id__line(self, order_id: int, fiscal_id: str, project_ledger_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{orderId}/Line"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{order_id}/Line"
        params: Dict[str, Any] = {}
        if project_ledger_id is not None:
            params['projectLedgerId'] = project_ledger_id
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

    def api_order_task_line__get_get__api__fiscal_fiscal_id__order_task_line_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTaskLine/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskLine/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_line__put_put__api__fiscal_fiscal_id__order_task_line_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/OrderTaskLine/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskLine/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_line__delete_delete__api__fiscal_fiscal_id__order_task_line_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/OrderTaskLine/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskLine/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_line__post_bulk_post__api__fiscal_fiscal_id__order_task_line__bulk(self, dtos: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderTaskLine/Bulk"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskLine/Bulk"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dtos, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_line__put_bookkeep_put__api__fiscal_fiscal_id__order_task_line__bookkeep(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/OrderTaskLine/Bookkeep"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskLine/Bookkeep"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_line__get_order_task_line_type_get__api__fiscal_fiscal_id__order_task_line__order_task_line_type(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTaskLine/OrderTaskLineType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskLine/OrderTaskLineType"
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

    def api_order_task_line__put_send_receipts_put__api__fiscal_fiscal_id__order_task_line__send_receipts(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/OrderTaskLine/SendReceipts"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskLine/SendReceipts"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_post__get_list_get__api__fiscal_fiscal_id__order_task_post(self, fiscal_id: str, cost_type_id: list = None, filter_project_id: int = None, filter_responsible_id: int = None, filter_resource_id: int = None, filter_entry_by_id: int = None, filter_order_task_status_id: int = None, filter_limit_to_project: bool = None, filter_limit_to_responsible: bool = None, filter_limit_to_resource: bool = None, filter_limit_to_entry_by: bool = None, filter_limit_to_cost_type: bool = None, filter_date_from: int = None, filter_date_to: int = None, filter_order_id: int = None, filter_order_task_id: int = None, filter_is_approved: bool = None, filter_voucher_id: int = None, filter_article_id: int = None, filter_partner_id: int = None, filter_department_id: int = None, filter_bearer_id: int = None, filter_purpose_id: int = None, filter_limit_to_department: bool = None, filter_limit_to_bearer: bool = None, filter_limit_to_purpose: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTaskPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskPost"
        params: Dict[str, Any] = {}
        if cost_type_id is not None:
            params['costTypeId'] = cost_type_id
        if filter_project_id is not None:
            params['filter.projectId'] = filter_project_id
        if filter_responsible_id is not None:
            params['filter.responsibleId'] = filter_responsible_id
        if filter_resource_id is not None:
            params['filter.resourceId'] = filter_resource_id
        if filter_entry_by_id is not None:
            params['filter.entryById'] = filter_entry_by_id
        if filter_order_task_status_id is not None:
            params['filter.orderTaskStatusId'] = filter_order_task_status_id
        if filter_limit_to_project is not None:
            params['filter.limitToProject'] = filter_limit_to_project
        if filter_limit_to_responsible is not None:
            params['filter.limitToResponsible'] = filter_limit_to_responsible
        if filter_limit_to_resource is not None:
            params['filter.limitToResource'] = filter_limit_to_resource
        if filter_limit_to_entry_by is not None:
            params['filter.limitToEntryBy'] = filter_limit_to_entry_by
        if filter_limit_to_cost_type is not None:
            params['filter.limitToCostType'] = filter_limit_to_cost_type
        if filter_date_from is not None:
            params['filter.dateFrom'] = filter_date_from
        if filter_date_to is not None:
            params['filter.dateTo'] = filter_date_to
        if filter_order_id is not None:
            params['filter.orderId'] = filter_order_id
        if filter_order_task_id is not None:
            params['filter.orderTaskId'] = filter_order_task_id
        if filter_is_approved is not None:
            params['filter.isApproved'] = filter_is_approved
        if filter_voucher_id is not None:
            params['filter.voucherId'] = filter_voucher_id
        if filter_article_id is not None:
            params['filter.articleId'] = filter_article_id
        if filter_partner_id is not None:
            params['filter.partnerId'] = filter_partner_id
        if filter_department_id is not None:
            params['filter.departmentId'] = filter_department_id
        if filter_bearer_id is not None:
            params['filter.bearerId'] = filter_bearer_id
        if filter_purpose_id is not None:
            params['filter.purposeId'] = filter_purpose_id
        if filter_limit_to_department is not None:
            params['filter.limitToDepartment'] = filter_limit_to_department
        if filter_limit_to_bearer is not None:
            params['filter.limitToBearer'] = filter_limit_to_bearer
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

    def api_order_task_post__get_by_order_task_get__api__fiscal_fiscal_id__order_task_id__post(self, id: int, fiscal_id: str, fiscal_date_from: int = None, fiscal_date_to: int = None, cost_type_id: int = None, order_task_post_type: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTask/{id}/Post"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTask/{id}/Post"
        params: Dict[str, Any] = {}
        if fiscal_date_from is not None:
            params['fiscalDateFrom'] = fiscal_date_from
        if fiscal_date_to is not None:
            params['fiscalDateTo'] = fiscal_date_to
        if cost_type_id is not None:
            params['costTypeId'] = cost_type_id
        if order_task_post_type is not None:
            params['orderTaskPostType'] = order_task_post_type
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

    def api_order_task_post__get_by_order_line_get__api__fiscal_fiscal_id__order_line_id__post(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderLine/{id}/Post"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderLine/{id}/Post"
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

    def api_order_task_post__get_by_order_grouped_get__api__fiscal_fiscal_id__order_id__post__grouped(self, id: int, order_task_ids: list, fiscal_id: str, cost_type_ids: list = None, fiscal_date_from: int = None, fiscal_date_to: int = None, include_transferred: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{id}/Post/Grouped"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/Post/Grouped"
        params: Dict[str, Any] = {}
        if order_task_ids is not None:
            params['orderTaskIds'] = order_task_ids
        if cost_type_ids is not None:
            params['costTypeIds'] = cost_type_ids
        if fiscal_date_from is not None:
            params['fiscalDateFrom'] = fiscal_date_from
        if fiscal_date_to is not None:
            params['fiscalDateTo'] = fiscal_date_to
        if include_transferred is not None:
            params['includeTransferred'] = include_transferred
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

    def api_order_task_post__get_by_order_get__api__fiscal_fiscal_id__order_id__post(self, id: int, order_task_ids: list, fiscal_id: str, cost_type_ids: list = None, fiscal_date_from: int = None, fiscal_date_to: int = None, include_transferred: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{id}/Post"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/Post"
        params: Dict[str, Any] = {}
        if order_task_ids is not None:
            params['orderTaskIds'] = order_task_ids
        if cost_type_ids is not None:
            params['costTypeIds'] = cost_type_ids
        if fiscal_date_from is not None:
            params['fiscalDateFrom'] = fiscal_date_from
        if fiscal_date_to is not None:
            params['fiscalDateTo'] = fiscal_date_to
        if include_transferred is not None:
            params['includeTransferred'] = include_transferred
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

    def api_order_task_post__get_by_order_total_filtered_get__api__fiscal_fiscal_id__order_id__post__total_filtered(self, id: int, order_task_ids: list, fiscal_id: str, cost_type_ids: list = None, fiscal_date_from: int = None, fiscal_date_to: int = None, include_transferred: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{id}/Post/TotalFiltered"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/Post/TotalFiltered"
        params: Dict[str, Any] = {}
        if order_task_ids is not None:
            params['orderTaskIds'] = order_task_ids
        if cost_type_ids is not None:
            params['costTypeIds'] = cost_type_ids
        if fiscal_date_from is not None:
            params['fiscalDateFrom'] = fiscal_date_from
        if fiscal_date_to is not None:
            params['fiscalDateTo'] = fiscal_date_to
        if include_transferred is not None:
            params['includeTransferred'] = include_transferred
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

    def api_order_task_post__get_by_order_total_get__api__fiscal_fiscal_id__order_id__post__total(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{id}/Post/Total"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/Post/Total"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_post__get_by_project_get__api__fiscal_fiscal_id__project_id__post(self, id: int, fiscal_date_from: int, fiscal_date_to: int, fiscal_id: str, cost_type_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Project/{id}/Post"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Project/{id}/Post"
        params: Dict[str, Any] = {}
        if fiscal_date_from is not None:
            params['fiscalDateFrom'] = fiscal_date_from
        if fiscal_date_to is not None:
            params['fiscalDateTo'] = fiscal_date_to
        if cost_type_id is not None:
            params['costTypeId'] = cost_type_id
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

    def api_order_task_post__put_create_order_lines_put__api__fiscal_fiscal_id__order_id__transfer_cost_to_lines(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Order/{id}/TransferCostToLines"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/TransferCostToLines"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_post__put_move_put__api__fiscal_fiscal_id__order_task_post__move(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/OrderTaskPost/Move"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskPost/Move"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_post__get_get__api__fiscal_fiscal_id__order_task_post_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTaskPost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskPost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_post__put_put__api__fiscal_fiscal_id__order_task_post_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/OrderTaskPost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskPost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_status__get_get__api__fiscal_fiscal_id__order_task_status(self, fiscal_id: str, query_string: str = None, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTaskStatus"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskStatus"
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

    def api_order_task_status__post_post__api__fiscal_fiscal_id__order_task_status(self, order_status: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderTaskStatus"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskStatus"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=order_status, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_status__get_get__api__fiscal_fiscal_id__order_task_status_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTaskStatus/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskStatus/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_status__put_put__api__fiscal_fiscal_id__order_task_status_id(self, order_status: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/OrderTaskStatus/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskStatus/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=order_status, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_status__delete_delete__api__fiscal_fiscal_id__order_task_status_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/OrderTaskStatus/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskStatus/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_status__post_create_standard_post__api__fiscal_fiscal_id__order_task_status__standard(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderTaskStatus/Standard"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskStatus/Standard"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partially_paid_partner_post__get_list_for_partner_post_get__api__fiscal_fiscal_id__partner_post_id__partially_paid(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PartnerPost/{id}/PartiallyPaid"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PartnerPost/{id}/PartiallyPaid"
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

    def api_purchase_draft__get_get__api__fiscal_fiscal_id__purchase_draft(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PurchaseDraft"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PurchaseDraft"
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

    def api_purchase_draft__post_post__api__fiscal_fiscal_id__purchase_draft(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/PurchaseDraft"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PurchaseDraft"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_purchase_draft__get_get__api__fiscal_fiscal_id__purchase_draft_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PurchaseDraft/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PurchaseDraft/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_purchase_draft__put_put__api__fiscal_fiscal_id__purchase_draft_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/PurchaseDraft/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PurchaseDraft/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_purchase_draft__delete_delete__api__fiscal_fiscal_id__purchase_draft_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/PurchaseDraft/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PurchaseDraft/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_purchase_draft__post_create_from_article_replenishment_post__api__fiscal_fiscal_id__purchase_draft__article_replenishment(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/PurchaseDraft/ArticleReplenishment"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PurchaseDraft/ArticleReplenishment"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_purchase_draft__post_order_task_post__api__fiscal_fiscal_id__purchase_draft_id__create_order_task(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/PurchaseDraft/{id}/CreateOrderTask"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PurchaseDraft/{id}/CreateOrderTask"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_purchase_draft_line__get_get__api__fiscal_fiscal_id__purchase_draft_id__lines(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PurchaseDraft/{id}/Lines"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PurchaseDraft/{id}/Lines"
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

    def api_purchase_draft_line__get_get__api__fiscal_fiscal_id__purchase_draft_line_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PurchaseDraftLine/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PurchaseDraftLine/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_purchase_draft_line__put_put__api__fiscal_fiscal_id__purchase_draft_line_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/PurchaseDraftLine/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PurchaseDraftLine/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_purchase_draft_line__delete_delete__api__fiscal_fiscal_id__purchase_draft_line_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/PurchaseDraftLine/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PurchaseDraftLine/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_purchase_draft_line__post_post__api__fiscal_fiscal_id__purchase_draft_line(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/PurchaseDraftLine"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PurchaseDraftLine"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_resource_post__get_list_get__api__fiscal_fiscal_id__resource_post(self, fiscal_id: str, filter_resource_ids: list = None, filter_is_billable: bool = None, filter_is_at_work: bool = None, filter_is_paid: bool = None, filter_date_from: int = None, filter_date_to: int = None, filter_order_id: int = None, filter_order_task_id: int = None, filter_activity_type_id: int = None, filter_is_approved: bool = None, filter_project_id: int = None, filter_partner_id: int = None, filter_bearer_id: int = None, filter_department_id: int = None, filter_purpose_id: int = None, filter_limit_to_department: bool = None, filter_limit_to_bearer: bool = None, filter_limit_to_purpose: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ResourcePost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ResourcePost"
        params: Dict[str, Any] = {}
        if filter_resource_ids is not None:
            params['filter.resourceIds'] = filter_resource_ids
        if filter_is_billable is not None:
            params['filter.isBillable'] = filter_is_billable
        if filter_is_at_work is not None:
            params['filter.isAtWork'] = filter_is_at_work
        if filter_is_paid is not None:
            params['filter.isPaid'] = filter_is_paid
        if filter_date_from is not None:
            params['filter.dateFrom'] = filter_date_from
        if filter_date_to is not None:
            params['filter.dateTo'] = filter_date_to
        if filter_order_id is not None:
            params['filter.orderId'] = filter_order_id
        if filter_order_task_id is not None:
            params['filter.orderTaskId'] = filter_order_task_id
        if filter_activity_type_id is not None:
            params['filter.activityTypeId'] = filter_activity_type_id
        if filter_is_approved is not None:
            params['filter.isApproved'] = filter_is_approved
        if filter_project_id is not None:
            params['filter.projectId'] = filter_project_id
        if filter_partner_id is not None:
            params['filter.partnerId'] = filter_partner_id
        if filter_bearer_id is not None:
            params['filter.bearerId'] = filter_bearer_id
        if filter_department_id is not None:
            params['filter.departmentId'] = filter_department_id
        if filter_purpose_id is not None:
            params['filter.purposeId'] = filter_purpose_id
        if filter_limit_to_department is not None:
            params['filter.limitToDepartment'] = filter_limit_to_department
        if filter_limit_to_bearer is not None:
            params['filter.limitToBearer'] = filter_limit_to_bearer
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
