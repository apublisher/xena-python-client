from typing import Any, Dict, Optional
import requests

class PriceApi:
    """API client for the Price domain of the Xena API."""
    def __init__(self, base_url: str, session: Optional[requests.Session] = None) -> None:
        self.base_url = base_url.rstrip('/')
        self.session = session or requests.Session()

    def api_price_discount_agreement__get_by_article_group_get__api__fiscal_fiscal_id__article_group_id__price_discount_agreement(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ArticleGroup/{id}/PriceDiscountAgreement"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ArticleGroup/{id}/PriceDiscountAgreement"
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

    def api_price_discount_agreement__get_by_article_get__api__fiscal_fiscal_id__article_id__price_discount_agreement(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Article/{id}/PriceDiscountAgreement"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Article/{id}/PriceDiscountAgreement"
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

    def api_price_discount_agreement__get_by_price_group_get__api__fiscal_fiscal_id__price_group_id__price_discount_agreement(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PriceGroup/{id}/PriceDiscountAgreement"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PriceGroup/{id}/PriceDiscountAgreement"
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

    def api_price_discount_agreement__get_by_partner_get__api__fiscal_fiscal_id__partner_id__price_discount_agreement(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Partner/{id}/PriceDiscountAgreement"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Partner/{id}/PriceDiscountAgreement"
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

    def api_price_discount_agreement__get_get__api__fiscal_fiscal_id__price_discount_agreement_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PriceDiscountAgreement/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PriceDiscountAgreement/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_price_discount_agreement__put_put__api__fiscal_fiscal_id__price_discount_agreement_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/PriceDiscountAgreement/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PriceDiscountAgreement/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_price_discount_agreement__delete_delete__api__fiscal_fiscal_id__price_discount_agreement_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/PriceDiscountAgreement/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PriceDiscountAgreement/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_price_discount_agreement__post_post__api__fiscal_fiscal_id__price_discount_agreement(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/PriceDiscountAgreement"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PriceDiscountAgreement"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_price_group__get_get__api__fiscal_fiscal_id__price_group(self, fiscal_id: str, query_string: str = None, include_defaults: bool = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PriceGroup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PriceGroup"
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

    def api_price_group__post_post__api__fiscal_fiscal_id__price_group(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/PriceGroup"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PriceGroup"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_price_group__get_get__api__fiscal_fiscal_id__price_group_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/PriceGroup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PriceGroup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_price_group__put_put__api__fiscal_fiscal_id__price_group_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/PriceGroup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PriceGroup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_price_group__delete_delete__api__fiscal_fiscal_id__price_group_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/PriceGroup/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/PriceGroup/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_volume_price_agreement__get_get__api__fiscal_fiscal_id__volume_price_agreement(self, fiscal_id: str, partner_id: int = None, price_group_id: int = None, article_id: int = None, per_date: int = None, context_type: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VolumePriceAgreement"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VolumePriceAgreement"
        params: Dict[str, Any] = {}
        if partner_id is not None:
            params['partnerId'] = partner_id
        if price_group_id is not None:
            params['priceGroupId'] = price_group_id
        if article_id is not None:
            params['articleId'] = article_id
        if per_date is not None:
            params['perDate'] = per_date
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

    def api_volume_price_agreement__post_post__api__fiscal_fiscal_id__volume_price_agreement(self, dto: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/VolumePriceAgreement"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VolumePriceAgreement"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_volume_price_agreement__get_get__api__fiscal_fiscal_id__volume_price_agreement_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/VolumePriceAgreement/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VolumePriceAgreement/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_volume_price_agreement__put_put__api__fiscal_fiscal_id__volume_price_agreement_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/VolumePriceAgreement/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VolumePriceAgreement/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_volume_price_agreement__delete_delete__api__fiscal_fiscal_id__volume_price_agreement_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/VolumePriceAgreement/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VolumePriceAgreement/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_volume_price_agreement__post_render_price_agreement_report_post__api__fiscal_fiscal_id__volume_price_agreement__render_price_agreement_report(self, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/VolumePriceAgreement/RenderPriceAgreementReport"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/VolumePriceAgreement/RenderPriceAgreementReport"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text
