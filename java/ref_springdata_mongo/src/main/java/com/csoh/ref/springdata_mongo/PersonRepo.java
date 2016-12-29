package com.csoh.ref.springdata_mongo;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.repository.Repository;

/**
 * Created by I319984 on 29/12/2016.
 */
public interface PersonRepo extends MongoRepository<PersonPojo, String> {


    PersonPojo findByName(String name);



}
