import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.Capabilities;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.phantomjs.PhantomJSDriver;

import org.openqa.selenium.phantomjs.PhantomJSDriverService;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.support.PageFactory;

import java.lang.ref.PhantomReference;

import static org.hamcrest.core.StringContains.containsString;
import static org.junit.Assert.assertThat;


/**
 * Created by I319984 on 27/9/2016.
 */



public class TestPages {

    private JobMatcherMainPage page;

    @Before
    public void openTheBrowser() {
        System.setProperty("webdriver.chrome.driver", "C:/sdrive/projects/CV-Recommender/dev-ops/functional_test/drivers/chromedriver.exe");
        System.setProperty("phantomjs.binary.path", "C:/sdrive/projects/CV-Recommender/dev-ops/functional_test/drivers/phantomjs.exe");

        WebDriver driver = null;
        if(false) {
            driver = new ChromeDriver(); //new FirefoxDriver()
        }else {
            Capabilities caps = new DesiredCapabilities();
            ((DesiredCapabilities) caps).setJavascriptEnabled(true);
            ((DesiredCapabilities) caps).setCapability("takesScreenshot", true);
        ((DesiredCapabilities) caps).setCapability(
                PhantomJSDriverService.PHANTOMJS_EXECUTABLE_PATH_PROPERTY,
                "C:/sdrive/projects/CV-Recommender/dev-ops/functional_test/drivers/phantomjs.exe"
        );
            driver = new PhantomJSDriver(caps);

        }
        page = PageFactory.initElements(driver, JobMatcherMainPage.class);
        page.open("https://int-sap-jobmatcher.cfapps.sap.hana.ondemand.com/#/");
    }

    @After
    public void closeTheBrowser() {
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        page.close();
    }

    @Test
    public void whenTheUserSearchesForSeleniumTheResultPageTitleShouldContainCats() {
        page.searchFor("selenium");
        assertThat(page.getTitle(), containsString("selenium") );
    }
}



