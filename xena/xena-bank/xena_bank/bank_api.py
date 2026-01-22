from typing import Any, Dict, Optional
import requests

class BankApi:
    """API client for the Bank domain of the Xena API."""
    def __init__(self, base_url: str, session: Optional[requests.Session] = None) -> None:
        self.base_url = base_url.rstrip('/')
        self.session = session or requests.Session()

    def api_bank_posting__get_by_bank_context_get__api__fiscal_fiscal_id__ledger_tag_bank_context_id__posting(self, id: int, fiscal_id: str, fiscal_date_from: int = None, fiscal_date_to: int = None, show_reconciled: bool = None, reverse_date_sort: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTagBankContext/{id}/Posting"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTagBankContext/{id}/Posting"
        params: Dict[str, Any] = {}
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

    def api_bank_posting__get_get__api__fiscal_fiscal_id__bank_posting_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/BankPosting/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BankPosting/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bank_posting__delete_delete__api__fiscal_fiscal_id__bank_posting_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/BankPosting/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BankPosting/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bank_posting__post_post__api__fiscal_fiscal_id__bank_posting(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/BankPosting"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BankPosting"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bank_posting__post_reconciliate_post__api__fiscal_fiscal_id__bank_posting__reconciliate(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/BankPosting/Reconciliate"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BankPosting/Reconciliate"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bank_posting__get_reconciliation_summary_get__api__fiscal_fiscal_id__bank_posting__reconciliation_summary(self, bank_posting_ids: list, ledger_post_ids: list, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/BankPosting/ReconciliationSummary"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BankPosting/ReconciliationSummary"
        params: Dict[str, Any] = {}
        if bank_posting_ids is not None:
            params['bankPostingIds'] = bank_posting_ids
        if ledger_post_ids is not None:
            params['ledgerPostIds'] = ledger_post_ids
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bank_posting__delete_un_reconciled_post_delete__api__fiscal_fiscal_id__ledger_tag_bank_context_id__un_reconciled_posting(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/LedgerTagBankContext/{id}/UnReconciledPosting"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTagBankContext/{id}/UnReconciledPosting"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bank_posting__put_selected_post_to_ledger_put__api__fiscal_fiscal_id__ledger_tag_bank_context_id__selected_posting(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/LedgerTagBankContext/{id}/SelectedPosting"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTagBankContext/{id}/SelectedPosting"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bank_posting__get_involved_bank_postings_get__api__fiscal_fiscal_id__bank_posting__involved_bank_postings(self, bank_settlement_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/BankPosting/InvolvedBankPostings"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BankPosting/InvolvedBankPostings"
        params: Dict[str, Any] = {}
        if bank_settlement_id is not None:
            params['bankSettlementId'] = bank_settlement_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bank_posting_reconciliation_suggestion__get_list_get__api__fiscal_fiscal_id__bank_posting_reconciliation_suggestion(self, fiscal_id: str, data_bank_posting_ids: list = None, data_ledger_post_ids: list = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/BankPostingReconciliationSuggestion"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BankPostingReconciliationSuggestion"
        params: Dict[str, Any] = {}
        if data_bank_posting_ids is not None:
            params['data.bankPostingIds'] = data_bank_posting_ids
        if data_ledger_post_ids is not None:
            params['data.ledgerPostIds'] = data_ledger_post_ids
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bank_posting_reconciliation_suggestion__get_reconciliation_suggestions_for_bank_posting_get__api__fiscal_fiscal_id__bank_posting_id__reconciliation_suggestion(self, id: int, fiscal_id: str, suggestion_type: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/BankPosting/{id}/ReconciliationSuggestion"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BankPosting/{id}/ReconciliationSuggestion"
        params: Dict[str, Any] = {}
        if suggestion_type is not None:
            params['suggestionType'] = suggestion_type
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bank_posting_reconciliation_suggestion__get_reconciliation_suggestions_for_ledger_post_get__api__fiscal_fiscal_id__ledger_post_id__reconciliation_suggestion(self, id: int, fiscal_id: str, suggestion_type: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerPost/{id}/ReconciliationSuggestion"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerPost/{id}/ReconciliationSuggestion"
        params: Dict[str, Any] = {}
        if suggestion_type is not None:
            params['suggestionType'] = suggestion_type
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bank_settlement__get_get__api__fiscal_fiscal_id__bank_settlement_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/BankSettlement/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BankSettlement/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bank_settlement__delete_delete__api__fiscal_fiscal_id__bank_settlement_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/BankSettlement/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BankSettlement/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag_bank_context__get_get__api__fiscal_fiscal_id__ledger_tag_bank_context(self, fiscal_id: str, excluded_id: int = None, query_string: str = None, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTagBankContext"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTagBankContext"
        params: Dict[str, Any] = {}
        if excluded_id is not None:
            params['excludedId'] = excluded_id
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

    def api_ledger_tag_bank_context__post_post__api__fiscal_fiscal_id__ledger_tag_bank_context(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/LedgerTagBankContext"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTagBankContext"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag_bank_context__get_get__api__fiscal_fiscal_id__ledger_tag_bank_context_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTagBankContext/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTagBankContext/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag_bank_context__put_put__api__fiscal_fiscal_id__ledger_tag_bank_context_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/LedgerTagBankContext/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTagBankContext/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag_bank_context__delete_delete__api__fiscal_fiscal_id__ledger_tag_bank_context_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/LedgerTagBankContext/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTagBankContext/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_ledger_tag_bank_context__get_by_ledger_tag_get__api__fiscal_fiscal_id__ledger_tag_id__bank_context(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/LedgerTag/{id}/BankContext"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/LedgerTag/{id}/BankContext"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text
