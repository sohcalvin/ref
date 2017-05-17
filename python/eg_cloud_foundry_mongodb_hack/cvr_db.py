
class CvrDb(object):

    def __init__(self, client_conn):
        self.db = client_conn


    def _getDistinctJobOwner(self):
        return self.db.job.distinct("owner")

    def _getDistinctJobOrganization(self):
        return self.db.job.distinct("organization")

    def _getJobCount(self, db_filter={}):
        if (db_filter is None): db_filter = {}
        return self.db.job.find(db_filter).count()

    def _getCVCount(self, db_filter={}):
        if(db_filter is None ) : db_filter = {}
        return self.db.cv.find(db_filter).count()

    def getSummary(self):
        distinct_owner = self._getDistinctJobOwner()
        summary = []
        for owner in distinct_owner :
            db_filter = {"owner" : owner}
            a_job_count = self._getJobCount(db_filter=db_filter)
            a_cv_count = self._getCVCount(db_filter=db_filter)
            db_filter["active"] = True
            a_job_count_active = self._getJobCount(db_filter=db_filter)

            db_filter["cv_ids"] = {'$exists': True, '$ne': []}
            a_job_count_active_with_cvs = self._getJobCount(db_filter=db_filter)

            data = {
                "owner": owner,
                "job_count": a_job_count,
                "job_count_active": a_job_count_active,
                "job_count_active_with_cvs": a_job_count_active_with_cvs,
                "cv_count": a_cv_count
            }
            summary.append(data)

        return summary

    def getDistinctSummary(self):
        distinct_owner_org = self.db.job.aggregate([{
            "$group": {
            "_id": {"owner": "$owner", "organization": "$organization"}
            }}])

        list_dict = []
        for o in distinct_owner_org :
            list_dict.append(o.get("_id"))
        print(list_dict)
        return list_dict







