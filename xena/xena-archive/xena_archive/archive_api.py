from typing import Any, Dict, Optional
import requests

class ArchiveApi:
    """API client for the Archive domain of the Xena API."""
    def __init__(self, base_url: str, session: Optional[requests.Session] = None) -> None:
        self.base_url = base_url.rstrip('/')
        self.session = session or requests.Session()

    def api_data_import__get_get__api__fiscal_fiscal_id__data_import(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/DataImport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DataImport"
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

    def api_data_import__post_post__api__fiscal_fiscal_id__data_import(self, data_import: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/DataImport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DataImport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data_import, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_data_import__get_get__api__fiscal_fiscal_id__data_import_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/DataImport/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DataImport/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_data_import__delete_delete__api__fiscal_fiscal_id__data_import_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/DataImport/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DataImport/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_data_import__put_trigger_import_put__api__fiscal_fiscal_id__data_import_id__trigger_import(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/DataImport/{id}/TriggerImport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DataImport/{id}/TriggerImport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_data_import_task__get_by_data_import_get__api__fiscal_fiscal_id__data_import_id__task(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/DataImport/{id}/Task"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DataImport/{id}/Task"
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

    def api_data_import_task__get_get__api__fiscal_fiscal_id__data_import_task_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/DataImportTask/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DataImportTask/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_data_import_task_log__get_by_data_import_task_get__api__fiscal_fiscal_id__data_import_task_id__log(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/DataImportTask/{id}/Log"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DataImportTask/{id}/Log"
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

    def api_imported_account__get_get__api__fiscal_fiscal_id__imported_account(self, fiscal_id: str, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, data_import_data_filter_limit_to_data_import: bool = None, data_import_data_filter_data_import_id: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ImportedAccount"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedAccount"
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
        if data_import_data_filter_limit_to_data_import is not None:
            params['dataImportDataFilter.limitToDataImport'] = data_import_data_filter_limit_to_data_import
        if data_import_data_filter_data_import_id is not None:
            params['dataImportDataFilter.dataImportId'] = data_import_data_filter_data_import_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_account__get_get__api__fiscal_fiscal_id__imported_account_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ImportedAccount/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedAccount/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_account__put_put__api__fiscal_fiscal_id__imported_account_id(self, imported_account: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ImportedAccount/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedAccount/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=imported_account, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_account__delete_delete__api__fiscal_fiscal_id__imported_account_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ImportedAccount/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedAccount/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_account__post_import_multiple_post__api__fiscal_fiscal_id__imported_account__import_multiple(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ImportedAccount/ImportMultiple"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedAccount/ImportMultiple"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_article__get_get__api__fiscal_fiscal_id__imported_article(self, fiscal_id: str, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, data_import_data_filter_limit_to_data_import: bool = None, data_import_data_filter_data_import_id: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ImportedArticle"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedArticle"
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
        if data_import_data_filter_limit_to_data_import is not None:
            params['dataImportDataFilter.limitToDataImport'] = data_import_data_filter_limit_to_data_import
        if data_import_data_filter_data_import_id is not None:
            params['dataImportDataFilter.dataImportId'] = data_import_data_filter_data_import_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_article__get_get__api__fiscal_fiscal_id__imported_article_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ImportedArticle/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedArticle/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_article__put_put__api__fiscal_fiscal_id__imported_article_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ImportedArticle/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedArticle/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_article__delete_delete__api__fiscal_fiscal_id__imported_article_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ImportedArticle/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedArticle/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_article_group__get_get__api__fiscal_fiscal_id__imported_article_group(self, fiscal_id: str, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, data_import_data_filter_limit_to_data_import: bool = None, data_import_data_filter_data_import_id: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ImportedArticleGroup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedArticleGroup"
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
        if data_import_data_filter_limit_to_data_import is not None:
            params['dataImportDataFilter.limitToDataImport'] = data_import_data_filter_limit_to_data_import
        if data_import_data_filter_data_import_id is not None:
            params['dataImportDataFilter.dataImportId'] = data_import_data_filter_data_import_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_article_group__get_get__api__fiscal_fiscal_id__imported_article_group_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ImportedArticleGroup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedArticleGroup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_article_group__put_put__api__fiscal_fiscal_id__imported_article_group_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ImportedArticleGroup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedArticleGroup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_article_group__delete_delete__api__fiscal_fiscal_id__imported_article_group_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ImportedArticleGroup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedArticleGroup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_article_group__put_import_group_put__api__fiscal_fiscal_id__imported_article_group_id__link_articles(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ImportedArticleGroup/{id}/LinkArticles"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedArticleGroup/{id}/LinkArticles"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_article_group__post_import_multiple_post__api__fiscal_fiscal_id__imported_article_group__import_multiple(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ImportedArticleGroup/ImportMultiple"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedArticleGroup/ImportMultiple"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_fiscal_year__get_get__api__fiscal_fiscal_id__imported_fiscal_year(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ImportedFiscalYear"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedFiscalYear"
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

    def api_imported_fiscal_year__get_get__api__fiscal_fiscal_id__imported_fiscal_year_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ImportedFiscalYear/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedFiscalYear/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_partner__get_get__api__fiscal_fiscal_id__imported_partner(self, fiscal_id: str, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, data_import_data_filter_limit_to_data_import: bool = None, data_import_data_filter_data_import_id: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ImportedPartner"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedPartner"
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
        if data_import_data_filter_limit_to_data_import is not None:
            params['dataImportDataFilter.limitToDataImport'] = data_import_data_filter_limit_to_data_import
        if data_import_data_filter_data_import_id is not None:
            params['dataImportDataFilter.dataImportId'] = data_import_data_filter_data_import_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_partner__get_get__api__fiscal_fiscal_id__imported_partner_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ImportedPartner/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedPartner/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_partner__put_put__api__fiscal_fiscal_id__imported_partner_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ImportedPartner/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedPartner/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_partner__delete_delete__api__fiscal_fiscal_id__imported_partner_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ImportedPartner/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedPartner/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_partner__post_import_multiple_post__api__fiscal_fiscal_id__imported_partner__import_multiple(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ImportedPartner/ImportMultiple"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedPartner/ImportMultiple"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_posting__get_get__api__fiscal_fiscal_id__imported_account_id__imported_posting(self, id: int, fiscal_id: str, query_string: str = None, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, fiscal_period_version: int = None, fiscal_period_data_import_id: int = None, fiscal_period_from_date_days: int = None, fiscal_period_to_date_days: int = None, fiscal_period_description: str = None, fiscal_period_is_closed: bool = None, fiscal_period_to_date_days_friendly: str = None, fiscal_period_id: int = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ImportedAccount/{id}/ImportedPosting"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedAccount/{id}/ImportedPosting"
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
        if fiscal_period_version is not None:
            params['fiscalPeriod.version'] = fiscal_period_version
        if fiscal_period_data_import_id is not None:
            params['fiscalPeriod.dataImportId'] = fiscal_period_data_import_id
        if fiscal_period_from_date_days is not None:
            params['fiscalPeriod.fromDateDays'] = fiscal_period_from_date_days
        if fiscal_period_to_date_days is not None:
            params['fiscalPeriod.toDateDays'] = fiscal_period_to_date_days
        if fiscal_period_description is not None:
            params['fiscalPeriod.description'] = fiscal_period_description
        if fiscal_period_is_closed is not None:
            params['fiscalPeriod.isClosed'] = fiscal_period_is_closed
        if fiscal_period_to_date_days_friendly is not None:
            params['fiscalPeriod.toDateDaysFriendly'] = fiscal_period_to_date_days_friendly
        if fiscal_period_id is not None:
            params['fiscalPeriod.id'] = fiscal_period_id
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_posting__get_get__api__fiscal_fiscal_id__imported_posting_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ImportedPosting/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedPosting/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_posting__delete_delete__api__fiscal_fiscal_id__imported_posting_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ImportedPosting/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedPosting/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_imported_posting__post_import_multiple_post__api__fiscal_fiscal_id__imported_posting__import_multiple(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ImportedPosting/ImportMultiple"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportedPosting/ImportMultiple"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_import_vat_line_draft__get_get__api__fiscal_fiscal_id__import_vat_line_draft(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ImportVatLineDraft"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportVatLineDraft"
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

    def api_import_vat_line_draft__post_post__api__fiscal_fiscal_id__import_vat_line_draft(self, vat: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ImportVatLineDraft"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportVatLineDraft"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=vat, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_import_vat_line_draft__get_get__api__fiscal_fiscal_id__import_vat_line_draft_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ImportVatLineDraft/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportVatLineDraft/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_import_vat_line_draft__put_put__api__fiscal_fiscal_id__import_vat_line_draft_id(self, vat: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ImportVatLineDraft/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportVatLineDraft/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=vat, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_import_vat_line_draft__delete_delete__api__fiscal_fiscal_id__import_vat_line_draft_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ImportVatLineDraft/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportVatLineDraft/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_import_vat_line_draft__get_import_vat_line_type_get__api__fiscal_fiscal_id__import_vat_line_draft__import_vat_line_type(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ImportVatLineDraft/ImportVatLineType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportVatLineDraft/ImportVatLineType"
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

    def api_import_vat_line_draft__post_bookkeep_post__api__fiscal_fiscal_id__import_vat_line_draft__bookkeep(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ImportVatLineDraft/Bookkeep"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportVatLineDraft/Bookkeep"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_import_vat_transaction__get_get__api__fiscal_fiscal_id__import_vat_transaction(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ImportVatTransaction"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportVatTransaction"
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

    def api_import_vat_transaction__get_get__api__fiscal_fiscal_id__import_vat_transaction_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ImportVatTransaction/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportVatTransaction/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_import_vat_transaction__delete_delete__api__fiscal_fiscal_id__import_vat_transaction_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ImportVatTransaction/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ImportVatTransaction/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text
