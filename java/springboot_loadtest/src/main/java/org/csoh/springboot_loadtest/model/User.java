package org.csoh.springboot_loadtest.model;


import org.springframework.boot.autoconfigure.mongo.MongoProperties;
import org.springframework.data.annotation.Id;


/**
 * Created by i319984 on 3/6/17.
 */
public class User {
    @Id
    public String id;

    public String firstName;

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String lastName;

    public User() {}

    public User(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;

    }

}

