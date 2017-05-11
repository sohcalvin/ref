
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

        # if(organization is not None): db_filter["organization"] = organization

        distinct_owner = self._getDistinctJobOwner()
        distinct_organization = self._getDistinctJobOrganization()
        summary = []
        for owner in distinct_owner :
            db_filter = {"owner" : owner}
            a_job_count = self._getJobCount(db_filter=db_filter)
            a_cv_count = self._getCVCount(db_filter=db_filter)
            data = {
                "owner": owner,
                "job_count": a_job_count,
                "cv_count": a_cv_count
            }
            summary.append(data)

        return summary



