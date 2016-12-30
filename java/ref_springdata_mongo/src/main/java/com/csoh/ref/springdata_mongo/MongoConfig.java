package com.csoh.ref.springdata_mongo;

import com.mongodb.Mongo;
import com.mongodb.MongoClient;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.support.PropertySourcesPlaceholderConfigurer;
import org.springframework.data.mongodb.config.AbstractMongoConfiguration;
import org.springframework.data.mongodb.repository.config.EnableMongoRepositories;

@Configuration
@EnableMongoRepositories
class MongoConfig extends AbstractMongoConfiguration {

    @Value("${mongo.name}")
    private String mongoName;

    @Value("${mongo.host}")
    private String mongoHost;

    @Override
    protected String getDatabaseName() {
        return mongoName;
    }

    @Override
    @Bean
    public MongoClient mongo() throws Exception {
        return new MongoClient(mongoHost);
    }

    //================================================================
    // Needs this in order for application.properties to be read !!!!!
    //================================================================
    @Bean
    public static PropertySourcesPlaceholderConfigurer propertyPlaceholderConfigurer() {
        return new PropertySourcesPlaceholderConfigurer();
    }
}