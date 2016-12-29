package com.csoh.ref.springdata_mongo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.context.annotation.ComponentScan;

/**
 * Created by I319984 on 29/12/2016.
 */

@ComponentScan("com.csoh.ref")
//@EnableAutoConfiguration
//@Component
//@ComponentScan
//@EnableMongoRepositories("com.sap.icn")
public class App {

    @Autowired
    PersonRepo repo;

    public void init(){
        System.out.println("Initializing App");

    }
    public void queryMongo(){
        PersonPojo pp = new PersonPojo("Calvin", 12);
        repo.save(pp);

        System.out.println("Query mongo for " + repo);
        PersonPojo p = repo.findByName("Calvin");
        System.out.println(p);


    }

    public static void main(String[] args) {
        ConfigurableApplicationContext ctx = SpringApplication.run(App.class, args);
        App mainObj = ctx.getBean(App.class);
        mainObj.init();
        mainObj.queryMongo();
    }



}
