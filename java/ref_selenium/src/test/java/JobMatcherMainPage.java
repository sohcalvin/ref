import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

/**
 * Created by I319984 on 27/9/2016.
 */
public class JobMatcherMainPage {
    protected WebDriver driver;
    private WebElement q;
    private WebElement btn;

    public JobMatcherMainPage(WebDriver driver) {
        this.driver = driver;
    }
    public void open(String url) {
        driver.get(url);
    }
    public void close() {
        driver.quit();
    }
    public String getTitle() {
        return driver.getTitle();
    }
    public void searchFor(String searchTerm) {
//        q.sendKeys(searchTerm);
        btn.click();
    }
    public void typeSearchTerm(String searchTerm) {
//        q.sendKeys(searchTerm);
    }
    public void clickOnSearch() {
//        btn.click();
    }


}
