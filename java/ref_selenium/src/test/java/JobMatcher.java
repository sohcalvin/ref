import org.junit.Test;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.firefox.FirefoxBinary;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.chrome.ChromeDriver;
//import org.openqa.selenium.phantomjs;

import static org.junit.Assert.assertTrue;


/**
 * Created by I319984 on 26/9/2016.
 */
public class JobMatcher {
    @Test
    public void goToWebPage() {
//        FirefoxBinary fb = new FirefoxBinary(new File(""))
//        FirefoxDriver driver = new FirefoxDriver( );
//        ChromeOptions co = new ChromeOptions();
//        co.setBinary "C:/sdrive/projects/CV-Recommender/dev-ops/functional_test/drivers/chromedriver.exe");

        // NEED TO set Java -Dwebdriver.chrome.driver=<pathtodriver>
        ChromeDriver driver = new ChromeDriver();
        System.out.println("----1");
        driver.get("http://the-internet.herokuapp.com");
        System.out.println("----2");
        assertTrue(driver.getTitle().equals("The Internet"));
        System.out.println("----3");
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        driver.quit();
    }

}
