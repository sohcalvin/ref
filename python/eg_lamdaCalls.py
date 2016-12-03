


def _computeUpdateRecommendation2(job_id, compute_function, job_text_extractor, cv_text_extractor, score_key_name, db=CVRDb()):
        job = db.getJob(job_id)["content"]
        job_text = job_text_extractor(job)
        cv_ids = job["cv_ids"]
        cv_list = db.getCVsByIds(cv_ids)
        cv_list_text = [cv_text_extractor(cv) for cv in cv_list]
        if(job_text is None ) :
            i=-1
            results = [ {"id": i , "score" : None }for cvid, i  in cv_ids ]
        else :
            results = compute_function([job_text], cv_list_text)
        print(results)
        results_with_cvid = {}
        for r in results :
            cv_id = cv_ids[r["id"]]
            results_with_cvid[cv_id]=r["score"]
        db.updateJobRecommendationScore(job_id, score_key_name, results_with_cvid)
        return results_with_cvid


def computeUpdateRecommendationWithRawText(job_id, compute_job2cv_similarity_matching, score_key_name) :
         return _computeUpdateRecommendation(job_id,compute_job2cv_similarity_matching, lambda job : job["description"], lambda cv : cv["raw_content"], score_key_name )


def computeUpdateRecommendationWithEducation(job_id, compute_job2cv_similarity_matching, score_key_name) :
         return _computeUpdateRecommendation(job_id,compute_job2cv_similarity_matching
                                             , lambda job : predictCVClassification(job["description"]).get("edu")
                                             , lambda cv  : predictCVClassification(cv["raw_content"]).get("edu")
                                             , score_key_name )

def computeUpdateRecommendationWithSkills(job_id, compute_job2cv_similarity_matching, score_key_name) :
         return _computeUpdateRecommendation(job_id,compute_job2cv_similarity_matching
                                             , lambda job : predictCVClassification(job["description"]).get("skills")
                                             , lambda cv  : predictCVClassification(cv["raw_content"]).get("skills")
                                             , score_key_name )
