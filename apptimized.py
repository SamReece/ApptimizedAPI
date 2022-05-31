import requests
from requests.structures import CaseInsensitiveDict
import json


class ApptimizedAPI(object):
    """The main suite that contains the JSON ingestion methods"""

    def __init__(self, token):
        self.token = token
        self.headers = CaseInsensitiveDict()
        self.headers["Accept"] = "application/json"
        self.headers["Authorization"] = "Bearer {}".format(self.token)
        self.validate = "https://app.apptimized.com/api/token/checkToken"

    def connection_without_params(self, url):
        """download without parameters"""
        try:
            request = requests.get(url, headers=self.headers)
            return request
        except requests.exceptions.HTTPError as errh:
            return errh
        except requests.exceptions.ConnectionError as errc:
            return errc
        except requests.exceptions.Timeout as errt:
            return errt
        except requests.exceptions.RequestException as err:
            return err

    def post_request(self, url, data):
        """download without parameters"""
        try:
            post = requests.post(
                url,
                headers=self.headers,
                data=data,
            )
            return post
        except requests.exceptions.HTTPError as errh:
            return errh
        except requests.exceptions.ConnectionError as errc:
            return errc
        except requests.exceptions.Timeout as errt:
            return errt
        except requests.exceptions.RequestException as err:
            return err

    def delete_request(self, url):
        """download without parameters"""
        try:
            request = requests.delete(url, headers=self.headers)
            return request
        except requests.exceptions.HTTPError as errh:
            return errh
        except requests.exceptions.ConnectionError as errc:
            return errc
        except requests.exceptions.Timeout as errt:
            return errt
        except requests.exceptions.RequestException as err:
            return err

    def put_request(self, url, data):
        """download without parameters"""
        try:
            put = requests.put(
                url,
                headers=self.headers,
                data=data,
            )
            return put
        except requests.exceptions.HTTPError as errh:
            return errh
        except requests.exceptions.ConnectionError as errc:
            return errc
        except requests.exceptions.Timeout as errt:
            return errt
        except requests.exceptions.RequestException as err:
            return err

    def patch_request(self, url, data):
        """download without parameters"""
        try:
            patch = requests.patch(
                url,
                headers=self.headers,
                data=data,
            )
            return patch
        except requests.exceptions.HTTPError as errh:
            return errh
        except requests.exceptions.ConnectionError as errc:
            return errc
        except requests.exceptions.Timeout as errt:
            return errt
        except requests.exceptions.RequestException as err:
            return err

    def download_from_Url(self, url, fileName, fileExtension):
        download = url
        response = requests.get(url)
        open("{}.{}".format(fileName, fileExtension)).write(response.content)

    def validate_access_token(self):
        validation = self.connection_without_params(self.validate)
        return validation.json()


