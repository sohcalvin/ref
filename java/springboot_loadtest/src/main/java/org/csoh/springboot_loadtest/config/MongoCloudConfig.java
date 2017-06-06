package org.csoh.springboot_loadtest.config;



import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.cloud.Cloud;
import org.springframework.cloud.CloudFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;

@Configuration
@Profile("cloud")
public class MongoCloudConfig {

    @Bean
    public Cloud cloud() {
        return new CloudFactory().getCloud();
    }

    @Bean
    @ConfigurationProperties(DataSourceProperties.PREFIX)
    public DataSource dataSource() {
        return cloud().getSingletonServiceConnector(DataSourceclass, null);
    }

}