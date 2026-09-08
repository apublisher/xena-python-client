from typing import Any, Dict, Optional
import requests

class FinanceApi:
    """API client for the Finance domain of the Xena API."""
    def __init__(self, base_url: str, session: Optional[requests.Session] = None) -> None:
        self.base_url = base_url.rstrip('/')
        self.session = session or requests.Session()

    def api_bank_export__get_export_type_list_get__api__fiscal_fiscal_id__bank_export__export_type(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/BankExport/ExportType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BankExport/ExportType"
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

    def api_bank_export__get_by_context_list_get__api__fiscal_fiscal_id__bank_export(self, fiscal_id: str, context_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/BankExport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BankExport"
        params: Dict[str, Any] = {}
        if context_id is not None:
            params['contextId'] = context_id
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

    def api_bank_export__get_get__api__fiscal_fiscal_id__bank_export_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/BankExport/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BankExport/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bank_export__post_export_payment_to_ledger_post__api__fiscal_fiscal_id__bank_export__export_payment_to_ledger(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/BankExport/ExportPaymentToLedger"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BankExport/ExportPaymentToLedger"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bearer__get_get__api__fiscal_fiscal_id__bearer(self, fiscal_id: str, query_string: str = None, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Bearer"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Bearer"
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

    def api_bearer__post_post__api__fiscal_fiscal_id__bearer(self, bearer: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Bearer"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Bearer"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=bearer, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bearer__get_get__api__fiscal_fiscal_id__bearer_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Bearer/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Bearer/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bearer__put_put__api__fiscal_fiscal_id__bearer_id(self, bearer: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Bearer/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Bearer/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=bearer, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bearer__delete_delete__api__fiscal_fiscal_id__bearer_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Bearer/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Bearer/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bookkeeping__get_unpaid_stock_details_get__api__fiscal_fiscal_id__bookkeeping__unpaid_stock_details(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Bookkeeping/UnpaidStockDetails"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Bookkeeping/UnpaidStockDetails"
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

    def api_bookkeeping__put_settle_unpaid_stock_put__api__fiscal_fiscal_id__bookkeeping_order_id__settle_unpaid_stock(self, order_id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Bookkeeping/{orderId}/SettleUnpaidStock"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Bookkeeping/{order_id}/SettleUnpaidStock"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bookkeeping__get_voucher_modified_history_get__api__fiscal_fiscal_id__bookkeeping__voucher_modified_history(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Bookkeeping/VoucherModifiedHistory"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Bookkeeping/VoucherModifiedHistory"
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

    def api_bookkeeping__post_transfer_voucher_preview_to_order_post__api__fiscal_fiscal_id__bookkeeping__transfer_voucher_preview_to_order(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Bookkeeping/TransferVoucherPreviewToOrder"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Bookkeeping/TransferVoucherPreviewToOrder"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_currency__get_get__api__fiscal_fiscal_id__currency(self, fiscal_id: str, query_string: str = None, show_all: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Currency"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Currency"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if show_all is not None:
            params['showAll'] = show_all
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

    def api_currency__get_exchange_rate_by_date_get__api__fiscal_fiscal_id__currency_currency_abbreviation__exchange_rate_by_date(self, currency_abbreviation: str, fiscal_id: str, fiscal_date: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Currency/{currencyAbbreviation}/ExchangeRateByDate"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Currency/{currency_abbreviation}/ExchangeRateByDate"
        params: Dict[str, Any] = {}
        if fiscal_date is not None:
            params['fiscalDate'] = fiscal_date
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_currency__get_currency_amount_to_pay_get__api__fiscal_fiscal_id__currency_currency_abbreviation__currency_amount_to_pay(self, currency_abbreviation: str, partner_post_ids: list, fiscal_id: str, fiscal_date: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Currency/{currencyAbbreviation}/CurrencyAmountToPay"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Currency/{currency_abbreviation}/CurrencyAmountToPay"
        params: Dict[str, Any] = {}
        if partner_post_ids is not None:
            params['partnerPostIds'] = partner_post_ids
        if fiscal_date is not None:
            params['fiscalDate'] = fiscal_date
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_currency_exchange_rate__get_get__api__fiscal_fiscal_id__currency_exchange_rate_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/CurrencyExchangeRate/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/CurrencyExchangeRate/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_currency_exchange_rate__put_put__api__fiscal_fiscal_id__currency_exchange_rate_id(self, currency_exchange_rate: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/CurrencyExchangeRate/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/CurrencyExchangeRate/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=currency_exchange_rate, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_currency_exchange_rate__delete_delete__api__fiscal_fiscal_id__currency_exchange_rate_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/CurrencyExchangeRate/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/CurrencyExchangeRate/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_currency_exchange_rate__post_post__api__fiscal_fiscal_id__currency_exchange_rate(self, currency_exchange_rate: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/CurrencyExchangeRate"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/CurrencyExchangeRate"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=currency_exchange_rate, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_currency_exchange_rate__get_by_currency_get__api__fiscal_fiscal_id__currency_currency_abbreviation__exchange_rate(self, currency_abbreviation: str, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Currency/{currencyAbbreviation}/ExchangeRate"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Currency/{currency_abbreviation}/ExchangeRate"
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

    def api_currency_exchange_rate__get_exchange_rate_by_currency_get__api__fiscal_fiscal_id__currency_exchange_rate__exchange_rate_by_currency(self, currency_abbreviation: str, fiscal_date: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/CurrencyExchangeRate/ExchangeRateByCurrency"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/CurrencyExchangeRate/ExchangeRateByCurrency"
        params: Dict[str, Any] = {}
        if currency_abbreviation is not None:
            params['currencyAbbreviation'] = currency_abbreviation
        if fiscal_date is not None:
            params['fiscalDate'] = fiscal_date
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_currency_exchange_rate__get_by_exact_date_and_currency_get__api__fiscal_fiscal_id__currency_exchange_rate__exact_date(self, currency_abbreviation: str, fiscal_date: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/CurrencyExchangeRate/ExactDate"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/CurrencyExchangeRate/ExactDate"
        params: Dict[str, Any] = {}
        if currency_abbreviation is not None:
            params['currencyAbbreviation'] = currency_abbreviation
        if fiscal_date is not None:
            params['fiscalDate'] = fiscal_date
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_currency_exchange_rate__get_currency_exchange_rate_ecb_get__api__fiscal_fiscal_id__currency_exchange_rate__currency_exchange_rate_ecb(self, currency_abbreviation: str, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/CurrencyExchangeRate/CurrencyExchangeRateECB"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/CurrencyExchangeRate/CurrencyExchangeRateECB"
        params: Dict[str, Any] = {}
        if currency_abbreviation is not None:
            params['currencyAbbreviation'] = currency_abbreviation
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_default_price_margin__get_get__api__fiscal_fiscal_id__default_price_margin(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/DefaultPriceMargin"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DefaultPriceMargin"
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

    def api_default_price_margin__post_post__api__fiscal_fiscal_id__default_price_margin(self, margin: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/DefaultPriceMargin"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DefaultPriceMargin"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=margin, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_default_price_margin__get_get__api__fiscal_fiscal_id__default_price_margin_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/DefaultPriceMargin/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DefaultPriceMargin/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_default_price_margin__put_put__api__fiscal_fiscal_id__default_price_margin_id(self, margin: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/DefaultPriceMargin/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DefaultPriceMargin/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=margin, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_default_price_margin__delete_delete__api__fiscal_fiscal_id__default_price_margin_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/DefaultPriceMargin/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DefaultPriceMargin/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_department__get_get__api__fiscal_fiscal_id__department(self, fiscal_id: str, query_string: str = None, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Department"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Department"
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

    def api_department__post_post__api__fiscal_fiscal_id__department(self, department: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Department"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Department"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=department, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_department__get_get__api__fiscal_fiscal_id__department_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Department/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Department/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_department__put_put__api__fiscal_fiscal_id__department_id(self, department: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Department/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Department/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=department, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_department__delete_delete__api__fiscal_fiscal_id__department_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Department/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Department/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_department__get_exists_get__api__fiscal_fiscal_id__department__exists(self, description: str, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Department/Exists"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Department/Exists"
        params: Dict[str, Any] = {}
        if description is not None:
            params['description'] = description
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_electronic_invoicing__post_sproom_register_nem_handel_post__api__fiscal_fiscal_id__electronic_invoicing__sproom__registration__nemhandel(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ElectronicInvoicing/Sproom/Registration/Nemhandel"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ElectronicInvoicing/Sproom/Registration/Nemhandel"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_period__get_get__api__fiscal_fiscal_id__fiscal_period(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalPeriod"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalPeriod"
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

    def api_fiscal_period__post_post__api__fiscal_fiscal_id__fiscal_period(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalPeriod"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalPeriod"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_period__get_get__api__fiscal_fiscal_id__fiscal_period_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalPeriod/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalPeriod/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_period__put_put__api__fiscal_fiscal_id__fiscal_period_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/FiscalPeriod/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalPeriod/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_period__delete_delete__api__fiscal_fiscal_id__fiscal_period_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/FiscalPeriod/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalPeriod/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_period__get_recalculate_summary_get__api__fiscal_fiscal_id__fiscal_period_id__recalculate_summary(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalPeriod/{id}/RecalculateSummary"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalPeriod/{id}/RecalculateSummary"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_period__put_recalculate_primo_posts_put__api__fiscal_fiscal_id__fiscal_period_id__recalculate_primo(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/FiscalPeriod/{id}/RecalculatePrimo"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalPeriod/{id}/RecalculatePrimo"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_period__get_fiscal_period_data_get__api__fiscal_fiscal_id__fiscal_period_id__data(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalPeriod/{id}/Data"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalPeriod/{id}/Data"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_period__get_dates_get__api__fiscal_fiscal_id__fiscal_period__dates(self, fiscal_id: str, date: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalPeriod/Dates"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalPeriod/Dates"
        params: Dict[str, Any] = {}
        if date is not None:
            params['date'] = date
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_settings__get_double_get__api__fiscal_fiscal_id__setting__double_setting(self, setting: str, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Setting/Double/{setting}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Setting/Double/{setting}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_settings__put_double_put__api__fiscal_fiscal_id__setting__double_setting(self, setting: str, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Setting/Double/{setting}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Setting/Double/{setting}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_settings__get_bool_get__api__fiscal_fiscal_id__setting__bool_setting(self, setting: str, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Setting/Bool/{setting}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Setting/Bool/{setting}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_settings__put_bool_put__api__fiscal_fiscal_id__setting__bool_setting(self, setting: str, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Setting/Bool/{setting}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Setting/Bool/{setting}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_settings__get_string_get__api__fiscal_fiscal_id__setting__string_setting(self, setting: str, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Setting/String/{setting}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Setting/String/{setting}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_settings__put_string_put__api__fiscal_fiscal_id__setting__string_setting(self, setting: str, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Setting/String/{setting}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Setting/String/{setting}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__post_copy_post__api__fiscal_fiscal_id__fiscal_setup__copy(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalSetup/Copy"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/Copy"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__delete_logo_delete__api__fiscal_fiscal_id__fiscal_setup__logo(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/FiscalSetup/Logo"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/Logo"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__get_installed_apps_get__api__fiscal_fiscal_id__fiscal_setup__installed_apps(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/InstalledApps"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/InstalledApps"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__post_import_manually_post__api__fiscal_fiscal_id__fiscal_setup__import_manually(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalSetup/ImportManually"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/ImportManually"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__get_subscription_partner_post_list_get__api__fiscal_fiscal_id__fiscal_setup__subscription_id__partner_post(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/Subscription/{id}/PartnerPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/Subscription/{id}/PartnerPost"
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

    def api_fiscal_setup__get_partner_post_list_get__api__fiscal_fiscal_id__fiscal_setup__partner_id__partner_post(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/Partner/{id}/PartnerPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/Partner/{id}/PartnerPost"
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

    def api_fiscal_setup__get_location_get__api__fiscal_fiscal_id__fiscal_setup__location_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/Location/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/Location/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__put_location_put__api__fiscal_fiscal_id__fiscal_setup__location_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/FiscalSetup/Location/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/Location/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__get_location_by_fiscal_setup_get__api__fiscal_fiscal_id__fiscal_setup__location_by_fiscal_setup(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/LocationByFiscalSetup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/LocationByFiscalSetup"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__get_get__api__fiscal_fiscal_id__fiscal_setup(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__put_put__api__fiscal_fiscal_id__fiscal_setup(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/FiscalSetup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__delete_delete__api__fiscal_fiscal_id__fiscal_setup(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/FiscalSetup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__get_membership_list_get__api__fiscal_fiscal_id__fiscal_setup__membership(self, fiscal_id: str, query_string: str = None, date_to_end_of_employment: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/Membership"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/Membership"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if date_to_end_of_employment is not None:
            params['dateToEndOfEmployment'] = date_to_end_of_employment
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

    def api_fiscal_setup__get_api_key_get__api__fiscal_fiscal_id__fiscal_setup__api_keys(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/ApiKeys"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/ApiKeys"
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

    def api_fiscal_setup__get_api_key_get__api__fiscal_fiscal_id__fiscal_setup__virtual_user(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/VirtualUser"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/VirtualUser"
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

    def api_fiscal_setup__get_membership_get__api__fiscal_fiscal_id__fiscal_setup__membership_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/Membership/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/Membership/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__delete_membership_delete__api__fiscal_fiscal_id__fiscal_setup__membership_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/FiscalSetup/Membership/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/Membership/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__post_create_iso_post__api__fiscal_fiscal_id__fiscal_setup__create_iso(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalSetup/CreateISO"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/CreateISO"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__put_change_security_group_put__api__fiscal_fiscal_id__fiscal_setup__membership_id__change_security_group(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/FiscalSetup/Membership/{id}/ChangeSecurityGroup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/Membership/{id}/ChangeSecurityGroup"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__put_manage_apps_put__api__fiscal_fiscal_id__fiscal_setup__membership_id__manage_apps(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/FiscalSetup/Membership/{id}/ManageApps"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/Membership/{id}/ManageApps"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__get_v_card_by_fiscal_setup_get__api__fiscal_fiscal_id__fiscal_setup_v_card_by_fiscal_setup(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/VCardByFiscalSetup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/VCardByFiscalSetup"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__get_v_card_get__api__fiscal_fiscal_id__fiscal_setup_v_card_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/VCard/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/VCard/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__put_v_card_put__api__fiscal_fiscal_id__fiscal_setup_v_card_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/FiscalSetup/VCard/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/VCard/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__delete_v_card_delete__api__fiscal_fiscal_id__fiscal_setup_v_card_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/FiscalSetup/VCard/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/VCard/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__post_v_card_post__api__fiscal_fiscal_id__fiscal_setup_v_card(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalSetup/VCard"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/VCard"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__get_get__api__fiscal_fiscal_id__fiscal_setup__xena_apps(self, fiscal_id: str, query_string: str = None, include_xena: bool = None, include_internal: bool = None, include_bundles: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/XenaApps"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/XenaApps"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if include_xena is not None:
            params['includeXena'] = include_xena
        if include_internal is not None:
            params['includeInternal'] = include_internal
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

    def api_fiscal_setup__post_invite_user_post__api__fiscal_fiscal_id__fiscal_setup__user_id__invite(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalSetup/User/{id}/Invite"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/User/{id}/Invite"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__post_invite_user_by_email_post__api__fiscal_fiscal_id__fiscal_setup__invite_user_by_email(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalSetup/InviteUserByEmail"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/InviteUserByEmail"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__post_create_api_user_post__api__fiscal_fiscal_id__fiscal_setup__create_api_user(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalSetup/CreateApiUser"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/CreateApiUser"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__get_security_role_list_get__api__fiscal_fiscal_id__fiscal_setup__security_role(self, fiscal_id: str, list_option_show_deactivated: bool = None, list_option_page: int = None, list_option_page_size: int = None, list_option_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/SecurityRole"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/SecurityRole"
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

    def api_fiscal_setup__get_membership_security_role_get__api__fiscal_fiscal_id__fiscal_setup__membership_id__security_role(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/Membership/{id}/SecurityRole"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/Membership/{id}/SecurityRole"
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

    def api_fiscal_setup__post_request_sproom_account_post__api__fiscal_fiscal_id__fiscal_setup__request_sproom_account(self, account: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalSetup/RequestSproomAccount"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/RequestSproomAccount"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=account, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__put_sproom_account_put__api__fiscal_fiscal_id__fiscal_setup__sproom_setup(self, account: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/FiscalSetup/SproomSetup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/SproomSetup"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=account, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__delete_request_removal_from_sproom_account_delete__api__fiscal_fiscal_id__fiscal_setup__sproom_setup(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/FiscalSetup/SproomSetup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/SproomSetup"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__get_xena_subscription_for_current_fiscal_get__api__fiscal_fiscal_id__fiscal_setup__xena_subscription_id(self, fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/XenaSubscription/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/XenaSubscription/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__get_xena_subscription_for_current_fiscal_get__api__fiscal_fiscal_id__fiscal_setup__xena_subscription(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/XenaSubscription"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/XenaSubscription"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__put_request_premium_put__api__fiscal_fiscal_id__fiscal_setup__request_premium(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/FiscalSetup/RequestPremium"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/RequestPremium"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__get_subscription_ticket_get__api__fiscal_fiscal_id__fiscal_setup__subscription_id__subscription_ticket(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/Subscription/{id}/SubscriptionTicket"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/Subscription/{id}/SubscriptionTicket"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__put_update_v_card_picture_put__api__fiscal_fiscal_id__fiscal_setup__update_v_card_picture(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/FiscalSetup/UpdateVCardPicture"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/UpdateVCardPicture"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__delete_archive_delete__api__fiscal_fiscal_id__fiscal_setup__delete_archive(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/FiscalSetup/DeleteArchive"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/DeleteArchive"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__delete_reset_import_task_delete__api__fiscal_fiscal_id__fiscal_setup__reset_data_import_task(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/FiscalSetup/ResetDataImportTask"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/ResetDataImportTask"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__post_transfer_membership_post__api__fiscal_fiscal_id__fiscal_setup__transfer_user_id(self, user_id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalSetup/Transfer/{userId}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/Transfer/{user_id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__post_transfer_membership_to_email_post__api__fiscal_fiscal_id__fiscal_setup__transfer_to_email(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalSetup/TransferToEmail"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/TransferToEmail"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__put_update_fiscal_setup_accountant_put__api__fiscal_fiscal_id__fiscal_setup__update_fiscal_setup_accountant(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/FiscalSetup/UpdateFiscalSetupAccountant"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/UpdateFiscalSetupAccountant"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__get_xena_subscription_data_get__api__fiscal_fiscal_id__fiscal_setup__xena_subscription_data(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/XenaSubscriptionData"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/XenaSubscriptionData"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__get_has_valid_xena_payment_get__api__fiscal_fiscal_id__fiscal_setup__has_valid_xena_payment(self, fiscal_id: str, xena_app: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/HasValidXenaPayment"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/HasValidXenaPayment"
        params: Dict[str, Any] = {}
        if xena_app is not None:
            params['xenaApp'] = xena_app
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__get_xena_fiscal_subscription_list_get__api__fiscal_fiscal_id__fiscal_setup__fiscal_setup_id__xena_fiscal_subscription(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/FiscalSetup/{id}/XenaFiscalSubscription"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/FiscalSetup/{id}/XenaFiscalSubscription"
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

    def api_fiscal_setup__get_xena_fiscal_partner_post_for_fiscal_list_get__api__fiscal_fiscal_id__fiscal_setup__fiscal_setup_id__xena_fiscal_partner_post(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/FiscalSetup/{id}/XenaFiscalPartnerPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/FiscalSetup/{id}/XenaFiscalPartnerPost"
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

    def api_fiscal_setup__get_connection_data_for_fiscal_get__api__fiscal_fiscal_id__fiscal_setup__fiscal_id__connection_data(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/Fiscal/{id}/ConnectionData"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/Fiscal/{id}/ConnectionData"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__get_connection_data_for_user_get__api__fiscal_fiscal_id__fiscal_setup__user_data_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/UserData/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/UserData/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__post_md5_key_post__api__fiscal_fiscal_id__fiscal_setup_md5_key(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalSetup/MD5Key"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/MD5Key"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__post_epay_data_for_online_fiscal_payment_post__api__fiscal_fiscal_id__fiscal_setup__epay_data_for_online_fiscal_payment(self, payment_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalSetup/EpayDataForOnlineFiscalPayment"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/EpayDataForOnlineFiscalPayment"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=payment_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__post_epay_data_for_blank_subscription_post__api__fiscal_fiscal_id__fiscal_setup__epay_data_for_blank_subscription(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalSetup/EpayDataForBlankSubscription"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/EpayDataForBlankSubscription"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__post_epay_ticket_for_existing_fiscal_subscription_post__api__fiscal_fiscal_id__fiscal_setup__epay_ticket_for_existing_fiscal_subscription(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalSetup/EpayTicketForExistingFiscalSubscription"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/EpayTicketForExistingFiscalSubscription"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__post_request_premium_by_epay_post__api__fiscal_fiscal_id__fiscal_setup__request_premium_by_epay(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalSetup/RequestPremiumByEpay"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/RequestPremiumByEpay"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__get_outstanding_payment_get__api__fiscal_fiscal_id__fiscal_setup__outstanding_payment(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/OutstandingPayment"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/OutstandingPayment"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__get_statistics_get__api__fiscal_fiscal_id__fiscal_setup__statistics(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/Statistics"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/Statistics"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__post_redeem_discount_code_post__api__fiscal_fiscal_id__fiscal_setup__redeem_discount_code(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalSetup/RedeemDiscountCode"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/RedeemDiscountCode"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__get_used_discount_codes_get__api__fiscal_fiscal_id__fiscal_setup__used_discount_codes(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/UsedDiscountCodes"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/UsedDiscountCodes"
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

    def api_fiscal_setup__get_account_plan_template_applicable_get__api__fiscal_fiscal_id__fiscal_setup__account_plan_template_applicable(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/AccountPlanTemplateApplicable"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/AccountPlanTemplateApplicable"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup__delete_imported_not_connected_to_data_import_delete__api__fiscal_fiscal_id__fiscal_setup__delete_imported_not_connected_to_data_import(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/FiscalSetup/DeleteImportedNotConnectedToDataImport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/DeleteImportedNotConnectedToDataImport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup_approval_context__get_get__api__fiscal_fiscal_id__fiscal_setup__approval_context(self, fiscal_id: int, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalSetup/ApprovalContext"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/ApprovalContext"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_fiscal_setup_approval_context__put_put__api__fiscal_fiscal_id__fiscal_setup__approval_context(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/FiscalSetup/ApprovalContext"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalSetup/ApprovalContext"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger__get_get__api__fiscal_fiscal_id__ledger(self, fiscal_id: str, querystring: str = None, include_defaults: bool = None, excluded_ledger_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Ledger"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Ledger"
        params: Dict[str, Any] = {}
        if querystring is not None:
            params['querystring'] = querystring
        if include_defaults is not None:
            params['includeDefaults'] = include_defaults
        if excluded_ledger_id is not None:
            params['excludedLedgerId'] = excluded_ledger_id
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

    def api_ledger__post_post__api__fiscal_fiscal_id__ledger(self, vat: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Ledger"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Ledger"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=vat, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger__get_get__api__fiscal_fiscal_id__ledger_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Ledger/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Ledger/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger__put_put__api__fiscal_fiscal_id__ledger_id(self, ledger: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Ledger/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Ledger/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=ledger, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger__delete_delete__api__fiscal_fiscal_id__ledger_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Ledger/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Ledger/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger__get_ready_for_bookkeeping_get__api__fiscal_fiscal_id__ledger__get_ready_for_bookkeeping(self, fiscal_id: str, are_ready_for_bookkeeping: bool = None, querystring: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Ledger/GetReadyForBookkeeping"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Ledger/GetReadyForBookkeeping"
        params: Dict[str, Any] = {}
        if are_ready_for_bookkeeping is not None:
            params['areReadyForBookkeeping'] = are_ready_for_bookkeeping
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

    def api_ledger__get_voucher_numbers_get__api__fiscal_fiscal_id__ledger_id__next_voucher_numbers(self, id: int, fiscal_id: str, quantity: int = None, fiscal_period_id: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Ledger/{id}/NextVoucherNumbers"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Ledger/{id}/NextVoucherNumbers"
        params: Dict[str, Any] = {}
        if quantity is not None:
            params['quantity'] = quantity
        if fiscal_period_id is not None:
            params['fiscalPeriodId'] = fiscal_period_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger__get_summary_get__api__fiscal_fiscal_id__ledger_id__summary(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Ledger/{id}/Summary"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Ledger/{id}/Summary"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger__post_summary_post__api__fiscal_fiscal_id__ledger_id__summary(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Ledger/{id}/Summary"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Ledger/{id}/Summary"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger__put_bookkeep_put__api__fiscal_fiscal_id__ledger_id__bookkeep(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Ledger/{id}/Bookkeep"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Ledger/{id}/Bookkeep"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger__delete_lines_delete__api__fiscal_fiscal_id__ledger_id__lines(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Ledger/{id}/Lines"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Ledger/{id}/Lines"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger__post_default_ledger_post__api__fiscal_fiscal_id__ledger__default(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Ledger/Default"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Ledger/Default"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger__put_update_ledger_number_series_put__api__fiscal_fiscal_id__ledger_id__put_update_ledger_number_series(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Ledger/{id}/PutUpdateLedgerNumberSeries"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Ledger/{id}/PutUpdateLedgerNumberSeries"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_account__get_list_get__api__fiscal_fiscal_id__ledger_account(self, fiscal_id: str, ledger_account: str = None, query_string: str = None, include_default: bool = None, exclude_vats: bool = None, exclude_article_groups: bool = None, exclude_ledger_tags: bool = None, exclude_system_accounts: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, exclude_article_groups_without_number: Optional[bool] = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerAccount"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerAccount"
        params: Dict[str, Any] = {}
        if ledger_account is not None:
            params['ledgerAccount'] = ledger_account
        if query_string is not None:
            params['queryString'] = query_string
        if include_default is not None:
            params['includeDefault'] = include_default
        if exclude_vats is not None:
            params['excludeVats'] = exclude_vats
        if exclude_article_groups is not None:
            params['excludeArticleGroups'] = exclude_article_groups
        if exclude_ledger_tags is not None:
            params['excludeLedgerTags'] = exclude_ledger_tags
        if exclude_system_accounts is not None:
            params['excludeSystemAccounts'] = exclude_system_accounts
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        if exclude_article_groups_without_number is not None:
            params['excludeArticleGroupsWithoutNumber'] = exclude_article_groups_without_number
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_account__get_get__api__fiscal_fiscal_id__ledger_account_id(self, id: str, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerAccount/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerAccount/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_account__put_put__api__fiscal_fiscal_id__ledger_account_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/LedgerAccount/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerAccount/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_account__delete_delete__api__fiscal_fiscal_id__ledger_account_id(self, id: str, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/LedgerAccount/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerAccount/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_line__get_get__api__fiscal_fiscal_id__ledger_id__line(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Ledger/{id}/Line"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Ledger/{id}/Line"
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

    def api_ledger_line__get_get__api__fiscal_fiscal_id__ledger_line_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerLine/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerLine/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_line__put_put__api__fiscal_fiscal_id__ledger_line_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/LedgerLine/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerLine/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_line__delete_delete__api__fiscal_fiscal_id__ledger_line_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/LedgerLine/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerLine/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_line__put_reorder_lines_put__api__fiscal_fiscal_id__ledger_id__reorder_lines(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Ledger/{id}/ReorderLines"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Ledger/{id}/ReorderLines"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_line__post_post__api__fiscal_fiscal_id__ledger_line(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/LedgerLine"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerLine"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_line__post_bulk_post__api__fiscal_fiscal_id__ledger_line_ledger_id__bulk(self, ledger_id: int, dtos: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/LedgerLine/{ledgerId}/Bulk"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerLine/{ledger_id}/Bulk"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dtos, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_line__post_multiple_post__api__fiscal_fiscal_id__ledger_line_ledger_id__multiple(self, ledger_id: int, ledger_lines: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/LedgerLine/{ledgerId}/Multiple"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerLine/{ledger_id}/Multiple"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=ledger_lines, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_line__post_payment_post__api__fiscal_fiscal_id__ledger_line_ledger_id__payment(self, ledger_id: int, ledger_line_payment_datas: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/LedgerLine/{ledgerId}/Payment"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerLine/{ledger_id}/Payment"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=ledger_line_payment_datas, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_line__get_ledger_line_type_get__api__fiscal_fiscal_id__ledger_line__ledger_line_type(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerLine/LedgerLineType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerLine/LedgerLineType"
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

    def api_ledger_line__put_accrual_accounting_put__api__fiscal_fiscal_id__ledger_line_id__accrual_accounting(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/LedgerLine/{id}/AccrualAccounting"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerLine/{id}/AccrualAccounting"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_post__get_get__api__fiscal_fiscal_id__ledger_post_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerPost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerPost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_post__put_put__api__fiscal_fiscal_id__ledger_post_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/LedgerPost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerPost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_post__get_by_ledger_tag_get__api__fiscal_fiscal_id__ledger_tag_id__ledger_post(self, id: int, fiscal_id: str, include_running_totals: bool = None, fiscal_date_from: int = None, fiscal_date_to: int = None, show_reconciled: bool = None, reverse_date_sort: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTag/{id}/LedgerPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/{id}/LedgerPost"
        params: Dict[str, Any] = {}
        if include_running_totals is not None:
            params['includeRunningTotals'] = include_running_totals
        if fiscal_date_from is not None:
            params['fiscalDateFrom'] = fiscal_date_from
        if fiscal_date_to is not None:
            params['fiscalDateTo'] = fiscal_date_to
        if show_reconciled is not None:
            params['showReconciled'] = show_reconciled
        if reverse_date_sort is not None:
            params['reverseDateSort'] = reverse_date_sort
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

    def api_ledger_post_preview__get_ledger_post_preview_get__api__fiscal_fiscal_id__voucher_preview_id__ledger_post_preview(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VoucherPreview/{id}/LedgerPostPreview"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VoucherPreview/{id}/LedgerPostPreview"
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

    def api_ledger_post_preview__get_contra_ledger_post_preview_get__api__fiscal_fiscal_id__voucher_preview_id__contra_ledger_post_preview(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VoucherPreview/{id}/ContraLedgerPostPreview"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VoucherPreview/{id}/ContraLedgerPostPreview"
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

    def api_ledger_post_preview__get_difference_ledger_post_preview_get__api__fiscal_fiscal_id__voucher_preview_id__difference_ledger_post_preview(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VoucherPreview/{id}/DifferenceLedgerPostPreview"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VoucherPreview/{id}/DifferenceLedgerPostPreview"
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

    def api_ledger_post_preview__get_get__api__fiscal_fiscal_id__ledger_post_preview_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerPostPreview/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerPostPreview/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_post_preview__put_put__api__fiscal_fiscal_id__ledger_post_preview_id(self, ledger_post_preview: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/LedgerPostPreview/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerPostPreview/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=ledger_post_preview, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_post_preview__delete_delete__api__fiscal_fiscal_id__ledger_post_preview_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/LedgerPostPreview/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerPostPreview/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_post_preview__post_post__api__fiscal_fiscal_id__ledger_post_preview(self, ledger_post_preview: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/LedgerPostPreview"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerPostPreview"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=ledger_post_preview, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_search__get_list_get__api__fiscal_fiscal_id__ledger_search(self, fiscal_id: str, ledger_account: str = None, query_string: str = None, include_defaults: bool = None, include_vat: bool = None, include_article_group: bool = None, include_system_accounts: bool = None, country_name: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerSearch"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerSearch"
        params: Dict[str, Any] = {}
        if ledger_account is not None:
            params['ledgerAccount'] = ledger_account
        if query_string is not None:
            params['queryString'] = query_string
        if include_defaults is not None:
            params['includeDefaults'] = include_defaults
        if include_vat is not None:
            params['includeVat'] = include_vat
        if include_article_group is not None:
            params['includeArticleGroup'] = include_article_group
        if include_system_accounts is not None:
            params['includeSystemAccounts'] = include_system_accounts
        if country_name is not None:
            params['countryName'] = country_name
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

    def api_ledger_search__get_full_list_get__api__fiscal_fiscal_id__ledger_search__full_list(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerSearch/FullList"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerSearch/FullList"
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

    def api_ledger_search__get_get__api__fiscal_fiscal_id__ledger_search_id(self, id: str, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerSearch/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerSearch/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_search__put_put__api__fiscal_fiscal_id__ledger_search_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/LedgerSearch/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerSearch/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_search__delete_delete__api__fiscal_fiscal_id__ledger_search_id(self, id: str, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/LedgerSearch/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerSearch/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag__get_get__api__fiscal_fiscal_id__ledger_tag(self, fiscal_id: str, ledger_account: str = None, query_string: str = None, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTag"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag"
        params: Dict[str, Any] = {}
        if ledger_account is not None:
            params['ledgerAccount'] = ledger_account
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

    def api_ledger_tag__post_post__api__fiscal_fiscal_id__ledger_tag(self, ledger_tag: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/LedgerTag"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=ledger_tag, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag__get_get__api__fiscal_fiscal_id__ledger_tag_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTag/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag__put_put__api__fiscal_fiscal_id__ledger_tag_id(self, ledger_tag: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/LedgerTag/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=ledger_tag, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag__delete_delete__api__fiscal_fiscal_id__ledger_tag_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/LedgerTag/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag__post_default_currency_difference_post__api__fiscal_fiscal_id__ledger_tag__default_currency_difference_tag(self, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/LedgerTag/DefaultCurrencyDifferenceTag"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/DefaultCurrencyDifferenceTag"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag__get_duplicate_account_numbers_get__api__fiscal_fiscal_id__ledger_tag_id__duplicate_account_numbers(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTag/{id}/DuplicateAccountNumbers"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/{id}/DuplicateAccountNumbers"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag__get_duplicate_account_number_by_numbers_get__api__fiscal_fiscal_id__ledger_tag__duplicate_account_number(self, fiscal_id: str, data_account_numbers: list = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTag/DuplicateAccountNumber"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/DuplicateAccountNumber"
        params: Dict[str, Any] = {}
        if data_account_numbers is not None:
            params['data.accountNumbers'] = data_account_numbers
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag__get_ledger_tag_type_get__api__fiscal_fiscal_id__ledger_tag__ledger_tag_type(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTag/LedgerTagType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/LedgerTagType"
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

    def api_ledger_tag__get_settlement_tag_get__api__fiscal_fiscal_id__ledger_tag__settlement_tag(self, fiscal_id: str, include_default: bool = None, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTag/SettlementTag"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/SettlementTag"
        params: Dict[str, Any] = {}
        if include_default is not None:
            params['includeDefault'] = include_default
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

    def api_ledger_tag__get_currency_difference_tag_get__api__fiscal_fiscal_id__ledger_tag__currency_difference_tag(self, fiscal_id: str, include_default: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTag/CurrencyDifferenceTag"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/CurrencyDifferenceTag"
        params: Dict[str, Any] = {}
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

    def api_ledger_tag__get_ledger_account_info_list_get__api__fiscal_fiscal_id__ledger_tag__ledger_account_info(self, fiscal_id: str, ledger_group: str = None, list_option_show_deactivated: bool = None, list_option_page: int = None, list_option_page_size: int = None, list_option_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTag/LedgerAccountInfo"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/LedgerAccountInfo"
        params: Dict[str, Any] = {}
        if ledger_group is not None:
            params['ledgerGroup'] = ledger_group
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

    def api_ledger_tag__get_ledger_group_list_get__api__fiscal_fiscal_id__ledger_tag__ledger_group(self, fiscal_id: str, list_option_show_deactivated: bool = None, list_option_page: int = None, list_option_page_size: int = None, list_option_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTag/LedgerGroup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/LedgerGroup"
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

    def api_ledger_tag__get_ledger_accounts_allowing_article_group_list_get__api__fiscal_fiscal_id__ledger_tag__ledger_accounts__article_group(self, fiscal_id: str, list_option_show_deactivated: bool = None, list_option_page: int = None, list_option_page_size: int = None, list_option_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTag/LedgerAccounts/ArticleGroup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/LedgerAccounts/ArticleGroup"
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

    def api_ledger_tag__get_ledger_accounts_allowing_ledger_tag_list_get__api__fiscal_fiscal_id__ledger_tag__ledger_accounts__ledger_tag(self, fiscal_id: str, list_option_show_deactivated: bool = None, list_option_page: int = None, list_option_page_size: int = None, list_option_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTag/LedgerAccounts/LedgerTag"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/LedgerAccounts/LedgerTag"
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

    def api_ledger_tag__get_tax_types_list_get__api__fiscal_fiscal_id__ledger_tag__tax_type(self, fiscal_id: str, list_option_show_deactivated: bool = None, list_option_page: int = None, list_option_page_size: int = None, list_option_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTag/TaxType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/TaxType"
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

    def api_ledger_tag__get_ledger_accounts_allowing_ledger_tag_get__api__fiscal_fiscal_id__ledger_tag__ledger_accounts__ledger_tag__new(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTag/LedgerAccounts/LedgerTag/New"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/LedgerAccounts/LedgerTag/New"
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

    def api_ledger_tag__get_ledger_tag_account_get__api__fiscal_fiscal_id__ledger_tag__ledger_tag_account(self, fiscal_id: str, list_option_show_deactivated: bool = None, list_option_page: int = None, list_option_page_size: int = None, list_option_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTag/LedgerTagAccount"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/LedgerTagAccount"
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

    def api_ledger_tag__get_ledger_account_list_get__api__fiscal_fiscal_id__ledger_tag__ledger_account(self, fiscal_id: str, list_option_show_deactivated: bool = None, list_option_page: int = None, list_option_page_size: int = None, list_option_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTag/LedgerAccount"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/LedgerAccount"
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

    def api_ledger_tag__get_history_get__api__fiscal_fiscal_id__ledger_tag__history(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTag/History"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/History"
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

    def api_ledger_tag__get_suggestion_get__api__fiscal_fiscal_id__ledger_tag__suggestion(self, fiscal_id: str, ledger_account: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTag/Suggestion"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/Suggestion"
        params: Dict[str, Any] = {}
        if ledger_account is not None:
            params['ledgerAccount'] = ledger_account
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

    def api_ledger_tag_group__get_get__api__fiscal_fiscal_id__ledger_tag_group(self, fiscal_id: str, ledger_account: str = None, query_string: str = None, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTagGroup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTagGroup"
        params: Dict[str, Any] = {}
        if ledger_account is not None:
            params['ledgerAccount'] = ledger_account
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

    def api_ledger_tag_group__post_post__api__fiscal_fiscal_id__ledger_tag_group(self, ledger_tag_group: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/LedgerTagGroup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTagGroup"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=ledger_tag_group, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag_group__get_get__api__fiscal_fiscal_id__ledger_tag_group_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTagGroup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTagGroup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag_group__put_put__api__fiscal_fiscal_id__ledger_tag_group_id(self, ledger_tag_group: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/LedgerTagGroup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTagGroup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=ledger_tag_group, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag_group__delete_delete__api__fiscal_fiscal_id__ledger_tag_group_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/LedgerTagGroup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTagGroup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_invoice_setup__get_get__api__fiscal_fiscal_id__order_invoice_setup(self, fiscal_id: str, query_string: str = None, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderInvoiceSetup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderInvoiceSetup"
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

    def api_order_invoice_setup__post_post__api__fiscal_fiscal_id__order_invoice_setup(self, setup: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderInvoiceSetup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderInvoiceSetup"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=setup, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_invoice_setup__get_get__api__fiscal_fiscal_id__order_invoice_setup_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderInvoiceSetup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderInvoiceSetup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_invoice_setup__put_put__api__fiscal_fiscal_id__order_invoice_setup_id(self, setup: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/OrderInvoiceSetup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderInvoiceSetup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=setup, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_invoice_setup__delete_delete__api__fiscal_fiscal_id__order_invoice_setup_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/OrderInvoiceSetup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderInvoiceSetup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_invoice_setup__get_by_order_get__api__fiscal_fiscal_id__order_id__invoice_setup(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Order/{id}/InvoiceSetup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Order/{id}/InvoiceSetup"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_price_margin__get_get__api__fiscal_fiscal_id__order_price_margin(self, fiscal_id: str, query_string: str = None, include_defaults: bool = None, order_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderPriceMargin"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderPriceMargin"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if include_defaults is not None:
            params['includeDefaults'] = include_defaults
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

    def api_order_price_margin__post_post__api__fiscal_fiscal_id__order_price_margin(self, margin: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderPriceMargin"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderPriceMargin"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=margin, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_price_margin__get_get__api__fiscal_fiscal_id__order_price_margin_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderPriceMargin/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderPriceMargin/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_price_margin__put_put__api__fiscal_fiscal_id__order_price_margin_id(self, margin: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/OrderPriceMargin/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderPriceMargin/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=margin, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_price_margin__delete_delete__api__fiscal_fiscal_id__order_price_margin_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/OrderPriceMargin/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderPriceMargin/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_post_preview__get_order_task_post_preview_get__api__fiscal_fiscal_id__voucher_preview_id__order_task_post_preview(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VoucherPreview/{id}/OrderTaskPostPreview"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VoucherPreview/{id}/OrderTaskPostPreview"
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

    def api_order_task_post_preview__get_get__api__fiscal_fiscal_id__order_task_post_preview_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/OrderTaskPostPreview/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskPostPreview/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_post_preview__put_put__api__fiscal_fiscal_id__order_task_post_preview_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/OrderTaskPostPreview/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskPostPreview/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_post_preview__delete_delete__api__fiscal_fiscal_id__order_task_post_preview_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/OrderTaskPostPreview/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskPostPreview/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_order_task_post_preview__post_post__api__fiscal_fiscal_id__order_task_post_preview(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/OrderTaskPostPreview"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/OrderTaskPostPreview"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_partner_post_payment__get_by_bank_export_list_get__api__fiscal_fiscal_id__bank_export_bank_export_id__partner_post_payment(self, bank_export_id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/BankExport/{bankExportId}/PartnerPostPayment"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BankExport/{bank_export_id}/PartnerPostPayment"
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

    def api_payment__get_partner_payment_get__api__fiscal_fiscal_id__payment__partner_payment(self, calculated_by: int, fiscal_id: str, filter_payment_mean_type: str = None, filter_supplier_partner_ids: list = None, context_id: int = None, include_transferred: bool = None, is_parked: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Payment/PartnerPayment"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Payment/PartnerPayment"
        params: Dict[str, Any] = {}
        if calculated_by is not None:
            params['calculatedBy'] = calculated_by
        if filter_payment_mean_type is not None:
            params['filterPaymentMeanType'] = filter_payment_mean_type
        if filter_supplier_partner_ids is not None:
            params['filterSupplierPartnerIds'] = filter_supplier_partner_ids
        if context_id is not None:
            params['contextId'] = context_id
        if include_transferred is not None:
            params['includeTransferred'] = include_transferred
        if is_parked is not None:
            params['isParked'] = is_parked
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

    def api_payment__get_get__api__fiscal_fiscal_id__payment_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Payment/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Payment/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_payment__get_unsettled_partner_post_get__api__fiscal_fiscal_id__partner_id__unsettled_post(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/UnsettledPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/UnsettledPost"
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

    def api_payment__post_export_post__api__fiscal_fiscal_id__payment__export(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Payment/Export"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Payment/Export"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_payment__delete_settlement_delete__api__fiscal_fiscal_id__payment__settlment_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Payment/Settlment/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Payment/Settlment/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_payment__delete_partial_settlements_delete__api__fiscal_fiscal_id__payment__partial_settlements_settled_partner_post_id(self, settled_partner_post_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Payment/PartialSettlements/{settledPartnerPostId}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Payment/PartialSettlements/{settled_partner_post_id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_payment__get_payment_suggestion_get__api__fiscal_fiscal_id__payment__unsettled_post(self, query_string: str, fiscal_id: str, per_date: int = None, include_manual_payment: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Payment/UnsettledPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Payment/UnsettledPost"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if per_date is not None:
            params['perDate'] = per_date
        if include_manual_payment is not None:
            params['includeManualPayment'] = include_manual_payment
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

    def api_payment_export_draft__get_partner_payment_by_ids_get__api__fiscal_fiscal_id__payment_export_draft_context_id__by_payment_ids(self, context_id: int, ids: list, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PaymentExportDraft/{contextId}/ByPaymentIds"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PaymentExportDraft/{context_id}/ByPaymentIds"
        params: Dict[str, Any] = {}
        if ids is not None:
            params['ids'] = ids
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_payment_export_draft__put_put__api__fiscal_fiscal_id__payment_export_draft_id(self, data: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/PaymentExportDraft/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PaymentExportDraft/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_payment_means__get_get__api__fiscal_fiscal_id__payment_means(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PaymentMeans"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PaymentMeans"
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

    def api_payment_means__post_post__api__fiscal_fiscal_id__payment_means(self, payment_means: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/PaymentMeans"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PaymentMeans"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=payment_means, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_payment_means__get_get__api__fiscal_fiscal_id__payment_means_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PaymentMeans/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PaymentMeans/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_payment_means__put_put__api__fiscal_fiscal_id__payment_means_id(self, payment_means: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/PaymentMeans/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PaymentMeans/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=payment_means, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_payment_means__delete_delete__api__fiscal_fiscal_id__payment_means_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/PaymentMeans/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PaymentMeans/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_payment_means__get_payment_means_type_get__api__fiscal_fiscal_id__payment_means__payment_means_type(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PaymentMeans/PaymentMeansType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PaymentMeans/PaymentMeansType"
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

    def api_payment_means__get_payment_means_type_for_supplier_get__api__fiscal_fiscal_id__payment_means__payment_means_type_data__supplier(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PaymentMeans/PaymentMeansTypeData/Supplier"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PaymentMeans/PaymentMeansTypeData/Supplier"
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

    def api_payment_means__get_supplier_payment_means_type_list_get__api__fiscal_fiscal_id__payment_means__payment_means_type__supplier__select(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PaymentMeans/PaymentMeansType/Supplier/Select"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PaymentMeans/PaymentMeansType/Supplier/Select"
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

    def api_payment_means__get_payment_identification_layouts_list_get__api__fiscal_fiscal_id__payment_means__payment_identification_layouts(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PaymentMeans/PaymentIdentificationLayouts"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PaymentMeans/PaymentIdentificationLayouts"
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

    def api_payment_means__get_payment_layout_example_get__api__fiscal_fiscal_id__payment_means__get_payment_layout_example(self, payment_means_type: str, payment_identification_layout: str, account_number_length: int, invoice_number_length: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PaymentMeans/GetPaymentLayoutExample"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PaymentMeans/GetPaymentLayoutExample"
        params: Dict[str, Any] = {}
        if payment_means_type is not None:
            params['paymentMeansType'] = payment_means_type
        if payment_identification_layout is not None:
            params['paymentIdentificationLayout'] = payment_identification_layout
        if account_number_length is not None:
            params['accountNumberLength'] = account_number_length
        if invoice_number_length is not None:
            params['invoiceNumberLength'] = invoice_number_length
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_primo_article_post__get_get__api__fiscal_fiscal_id__primo_article_post_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PrimoArticlePost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PrimoArticlePost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_primo_article_post__put_put__api__fiscal_fiscal_id__primo_article_post_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/PrimoArticlePost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PrimoArticlePost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_primo_article_post__delete_delete__api__fiscal_fiscal_id__primo_article_post_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/PrimoArticlePost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PrimoArticlePost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_primo_article_post__post_post__api__fiscal_fiscal_id__primo_article_post(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/PrimoArticlePost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PrimoArticlePost"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_primo_article_post__get_primo_article_post_list_get__api__fiscal_fiscal_id__fiscal_period_id__primo_article_post(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalPeriod/{id}/PrimoArticlePost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalPeriod/{id}/PrimoArticlePost"
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

    def api_primo_article_post__put_clear_all_put__api__fiscal_fiscal_id__fiscal_period_id__primo_article_post(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/FiscalPeriod/{id}/PrimoArticlePost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalPeriod/{id}/PrimoArticlePost"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_primo_article_post__post_multiple_post__api__fiscal_fiscal_id__fiscal_period_id__primo_article_post(self, id: int, posts: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/FiscalPeriod/{id}/PrimoArticlePost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalPeriod/{id}/PrimoArticlePost"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=posts, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_primo_article_post__delete_all_delete__api__fiscal_fiscal_id__fiscal_period_id__primo_article_post(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/FiscalPeriod/{id}/PrimoArticlePost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalPeriod/{id}/PrimoArticlePost"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_primo_ledger_post__get_get__api__fiscal_fiscal_id__primo_ledger_post_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PrimoLedgerPost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PrimoLedgerPost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_primo_ledger_post__put_put__api__fiscal_fiscal_id__primo_ledger_post_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/PrimoLedgerPost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PrimoLedgerPost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_primo_ledger_post__delete_delete__api__fiscal_fiscal_id__primo_ledger_post_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/PrimoLedgerPost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PrimoLedgerPost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_primo_ledger_post__post_post__api__fiscal_fiscal_id__primo_ledger_post(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/PrimoLedgerPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PrimoLedgerPost"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_primo_ledger_post__get_by_fiscal_period_list_get__api__fiscal_fiscal_id__fiscal_period_id__primo_ledger_post(self, id: int, ledger_account: str, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalPeriod/{id}/PrimoLedgerPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalPeriod/{id}/PrimoLedgerPost"
        params: Dict[str, Any] = {}
        if ledger_account is not None:
            params['ledgerAccount'] = ledger_account
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

    def api_primo_partner_post__get_get__api__fiscal_fiscal_id__primo_partner_post_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PrimoPartnerPost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PrimoPartnerPost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_primo_partner_post__put_put__api__fiscal_fiscal_id__primo_partner_post_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/PrimoPartnerPost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PrimoPartnerPost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_primo_partner_post__delete_delete__api__fiscal_fiscal_id__primo_partner_post_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/PrimoPartnerPost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PrimoPartnerPost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_primo_partner_post__post_post__api__fiscal_fiscal_id__primo_partner_post(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/PrimoPartnerPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PrimoPartnerPost"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_primo_partner_post__get_primo_partner_post_list_get__api__fiscal_fiscal_id__fiscal_period_id__primo_partner_post(self, id: int, context_type: str, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/FiscalPeriod/{id}/PrimoPartnerPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/FiscalPeriod/{id}/PrimoPartnerPost"
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

    def api_purpose__get_get__api__fiscal_fiscal_id__purpose(self, fiscal_id: str, query_string: str = None, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Purpose"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Purpose"
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

    def api_purpose__post_post__api__fiscal_fiscal_id__purpose(self, purpose: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Purpose"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Purpose"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=purpose, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_purpose__get_get__api__fiscal_fiscal_id__purpose_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Purpose/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Purpose/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_purpose__put_put__api__fiscal_fiscal_id__purpose_id(self, purpose: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Purpose/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Purpose/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=purpose, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_purpose__delete_delete__api__fiscal_fiscal_id__purpose_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Purpose/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Purpose/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_resource_authorization_context__get_list_get__api__fiscal_fiscal_id__resource_authorization_context(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ResourceAuthorizationContext"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ResourceAuthorizationContext"
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

    def api_resource_authorization_context__post_post__api__fiscal_fiscal_id__resource_authorization_context(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ResourceAuthorizationContext"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ResourceAuthorizationContext"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_resource_authorization_context__get_get__api__fiscal_fiscal_id__resource_authorization_context_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ResourceAuthorizationContext/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ResourceAuthorizationContext/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_resource_authorization_context__put_put__api__fiscal_fiscal_id__resource_authorization_context_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ResourceAuthorizationContext/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ResourceAuthorizationContext/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_resource_authorization_context__delete_delete__api__fiscal_fiscal_id__resource_authorization_context_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ResourceAuthorizationContext/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ResourceAuthorizationContext/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_theme__put_change_theme_put__api__fiscal_fiscal_id__change_theme(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ChangeTheme"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ChangeTheme"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_article_post_by_article_list_get__api__fiscal_fiscal_id__transaction__article_id__post(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/Article/{id}/Post"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/Article/{id}/Post"
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

    def api_transaction__get_partner_statistics_report_list_get__api__fiscal_fiscal_id__transaction__partner_statistics_report(self, fiscal_id: str, date_from: int = None, date_to: int = None, partner_id: int = None, article_group_id: int = None, context_type: str = None, department_id: int = None, bearer_id: int = None, purpose_id: int = None, limit_to_department: bool = None, limit_to_bearer: bool = None, limit_to_purpose: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/PartnerStatisticsReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/PartnerStatisticsReport"
        params: Dict[str, Any] = {}
        if date_from is not None:
            params['dateFrom'] = date_from
        if date_to is not None:
            params['dateTo'] = date_to
        if partner_id is not None:
            params['partnerId'] = partner_id
        if article_group_id is not None:
            params['articleGroupId'] = article_group_id
        if context_type is not None:
            params['contextType'] = context_type
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

    def api_transaction__get_partner_article_statistics_report_list_get__api__fiscal_fiscal_id__transaction__partner_article_statistics_report(self, fiscal_id: str, date_from: int = None, date_to: int = None, partner_id: int = None, article_group_id: int = None, article_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/PartnerArticleStatisticsReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/PartnerArticleStatisticsReport"
        params: Dict[str, Any] = {}
        if date_from is not None:
            params['dateFrom'] = date_from
        if date_to is not None:
            params['dateTo'] = date_to
        if partner_id is not None:
            params['partnerId'] = partner_id
        if article_group_id is not None:
            params['articleGroupId'] = article_group_id
        if article_id is not None:
            params['articleId'] = article_id
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

    def api_transaction__get_article_post_report_get__api__fiscal_fiscal_id__transaction__article_post_report(self, fiscal_id: str, date_from: int = None, date_to: int = None, article_id: int = None, location_id: int = None, warehouse_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/ArticlePostReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/ArticlePostReport"
        params: Dict[str, Any] = {}
        if date_from is not None:
            params['dateFrom'] = date_from
        if date_to is not None:
            params['dateTo'] = date_to
        if article_id is not None:
            params['articleId'] = article_id
        if location_id is not None:
            params['locationId'] = location_id
        if warehouse_id is not None:
            params['warehouseId'] = warehouse_id
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

    def api_transaction__get_ongoing_order_report_get__api__fiscal_fiscal_id__transaction__ongoing_order_report(self, fiscal_id: str, cost_type_id: list = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, filter_partner_id: int = None, filter_limit_to_partner: bool = None, filter_department_id: int = None, filter_limit_to_department: bool = None, filter_bearer_id: int = None, filter_limit_to_bearer: bool = None, filter_purpose_id: int = None, filter_limit_to_purpose: bool = None, filter_is_fully_invoiced: bool = None, filter_date_from: int = None, filter_date_to: int = None, filter_responsible_id: int = None, filter_limit_to_responsible: bool = None, filter_limit_to_cost_type: bool = None, filter_last_invoice_date_from: int = None, filter_last_invoice_date_to: int = None, filter_order_status_id: int = None, filter_limit_to_order_status: bool = None, filter_invoice_period_from: int = None, filter_invoice_period_to: int = None, filter_hide_empty_orders: bool = None, filter_order_id: int = None, filter_limit_to_project: bool = None, filter_project_id: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/OngoingOrderReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/OngoingOrderReport"
        params: Dict[str, Any] = {}
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
        if filter_is_fully_invoiced is not None:
            params['filter.isFullyInvoiced'] = filter_is_fully_invoiced
        if filter_date_from is not None:
            params['filter.dateFrom'] = filter_date_from
        if filter_date_to is not None:
            params['filter.dateTo'] = filter_date_to
        if filter_responsible_id is not None:
            params['filter.responsibleId'] = filter_responsible_id
        if filter_limit_to_responsible is not None:
            params['filter.limitToResponsible'] = filter_limit_to_responsible
        if filter_limit_to_cost_type is not None:
            params['filter.limitToCostType'] = filter_limit_to_cost_type
        if filter_last_invoice_date_from is not None:
            params['filter.lastInvoiceDateFrom'] = filter_last_invoice_date_from
        if filter_last_invoice_date_to is not None:
            params['filter.lastInvoiceDateTo'] = filter_last_invoice_date_to
        if filter_order_status_id is not None:
            params['filter.orderStatusId'] = filter_order_status_id
        if filter_limit_to_order_status is not None:
            params['filter.limitToOrderStatus'] = filter_limit_to_order_status
        if filter_invoice_period_from is not None:
            params['filter.invoicePeriodFrom'] = filter_invoice_period_from
        if filter_invoice_period_to is not None:
            params['filter.invoicePeriodTo'] = filter_invoice_period_to
        if filter_hide_empty_orders is not None:
            params['filter.hideEmptyOrders'] = filter_hide_empty_orders
        if filter_order_id is not None:
            params['filter.orderId'] = filter_order_id
        if filter_limit_to_project is not None:
            params['filter.limitToProject'] = filter_limit_to_project
        if filter_project_id is not None:
            params['filter.projectId'] = filter_project_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_ongoing_order_historic_report_get__api__fiscal_fiscal_id__transaction__ongoing_order_historic_report(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, filter_partner_id: int = None, filter_limit_to_partner: bool = None, filter_bearer_id: int = None, filter_limit_to_bearer: bool = None, filter_department_id: int = None, filter_limit_to_department: bool = None, filter_purpose_id: int = None, filter_limit_to_purpose: bool = None, filter_responsible_id: int = None, filter_limit_to_responsible: bool = None, filter_cost_type_id: int = None, filter_limit_to_cost_type: bool = None, filter_open_per: int = None, filter_order_status_id: int = None, filter_limit_to_order_status: bool = None, filter_project_id: int = None, filter_limit_to_project: bool = None, filter_order_id: int = None, filter_report_layout_id: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/OngoingOrderHistoricReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/OngoingOrderHistoricReport"
        params: Dict[str, Any] = {}
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        if filter_partner_id is not None:
            params['filter.partnerId'] = filter_partner_id
        if filter_limit_to_partner is not None:
            params['filter.limitToPartner'] = filter_limit_to_partner
        if filter_bearer_id is not None:
            params['filter.bearerId'] = filter_bearer_id
        if filter_limit_to_bearer is not None:
            params['filter.limitToBearer'] = filter_limit_to_bearer
        if filter_department_id is not None:
            params['filter.departmentId'] = filter_department_id
        if filter_limit_to_department is not None:
            params['filter.limitToDepartment'] = filter_limit_to_department
        if filter_purpose_id is not None:
            params['filter.purposeId'] = filter_purpose_id
        if filter_limit_to_purpose is not None:
            params['filter.limitToPurpose'] = filter_limit_to_purpose
        if filter_responsible_id is not None:
            params['filter.responsibleId'] = filter_responsible_id
        if filter_limit_to_responsible is not None:
            params['filter.limitToResponsible'] = filter_limit_to_responsible
        if filter_cost_type_id is not None:
            params['filter.costTypeId'] = filter_cost_type_id
        if filter_limit_to_cost_type is not None:
            params['filter.limitToCostType'] = filter_limit_to_cost_type
        if filter_open_per is not None:
            params['filter.openPer'] = filter_open_per
        if filter_order_status_id is not None:
            params['filter.orderStatusId'] = filter_order_status_id
        if filter_limit_to_order_status is not None:
            params['filter.limitToOrderStatus'] = filter_limit_to_order_status
        if filter_project_id is not None:
            params['filter.projectId'] = filter_project_id
        if filter_limit_to_project is not None:
            params['filter.limitToProject'] = filter_limit_to_project
        if filter_order_id is not None:
            params['filter.orderId'] = filter_order_id
        if filter_report_layout_id is not None:
            params['filter.reportLayoutId'] = filter_report_layout_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_order_budget_report_list_get__api__fiscal_fiscal_id__transaction__order_budget_report(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, filter_open_per: int = None, filter_order_status_id: int = None, filter_order_id: int = None, filter_limit_to_order: bool = None, filter_project_id: int = None, filter_limit_to_project: bool = None, filter_limit_to_order_status: bool = None, filter_responsible_id: int = None, filter_limit_to_responsible: bool = None, filter_partner_id: int = None, filter_limit_to_partner: bool = None, filter_department_id: int = None, filter_limit_to_department: bool = None, filter_bearer_id: int = None, filter_limit_to_bearer: bool = None, filter_purpose_id: int = None, filter_limit_to_purpose: bool = None, filter_is_fully_invoiced: bool = None, filter_last_invoice_date_from: int = None, filter_last_invoice_date_to: int = None, filter_report_layout_id: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/OrderBudgetReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/OrderBudgetReport"
        params: Dict[str, Any] = {}
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        if filter_open_per is not None:
            params['filter.openPer'] = filter_open_per
        if filter_order_status_id is not None:
            params['filter.orderStatusId'] = filter_order_status_id
        if filter_order_id is not None:
            params['filter.orderId'] = filter_order_id
        if filter_limit_to_order is not None:
            params['filter.limitToOrder'] = filter_limit_to_order
        if filter_project_id is not None:
            params['filter.projectId'] = filter_project_id
        if filter_limit_to_project is not None:
            params['filter.limitToProject'] = filter_limit_to_project
        if filter_limit_to_order_status is not None:
            params['filter.limitToOrderStatus'] = filter_limit_to_order_status
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
        if filter_is_fully_invoiced is not None:
            params['filter.isFullyInvoiced'] = filter_is_fully_invoiced
        if filter_last_invoice_date_from is not None:
            params['filter.lastInvoiceDateFrom'] = filter_last_invoice_date_from
        if filter_last_invoice_date_to is not None:
            params['filter.lastInvoiceDateTo'] = filter_last_invoice_date_to
        if filter_report_layout_id is not None:
            params['filter.reportLayoutId'] = filter_report_layout_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_order_budget_report_list_get__api__fiscal_fiscal_id__transaction__project_budget_report(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, filter_statement_date: int = None, filter_is_closed: bool = None, filter_project_id: int = None, filter_limit_to_project: bool = None, filter_project_group_id: int = None, filter_limit_to_project_group: bool = None, filter_project_status_id: int = None, filter_limit_to_project_status: bool = None, filter_responsible_id: int = None, filter_limit_to_responsible: bool = None, filter_partner_id: int = None, filter_limit_to_partner: bool = None, filter_department_id: int = None, filter_limit_to_department: bool = None, filter_bearer_id: int = None, filter_limit_to_bearer: bool = None, filter_purpose_id: int = None, filter_limit_to_purpose: bool = None, filter_report_layout_id: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/ProjectBudgetReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/ProjectBudgetReport"
        params: Dict[str, Any] = {}
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        if filter_statement_date is not None:
            params['filter.statementDate'] = filter_statement_date
        if filter_is_closed is not None:
            params['filter.isClosed'] = filter_is_closed
        if filter_project_id is not None:
            params['filter.projectId'] = filter_project_id
        if filter_limit_to_project is not None:
            params['filter.limitToProject'] = filter_limit_to_project
        if filter_project_group_id is not None:
            params['filter.projectGroupId'] = filter_project_group_id
        if filter_limit_to_project_group is not None:
            params['filter.limitToProjectGroup'] = filter_limit_to_project_group
        if filter_project_status_id is not None:
            params['filter.projectStatusId'] = filter_project_status_id
        if filter_limit_to_project_status is not None:
            params['filter.limitToProjectStatus'] = filter_limit_to_project_status
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
        if filter_report_layout_id is not None:
            params['filter.reportLayoutId'] = filter_report_layout_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_detailed_order_task_summary_report_get__api__fiscal_fiscal_id__transaction__detailed_order_task_summary_report(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, filter_invoice_period_from: int = None, filter_invoice_period_to: int = None, filter_cost_period_from: int = None, filter_cost_period_to: int = None, filter_is_invoiced: bool = None, filter_order_task_status_id: int = None, filter_limit_to_order_task_status: bool = None, filter_limit_to_responsible: bool = None, filter_responsible_id: int = None, filter_department_id: int = None, filter_limit_to_department: bool = None, filter_bearer_id: int = None, filter_limit_to_bearer: bool = None, filter_purpose_id: int = None, filter_limit_to_purpose: bool = None, filter_report_layout_id: int = None, filter_order_id: int = None, filter_project_id: int = None, filter_limit_to_project: bool = None, filter_partner_id: int = None, filter_hide_empty_tasks: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/DetailedOrderTaskSummaryReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/DetailedOrderTaskSummaryReport"
        params: Dict[str, Any] = {}
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        if filter_invoice_period_from is not None:
            params['filter.invoicePeriodFrom'] = filter_invoice_period_from
        if filter_invoice_period_to is not None:
            params['filter.invoicePeriodTo'] = filter_invoice_period_to
        if filter_cost_period_from is not None:
            params['filter.costPeriodFrom'] = filter_cost_period_from
        if filter_cost_period_to is not None:
            params['filter.costPeriodTo'] = filter_cost_period_to
        if filter_is_invoiced is not None:
            params['filter.isInvoiced'] = filter_is_invoiced
        if filter_order_task_status_id is not None:
            params['filter.orderTaskStatusId'] = filter_order_task_status_id
        if filter_limit_to_order_task_status is not None:
            params['filter.limitToOrderTaskStatus'] = filter_limit_to_order_task_status
        if filter_limit_to_responsible is not None:
            params['filter.limitToResponsible'] = filter_limit_to_responsible
        if filter_responsible_id is not None:
            params['filter.responsibleId'] = filter_responsible_id
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
        if filter_report_layout_id is not None:
            params['filter.reportLayoutId'] = filter_report_layout_id
        if filter_order_id is not None:
            params['filter.orderId'] = filter_order_id
        if filter_project_id is not None:
            params['filter.projectId'] = filter_project_id
        if filter_limit_to_project is not None:
            params['filter.limitToProject'] = filter_limit_to_project
        if filter_partner_id is not None:
            params['filter.partnerId'] = filter_partner_id
        if filter_hide_empty_tasks is not None:
            params['filter.hideEmptyTasks'] = filter_hide_empty_tasks
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_detailed_order_task_summary_report_list_post__api__fiscal_fiscal_id__transaction__render_detailed_order_task_summary_report(self, filter: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderDetailedOrderTaskSummaryReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderDetailedOrderTaskSummaryReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=filter, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_eu_sales_without_vat_get__api__fiscal_fiscal_id__transaction_eu_sales_without_vat(self, date_from: int, date_to: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/EUSalesWithoutVAT"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/EUSalesWithoutVAT"
        params: Dict[str, Any] = {}
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

    def api_transaction__get_article_stock_report_get__api__fiscal_fiscal_id__transaction__article_stock_report(self, fiscal_id: str, article_group_id: int = None, location_id: int = None, warehouse_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/ArticleStockReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/ArticleStockReport"
        params: Dict[str, Any] = {}
        if article_group_id is not None:
            params['articleGroupId'] = article_group_id
        if location_id is not None:
            params['locationId'] = location_id
        if warehouse_id is not None:
            params['warehouseId'] = warehouse_id
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

    def api_transaction__get_article_stock_statistics_report_get__api__fiscal_fiscal_id__transaction__article_stock_statistics_report(self, date_from: int, date_to: int, fiscal_id: str, article_id: int = None, article_group_id: int = None, location_id: int = None, warehouse_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/ArticleStockStatisticsReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/ArticleStockStatisticsReport"
        params: Dict[str, Any] = {}
        if date_from is not None:
            params['dateFrom'] = date_from
        if date_to is not None:
            params['dateTo'] = date_to
        if article_id is not None:
            params['articleId'] = article_id
        if article_group_id is not None:
            params['articleGroupId'] = article_group_id
        if location_id is not None:
            params['locationId'] = location_id
        if warehouse_id is not None:
            params['warehouseId'] = warehouse_id
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

    def api_transaction__get_historic_stock_value_report_get__api__fiscal_fiscal_id__transaction__historic_stock_value_report(self, fiscal_id: str, article_group_id: int = None, fiscal_date: int = None, location_id: int = None, warehouse_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/HistoricStockValueReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/HistoricStockValueReport"
        params: Dict[str, Any] = {}
        if article_group_id is not None:
            params['articleGroupId'] = article_group_id
        if fiscal_date is not None:
            params['fiscalDate'] = fiscal_date
        if location_id is not None:
            params['locationId'] = location_id
        if warehouse_id is not None:
            params['warehouseId'] = warehouse_id
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

    def api_transaction__get_article_group_statistic_report_get__api__fiscal_fiscal_id__transaction__article_group_statistic_report(self, article_group_id: int, fiscal_id: str, fiscal_period_id: int = None, end_date: int = None, department_id: int = None, bearer_id: int = None, purpose_id: int = None, limit_to_department: bool = None, limit_to_bearer: bool = None, limit_to_purpose: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/ArticleGroupStatisticReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/ArticleGroupStatisticReport"
        params: Dict[str, Any] = {}
        if article_group_id is not None:
            params['articleGroupId'] = article_group_id
        if fiscal_period_id is not None:
            params['fiscalPeriodId'] = fiscal_period_id
        if end_date is not None:
            params['endDate'] = end_date
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

    def api_transaction__get_ledger_tag_statistic_report_get__api__fiscal_fiscal_id__transaction__ledger_tag_statistic_report(self, ledger_tag_id: int, fiscal_id: str, fiscal_period_id: int = None, end_date: int = None, department_id: int = None, bearer_id: int = None, purpose_id: int = None, limit_to_department: bool = None, limit_to_bearer: bool = None, limit_to_purpose: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/LedgerTagStatisticReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/LedgerTagStatisticReport"
        params: Dict[str, Any] = {}
        if ledger_tag_id is not None:
            params['ledgerTagId'] = ledger_tag_id
        if fiscal_period_id is not None:
            params['fiscalPeriodId'] = fiscal_period_id
        if end_date is not None:
            params['endDate'] = end_date
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

    def api_transaction__get_article_margin_report_get__api__fiscal_fiscal_id__transaction__article_margin_report(self, fiscal_date_from: int, fiscal_date_to: int, fiscal_id: str, article_id: int = None, article_group_id: int = None, fiscal_period_id: int = None, department_id: int = None, bearer_id: int = None, purpose_id: int = None, limit_to_department: bool = None, limit_to_bearer: bool = None, limit_to_purpose: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/ArticleMarginReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/ArticleMarginReport"
        params: Dict[str, Any] = {}
        if fiscal_date_from is not None:
            params['fiscalDateFrom'] = fiscal_date_from
        if fiscal_date_to is not None:
            params['fiscalDateTo'] = fiscal_date_to
        if article_id is not None:
            params['articleId'] = article_id
        if article_group_id is not None:
            params['articleGroupId'] = article_group_id
        if fiscal_period_id is not None:
            params['fiscalPeriodId'] = fiscal_period_id
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

    def api_transaction__get_settled_posts_get__api__fiscal_fiscal_id__transaction__settlement_id__post(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/Settlement/{id}/Post"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/Settlement/{id}/Post"
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

    def api_transaction__get_partner_post_report_get__api__fiscal_fiscal_id__transaction__partner_post_report(self, date_from: int, date_to: int, fiscal_id: str, partner_id: int = None, context_type: str = None, is_settled: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/PartnerPostReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/PartnerPostReport"
        params: Dict[str, Any] = {}
        if date_from is not None:
            params['dateFrom'] = date_from
        if date_to is not None:
            params['dateTo'] = date_to
        if partner_id is not None:
            params['partnerId'] = partner_id
        if context_type is not None:
            params['contextType'] = context_type
        if is_settled is not None:
            params['isSettled'] = is_settled
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

    def api_transaction__get_partner_balance_report_get__api__fiscal_fiscal_id__transaction__partner_balance_report(self, calculated_by: int, fiscal_id: str, account_number_from: int = None, account_number_to: int = None, saldo_from: float = None, saldo_to: float = None, context_type: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/PartnerBalanceReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/PartnerBalanceReport"
        params: Dict[str, Any] = {}
        if calculated_by is not None:
            params['calculatedBy'] = calculated_by
        if account_number_from is not None:
            params['accountNumberFrom'] = account_number_from
        if account_number_to is not None:
            params['accountNumberTo'] = account_number_to
        if saldo_from is not None:
            params['saldoFrom'] = saldo_from
        if saldo_to is not None:
            params['saldoTo'] = saldo_to
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

    def api_transaction__get_partner_saldo_total_balance_by_context_type_get__api__fiscal_fiscal_id__transaction__partner_saldo_total_balance_by_context_type(self, calculated_by: int, fiscal_id: str, account_number_from: int = None, account_number_to: int = None, context_type: str = None, over_due_only: bool = None, non_settled_only: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/PartnerSaldoTotalBalanceByContextType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/PartnerSaldoTotalBalanceByContextType"
        params: Dict[str, Any] = {}
        if calculated_by is not None:
            params['calculatedBy'] = calculated_by
        if account_number_from is not None:
            params['accountNumberFrom'] = account_number_from
        if account_number_to is not None:
            params['accountNumberTo'] = account_number_to
        if context_type is not None:
            params['contextType'] = context_type
        if over_due_only is not None:
            params['overDueOnly'] = over_due_only
        if non_settled_only is not None:
            params['nonSettledOnly'] = non_settled_only
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_partner_saldo_total_balance_by_partner_post_type_get__api__fiscal_fiscal_id__transaction__partner_saldo_total_balance_by_partner_post_type(self, calculated_by: int, partner_post_type: str, fiscal_id: str, account_number_from: int = None, account_number_to: int = None, over_due_only: bool = None, non_settled_only: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/PartnerSaldoTotalBalanceByPartnerPostType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/PartnerSaldoTotalBalanceByPartnerPostType"
        params: Dict[str, Any] = {}
        if calculated_by is not None:
            params['calculatedBy'] = calculated_by
        if partner_post_type is not None:
            params['partnerPostType'] = partner_post_type
        if account_number_from is not None:
            params['accountNumberFrom'] = account_number_from
        if account_number_to is not None:
            params['accountNumberTo'] = account_number_to
        if over_due_only is not None:
            params['overDueOnly'] = over_due_only
        if non_settled_only is not None:
            params['nonSettledOnly'] = non_settled_only
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_partner_saldo_by_unit_report_get__api__fiscal_fiscal_id__transaction__partner_saldo_by_unit_report_list(self, calculated_by: int, fiscal_id: str, account_number_from: int = None, account_number_to: int = None, context_type: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/PartnerSaldoByUnitReportList"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/PartnerSaldoByUnitReportList"
        params: Dict[str, Any] = {}
        if calculated_by is not None:
            params['calculatedBy'] = calculated_by
        if account_number_from is not None:
            params['accountNumberFrom'] = account_number_from
        if account_number_to is not None:
            params['accountNumberTo'] = account_number_to
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

    def api_transaction__get_partner_saldo_by_unit_report_totals_get__api__fiscal_fiscal_id__transaction__partner_saldo_by_unit_report_totals(self, calculated_by: int, fiscal_id: str, account_number_from: int = None, account_number_to: int = None, context_type: str = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/PartnerSaldoByUnitReportTotals"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/PartnerSaldoByUnitReportTotals"
        params: Dict[str, Any] = {}
        if calculated_by is not None:
            params['calculatedBy'] = calculated_by
        if account_number_from is not None:
            params['accountNumberFrom'] = account_number_from
        if account_number_to is not None:
            params['accountNumberTo'] = account_number_to
        if context_type is not None:
            params['contextType'] = context_type
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_partner_balance_by_due_date_report_get__api__fiscal_fiscal_id__transaction__partner_balance_by_due_date_report(self, calculated_by: int, interval: int, schedule_method: str, fiscal_id: str, context_type: str = None, statement_date: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/PartnerBalanceByDueDateReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/PartnerBalanceByDueDateReport"
        params: Dict[str, Any] = {}
        if calculated_by is not None:
            params['calculatedBy'] = calculated_by
        if interval is not None:
            params['interval'] = interval
        if schedule_method is not None:
            params['scheduleMethod'] = schedule_method
        if context_type is not None:
            params['contextType'] = context_type
        if statement_date is not None:
            params['statementDate'] = statement_date
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

    def api_transaction__get_partner_balance_by_due_date_report_totals_get__api__fiscal_fiscal_id__transaction__partner_balance_by_due_date_report_totals(self, calculated_by: int, interval: int, schedule_method: str, fiscal_id: str, context_type: str = None, statement_date: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/PartnerBalanceByDueDateReportTotals"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/PartnerBalanceByDueDateReportTotals"
        params: Dict[str, Any] = {}
        if calculated_by is not None:
            params['calculatedBy'] = calculated_by
        if interval is not None:
            params['interval'] = interval
        if schedule_method is not None:
            params['scheduleMethod'] = schedule_method
        if context_type is not None:
            params['contextType'] = context_type
        if statement_date is not None:
            params['statementDate'] = statement_date
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_ledger_post_get__api__fiscal_fiscal_id__transaction__ledger_post_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/LedgerPost/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/LedgerPost/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_ledger_post_report_get__api__fiscal_fiscal_id__transaction__ledger_post_report(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, data_date_from: int = None, data_date_to: int = None, data_ledger_account: str = None, data_ledger_tag_id: int = None, data_limit_to_ledger_tag: bool = None, data_article_group_id: int = None, data_vat_id: int = None, data_department_id: int = None, data_bearer_id: int = None, data_purpose_id: int = None, data_partner_id: int = None, data_limit_to_article_group: bool = None, data_limit_to_vat: bool = None, data_limit_to_department: bool = None, data_limit_to_bearer: bool = None, data_limit_to_purpose: bool = None, data_limit_to_partner: bool = None, data_voucher_number_from: int = None, data_voucher_number_to: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/LedgerPostReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/LedgerPostReport"
        params: Dict[str, Any] = {}
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        if data_date_from is not None:
            params['data.dateFrom'] = data_date_from
        if data_date_to is not None:
            params['data.dateTo'] = data_date_to
        if data_ledger_account is not None:
            params['data.ledgerAccount'] = data_ledger_account
        if data_ledger_tag_id is not None:
            params['data.ledgerTagId'] = data_ledger_tag_id
        if data_limit_to_ledger_tag is not None:
            params['data.limitToLedgerTag'] = data_limit_to_ledger_tag
        if data_article_group_id is not None:
            params['data.articleGroupId'] = data_article_group_id
        if data_vat_id is not None:
            params['data.vatId'] = data_vat_id
        if data_department_id is not None:
            params['data.departmentId'] = data_department_id
        if data_bearer_id is not None:
            params['data.bearerId'] = data_bearer_id
        if data_purpose_id is not None:
            params['data.purposeId'] = data_purpose_id
        if data_partner_id is not None:
            params['data.partnerId'] = data_partner_id
        if data_limit_to_article_group is not None:
            params['data.limitToArticleGroup'] = data_limit_to_article_group
        if data_limit_to_vat is not None:
            params['data.limitToVat'] = data_limit_to_vat
        if data_limit_to_department is not None:
            params['data.limitToDepartment'] = data_limit_to_department
        if data_limit_to_bearer is not None:
            params['data.limitToBearer'] = data_limit_to_bearer
        if data_limit_to_purpose is not None:
            params['data.limitToPurpose'] = data_limit_to_purpose
        if data_limit_to_partner is not None:
            params['data.limitToPartner'] = data_limit_to_partner
        if data_voucher_number_from is not None:
            params['data.voucherNumberFrom'] = data_voucher_number_from
        if data_voucher_number_to is not None:
            params['data.voucherNumberTo'] = data_voucher_number_to
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_ledger_post_article_specification_get__api__fiscal_fiscal_id__transaction__ledger_post_article_specification(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, data_date_from: int = None, data_date_to: int = None, data_ledger_account: str = None, data_economic_transaction_id: int = None, data_ledger_post_id: int = None, data_article_id: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/LedgerPostArticleSpecification"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/LedgerPostArticleSpecification"
        params: Dict[str, Any] = {}
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        if data_date_from is not None:
            params['data.dateFrom'] = data_date_from
        if data_date_to is not None:
            params['data.dateTo'] = data_date_to
        if data_ledger_account is not None:
            params['data.ledgerAccount'] = data_ledger_account
        if data_economic_transaction_id is not None:
            params['data.economicTransactionId'] = data_economic_transaction_id
        if data_ledger_post_id is not None:
            params['data.ledgerPostId'] = data_ledger_post_id
        if data_article_id is not None:
            params['data.articleId'] = data_article_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_vat_reconciliation_report_get__api__fiscal_fiscal_id__transaction__vat_reconciliation_report(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, data_date_from: int = None, data_date_to: int = None, data_ledger_account: str = None, data_ledger_tag_id: int = None, data_limit_to_ledger_tag: bool = None, data_article_group_id: int = None, data_vat_id: int = None, data_department_id: int = None, data_bearer_id: int = None, data_purpose_id: int = None, data_limit_to_article_group: bool = None, data_limit_to_vat: bool = None, data_limit_to_department: bool = None, data_limit_to_bearer: bool = None, data_limit_to_purpose: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/VatReconciliationReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/VatReconciliationReport"
        params: Dict[str, Any] = {}
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        if data_date_from is not None:
            params['data.dateFrom'] = data_date_from
        if data_date_to is not None:
            params['data.dateTo'] = data_date_to
        if data_ledger_account is not None:
            params['data.ledgerAccount'] = data_ledger_account
        if data_ledger_tag_id is not None:
            params['data.ledgerTagId'] = data_ledger_tag_id
        if data_limit_to_ledger_tag is not None:
            params['data.limitToLedgerTag'] = data_limit_to_ledger_tag
        if data_article_group_id is not None:
            params['data.articleGroupId'] = data_article_group_id
        if data_vat_id is not None:
            params['data.vatId'] = data_vat_id
        if data_department_id is not None:
            params['data.departmentId'] = data_department_id
        if data_bearer_id is not None:
            params['data.bearerId'] = data_bearer_id
        if data_purpose_id is not None:
            params['data.purposeId'] = data_purpose_id
        if data_limit_to_article_group is not None:
            params['data.limitToArticleGroup'] = data_limit_to_article_group
        if data_limit_to_vat is not None:
            params['data.limitToVat'] = data_limit_to_vat
        if data_limit_to_department is not None:
            params['data.limitToDepartment'] = data_limit_to_department
        if data_limit_to_bearer is not None:
            params['data.limitToBearer'] = data_limit_to_bearer
        if data_limit_to_purpose is not None:
            params['data.limitToPurpose'] = data_limit_to_purpose
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_ledger_account_specification_report_get__api__fiscal_fiscal_id__transaction__ledger_account_specification_report(self, fiscal_period_id: int, fiscal_id: str, ledger_account: str = None, article_group_id: int = None, ledger_tag_id: int = None, vat_id: int = None, department_id: int = None, bearer_id: int = None, purpose_id: int = None, limit_to_article_group: bool = None, limit_to_ledger_tag: bool = None, limit_to_vat: bool = None, limit_to_department: bool = None, limit_to_bearer: bool = None, limit_to_purpose: bool = None, accounts_filter_type: str = None, fiscal_period_fiscal_date_from: int = None, fiscal_period_fiscal_date_to: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/LedgerAccountSpecificationReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/LedgerAccountSpecificationReport"
        params: Dict[str, Any] = {}
        if fiscal_period_id is not None:
            params['fiscalPeriodId'] = fiscal_period_id
        if ledger_account is not None:
            params['ledgerAccount'] = ledger_account
        if article_group_id is not None:
            params['articleGroupId'] = article_group_id
        if ledger_tag_id is not None:
            params['ledgerTagId'] = ledger_tag_id
        if vat_id is not None:
            params['vatId'] = vat_id
        if department_id is not None:
            params['departmentId'] = department_id
        if bearer_id is not None:
            params['bearerId'] = bearer_id
        if purpose_id is not None:
            params['purposeId'] = purpose_id
        if limit_to_article_group is not None:
            params['limitToArticleGroup'] = limit_to_article_group
        if limit_to_ledger_tag is not None:
            params['limitToLedgerTag'] = limit_to_ledger_tag
        if limit_to_vat is not None:
            params['limitToVat'] = limit_to_vat
        if limit_to_department is not None:
            params['limitToDepartment'] = limit_to_department
        if limit_to_bearer is not None:
            params['limitToBearer'] = limit_to_bearer
        if limit_to_purpose is not None:
            params['limitToPurpose'] = limit_to_purpose
        if accounts_filter_type is not None:
            params['accountsFilterType'] = accounts_filter_type
        if fiscal_period_fiscal_date_from is not None:
            params['fiscalPeriod.fiscalDateFrom'] = fiscal_period_fiscal_date_from
        if fiscal_period_fiscal_date_to is not None:
            params['fiscalPeriod.fiscalDateTo'] = fiscal_period_fiscal_date_to
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

    def api_transaction__get_article_post_get__api__fiscal_fiscal_id__transaction__article_post(self, fiscal_id: str, article_id: int = None, location_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/ArticlePost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/ArticlePost"
        params: Dict[str, Any] = {}
        if article_id is not None:
            params['articleId'] = article_id
        if location_id is not None:
            params['locationId'] = location_id
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

    def api_transaction__get_article_post_with_variants_get__api__fiscal_fiscal_id__transaction__article_id__article_post_with_variant(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/Article/{id}/ArticlePostWithVariant"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/Article/{id}/ArticlePostWithVariant"
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

    def api_transaction__delete_economic_transaction_delete__api__fiscal_fiscal_id__transaction_id__cancel_economic_transaction(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Transaction/{id}/CancelEconomicTransaction"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/{id}/CancelEconomicTransaction"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__put_economic_transaction_put__api__fiscal_fiscal_id__transaction_id(self, id: int, model: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Transaction/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=model, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_journal_entry_by_transaction_get__api__fiscal_fiscal_id__transaction_id__journal_entry(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/{id}/JournalEntry"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/{id}/JournalEntry"
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

    def api_transaction__get_ledger_post_by_transaction_get__api__fiscal_fiscal_id__transaction_id__ledger_post(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/{id}/LedgerPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/{id}/LedgerPost"
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

    def api_transaction__get_ledger_post_by_settlement_get__api__fiscal_fiscal_id__transaction__settlement_id__ledger_post(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/Settlement/{id}/LedgerPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/Settlement/{id}/LedgerPost"
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

    def api_transaction__get_article_post_by_transaction_get__api__fiscal_fiscal_id__transaction_id__article_post(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/{id}/ArticlePost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/{id}/ArticlePost"
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

    def api_transaction__get_article_post_by_physical_transaction_get__api__fiscal_fiscal_id__transaction__physical_transaction_id__article_post(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/PhysicalTransaction/{id}/ArticlePost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/PhysicalTransaction/{id}/ArticlePost"
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

    def api_transaction__get_partner_post_by_transaction_get__api__fiscal_fiscal_id__transaction_id__partner_post(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/{id}/PartnerPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/{id}/PartnerPost"
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

    def api_transaction__get_partner_post_list_get__api__fiscal_fiscal_id__transaction__partner_post(self, fiscal_id: str, only_open: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/PartnerPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/PartnerPost"
        params: Dict[str, Any] = {}
        if only_open is not None:
            params['onlyOpen'] = only_open
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

    def api_transaction__get_partner_post_by_settlement_get__api__fiscal_fiscal_id__transaction__settlement_id__partner_post(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/Settlement/{id}/PartnerPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/Settlement/{id}/PartnerPost"
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

    def api_transaction__get_ledger_group_data_get__api__fiscal_fiscal_id__transaction__ledger_group_data(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, fiscal_period_fiscal_date_from: int = None, fiscal_period_fiscal_date_to: int = None, filter_bearer_id: list = None, filter_department_id: list = None, filter_purpose_id: list = None, filter_ledger_group: str = None, filter_fiscal_period_id: int = None, filter_ledger_id: int = None, filter_include_simulated_bookkeeping: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/LedgerGroupData"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/LedgerGroupData"
        params: Dict[str, Any] = {}
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        if fiscal_period_fiscal_date_from is not None:
            params['fiscalPeriod.fiscalDateFrom'] = fiscal_period_fiscal_date_from
        if fiscal_period_fiscal_date_to is not None:
            params['fiscalPeriod.fiscalDateTo'] = fiscal_period_fiscal_date_to
        if filter_bearer_id is not None:
            params['filter.bearerId'] = filter_bearer_id
        if filter_department_id is not None:
            params['filter.departmentId'] = filter_department_id
        if filter_purpose_id is not None:
            params['filter.purposeId'] = filter_purpose_id
        if filter_ledger_group is not None:
            params['filter.ledgerGroup'] = filter_ledger_group
        if filter_fiscal_period_id is not None:
            params['filter.fiscalPeriodId'] = filter_fiscal_period_id
        if filter_ledger_id is not None:
            params['filter.ledgerId'] = filter_ledger_id
        if filter_include_simulated_bookkeeping is not None:
            params['filter.includeSimulatedBookkeeping'] = filter_include_simulated_bookkeeping
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_partner_post_by_primo_partner_post_get__api__fiscal_fiscal_id__transaction__primo_partner_post_id__posts(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/PrimoPartnerPost/{id}/Posts"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/PrimoPartnerPost/{id}/Posts"
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

    def api_transaction__get_article_post_by_primo_article_post_get__api__fiscal_fiscal_id__transaction__primo_article_post_id__posts(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/PrimoArticlePost/{id}/Posts"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/PrimoArticlePost/{id}/Posts"
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

    def api_transaction__get_ledger_post_by_primo_article_post_get__api__fiscal_fiscal_id__transaction__primo_article_post_id__ledger_posts(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/PrimoArticlePost/{id}/LedgerPosts"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/PrimoArticlePost/{id}/LedgerPosts"
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

    def api_transaction__get_partner_posts_by_partner_get__api__fiscal_fiscal_id__transaction__partner_id__partner_post(self, id: int, fiscal_id: str, context_type: str = None, fiscal_date_from: int = None, fiscal_date_to: int = None, is_settled: bool = None, post_type: str = None, is_parked: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/Partner/{id}/PartnerPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/Partner/{id}/PartnerPost"
        params: Dict[str, Any] = {}
        if context_type is not None:
            params['contextType'] = context_type
        if fiscal_date_from is not None:
            params['fiscalDateFrom'] = fiscal_date_from
        if fiscal_date_to is not None:
            params['fiscalDateTo'] = fiscal_date_to
        if is_settled is not None:
            params['isSettled'] = is_settled
        if post_type is not None:
            params['postType'] = post_type
        if is_parked is not None:
            params['isParked'] = is_parked
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

    def api_transaction__get_ledger_group_data_detail_get__api__fiscal_fiscal_id__transaction__ledger_group_data_detail(self, fiscal_id: str, ledger_account: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, fiscal_period_fiscal_date_from: int = None, fiscal_period_fiscal_date_to: int = None, filter_bearer_id: list = None, filter_department_id: list = None, filter_purpose_id: list = None, filter_ledger_group: str = None, filter_fiscal_period_id: int = None, filter_ledger_id: int = None, filter_include_simulated_bookkeeping: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/LedgerGroupDataDetail"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/LedgerGroupDataDetail"
        params: Dict[str, Any] = {}
        if ledger_account is not None:
            params['ledgerAccount'] = ledger_account
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        if fiscal_period_fiscal_date_from is not None:
            params['fiscalPeriod.fiscalDateFrom'] = fiscal_period_fiscal_date_from
        if fiscal_period_fiscal_date_to is not None:
            params['fiscalPeriod.fiscalDateTo'] = fiscal_period_fiscal_date_to
        if filter_bearer_id is not None:
            params['filter.bearerId'] = filter_bearer_id
        if filter_department_id is not None:
            params['filter.departmentId'] = filter_department_id
        if filter_purpose_id is not None:
            params['filter.purposeId'] = filter_purpose_id
        if filter_ledger_group is not None:
            params['filter.ledgerGroup'] = filter_ledger_group
        if filter_fiscal_period_id is not None:
            params['filter.fiscalPeriodId'] = filter_fiscal_period_id
        if filter_ledger_id is not None:
            params['filter.ledgerId'] = filter_ledger_id
        if filter_include_simulated_bookkeeping is not None:
            params['filter.includeSimulatedBookkeeping'] = filter_include_simulated_bookkeeping
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_article_group_sales_statistic_get__api__fiscal_fiscal_id__transaction__article_group_sales_statistic(self, article_group_id: int, fiscal_period_id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, fiscal_period_fiscal_date_from: int = None, fiscal_period_fiscal_date_to: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/ArticleGroupSalesStatistic"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/ArticleGroupSalesStatistic"
        params: Dict[str, Any] = {}
        if article_group_id is not None:
            params['articleGroupId'] = article_group_id
        if fiscal_period_id is not None:
            params['fiscalPeriodId'] = fiscal_period_id
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        if fiscal_period_fiscal_date_from is not None:
            params['fiscalPeriod.fiscalDateFrom'] = fiscal_period_fiscal_date_from
        if fiscal_period_fiscal_date_to is not None:
            params['fiscalPeriod.fiscalDateTo'] = fiscal_period_fiscal_date_to
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_article_group_purchasing_statistic_get__api__fiscal_fiscal_id__transaction__article_group_purchasing_statistic(self, article_group_id: int, fiscal_period_id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, fiscal_period_fiscal_date_from: int = None, fiscal_period_fiscal_date_to: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/ArticleGroupPurchasingStatistic"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/ArticleGroupPurchasingStatistic"
        params: Dict[str, Any] = {}
        if article_group_id is not None:
            params['articleGroupId'] = article_group_id
        if fiscal_period_id is not None:
            params['fiscalPeriodId'] = fiscal_period_id
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        if fiscal_period_fiscal_date_from is not None:
            params['fiscalPeriod.fiscalDateFrom'] = fiscal_period_fiscal_date_from
        if fiscal_period_fiscal_date_to is not None:
            params['fiscalPeriod.fiscalDateTo'] = fiscal_period_fiscal_date_to
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_ledger_post_by_vat_get__api__fiscal_fiscal_id__transaction__vat_id__ledger_post(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, fiscal_period_fiscal_date_from: int = None, fiscal_period_fiscal_date_to: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/Vat/{id}/LedgerPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/Vat/{id}/LedgerPost"
        params: Dict[str, Any] = {}
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        if fiscal_period_fiscal_date_from is not None:
            params['fiscalPeriod.fiscalDateFrom'] = fiscal_period_fiscal_date_from
        if fiscal_period_fiscal_date_to is not None:
            params['fiscalPeriod.fiscalDateTo'] = fiscal_period_fiscal_date_to
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_ledger_post_for_ledger_account_get__api__fiscal_fiscal_id__transaction__ledger_posts_for_ledger_account(self, ledger_account: str, fiscal_id: str, department_id: int = None, bearer_id: int = None, purpose_id: int = None, vat_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, fiscal_period_fiscal_date_from: int = None, fiscal_period_fiscal_date_to: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/LedgerPostsForLedgerAccount"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/LedgerPostsForLedgerAccount"
        params: Dict[str, Any] = {}
        if ledger_account is not None:
            params['ledgerAccount'] = ledger_account
        if department_id is not None:
            params['departmentId'] = department_id
        if bearer_id is not None:
            params['bearerId'] = bearer_id
        if purpose_id is not None:
            params['purposeId'] = purpose_id
        if vat_id is not None:
            params['vatId'] = vat_id
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        if fiscal_period_fiscal_date_from is not None:
            params['fiscalPeriod.fiscalDateFrom'] = fiscal_period_fiscal_date_from
        if fiscal_period_fiscal_date_to is not None:
            params['fiscalPeriod.fiscalDateTo'] = fiscal_period_fiscal_date_to
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__get_partner_reminder_get__api__fiscal_fiscal_id__transaction__partner_reminder(self, calculated_by: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/PartnerReminder"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/PartnerReminder"
        params: Dict[str, Any] = {}
        if calculated_by is not None:
            params['calculatedBy'] = calculated_by
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

    def api_transaction__get_xena_partner_get__api__fiscal_fiscal_id__transaction__xena_partner(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Transaction/XenaPartner"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/XenaPartner"
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

    def api_transaction__post_eu_sales_without_vat_post__api__fiscal_fiscal_id__transaction__render_eu_sales_without_vat(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderEUSalesWithoutVAT"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderEUSalesWithoutVAT"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_article_post_report_post__api__fiscal_fiscal_id__transaction__render_article_post_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderArticlePostReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderArticlePostReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_article_stock_report_post__api__fiscal_fiscal_id__transaction__render_article_stock_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderArticleStockReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderArticleStockReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_article_stock_staticstics_report_post__api__fiscal_fiscal_id__transaction__render_article_stock_staticstics_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderArticleStockStaticsticsReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderArticleStockStaticsticsReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_historic_stock_value_report_post__api__fiscal_fiscal_id__transaction__render_historic_stock_value_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderHistoricStockValueReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderHistoricStockValueReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_partner_post_report_post__api__fiscal_fiscal_id__transaction__render_partner_post_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderPartnerPostReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderPartnerPostReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_partner_statistic_report_post__api__fiscal_fiscal_id__transaction__render_partner_statistic_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderPartnerStatisticReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderPartnerStatisticReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_partner_saldo_report_post__api__fiscal_fiscal_id__transaction__render_partner_saldo_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderPartnerSaldoReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderPartnerSaldoReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_partner_saldo_by_unit_report_post__api__fiscal_fiscal_id__transaction__render_partner_saldo_by_unit_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderPartnerSaldoByUnitReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderPartnerSaldoByUnitReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_partner_saldo_by_due_date_report_post__api__fiscal_fiscal_id__transaction__render_partner_saldo_by_due_date_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderPartnerSaldoByDueDateReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderPartnerSaldoByDueDateReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_order_task_post_by_order_report_post__api__fiscal_fiscal_id__transaction__render_order_task_post_by_order_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderOrderTaskPostByOrderReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderOrderTaskPostByOrderReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_resource_post_report_post__api__fiscal_fiscal_id__transaction__render_resource_post_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderResourcePostReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderResourcePostReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_project_in_progress_report_post__api__fiscal_fiscal_id__transaction__render_project_in_progress(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderProjectInProgress"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderProjectInProgress"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_ongoing_orders_list_post__api__fiscal_fiscal_id__transaction__render_ongoing_orders_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderOngoingOrdersReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderOngoingOrdersReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_ongoing_orders_historic_list_post__api__fiscal_fiscal_id__transaction__render_ongoing_orders_historic_report(self, filter: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderOngoingOrdersHistoricReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderOngoingOrdersHistoricReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=filter, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_order_budget_list_post__api__fiscal_fiscal_id__transaction__render_order_budget_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderOrderBudgetReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderOrderBudgetReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_article_group_statistic_report_post__api__fiscal_fiscal_id__transaction__render_article_group_statistic_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderArticleGroupStatisticReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderArticleGroupStatisticReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_article_margin_report_post__api__fiscal_fiscal_id__transaction__render_article_margin_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderArticleMarginReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderArticleMarginReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_ledger_tag_statistic_report_post__api__fiscal_fiscal_id__transaction__render_ledger_tag_statistic_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderLedgerTagStatisticReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderLedgerTagStatisticReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_ledger_post_report_post__api__fiscal_fiscal_id__transaction__render_ledger_post_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderLedgerPostReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderLedgerPostReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_partner_article_statistics_report_post__api__fiscal_fiscal_id__transaction__render_partner_article_statistics_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderPartnerArticleStatisticsReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderPartnerArticleStatisticsReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_ledger_account_specification_list_post__api__fiscal_fiscal_id__transaction__render_ledger_account_specification(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderLedgerAccountSpecification"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderLedgerAccountSpecification"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_balance_report_for_fiscal_period_post__api__fiscal_fiscal_id__transaction__fiscal_period_id__render_balance_report(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/FiscalPeriod/{id}/RenderBalanceReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/FiscalPeriod/{id}/RenderBalanceReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_balance_accountant_report_for_fiscal_period_post__api__fiscal_fiscal_id__transaction__fiscal_period_id__render_balance_accountant_report(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/FiscalPeriod/{id}/RenderBalanceAccountantReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/FiscalPeriod/{id}/RenderBalanceAccountantReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_ledger_journal_post__api__fiscal_fiscal_id__transaction__ledger_id__render_journal(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/Ledger/{id}/RenderJournal"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/Ledger/{id}/RenderJournal"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_invoice_list_report_post__api__fiscal_fiscal_id__transaction__render_invoice_list_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderInvoiceListReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderInvoiceListReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_voucher_summary_cost_post_report_post__api__fiscal_fiscal_id__transaction__post_render_voucher_summary_cost_post_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/PostRenderVoucherSummaryCostPostReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/PostRenderVoucherSummaryCostPostReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_statement_for_partner_post__api__fiscal_fiscal_id__transaction__partner_id__render_statement(self, id: int, fiscal_id: str, report_layout_id: int = None, from_: int = None, to: int = None, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/Partner/{id}/RenderStatement"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/Partner/{id}/RenderStatement"
        params: Dict[str, Any] = {}
        if report_layout_id is not None:
            params['reportLayoutId'] = report_layout_id
        if from_ is not None:
            params['from'] = from_
        if to is not None:
            params['to'] = to
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_partner_extended_statement_post__api__fiscal_fiscal_id__transaction__partner_id__render_extended_statement(self, id: int, options: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/Partner/{id}/RenderExtendedStatement"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/Partner/{id}/RenderExtendedStatement"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=options, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_for_vat_settlement_post__api__fiscal_fiscal_id__transaction__vat_settlement_id__render(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/VatSettlement/{id}/Render"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/VatSettlement/{id}/Render"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_vat_reconciliation_report_post__api__fiscal_fiscal_id__transaction__render_vat_reconciliation_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderVatReconciliationReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderVatReconciliationReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_transaction__post_render_project_budget_list_post__api__fiscal_fiscal_id__transaction__render_project_budget_report(self, filter: Dict[str, Any], fiscal_id: str, report_layout_id: int = None, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Transaction/RenderProjectBudgetReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Transaction/RenderProjectBudgetReport"
        params: Dict[str, Any] = {}
        if report_layout_id is not None:
            params['reportLayoutId'] = report_layout_id
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=filter, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_vat__get_get__api__fiscal_fiscal_id__vat(self, fiscal_id: str, querystring: str = None, include_defaults: bool = None, excluded_vat_id: int = None, exclude_import_type: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Vat"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Vat"
        params: Dict[str, Any] = {}
        if querystring is not None:
            params['querystring'] = querystring
        if include_defaults is not None:
            params['includeDefaults'] = include_defaults
        if excluded_vat_id is not None:
            params['excludedVatId'] = excluded_vat_id
        if exclude_import_type is not None:
            params['excludeImportType'] = exclude_import_type
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

    def api_vat__post_post__api__fiscal_fiscal_id__vat(self, vat: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Vat"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Vat"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=vat, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_vat__get_get__api__fiscal_fiscal_id__vat_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Vat/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Vat/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_vat__put_put__api__fiscal_fiscal_id__vat_id(self, vat: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Vat/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Vat/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=vat, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_vat__delete_delete__api__fiscal_fiscal_id__vat_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Vat/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Vat/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_vat__get_by_type_get__api__fiscal_fiscal_id__vat__by_type(self, fiscal_id: str, query_string: str = None, vat_type: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Vat/ByType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Vat/ByType"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if vat_type is not None:
            params['vatType'] = vat_type
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

    def api_vat__get_possible_vat_problems_get__api__fiscal_fiscal_id__vat__possible_problems(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Vat/PossibleProblems"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Vat/PossibleProblems"
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

    def api_vat__get_duplicate_account_numbers_get__api__fiscal_fiscal_id__vat_id__duplicate_account_numbers(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Vat/{id}/DuplicateAccountNumbers"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Vat/{id}/DuplicateAccountNumbers"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_vat__get_has_been_used_get__api__fiscal_fiscal_id__vat_id__has_been_used(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Vat/{id}/HasBeenUsed"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Vat/{id}/HasBeenUsed"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_vat__get_vat_type_get__api__fiscal_fiscal_id__vat__vat_type(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Vat/VatType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Vat/VatType"
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

    def api_vat__get_vat_reconciliation_posts_get__api__fiscal_fiscal_id__vat_id__reconciliation_data(self, id: int, date_from: int, date_to: int, fiscal_id: str, ledger_tag_id: int = None, article_group_id: int = None, limit_to_department: bool = None, department_id: int = None, limit_to_bearer: bool = None, bearer_id: int = None, limit_to_purpose: bool = None, purpose_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Vat/{id}/ReconciliationData"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Vat/{id}/ReconciliationData"
        params: Dict[str, Any] = {}
        if date_from is not None:
            params['dateFrom'] = date_from
        if date_to is not None:
            params['dateTo'] = date_to
        if ledger_tag_id is not None:
            params['ledgerTagId'] = ledger_tag_id
        if article_group_id is not None:
            params['articleGroupId'] = article_group_id
        if limit_to_department is not None:
            params['limitToDepartment'] = limit_to_department
        if department_id is not None:
            params['departmentId'] = department_id
        if limit_to_bearer is not None:
            params['limitToBearer'] = limit_to_bearer
        if bearer_id is not None:
            params['bearerId'] = bearer_id
        if limit_to_purpose is not None:
            params['limitToPurpose'] = limit_to_purpose
        if purpose_id is not None:
            params['purposeId'] = purpose_id
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

    def api_vat_settlement__get_get__api__fiscal_fiscal_id__vat_settlement(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VatSettlement"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VatSettlement"
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

    def api_vat_settlement__get_get__api__fiscal_fiscal_id__vat_settlement_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VatSettlement/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VatSettlement/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_vat_settlement__delete_delete__api__fiscal_fiscal_id__vat_settlement_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/VatSettlement/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VatSettlement/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_vat_settlement__post_pay_vat_settlement_post__api__fiscal_fiscal_id__vat_settlement_id__pay(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/VatSettlement/{id}/Pay"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VatSettlement/{id}/Pay"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_vat_settlement__post_settle_vat_period_post__api__fiscal_fiscal_id__vat_settlement__settle_vat_period(self, settle_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/VatSettlement/SettleVatPeriod"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VatSettlement/SettleVatPeriod"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=settle_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_vat_settlement__post_submit_vat_to_skat_post__api__fiscal_fiscal_id__vat_settlement_id__submit_vat_to_skat(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/VatSettlement/{id}/SubmitVatToSkat"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VatSettlement/{id}/SubmitVatToSkat"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_vat_settlement__get_document_ids_from_vat_settlement_transaction_id_get__api__fiscal_fiscal_id__vat_settlement__get_document_ids_from_vat_settlement_transaction_id_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VatSettlement/GetDocumentIdsFromVatSettlementTransactionId/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VatSettlement/GetDocumentIdsFromVatSettlementTransactionId/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_vat_settlement__get_vat_settlement_posts_get__api__fiscal_fiscal_id__vat_settlement__vat_settlement_post(self, fiscal_id: str, vat_period_start: int = None, vat_period_end: int = None, vat_system: str = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VatSettlement/VatSettlementPost"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VatSettlement/VatSettlementPost"
        params: Dict[str, Any] = {}
        if vat_period_start is not None:
            params['vatPeriodStart'] = vat_period_start
        if vat_period_end is not None:
            params['vatPeriodEnd'] = vat_period_end
        if vat_system is not None:
            params['vatSystem'] = vat_system
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_vat_settlement__get_vat_settlement_data_get__api__fiscal_fiscal_id__vat_settlement__vat_settlement_data(self, fiscal_id: str, vat_system: str = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VatSettlement/VatSettlementData"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VatSettlement/VatSettlementData"
        params: Dict[str, Any] = {}
        if vat_system is not None:
            params['vatSystem'] = vat_system
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_vat_settlement__get_vat_settlement_summary_get__api__fiscal_fiscal_id__vat_settlement__vat_settlement_summary(self, fiscal_id: str, vat_period_start: int = None, vat_period_end: int = None, pay_date: int = None, vat_system: str = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VatSettlement/VatSettlementSummary"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VatSettlement/VatSettlementSummary"
        params: Dict[str, Any] = {}
        if vat_period_start is not None:
            params['vatPeriodStart'] = vat_period_start
        if vat_period_end is not None:
            params['vatPeriodEnd'] = vat_period_end
        if pay_date is not None:
            params['payDate'] = pay_date
        if vat_system is not None:
            params['vatSystem'] = vat_system
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_vat_settlement__get_altinn_vat_data_get__api__fiscal_fiscal_id__vat_settlement__altinn_vat_data(self, vat_settlement_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VatSettlement/AltinnVatData"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VatSettlement/AltinnVatData"
        params: Dict[str, Any] = {}
        if vat_settlement_id is not None:
            params['vatSettlementId'] = vat_settlement_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_voucher__get_get__api__fiscal_fiscal_id__voucher(self, fiscal_id: str, options_query_string: str = None, options_responsible_id: int = None, options_voucher_number_from: int = None, options_voucher_number_to: int = None, options_fiscal_date_from: int = None, options_fiscal_date_to: int = None, options_amount_from: float = None, options_amount_to: float = None, options_show_deactivated: bool = None, options_page: int = None, options_page_size: int = None, options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Voucher"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Voucher"
        params: Dict[str, Any] = {}
        if options_query_string is not None:
            params['options.queryString'] = options_query_string
        if options_responsible_id is not None:
            params['options.responsibleId'] = options_responsible_id
        if options_voucher_number_from is not None:
            params['options.voucherNumberFrom'] = options_voucher_number_from
        if options_voucher_number_to is not None:
            params['options.voucherNumberTo'] = options_voucher_number_to
        if options_fiscal_date_from is not None:
            params['options.fiscalDateFrom'] = options_fiscal_date_from
        if options_fiscal_date_to is not None:
            params['options.fiscalDateTo'] = options_fiscal_date_to
        if options_amount_from is not None:
            params['options.amountFrom'] = options_amount_from
        if options_amount_to is not None:
            params['options.amountTo'] = options_amount_to
        if options_show_deactivated is not None:
            params['options.showDeactivated'] = options_show_deactivated
        if options_page is not None:
            params['options.page'] = options_page
        if options_page_size is not None:
            params['options.pageSize'] = options_page_size
        if options_force_no_paging is not None:
            params['options.forceNoPaging'] = options_force_no_paging
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_voucher__get_get__api__fiscal_fiscal_id__voucher_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Voucher/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Voucher/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_voucher__put_put__api__fiscal_fiscal_id__voucher_id(self, voucher: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Voucher/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Voucher/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=voucher, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_voucher__get_history_get__api__fiscal_fiscal_id__voucher__history(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Voucher/History"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Voucher/History"
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

    def api_voucher__get_summary_get__api__fiscal_fiscal_id__voucher_id__summary(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Voucher/{id}/Summary"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Voucher/{id}/Summary"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_voucher__get_transactions_by_voucher_get__api__fiscal_fiscal_id__voucher_id__transaction(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Voucher/{id}/Transaction"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Voucher/{id}/Transaction"
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

    def api_voucher__get_summary_cost_posts_get__api__fiscal_fiscal_id__voucher__summary_cost_posts(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, filter_voucher_no_from: int = None, filter_voucher_no_to: int = None, filter_date_from: int = None, filter_date_to: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Voucher/SummaryCostPosts"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Voucher/SummaryCostPosts"
        params: Dict[str, Any] = {}
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        if filter_voucher_no_from is not None:
            params['filter.voucherNoFrom'] = filter_voucher_no_from
        if filter_voucher_no_to is not None:
            params['filter.voucherNoTo'] = filter_voucher_no_to
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

    def api_voucher_preview__get_get__api__fiscal_fiscal_id__voucher_preview_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VoucherPreview/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VoucherPreview/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_voucher_preview__put_put__api__fiscal_fiscal_id__voucher_preview_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/VoucherPreview/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VoucherPreview/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_voucher_preview__delete_delete__api__fiscal_fiscal_id__voucher_preview_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/VoucherPreview/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VoucherPreview/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_voucher_preview__get_voucher_preview_for_resource_inbox_get__api__fiscal_fiscal_id__resource_inbox_id__voucher_preview(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ResourceInbox/{id}/VoucherPreview"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ResourceInbox/{id}/VoucherPreview"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_voucher_preview__post_from_resource_inbox_post__api__fiscal_fiscal_id__resource_inbox_id__voucher_preview(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ResourceInbox/{id}/VoucherPreview"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ResourceInbox/{id}/VoucherPreview"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_voucher_preview__put_bookkeep_put__api__fiscal_fiscal_id__voucher_preview_id__bookkeep(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/VoucherPreview/{id}/Bookkeep"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VoucherPreview/{id}/Bookkeep"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_voucher_preview__put_move_to_next_approver_put__api__fiscal_fiscal_id__voucher_preview_id__move_to_next_approver(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/VoucherPreview/{id}/MoveToNextApprover"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VoucherPreview/{id}/MoveToNextApprover"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_voucher_preview__post_post__api__fiscal_fiscal_id__voucher_preview(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/VoucherPreview"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VoucherPreview"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_voucher_preview__get_summary_get__api__fiscal_fiscal_id__voucher_preview_id__summary(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VoucherPreview/{id}/Summary"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VoucherPreview/{id}/Summary"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def financial_statement__get_csv_get__api__fiscal_fiscal_id__report__financial_statement_csv(self, fiscal_period_id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Report/FinancialStatement/CSV"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Report/FinancialStatement/CSV"
        params: Dict[str, Any] = {}
        if fiscal_period_id is not None:
            params['fiscalPeriodId'] = fiscal_period_id
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

    def fiscal_data_to_saft__get_xml_get__api__fiscal_fiscal_id__report__fiscal_data_to_saf_t_xml(self, date_from: int, date_to: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Report/FiscalDataToSAF_T/XML"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Report/FiscalDataToSAF_T/XML"
        params: Dict[str, Any] = {}
        if date_from is not None:
            params['dateFrom'] = date_from
        if date_to is not None:
            params['dateTo'] = date_to
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_payment_export_draft__post_partner_payment_by_ids_post__api__fiscal_fiscal_id__payment_export_draft_context_id__by_payment_ids(self, context_id: int, payment_ids_request: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/PaymentExportDraft/{contextId}/ByPaymentIds"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PaymentExportDraft/{context_id}/ByPaymentIds"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=payment_ids_request, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text
