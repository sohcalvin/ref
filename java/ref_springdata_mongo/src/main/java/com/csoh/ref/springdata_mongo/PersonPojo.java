package com.csoh.ref.springdata_mongo;

import org.springframework.data.annotation.Id;

/**
 * Created by I319984 on 29/12/2016.
 */
public class PersonPojo {
    @Id
    private String id;
    private String name;
    private int age;

    public PersonPojo(String name, int age){
        this.name= name;
        this.age = age;
    }
    public String toString(){
        return "I am " + name + " and I am " + age + " years old. My Id is " + id;

    }
}