class ApptimizedApplications(ApptimizedAPI):
    """A class used to represent the Applications block"""

    def __init__(self, token):
        super().__init__(token)

    def create_application(
        self,
        projectId,
        vendor,
        software,
        version,
        language,
        FormFileCollection=None,
        DiscoveryDoc=None,
        FilesUrls=None,
        DocumentUrl=None,
        ParentId=None,
        ApplicationOwnerEmail=None,
    ):
        data = {
            "Vendor": vendor,
            "Software": software,
            "Version": version,
            "Language": language,
            "FormFileCollection": FormFileCollection,
            "DiscoveryDoc": DiscoveryDoc,
            "FilesUrls": FilesUrls,
            "DocumentUrl": DocumentUrl,
            "ParentId": ParentId,
            "ApplicationOwnerEmail": ApplicationOwnerEmail,
        }
        url = "https://app.apptimized.com/api/projects/{}/applications".format(
            projectId
        )
        application = self.post_request(url, data)
        return application.json()

    def delete_application(self, projectId, moduleId):
        url = "https://app.apptimized.com/api/projects/{}/applications/{}".format(
            projectId, moduleId
        )
        removeApplication = self.delete_request(url)
        return removeApplication.json()

    def update_application_metadata(
        self,
        projectId,
        workflowId,
        vendor=None,
        software=None,
        version=None,
        language=None,
        parentId=None,
        applicationOwnerEmail=None,
    ):
        data = {
            "Vendor": vendor,
            "Software": software,
            "Version": version,
            "Language": language,
            "ParentId": parentId,
            "ApplicationOwnerEmail": applicationOwnerEmail,
        }
        url = "https://app.apptimized.com/api/projects/{}/applications/{}".format(
            projectId, workflowId
        )
        updateMeta = self.put_request(url, data)
        return updateMeta.json()

    def update_application_sources_and_discovery_doc(
        self,
        projectId,
        workflowId,
        formFileCollection=None,
        discoveryDoc=None,
        filesUrls=None,
        documentUrl=None,
    ):
        data = {
            "FormFileCollection": formFileCollection,
            "DiscoveryDoc": discoveryDoc,
            "FilesUrls": filesUrls,
            "DocumentUrl": documentUrl,
        }
        url = (
            "https://app.apptimized.com/api/projects/{}/applications/{}/source".format(
                projectId, workflowId
            )
        )
        updateApplication = self.put_request(url, data)
        return updateApplication.json()

    def get_applications(self, id):
        url = "https://app.apptimized.com/api/projects/{}/applications".format(id)
        application = self.connection_without_params(url)
        return application.json()

    def get_applicaton_info(self, projectId, workflowId):
        url = "https://app.apptimized.com/api/projects/{}/applications/{}".format(
            projectId, workflowId
        )
        applicationInfo = self.connection_without_params(url)
        return applicationInfo.json()

    def get_applicaton_steps(self, projectId, workflowId):
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/steps".format(
            projectId, workflowId
        )
        steps = self.connection_without_params(url)
        return steps.json()

    def get_all_module_idenitifiers_in_a_project(self, projectId):
        dictionary = {"Application": [], "ModuleId": []}
        data = self.get_applications(projectId)
        for modules in data['Data']:
            dictionary["Application"].append(modules['Software'])
            dictionary["ModuleId"].append(modules['ModuleId'])
        return json.dumps(dictionary, indent=4)

class ApptimiziedFactory(ApptimizedAPI):
    """A class used to represent the Factory block"""

    def __init__(self, token):
        super().__init__(token)

    def add_comments_attachments_and_approve_requests(
        self,
        projectId,
        applicationId,
        moduleId,
        comments=None,
        files=None,
        trytoapprove: bool = True,
    ):

        data = {"Comments": comments, "Files": files, "TryToApprove": trytoapprove}
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/modules/{}/factory".format(
            projectId, applicationId, moduleId
        )
        amendment = self.put_request(url, data)
        return amendment.json()

    def create_factory_request_for_specified_module(
        self,
        projectId,
        applicationId,
        moduleId,
        priority,
        packagingPlatforms,
        packagingTechnology,
        reference=None,
        packagingWrapper=None,
    ):

        valid = {"Normal", "Urgent", "Emergency"}
        if priority not in valid:
            raise ValueError("priority: status must be one of {}".format(valid))
        data = {
            "Reference": reference,
            "Priority": priority,
            "PackagingPlatforms": packagingPlatforms,
            "PackagingTechnology": packagingTechnology,
            "ApplicationId": applicationId,
            "PackagingWrapper": packagingWrapper,
        }
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/modules/{}/factory".format(
            projectId, applicationId, moduleId
        )
        results = self.post_request(url, data)
        return results.json()

    def reject_factory_requests_deliverable(
        self, projectId, applicationId, moduleId, deliverableId, rejectcomment=None
    ):
        data = {"RejectComment": rejectcomment}
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/modules/{}/factory/deliverables/{}".format(
            projectId, applicationId, moduleId, deliverableId
        )
        rejection = self.put_request(url, data)
        return rejection.json()

    def cancel_factory_request_for_specified_module(
        self, projectId, applicationId, moduleId
    ):
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/modules/{}/factory".format(
            projectId, applicationId, moduleId
        )
        results = self.delete_request(url)
        return results.json()

    def get_factory_information(self, projectId, applicationId, moduleId):
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/modules/{}/factory".format(
            projectId, applicationId, moduleId
        )
        factoryInfo = self.connection_without_params(url)
        return factoryInfo.json()

    def download_attachment_from_request(
        self, projectId, appId, moduleId, attachmentId
    ):
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/modules/{}/factory/attachment/{}".format(
            projectId, appId, moduleId, attachmentId
        )
        attachment = self.connection_without_params(url)
        return attachment.json()

    def get_deliverables_for_factory_module(self, projectId, appId, moduleId):
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/modules/{}/factory/deliverables".format(
            projectId, appId, moduleId
        )
        deliverables = self.connection_without_params(url)
        return deliverables.json()


