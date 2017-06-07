package org.csoh.springboot_loadtest.controller;

/**
 * Created by I319984 on 13/1/2017.
 */

import org.csoh.springboot_loadtest.model.User;
import org.csoh.springboot_loadtest.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpServletRequest;
import java.util.Enumeration;

@RestController
public class TargetController {

    @Autowired
    private UserRepository repository;

    @Autowired
    private MongoTemplate mongoTemplate;


    @RequestMapping("/")
    public String index() {

//        repository.deleteAll();
//        repository.save(new User("Alice", "Smith"));
//        repository.save(new User("Bob", "Smith"));

        mongoTemplate.dropCollection("user");
        mongoTemplate.save(new User("Calvin", "Soh"));
        mongoTemplate.save(new User("Bob", "Smith"));


        return "What is my ips";
    }




    @RequestMapping("/myip")
    public String myip(HttpServletRequest req) {
        return new StringBuilder()
                .append("{\"ip\" : \"")
                .append(req.getRemoteAddr())
                .append("\"}").toString();
    }

    @RequestMapping("/headers")
    public String headers(HttpServletRequest req) {
        StringBuilder b = new StringBuilder();
        for (Enumeration<String> e = req.getHeaderNames(); e.hasMoreElements(); ) {
            String h = e.nextElement();
            b.append(h).append(":").append(req.getHeader(h)).append("<br>");
        }
        return b.toString();
    }

}