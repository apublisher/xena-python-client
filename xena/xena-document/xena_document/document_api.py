from typing import Any, Dict, Optional
import requests

class DocumentApi:
    """API client for the Document domain of the Xena API."""
    def __init__(self, base_url: str, session: Optional[requests.Session] = None) -> None:
        self.base_url = base_url.rstrip('/')
        self.session = session or requests.Session()

    def api_document__get_get__api__fiscal_fiscal_id__document(self, fiscal_id: str, query_string: str = None, date_from: int = None, date_to: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Document"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Document"
        params: Dict[str, Any] = {}
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

    def api_document__get_get__api__fiscal_fiscal_id__document_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Document/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Document/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document__delete_delete__api__fiscal_fiscal_id__document_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Document/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Document/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document__get_by_type_get__api__fiscal_fiscal_id_type_parent_id__document(self, type: str, parent_id: int, fiscal_id: str, query_string: str = None, date_from: int = None, date_to: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/{type}/{parentId}/Document"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/{type}/{parent_id}/Document"
        params: Dict[str, Any] = {}
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

    def api_document__get_inbox_get__api__fiscal_fiscal_id__document__inbox(self, fiscal_id: str, query_string: str = None, resource_context_id: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Document/Inbox"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Document/Inbox"
        params: Dict[str, Any] = {}
        if query_string is not None:
            params['queryString'] = query_string
        if resource_context_id is not None:
            params['resourceContextId'] = resource_context_id
        if list_options_show_deactivated is not None:
            params['listOptions.showDeactivated'] = list_options_show_deactivated
        if list_options_page is not None:
            params['listOptions.page'] = list_options_page
        if list_options_page_size is not None:
            params['listOptions.pageSize'] = list_options_page_size
        if list_options_force_no_paging is not None:
            params['listOptions.forceNoPaging'] = list_options_force_no_paging
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document__get_history_get__api__fiscal_fiscal_id__document__history(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Document/History"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Document/History"
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

    def api_document__put_name_and_description_put__api__fiscal_fiscal_id__document_id__name_and_description(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Document/{id}/NameAndDescription"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Document/{id}/NameAndDescription"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document__get_shared_from_partner_get__api__fiscal_fiscal_id__document__partner_id__shared(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Document/Partner/{id}/Shared"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Document/Partner/{id}/Shared"
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

    def api_document__get_shared_from_fiscal_get__api__fiscal_fiscal_id__document__fiscal_setup_id__shared(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Document/FiscalSetup/{id}/Shared"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Document/FiscalSetup/{id}/Shared"
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

    def api_document__put_rotate_put__api__fiscal_fiscal_id__document_id__rotate(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Document/{id}/Rotate"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Document/{id}/Rotate"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document__post_relation_post__api__fiscal_fiscal_id__document_id__relation_relation_type_relation_id_document_folder_id(self, id: int, relation_type: str, relation_id: int, document_folder_id: int, fiscal_id: str, existing_relation_type: str = None, existing_relation_id: int = None, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Document/{id}/Relation/{relationType}/{relationId}/{documentFolderId}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Document/{id}/Relation/{relation_type}/{relation_id}/{document_folder_id}"
        params: Dict[str, Any] = {}
        if existing_relation_type is not None:
            params['existingRelationType'] = existing_relation_type
        if existing_relation_id is not None:
            params['existingRelationId'] = existing_relation_id
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document__delete_relation_delete__api__fiscal_fiscal_id__document_id__relation_relation_type_relation_id_document_folder_id(self, id: int, relation_id: int, relation_type: str, document_folder_id: int, fiscal_id: str, try_delete_document: bool = None, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/Document/{id}/Relation/{relationType}/{relationId}/{documentFolderId}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Document/{id}/Relation/{relation_type}/{relation_id}/{document_folder_id}"
        params: Dict[str, Any] = {}
        if try_delete_document is not None:
            params['tryDeleteDocument'] = try_delete_document
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document__put_move_relation_to_folder_put__api__fiscal_fiscal_id__document_id__relation_relation_type_relation_id_document_folder_id__move_to_folder(self, id: int, relation_type: str, relation_id: int, document_folder_id: int, fiscal_id: str, target_document_folder_id: int = None, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Document/{id}/Relation/{relationType}/{relationId}/{documentFolderId}/MoveToFolder"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Document/{id}/Relation/{relation_type}/{relation_id}/{document_folder_id}/MoveToFolder"
        params: Dict[str, Any] = {}
        if target_document_folder_id is not None:
            params['targetDocumentFolderId'] = target_document_folder_id
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document__post_relation_from_version_post__api__fiscal_fiscal_id__document_id__version_from_xena_document_parent_id(self, id: int, parent_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Document/{id}/VersionFromXenaDocument/{parentId}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Document/{id}/VersionFromXenaDocument/{parent_id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document__get_last_version_get__api__fiscal_fiscal_id__document__document_id__last_version(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Document/Document/{id}/LastVersion"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Document/Document/{id}/LastVersion"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document__get_document_version_get__api__fiscal_fiscal_id__document__document_version_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Document/DocumentVersion/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Document/DocumentVersion/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document__get_version_get__api__fiscal_fiscal_id__document_id__version(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Document/{id}/Version"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Document/{id}/Version"
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

    def api_document__put_version_note_put__api__fiscal_fiscal_id__document__version_id__note(self, id: int, data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/Document/Version/{id}/Note"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Document/Version/{id}/Note"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document__get_relation_get__api__fiscal_fiscal_id__document_id__relation(self, id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/Document/{id}/Relation"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Document/{id}/Relation"
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

    def api_document__post_move_document_to_other_resource_inbox_post__api__fiscal_fiscal_id__document__document_id__resource_resource_context_id(self, id: int, resource_context_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/Document/Document/{id}/Resource/{resourceContextId}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/Document/Document/{id}/Resource/{resource_context_id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document_folder__get_get__api__fiscal_fiscal_id__document_folder(self, entity_id: int, fiscal_id: str, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/DocumentFolder"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DocumentFolder"
        params: Dict[str, Any] = {}
        if entity_id is not None:
            params['entityId'] = entity_id
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

    def api_document_folder__post_post__api__fiscal_fiscal_id__document_folder(self, create_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/DocumentFolder"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DocumentFolder"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=create_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document_folder__get_get__api__fiscal_fiscal_id__document_folder_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/DocumentFolder/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DocumentFolder/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document_folder__put_put__api__fiscal_fiscal_id__document_folder_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/DocumentFolder/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DocumentFolder/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document_folder__delete_delete__api__fiscal_fiscal_id__document_folder_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/DocumentFolder/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DocumentFolder/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document_folder__get_list_with_documents_get__api__fiscal_fiscal_id__document_folder__list_with_documents(self, entity_type: str, entity_id: int, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, filter_query_string: str = None, filter_document_folder_id: int = None, filter_document_folder_tags: list = None, filter_include_documents_from_root_folder: bool = None, filter_ignore_folders: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/DocumentFolder/ListWithDocuments"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DocumentFolder/ListWithDocuments"
        params: Dict[str, Any] = {}
        if entity_type is not None:
            params['entityType'] = entity_type
        if entity_id is not None:
            params['entityId'] = entity_id
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
        if filter_document_folder_id is not None:
            params['filter.documentFolderId'] = filter_document_folder_id
        if filter_document_folder_tags is not None:
            params['filter.documentFolderTags'] = filter_document_folder_tags
        if filter_include_documents_from_root_folder is not None:
            params['filter.includeDocumentsFromRootFolder'] = filter_include_documents_from_root_folder
        if filter_ignore_folders is not None:
            params['filter.ignoreFolders'] = filter_ignore_folders
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document_folder_configuration__get_get__api__fiscal_fiscal_id__document_folder_configuration(self, document_folder_type: str, fiscal_id: str, query_string: str = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/DocumentFolderConfiguration"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DocumentFolderConfiguration"
        params: Dict[str, Any] = {}
        if document_folder_type is not None:
            params['documentFolderType'] = document_folder_type
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

    def api_document_folder_configuration__post_post__api__fiscal_fiscal_id__document_folder_configuration(self, create_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Fiscal/{fiscalId}/DocumentFolderConfiguration"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DocumentFolderConfiguration"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=create_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document_folder_configuration__get_get__api__fiscal_fiscal_id__document_folder_configuration_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/DocumentFolderConfiguration/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DocumentFolderConfiguration/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document_folder_configuration__put_put__api__fiscal_fiscal_id__document_folder_configuration_id(self, dto: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/DocumentFolderConfiguration/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DocumentFolderConfiguration/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=dto, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_document_folder_configuration__delete_delete__api__fiscal_fiscal_id__document_folder_configuration_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/DocumentFolderConfiguration/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/DocumentFolderConfiguration/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_resource_inbox_document_relation__get_get__api__fiscal_fiscal_id__resource_inbox_document_relation_id(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ResourceInboxDocumentRelation/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ResourceInboxDocumentRelation/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_resource_inbox_document_relation__put_put__api__fiscal_fiscal_id__resource_inbox_document_relation_id(self, relation: Dict[str, Any], fiscal_id: str, id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ResourceInboxDocumentRelation/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ResourceInboxDocumentRelation/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, json=relation, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_resource_inbox_document_relation__delete_delete__api__fiscal_fiscal_id__resource_inbox_document_relation_id(self, id: int, fiscal_id: str, try_delete_document: bool = None, **kwargs) -> Any:
        """Auto-generated method for DELETE /Api/Fiscal/{fiscalId}/ResourceInboxDocumentRelation/{id}"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ResourceInboxDocumentRelation/{id}"
        params: Dict[str, Any] = {}
        if try_delete_document is not None:
            params['tryDeleteDocument'] = try_delete_document
        headers: Dict[str, Any] = {}
        response = self.session.delete(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_resource_inbox_document_relation__put_mark_read_put__api__fiscal_fiscal_id__resource_inbox_document_relation_id__mark_read(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for PUT /Api/Fiscal/{fiscalId}/ResourceInboxDocumentRelation/{id}/MarkRead"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ResourceInboxDocumentRelation/{id}/MarkRead"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.put(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def api_resource_inbox_document_relation__get_relations_for_inbox_get__api__fiscal_fiscal_id__resource_inbox_document_relation__by_resource(self, fiscal_id: str, resource_id: int = None, is_new: bool = None, is_parked: bool = None, is_all_approved: bool = None, date_from: int = None, date_to: int = None, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ResourceInboxDocumentRelation/ByResource"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ResourceInboxDocumentRelation/ByResource"
        params: Dict[str, Any] = {}
        if resource_id is not None:
            params['resourceId'] = resource_id
        if is_new is not None:
            params['isNew'] = is_new
        if is_parked is not None:
            params['isParked'] = is_parked
        if is_all_approved is not None:
            params['isAllApproved'] = is_all_approved
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

    def api_resource_inbox_document_relation__get_resource_inbox_get__api__fiscal_fiscal_id__resource_inbox_document_relation__get_resource_inbox(self, fiscal_id: str, list_options_show_deactivated: bool = None, list_options_page: int = None, list_options_page_size: int = None, list_options_force_no_paging: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Fiscal/{fiscalId}/ResourceInboxDocumentRelation/GetResourceInbox"""
        url = f"{self.base_url}/Api/Fiscal/{fiscal_id}/ResourceInboxDocumentRelation/GetResourceInbox"
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

    def blob_fiscal__post_by_type_post__api__blob__fiscal_fiscal_id_relation_type_relation_id(self, relation_type: str, relation_id: int, fiscal_id: str, document_folder_id: int = None, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Blob/Fiscal/{fiscalId}/{relationType}/{relationId}"""
        url = f"{self.base_url}/Api/Blob/Fiscal/{fiscal_id}/{relation_type}/{relation_id}"
        params: Dict[str, Any] = {}
        if document_folder_id is not None:
            params['documentFolderId'] = document_folder_id
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def blob_fiscal__post_document_from_url_by_type_post__api__blob__fiscal_fiscal_id__from_url_relation_type_relation_id(self, relation_type: str, relation_id: int, data: Dict[str, Any], fiscal_id: str, document_folder_id: int = None, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Blob/Fiscal/{fiscalId}/FromUrl/{relationType}/{relationId}"""
        url = f"{self.base_url}/Api/Blob/Fiscal/{fiscal_id}/FromUrl/{relation_type}/{relation_id}"
        params: Dict[str, Any] = {}
        if document_folder_id is not None:
            params['documentFolderId'] = document_folder_id
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def blob_fiscal__get_download_get__api__blob__fiscal_fiscal_id__download_version_id(self, version_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Blob/Fiscal/{fiscalId}/Download/{versionId}"""
        url = f"{self.base_url}/Api/Blob/Fiscal/{fiscal_id}/Download/{version_id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def blob_fiscal__download_multiple_post__api__blob__fiscal_fiscal_id__download(self, post_download_data: Dict[str, Any], fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Blob/Fiscal/{fiscalId}/Download"""
        url = f"{self.base_url}/Api/Blob/Fiscal/{fiscal_id}/Download"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, json=post_download_data, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def blob_fiscal__get_download_by_document_get__api__blob__fiscal_fiscal_id_id__download(self, id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Blob/Fiscal/{fiscalId}/{id}/Download"""
        url = f"{self.base_url}/Api/Blob/Fiscal/{fiscal_id}/{id}/Download"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def blob_fiscal__get_inline_get__api__blob__fiscal_fiscal_id__inline_version_id(self, version_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Blob/Fiscal/{fiscalId}/Inline/{versionId}"""
        url = f"{self.base_url}/Api/Blob/Fiscal/{fiscal_id}/Inline/{version_id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def blob_fiscal__get_xml_converted_get__api__blob__fiscal_fiscal_id__xml_converted_version_id(self, version_id: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Blob/Fiscal/{fiscalId}/XmlConverted/{versionId}"""
        url = f"{self.base_url}/Api/Blob/Fiscal/{fiscal_id}/XmlConverted/{version_id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def blob_fiscal__get_thumbnail_by_document_get__api__blob__fiscal_fiscal_id__thumbnail_by_document_document_id(self, document_id: int, width: int, height: int, fiscal_id: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Blob/Fiscal/{fiscalId}/ThumbnailByDocument/{documentId}"""
        url = f"{self.base_url}/Api/Blob/Fiscal/{fiscal_id}/ThumbnailByDocument/{document_id}"
        params: Dict[str, Any] = {}
        if width is not None:
            params['width'] = width
        if height is not None:
            params['height'] = height
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def blob_fiscal__get_scaled_image_get__api__blob__fiscal_fiscal_id__scaled_image_document_version_id(self, document_version_id: int, fiscal_id: str, data_width: int = None, data_height: int = None, data_page: int = None, data_cropped: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Blob/Fiscal/{fiscalId}/ScaledImage/{documentVersionId}"""
        url = f"{self.base_url}/Api/Blob/Fiscal/{fiscal_id}/ScaledImage/{document_version_id}"
        params: Dict[str, Any] = {}
        if data_width is not None:
            params['data.width'] = data_width
        if data_height is not None:
            params['data.height'] = data_height
        if data_page is not None:
            params['data.page'] = data_page
        if data_cropped is not None:
            params['data.cropped'] = data_cropped
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def blob_public__get_thumbnail_by_v_card_cache_get__api__blob__public_v_card_id__thumbnail_vi(self, id: int, width: int, height: int, message: dict, vi: str, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Blob/Public/VCard/{id}/Thumbnail/{vi}"""
        url = f"{self.base_url}/Api/Blob/Public/VCard/{id}/Thumbnail/{vi}"
        params: Dict[str, Any] = {}
        if width is not None:
            params['width'] = width
        if height is not None:
            params['height'] = height
        if message is not None:
            params['message'] = message
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def blob_public__get_thumbnail_by_v_card_get__api__blob__public_v_card_id__thumbnail(self, id: int, width: int, height: int, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Blob/Public/VCard/{id}/Thumbnail"""
        url = f"{self.base_url}/Api/Blob/Public/VCard/{id}/Thumbnail"
        params: Dict[str, Any] = {}
        if width is not None:
            params['width'] = width
        if height is not None:
            params['height'] = height
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def blob_public__get_thumbnail_by_xena_app_get__api__blob__public__xena_app_id__thumbnail(self, id: int, width: int, height: int, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Blob/Public/XenaApp/{id}/Thumbnail"""
        url = f"{self.base_url}/Api/Blob/Public/XenaApp/{id}/Thumbnail"
        params: Dict[str, Any] = {}
        if width is not None:
            params['width'] = width
        if height is not None:
            params['height'] = height
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def blob_public__get_thumbnail_by_xena_temp_app_get__api__blob__public__xena_temp_app_id__thumbnail(self, id: int, width: int, height: int, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Blob/Public/XenaTempApp/{id}/Thumbnail"""
        url = f"{self.base_url}/Api/Blob/Public/XenaTempApp/{id}/Thumbnail"
        params: Dict[str, Any] = {}
        if width is not None:
            params['width'] = width
        if height is not None:
            params['height'] = height
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def blob_public__get_terms_culture_get__api__blob__public__terms_culture_id(self, id: int, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Blob/Public/TermsCulture/{id}"""
        url = f"{self.base_url}/Api/Blob/Public/TermsCulture/{id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def blob_user__post_post__api__blob__user(self, **kwargs) -> Any:
        """Auto-generated method for POST /Api/Blob/User"""
        url = f"{self.base_url}/Api/Blob/User"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.post(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def blob_user__get_download_get__api__blob__user__download_version_id(self, version_id: int, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Blob/User/Download/{versionId}"""
        url = f"{self.base_url}/Api/Blob/User/Download/{version_id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def blob_user__get_inline_get__api__blob__user__inline_version_id(self, version_id: int, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Blob/User/Inline/{versionId}"""
        url = f"{self.base_url}/Api/Blob/User/Inline/{version_id}"
        params: Dict[str, Any] = {}
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def blob_user__get_scaled_image_get__api__blob__user__scaled_image_document_version_id(self, document_version_id: int, data_width: int = None, data_height: int = None, data_page: int = None, data_cropped: bool = None, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Blob/User/ScaledImage/{documentVersionId}"""
        url = f"{self.base_url}/Api/Blob/User/ScaledImage/{document_version_id}"
        params: Dict[str, Any] = {}
        if data_width is not None:
            params['data.width'] = data_width
        if data_height is not None:
            params['data.height'] = data_height
        if data_page is not None:
            params['data.page'] = data_page
        if data_cropped is not None:
            params['data.cropped'] = data_cropped
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def blob_user__get_thumbnail_by_document_get__api__blob__user__thumbnail_by_document_document_id(self, document_id: int, width: int, height: int, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Blob/User/ThumbnailByDocument/{documentId}"""
        url = f"{self.base_url}/Api/Blob/User/ThumbnailByDocument/{document_id}"
        params: Dict[str, Any] = {}
        if width is not None:
            params['width'] = width
        if height is not None:
            params['height'] = height
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def blob_user__get_user_image_get__api__blob__user__user_v_card_image(self, width: int, height: int, **kwargs) -> Any:
        """Auto-generated method for GET /Api/Blob/User/UserVCardImage"""
        url = f"{self.base_url}/Api/Blob/User/UserVCardImage"
        params: Dict[str, Any] = {}
        if width is not None:
            params['width'] = width
        if height is not None:
            params['height'] = height
        headers: Dict[str, Any] = {}
        response = self.session.get(url, params=params, headers=headers, **kwargs)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text
