package com.sap.icn.resumematching;

/**
 * Created by I319984 on 13/1/2017.
 */

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.lang.management.ManagementFactory;
import java.lang.management.RuntimeMXBean;

@SpringBootApplication
public class Main {

    public static void main(String[] args) {
        long pid = getPid();
        SpringApplication.run(Main.class, args);
    }
    public static long getPid(){
        RuntimeMXBean runtimeBean = ManagementFactory.getRuntimeMXBean();
        String jvmName = runtimeBean.getName();
//        System.out.println("JVM Name = " + jvmName);
        long pid = Long.valueOf(jvmName.split("@")[0]);
        System.out.println("JVM PID  = " + pid);
        return pid;

    }
}
