import json

import datetime
from bson import json_util
from flask_restful import Resource
from flask import request, session

from cvr.model.feature import Feature
from cvlib.util.logging_util import ds_logger
from cvr.common.decorators import cloud_auth_required, log_request
from cvr.common.constants import JOB_OWNER_FILTER_TYPE, USER_ROLES

logger = ds_logger


# def enco(obj):
#     return obj.isoformat() if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date)else None


class JobManager(Resource) :

    def __init__(self, **kwargs):
        self.db = kwargs["db"]
        self.user_service = kwargs['user_service']
        self.job_service = kwargs['job_service']



    @cloud_auth_required
    @log_request(Feature.job_view)
    def post(self, id):
        """Get job by id"""
        reqData = (request.data).decode(encoding='UTF-8')
        json_data = json.loads(reqData)
        cv_types = json_data['cvTypes']
        score_weightage = json_data['scoreWeightage']
        user_roles = self.user_service.getCurrentUserRoles(session['samlUserdata']['email'])
        job = self.job_service.getJobDetails(id, cv_types=cv_types, score_weightage=score_weightage, keywordsQuery= json_data['keywordsQuery'], domainSelected=json_data['domainSelected'], user_roles=user_roles)
        for k, v in job.items():
            if isinstance(v, datetime.datetime) or isinstance(v, datetime.date):
                job[k] = v.isoformat()
        return job
        #return json.loads(json.dumps(job, default=enco))



    @cloud_auth_required
    @log_request(Feature.job_view_all)
    def get(self):
        """Get all jobs"""
        if hasattr(request, 'args') and (request.args is not None) and "tenant" in list(request.args.keys()):
            return self._getAllJobsForTenant()
        else:
            return self._getAllJobsForUser()

    def _getAllJobsForUser(self):
        job_owner_filter_type = request.args.get("jobOwner", '')
        user_roles = self.user_service.getCurrentUserRoles(session['current_user_email'])

        if job_owner_filter_type == JOB_OWNER_FILTER_TYPE["ALL_JOBS"] and USER_ROLES['RECRUITERS'] in user_roles:
            user_organization = self.user_service.getUserOrganizationByEmail(session['current_user_email'])
            all_jobs = self.job_service.getAllJobsByOrganization(user_organization)
        else:
            all_jobs = self.job_service.getAllJobsByCurrentUser(session['current_user_email'])

        job_list_data = self.job_service.convertJobModelListToJobListData(all_jobs,
                                                                          USER_ROLES['RECRUITERS'] in user_roles)
        return job_list_data

    def _getAllJobsForTenant(self):
        job_owner_filter_type = request.args.get("tenant", '')
        user_roles = self.user_service.getCurrentUserRoles(session['current_user_email'])

        if job_owner_filter_type == JOB_OWNER_FILTER_TYPE["ALL_JOBS"] and USER_ROLES['RECRUITERS'] in user_roles:
            user_organization = self.user_service.getUserTenantInfo(session['current_user_email'])
            if user_organization is not None and isinstance(user_organization, str):
                all_jobs = self.job_service.getAllJobsByOrganization(user_organization)
            else:
                all_jobs = None
        else:
            all_jobs = self.job_service.getAllJobsByCurrentUser(session['current_user_email'])

        if all_jobs is not None and len(all_jobs) > 0:
            # Added requisition_id_required parameter to extract requisition id for tenant details
            job_list_data = self.job_service.convertJobModelListToJobListData(all_jobs,
                                                                          USER_ROLES['RECRUITERS'] in user_roles, True)
        else:
            job_list_data = []
        return job_list_data

    @cloud_auth_required
    @log_request(Feature.job_delete_id)
    def delete(self):
        """Delete job by id"""
        raw_data = (request.data).decode('utf-8')
        json_data = json.loads(raw_data)
        job_id = json_data['jobId']

        # Checking the job owner
        is_current_user_job_owner = self.job_service.isCurrentUserJobOwner(job_id, session['current_user_email'])
        if not is_current_user_job_owner:
            return {"error_message": 'User is not authorized to delete the job posting!', 'error_values': ''}, 403

        self.job_service.softDeleteJobById(job_id)
        return '', 200

    @cloud_auth_required
    @log_request(Feature.job_update_id)
    def put(self, id):
        """Update jobs"""
        raw_data = (request.data).decode('utf-8')
        json_data = json.loads(raw_data)
        job_id = id
        cv_id = json_data.get('cvId')
        if(cv_id is None) : return "'cvId' param required", 400

        # Checking the job owner
        is_current_user_job_owner = self.job_service.isCurrentUserJobOwner(job_id, session['current_user_email'])
        if not is_current_user_job_owner:
            return {"error_message": 'User is not authorized to act on the CV!', 'error_values': ''}, 403

        state = json_data.get('state')
        if state is not None:
            self.db.updateJobCVShortlist(job_id, cv_id, state)

        else:
            return "'cv marker' param not specified", 400

        return self.db.getJobCVState(job_id, cv_id), 200