class ApptimizedModules(ApptimizedAPI):
    """A class used to represent the Modules block"""

    def __init__(self, token):
        super().__init__(token)

    def build_discovery_or_testing_document(
        self,
        projectId,
        applicationId,
        moduleId,
        qaState,
        additionalComment=None,
        qaComment=None,
    ):
        states = {"Untested", "Success", "Failed", "Fixed"}
        if qaState not in states:
            raise ValueError("States: must be one of {}".format(states))
        data = {
            "AdditionalComment": additionalComment,
            "QaComment": qaComment,
            "QaState": qaState,
        }
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/modules/{}/document".format(
            projectId, applicationId, moduleId
        )
        build = self.post_request(url, data)
        return build.json()

    def start_self_service_module_and_virtual_machine(
        self, projectId, applicationId, moduleId, platformId, mainVm: bool = True
    ):
        data = {"mainVm": mainVm}
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/modules/{}/self-service/{}".format(
            projectId, applicationId, moduleId, platformId
        )
        start = self.post_request(url, data)
        return start.json()

    def start_self_service_module_in_togo_mode(
        self, projectId, applicationId, moduleId
    ):
        data = {}
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/modules/{}/togo-self-service".format(
            projectId, applicationId, moduleId
        )
        service = self.post_request(url, data)
        return service.json()

    def get_factory_configuration(self, projectId, appId):
        url = "https://app.apptimized.com/api/projects/{}/modules/{}/factory/config".format(
            projectId, appId
        )
        factoryConfig = self.connection_without_params(url)
        return factoryConfig.json()

    def get_self_service_configuration(self, projectId, moduleId):
        url = "https://app.apptimized.com/api/projects/{}/modules/{}/self-service/config".format(
            projectId, moduleId
        )
        serviceConfig = self.connection_without_params(url)
        return serviceConfig.json()

    def get_download_document_urls(self, projectId, appId, moduleId):
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/modules/{}/document".format(
            projectId, appId, moduleId
        )
        documentUrl = self.connection_without_params(url)
        return documentUrl.json()

    def get_current_module_state(self, projectId, appId, moduleId):
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/modules/{}".format(
            projectId, appId, moduleId
        )
        moduleState = self.connection_without_params(url)
        return moduleState.json()


class ApptimizedProjectAdditionalFields(ApptimizedAPI):
    """A class used to represent the Addtional Fields block"""

    def __init__(self, token):
        super().__init__(token)

    def create_or_update_the_project_additional_field(
        self,
        projectId,
        fieldId,
        fieldName,
        fieldRequired,
        fieldType,
        fieldSourceType,
        additionalFieldOptions,
        dataType,
    ):
        data = {
            "FieldId": fieldId,
            "DataType": dataType,
            "FieldName": fieldName,
            "FieldRequired": fieldRequired,
            "FieldType": fieldType,
            "FieldSourceType": fieldSourceType,
            "AdditionalFieldOptions": additionalFieldOptions,
        }
        url = "https://app.apptimized.com/api/projects/{}/set-additional-field".format(
            projectId
        )
        dataTypes = {"integer", "Text", "DateTime", "Boolean", "Html"}
        fieldTypes = {"Input", "Select", "MultiSelect"}
        fieldSourceTypes = {"None", "Custom", "Applications", "Users"}
        if dataType not in dataTypes:
            raise ValueError("DataType: must be one of {}".format(dataTypes))
        if fieldType not in fieldTypes:
            raise ValueError("FieldTypes: must be one of {}".format(fieldTypes))
        if fieldSourceType not in fieldSourceTypes:
            raise ValueError(
                "FieldSourceType: must be one of {}".format(fieldSourceTypes)
            )
        create = self.put_request(url, data)
        return create.json()

    def delete_additional_field(self, projectId, fieldId):
        url = "https://app.apptimized.com/api/projects/{}/additional-field/{}".format(
            projectId, fieldId
        )
        delete = self.delete_request(url)
        return delete.json()

    def delete_additional_field_option(self, projectId, fieldId, fieldOptionId):
        url = "https://app.apptimized.com/api/projects/{}/additional-field/{}/option/{}".format(
            projectId, fieldId, fieldOptionId
        )
        delete = self.delete_request(url)
        return delete.json()


