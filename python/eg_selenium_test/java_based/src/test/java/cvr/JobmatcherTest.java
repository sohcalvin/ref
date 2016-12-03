package cvr;

import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;

import org.junit.*;

import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;

import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class JobmatcherTest {
  private WebDriver driver;
  private String baseUrl;
  private boolean acceptNextAlert = true;
  private StringBuffer verificationErrors = new StringBuffer();

  @Before
  public void setUp() throws Exception {
	  System.setProperty("webdriver.chrome.driver", "C:/sdrive/projects/machinelearning/reference/eg_selenium_test/chromedriver.exe");
//    driver = new FirefoxDriver();
    driver = new ChromeDriver();
    baseUrl = "https://bertelsmann-jobmatcher.cfapps.us10.hana.ondemand.com/";
    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
  }

  @Test
  public void testJobmatcher() throws Exception {
    driver.get("https://bertelsmann-jobmatcher.cfapps.us10.hana.ondemand.com/");
    driver.findElement(By.xpath("//form[@id='candidate-text-form']/div/textarea")).clear();
    driver.findElement(By.xpath("//form[@id='candidate-text-form']/div/textarea")).sendKeys("java");
    driver.findElement(By.xpath("(//button[@type='submit'])[2]")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [getAllButtons |  | ]]
    // ERROR: Caught exception [ERROR: Unsupported command [getAllButtons |  | ]]
  }

  @After
  public void tearDown() throws Exception {
    driver.quit();
    String verificationErrorString = verificationErrors.toString();
    if (!"".equals(verificationErrorString)) {
      fail(verificationErrorString);
    }
  }

  private boolean isElementPresent(By by) {
    try {
      driver.findElement(by);
      return true;
    } catch (NoSuchElementException e) {
      return false;
    }
  }

  private boolean isAlertPresent() {
    try {
      driver.switchTo().alert();
      return true;
    } catch (NoAlertPresentException e) {
      return false;
    }
  }

  private String closeAlertAndGetItsText() {
    try {
      Alert alert = driver.switchTo().alert();
      String alertText = alert.getText();
      if (acceptNextAlert) {
        alert.accept();
      } else {
        alert.dismiss();
      }
      return alertText;
    } finally {
      acceptNextAlert = true;
    }
  }
}
