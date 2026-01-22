from typing import Any, Dict, Optional
import requests

class ArticleApi:
    """API client for the Article domain of the Xena API."""
    def __init__(self, base_url: str, session: Optional[requests.Session] = None) -> None:
        self.base_url = base_url.rstrip('/')
        self.session = session or requests.Session()

    def api_additional_article__get_by_article_list_get__api__fiscal_fiscal_id__article_id__additional_article(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/{id}/AdditionalArticle"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/AdditionalArticle"
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

    def api_additional_article__get_get__api__fiscal_fiscal_id__additional_article_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/AdditionalArticle/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AdditionalArticle/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_additional_article__put_put__api__fiscal_fiscal_id__additional_article_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/AdditionalArticle/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AdditionalArticle/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_additional_article__delete_delete__api__fiscal_fiscal_id__additional_article_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/AdditionalArticle/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AdditionalArticle/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_additional_article__post_post__api__fiscal_fiscal_id__additional_article(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/AdditionalArticle"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/AdditionalArticle"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__get_average_price_change_list_get__api__fiscal_fiscal_id__article_id__average_price_change(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/{id}/AveragePriceChange"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/AveragePriceChange"
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

    def api_article__get_get__api__fiscal_fiscal_id__article(self, fiscal_id: str, excluded_id: int = None, query_string: str = None, include_defaults: bool = None, required_has_inventory_management: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article"
        params: Dict[str, Any] = {}
        if excluded_id is not None:
            params['excludedId'] = excluded_id
        if query_string is not None:
            params['queryString'] = query_string
        if include_defaults is not None:
            params['includeDefaults'] = include_defaults
        if required_has_inventory_management is not None:
            params['requiredHasInventoryManagement'] = required_has_inventory_management
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__post_post__api__fiscal_fiscal_id__article(self, article: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Article"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=article, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__get_get__api__fiscal_fiscal_id__article_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__put_put__api__fiscal_fiscal_id__article_id(self, article: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Article/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=article, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__delete_delete__api__fiscal_fiscal_id__article_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Article/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__put_update_supplier_put__api__fiscal_fiscal_id__article_id__update_supplier(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Article/{id}/UpdateSupplier"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/UpdateSupplier"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__put_manual_recalculate_put__api__fiscal_fiscal_id__article_id__recalculate_stock(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Article/{id}/RecalculateStock"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/RecalculateStock"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__post_multiple_post__api__fiscal_fiscal_id__article__multiple_currency(self, currency: str, articles: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Article/Multiple/{currency}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/Multiple/{currency}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=articles, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__put_multiple_put__api__fiscal_fiscal_id__article__inventory__multiple(self, articles: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Article/Inventory/Multiple"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/Inventory/Multiple"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=articles, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__post_multiple_for_import_task_post__api__fiscal_fiscal_id__article__multiple_for_import_task(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Article/MultipleForImportTask"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/MultipleForImportTask"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__post_multiple_partner_articles_post__api__fiscal_fiscal_id__article__partner_partner_id(self, partner_id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Article/Partner/{partnerId}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/Partner/{partner_id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__get_is_article_group_read_only_get__api__fiscal_fiscal_id__article_id__is_article_group_readonly(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/{id}/IsArticleGroupReadonly"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/IsArticleGroupReadonly"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__get_exists_get__api__fiscal_fiscal_id__article__exists(self, article_number: str, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/Exists"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/Exists"
        params: Dict[str, Any] = {}
        if article_number is not None:
            params['articleNumber'] = article_number
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__get_by_number_get__api__fiscal_fiscal_id__article__by_number(self, article_number: str, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/ByNumber"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/ByNumber"
        params: Dict[str, Any] = {}
        if article_number is not None:
            params['articleNumber'] = article_number
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__put_enable_inventory_put__api__fiscal_fiscal_id__article_id__enable_inventory(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Article/{id}/EnableInventory"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/EnableInventory"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__put_enable_bundle_put__api__fiscal_fiscal_id__article_id__enable_bundle(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Article/{id}/EnableBundle"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/EnableBundle"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__put_enable_inventory_by_group_put__api__fiscal_fiscal_id__article_group_id__article__enable_inventory(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ArticleGroup/{id}/Article/EnableInventory"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleGroup/{id}/Article/EnableInventory"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__put_disable_inventory_by_group_put__api__fiscal_fiscal_id__article_group_id__article__disable_inventory(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ArticleGroup/{id}/Article/DisableInventory"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleGroup/{id}/Article/DisableInventory"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__put_adjust_average_price_put__api__fiscal_fiscal_id__article_id__adjust_average_price(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Article/{id}/AdjustAveragePrice"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/AdjustAveragePrice"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__put_disable_inventory_put__api__fiscal_fiscal_id__article_id__disable_inventory(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Article/{id}/DisableInventory"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/DisableInventory"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__put_disable_bundle_put__api__fiscal_fiscal_id__article_id__disable_bundle(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Article/{id}/DisableBundle"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/DisableBundle"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__put_enable_article_variants_put__api__fiscal_fiscal_id__article_id__enable_article_variants(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Article/{id}/EnableArticleVariants"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/EnableArticleVariants"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__put_disable_article_variants_put__api__fiscal_fiscal_id__article_id__disable_article_variants(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Article/{id}/DisableArticleVariants"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/DisableArticleVariants"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__get_article_availability_list_by_location_get__api__fiscal_fiscal_id__article__availability_by_location(self, fiscal_id: str, location_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/AvailabilityByLocation"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/AvailabilityByLocation"
        params: Dict[str, Any] = {}
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

    def api_article__get_availability_get__api__fiscal_fiscal_id__article__availability(self, fiscal_id: str, query_string: str = None, article_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/Availability"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/Availability"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
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

    def api_article__get_availability_get__api__fiscal_fiscal_id__article_id__availablity(self, id: int, fiscal_id: str, variant_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/{id}/Availablity"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/Availablity"
        params: Dict[str, Any] = {}
        if variant_id is not None:
            params['variantId'] = variant_id
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__get_article_get__api__fiscal_fiscal_id__article_group_id__article(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ArticleGroup/{id}/Article"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleGroup/{id}/Article"
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

    def api_article__get_variant_get__api__fiscal_fiscal_id__article_id__variant(self, id: int, fiscal_id: str, query_string: str = None, remove_impossibles: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/{id}/Variant"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/Variant"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if remove_impossibles is not None:
            params['removeImpossibles'] = remove_impossibles
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__post_specify_variants_post__api__fiscal_fiscal_id__article__specify_variants(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Article/SpecifyVariants"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/SpecifyVariants"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__get_article_variant_get__api__fiscal_fiscal_id__article__article_variant(self, fiscal_id: str, query_string: str = None, partner_id: int = None, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/ArticleVariant"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/ArticleVariant"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if partner_id is not None:
            params['partnerId'] = partner_id
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

    def api_article__get_article_variant_detail_get__api__fiscal_fiscal_id__article_id__availability_by_location(self, id: int, fiscal_id: str, article_variant_id: int = None, query_string: str = None, exclude_location_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/{id}/AvailabilityByLocation"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/AvailabilityByLocation"
        params: Dict[str, Any] = {}
        if article_variant_id is not None:
            params['articleVariantId'] = article_variant_id
        if query_string is not None:
            params['queryString'] = query_string
        if exclude_location_id is not None:
            params['excludeLocationId'] = exclude_location_id
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__get_article_inventory_low_get__api__fiscal_fiscal_id__article__article_inventory_low(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/ArticleInventoryLow"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/ArticleInventoryLow"
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

    def api_article__get_location_inventory_low_get__api__fiscal_fiscal_id__article__location_inventory_low(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/LocationInventoryLow"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/LocationInventoryLow"
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

    def api_article__get_history_get__api__fiscal_fiscal_id__article__history(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/History"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/History"
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

    def api_article__post_copy_post__api__fiscal_fiscal_id__article_id__copy(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Article/{id}/Copy"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/Copy"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__get_search_get__api__fiscal_fiscal_id__article__search(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, filter_article_number: str = None, filter_description: str = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/Search"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/Search"
        params: Dict[str, Any] = {}
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        if filter_article_number is not None:
            params['filter.articleNumber'] = filter_article_number
        if filter_description is not None:
            params['filter.description'] = filter_description
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article__get_article_bundle_parents_get__api__fiscal_fiscal_id__article_id__bundle__parents(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/{id}/Bundle/Parents"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/Bundle/Parents"
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

    def api_article_group__get_get__api__fiscal_fiscal_id__article_group(self, fiscal_id: str, query_string: str = None, excluded_id: int = None, include_default: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ArticleGroup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleGroup"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if excluded_id is not None:
            params['excludedId'] = excluded_id
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

    def api_article_group__post_post__api__fiscal_fiscal_id__article_group(self, article_group: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ArticleGroup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleGroup"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=article_group, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_group__get_get__api__fiscal_fiscal_id__article_group_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ArticleGroup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleGroup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_group__put_put__api__fiscal_fiscal_id__article_group_id(self, article_group: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ArticleGroup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleGroup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=article_group, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_group__delete_delete__api__fiscal_fiscal_id__article_group_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ArticleGroup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleGroup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_group__get_duplicate_account_numbers_get__api__fiscal_fiscal_id__article_group_id__duplicate_account_numbers(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ArticleGroup/{id}/DuplicateAccountNumbers"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleGroup/{id}/DuplicateAccountNumbers"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_group__get_history_get__api__fiscal_fiscal_id__article_group__history(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ArticleGroup/History"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleGroup/History"
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

    def api_article_group__delete_merge_delete__api__fiscal_fiscal_id__article_group_article_group_to_deactivate_id__merge_into_article_group_to_keep_id(self, article_group_to_keep_id: int, article_group_to_deactivate_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ArticleGroup/{articleGroupToDeactivateId}/MergeInto/{articleGroupToKeepId}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleGroup/{article_group_to_deactivate_id}/MergeInto/{article_group_to_keep_id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_group__delete_articles_delete__api__fiscal_fiscal_id__article_group_id__delete_articles(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ArticleGroup/{id}/DeleteArticles"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleGroup/{id}/DeleteArticles"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_group__get_eu_type_list_get__api__fiscal_fiscal_id__article_group_eu_type(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ArticleGroup/EUType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleGroup/EUType"
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

    def api_article_group_vat_setup__get_get__api__fiscal_fiscal_id__article_group_id__vat_setup(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ArticleGroup/{id}/VatSetup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleGroup/{id}/VatSetup"
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

    def api_article_group_vat_setup__get_get__api__fiscal_fiscal_id__article_group_vat_setup_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ArticleGroupVatSetup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleGroupVatSetup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_group_vat_setup__put_put__api__fiscal_fiscal_id__article_group_vat_setup_id(self, article: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ArticleGroupVatSetup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleGroupVatSetup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=article, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_group_vat_setup__delete_delete__api__fiscal_fiscal_id__article_group_vat_setup_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ArticleGroupVatSetup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleGroupVatSetup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_group_vat_setup__post_post__api__fiscal_fiscal_id__article_group_vat_setup(self, article: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ArticleGroupVatSetup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleGroupVatSetup"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=article, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_location_setup__get_by_article_list_get__api__fiscal_fiscal_id__article_id__location_setup(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/{id}/LocationSetup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/LocationSetup"
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

    def api_article_location_setup__get_by_location_list_get__api__fiscal_fiscal_id__location_id__article_setup(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Location/{id}/ArticleSetup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Location/{id}/ArticleSetup"
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

    def api_article_location_setup__get_get__api__fiscal_fiscal_id__article_location_setup_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ArticleLocationSetup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleLocationSetup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_location_setup__put_put__api__fiscal_fiscal_id__article_location_setup_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ArticleLocationSetup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleLocationSetup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_location_setup__delete_delete__api__fiscal_fiscal_id__article_location_setup_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ArticleLocationSetup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleLocationSetup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_location_setup__post_post__api__fiscal_fiscal_id__article_location_setup(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ArticleLocationSetup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleLocationSetup"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_location_setup__post_multiple_post__api__fiscal_fiscal_id__article_location_setup__multiple(self, import_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ArticleLocationSetup/Multiple"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleLocationSetup/Multiple"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=import_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_mapping__get_by_article_list_get__api__fiscal_fiscal_id__article_id__article_mapping(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/{id}/ArticleMapping"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/ArticleMapping"
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

    def api_article_mapping__get_by_partner_list_get__api__fiscal_fiscal_id__partner_id__article_mapping(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/ArticleMapping"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/ArticleMapping"
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

    def api_article_mapping__get_by_partner_and_article_list_get__api__fiscal_fiscal_id__article_id__partner_partner_id__mapping(self, id: int, partner_id: int, article_variant_id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/{id}/Partner/{partnerId}/Mapping"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/Partner/{partner_id}/Mapping"
        params: Dict[str, Any] = {}
        if article_variant_id is not None:
            params['articleVariantId'] = article_variant_id
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_mapping__get_get__api__fiscal_fiscal_id__article_mapping_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ArticleMapping/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleMapping/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_mapping__put_put__api__fiscal_fiscal_id__article_mapping_id(self, article: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ArticleMapping/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleMapping/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=article, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_mapping__delete_delete__api__fiscal_fiscal_id__article_mapping_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ArticleMapping/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleMapping/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_mapping__post_post__api__fiscal_fiscal_id__article_mapping(self, article: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ArticleMapping"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleMapping"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=article, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_mapping__post_multiple_post__api__fiscal_fiscal_id__partner_partner_id__article_mapping__multiple(self, partner_id: int, mappings: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Partner/{partnerId}/ArticleMapping/Multiple"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{partner_id}/ArticleMapping/Multiple"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=mappings, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_relocation_task__get_list_get__api__fiscal_fiscal_id__article_relocation_task(self, fiscal_id: str, location_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ArticleRelocationTask"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleRelocationTask"
        params: Dict[str, Any] = {}
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

    def api_article_relocation_task__post_post__api__fiscal_fiscal_id__article_relocation_task(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ArticleRelocationTask"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleRelocationTask"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_relocation_task__get_get__api__fiscal_fiscal_id__article_relocation_task_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ArticleRelocationTask/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleRelocationTask/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_relocation_task__put_put__api__fiscal_fiscal_id__article_relocation_task_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ArticleRelocationTask/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleRelocationTask/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_relocation_task__delete_delete__api__fiscal_fiscal_id__article_relocation_task_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ArticleRelocationTask/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleRelocationTask/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_relocation_task__put_move_put__api__fiscal_fiscal_id__article_relocation_task_id__move(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ArticleRelocationTask/{id}/Move"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleRelocationTask/{id}/Move"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_variant__get_article_variant_get__api__fiscal_fiscal_id__article_variant_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ArticleVariant/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleVariant/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_variant__put_article_variant_put__api__fiscal_fiscal_id__article_variant_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ArticleVariant/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleVariant/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_variant__delete_article_variant_delete__api__fiscal_fiscal_id__article_variant_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ArticleVariant/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleVariant/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_article_variant__post_article_variant_post__api__fiscal_fiscal_id__article_variant(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/ArticleVariant"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleVariant"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bar_code__get_by_article_list_get__api__fiscal_fiscal_id__article_id__bar_code(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/{id}/BarCode"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/BarCode"
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

    def api_bar_code__get_get__api__fiscal_fiscal_id__bar_code_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/BarCode/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BarCode/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bar_code__put_put__api__fiscal_fiscal_id__bar_code_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/BarCode/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BarCode/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bar_code__delete_delete__api__fiscal_fiscal_id__bar_code_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/BarCode/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BarCode/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bar_code__post_post__api__fiscal_fiscal_id__bar_code(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/BarCode"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BarCode"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bar_code__post_multiple_post__api__fiscal_fiscal_id__bar_code__multiple(self, bar_codes: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/BarCode/Multiple"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BarCode/Multiple"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=bar_codes, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bar_code__get_by_ean_number_get__api__fiscal_fiscal_id__bar_code__by_ean_number_ean_number(self, ean_number: str, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/BarCode/ByEANNumber/{eanNumber}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BarCode/ByEANNumber/{ean_number}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bundle_item__get_list_get__api__fiscal_fiscal_id__article_id__bundle_item(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/{id}/BundleItem"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/BundleItem"
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

    def api_bundle_item__get_get__api__fiscal_fiscal_id__bundle_item_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/BundleItem/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BundleItem/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bundle_item__put_put__api__fiscal_fiscal_id__bundle_item_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/BundleItem/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BundleItem/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bundle_item__delete_delete__api__fiscal_fiscal_id__bundle_item_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/BundleItem/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BundleItem/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_bundle_item__post_post__api__fiscal_fiscal_id__bundle_item(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/BundleItem"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/BundleItem"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_location__get_get__api__fiscal_fiscal_id__location(self, fiscal_id: str, warehouse_id: int = None, querystring: str = None, include_default: bool = None, excluded_id: int = None, location_type: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Location"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Location"
        params: Dict[str, Any] = {}
        if warehouse_id is not None:
            params['warehouseId'] = warehouse_id
        if querystring is not None:
            params['querystring'] = querystring
        if include_default is not None:
            params['includeDefault'] = include_default
        if excluded_id is not None:
            params['excludedId'] = excluded_id
        if location_type is not None:
            params['locationType'] = location_type
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_location__post_post__api__fiscal_fiscal_id__location(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Location"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Location"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_location__get_get__api__fiscal_fiscal_id__location_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Location/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Location/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_location__put_put__api__fiscal_fiscal_id__location_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Location/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Location/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_location__delete_delete__api__fiscal_fiscal_id__location_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Location/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Location/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_location__delete_merge_into_delete__api__fiscal_fiscal_id__location_location_to_deactivate_id__merge_into_location_to_keep_id(self, location_to_keep_id: int, location_to_deactivate_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Location/{locationToDeactivateId}/MergeInto/{locationToKeepId}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Location/{location_to_deactivate_id}/MergeInto/{location_to_keep_id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_location__get_location_type_get__api__fiscal_fiscal_id__location__location_type(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Location/LocationType"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Location/LocationType"
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

    def api_stock_count__get_get__api__fiscal_fiscal_id__stock_count(self, fiscal_id: str, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/StockCount"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/StockCount"
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

    def api_stock_count__post_post__api__fiscal_fiscal_id__stock_count(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/StockCount"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/StockCount"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_stock_count__get_get__api__fiscal_fiscal_id__stock_count_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/StockCount/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/StockCount/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_stock_count__put_put__api__fiscal_fiscal_id__stock_count_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/StockCount/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/StockCount/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_stock_count__delete_delete__api__fiscal_fiscal_id__stock_count_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/StockCount/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/StockCount/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_stock_count__put_bookkeep_put__api__fiscal_fiscal_id__stock_count_id__bookkeep(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/StockCount/{id}/Bookkeep"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/StockCount/{id}/Bookkeep"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_stock_count__get_can_bookkeep_get__api__fiscal_fiscal_id__stock_count_id__can_bookkeep(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/StockCount/{id}/CanBookkeep"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/StockCount/{id}/CanBookkeep"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_stock_count__put_reset_put__api__fiscal_fiscal_id__stock_count_id__reset(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/StockCount/{id}/Reset"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/StockCount/{id}/Reset"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_stock_count_draft__get_get__api__fiscal_fiscal_id__stock_count_id__draft(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/StockCount/{id}/Draft"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/StockCount/{id}/Draft"
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

    def api_stock_count_draft__get_get__api__fiscal_fiscal_id__stock_count_draft_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/StockCountDraft/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/StockCountDraft/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_stock_count_draft__put_put__api__fiscal_fiscal_id__stock_count_draft_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/StockCountDraft/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/StockCountDraft/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_stock_count_draft__delete_delete__api__fiscal_fiscal_id__stock_count_draft_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/StockCountDraft/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/StockCountDraft/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_stock_count_draft__put_reset_put__api__fiscal_fiscal_id__stock_count_draft_id__reset(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/StockCountDraft/{id}/Reset"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/StockCountDraft/{id}/Reset"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_stock_count_draft__post_post__api__fiscal_fiscal_id__stock_count_draft(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/StockCountDraft"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/StockCountDraft"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_stock_count_draft__put_multiple_put__api__fiscal_fiscal_id__stock_count_draft__multiple(self, stock_count: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/StockCountDraft/Multiple"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/StockCountDraft/Multiple"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=stock_count, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_unit__get_get__api__fiscal_fiscal_id__unit(self, fiscal_id: str, query_string: str = None, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Unit"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Unit"
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

    def api_unit__post_post__api__fiscal_fiscal_id__unit(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Unit"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Unit"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_unit__get_get__api__fiscal_fiscal_id__unit_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Unit/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Unit/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_unit__put_put__api__fiscal_fiscal_id__unit_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Unit/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Unit/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_unit__delete_delete__api__fiscal_fiscal_id__unit_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Unit/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Unit/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_variant__get_get__api__fiscal_fiscal_id__variant_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Variant/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Variant/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_variant__put_put__api__fiscal_fiscal_id__variant_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Variant/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Variant/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_variant__delete_delete__api__fiscal_fiscal_id__variant_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Variant/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Variant/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_variant__post_post__api__fiscal_fiscal_id__variant(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Variant"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Variant"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_variant_range__get_get__api__fiscal_fiscal_id__variant_range(self, fiscal_id: str, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VariantRange"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VariantRange"
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

    def api_variant_range__post_post__api__fiscal_fiscal_id__variant_range(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/VariantRange"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VariantRange"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_variant_range__get_get__api__fiscal_fiscal_id__variant_range_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VariantRange/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VariantRange/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_variant_range__put_put__api__fiscal_fiscal_id__variant_range_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/VariantRange/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VariantRange/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_variant_range__delete_delete__api__fiscal_fiscal_id__variant_range_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/VariantRange/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VariantRange/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_variant_range__get_variant_list_get__api__fiscal_fiscal_id__variant_range_id__variant(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VariantRange/{id}/Variant"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VariantRange/{id}/Variant"
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

    def api_warehouse__get_get__api__fiscal_fiscal_id__warehouse(self, fiscal_id: str, query_string: str = None, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Warehouse"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Warehouse"
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

    def api_warehouse__post_post__api__fiscal_fiscal_id__warehouse(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Warehouse"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Warehouse"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_warehouse__get_get__api__fiscal_fiscal_id__warehouse_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Warehouse/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Warehouse/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_warehouse__put_put__api__fiscal_fiscal_id__warehouse_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Warehouse/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Warehouse/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_warehouse__delete_delete__api__fiscal_fiscal_id__warehouse_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Warehouse/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Warehouse/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text
