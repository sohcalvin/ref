package com.sap.icn.resumematching.controller;

/**
 * Created by I319984 on 13/1/2017.
 */

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpServletRequest;
import java.util.Enumeration;

@RestController
public class WhatIsMyIpController {

    @RequestMapping("/")
    public String index() {
        return "What is my ip";
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