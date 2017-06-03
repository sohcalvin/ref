package org.csoh.springboot_loadtest.repository;
import org.csoh.springboot_loadtest.model.User;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;

/**
 * Created by i319984 on 3/6/17.
 */

public interface UserRepository extends MongoRepository<User, Long> {


    Long deleteByLastName(String lastName);

    List<User> removeByLastName(String lastName);

}