class ApptimizedProjects(ApptimizedAPI):
    """A class used to represent the Projects block"""

    def __init__(self, token):
        super().__init__(token)

    def get_projects_for_current_user(self):
        url = "https://app.apptimized.com/api/projects"
        projects = self.connection_without_params(url)
        return projects.json()

    def get_project_workflow_structure(self, projectId):
        url = "https://app.apptimized.com/api/projects/{}/steps".format(projectId)
        structure = self.connection_without_params(url)
        return structure.json()

    def get_module_workflow_structure_without_steps(self, projectId):
        url = "https://app.apptimized.com/api/projects/{}/modules".format(projectId)
        structure = self.connection_without_params(url)
        return structure.json()


class ApptimizedScreenShots(ApptimizedAPI):
    """A class used to represent the Screenshots block"""

    def __init__(self, token):
        super().__init__(token)

    def delete_screenshots_from_module(self, projectId, applicationId, moduleId):
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/modules/{}/screenshots".format(
            projectId, applicationId, moduleId
        )
        delete = self.delete_request(url)
        return delete.json()

    def get_links_to_screenshots(self, projectId, appId, moduleId):
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/modules/{}/screenshots".format(
            projectId, appId, moduleId
        )
        screenshots = self.connection_without_params(url)
        return screenshots.json()


class ApptimizedVirtualMachine(ApptimizedAPI):
    """A class used to represent the Virtual Machine block"""

    def __init__(self, token):
        super().__init__(token)

    def restart_virtual_machine(
        self,
        projectId,
        applicationId,
        moduleId,
        restartBehavior,
        mainVm,
        platformId,
        behaviorType,
    ):

        data = {"RestartBehavior": restartBehavior, "MainVm": mainVm}
        if mainVm is not bool:
            raise ValueError("MainVm: input must be boolean (True or False")
        behaviorTypes = {"Restart", "Reset", "Recreate"}
        if behaviorType not in behaviorTypes:
            raise ValueError("BehaviorType: must be one of {}".format(behaviorTypes))
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/modules/{}/vm/restart".format(
            projectId, applicationId, moduleId
        )
        restart = self.post_request(url, data)
        return restart.json()

    def restart_togo_virtual_machine(self, projectId, applicationId, moduleId):
        data = {}
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/modules/{}/vm/togo-restart".format(
            projectId, applicationId, moduleId
        )
        restartToGo = self.post_request(url, data)
        return restartToGo.json()

    def finish_virtual_machine(self, projectId, applicationId, moduleId, mainVm=True):
        data = {}
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/modules/{}/vm/finish".format(
            projectId, applicationId, moduleId
        )
        finish = self.post_request(url, data)
        return finish.json()

    def get_rdp_file_for_specific_module(self, projectId, appId, moduleId):
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/modules/{}/vm/downloadrdp".format(
            projectId, appId, moduleId
        )
        rdpFile = self.connection_without_params(url)
        return rdpFile.json()

    def get_information_about_virtual_machine(self, projectId, appId, moduleId):
        url = "https://app.apptimized.com/api/projects/{}/applications/{}/modules/{}/vm".format(
            projectId, appId, moduleId
        )
        rdpInfo = self.connection_without_params(url)
        return rdpInfo.json()