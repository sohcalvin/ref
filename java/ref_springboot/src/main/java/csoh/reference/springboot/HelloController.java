package csoh.reference.springboot;

/**
 * Created by calvinsoh on 25/9/2016.
 */


import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpServletRequest;
import java.util.Enumeration;
import java.util.Iterator;

@RestController
public class HelloController {

    @RequestMapping("/")
    public String index() {
        return "Greetings from Spring Bootx!";
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
        for (Enumeration<String> e = req.getHeaderNames(); e.hasMoreElements();) {
            String h = e.nextElement();
            b.append(h).append(":").append(req.getHeader(h)).append("<br>");
        }
        return b.toString();
    }

}