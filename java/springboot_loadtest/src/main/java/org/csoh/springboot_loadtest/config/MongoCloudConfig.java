package org.csoh.springboot_loadtest.config;




import org.springframework.cloud.Cloud;
import org.springframework.cloud.CloudFactory;

import org.springframework.cloud.service.common.MongoServiceInfo;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;
import org.springframework.data.mongodb.MongoDbFactory;
import org.springframework.data.mongodb.core.MongoTemplate;



@Configuration
@Profile("cloud")
public class MongoCloudConfig {

//    @Bean
//    public Cloud cloud() {
//        return new CloudFactory().getCloud();
//    }
//
//    @Bean
//    @ConfigurationProperties(DataSourceProperties.PREFIX)
//    public DataSource dataSource() {
//        return cloud().getSingletonServiceConnector(DataSourceclass, null);
//    }

    @Bean
    public MongoDbFactory mongoDbFactory() {
        CloudFactory cloudFactory = new CloudFactory();
        Cloud cloud = cloudFactory.getCloud();
        MongoServiceInfo serviceInfo = (MongoServiceInfo) cloud.getServiceInfo("my-mongodb");
        String serviceID = serviceInfo.getId();
        return cloud.getServiceConnector(serviceID, MongoDbFactory.class, null);
    }

    @Bean
    public MongoTemplate mongoTemplate() {
        return new MongoTemplate(mongoDbFactory());
    }

}