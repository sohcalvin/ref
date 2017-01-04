import org.glassfish.jersey.media.multipart.FormDataMultiPart;
import org.glassfish.jersey.media.multipart.MultiPartFeature;
import org.glassfish.jersey.media.multipart.file.FileDataBodyPart;
import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.io.File;
import java.io.IOException;


/**
 * Created by I319984 on 4/1/2017.
 */
public class Main {

    public static void main(String[] args) throws Exception {
        Client client = ClientBuilder.newBuilder().register(MultiPartFeature.class).build();


        WebTarget webtarget = client.target("https://cvr-recommenderapp.cfapps.sap.hana.ondemand.com/cvr/matchCVFiles2JobFile");

        FileDataBodyPart cvZipFileDataBodyPart = new FileDataBodyPart("cv_zipfile",   new File("c:/tmp/demo_cv/five_cvs.zip"),   MediaType.APPLICATION_OCTET_STREAM_TYPE);
        FileDataBodyPart jobDescFileDataBodyPart = new FileDataBodyPart("jd_file",   new File("c:/tmp/demo_cv/jd.txt"),   MediaType.APPLICATION_OCTET_STREAM_TYPE);

        FormDataMultiPart formDataMultipart = new FormDataMultiPart();
        formDataMultipart.setMediaType(MediaType.MULTIPART_FORM_DATA_TYPE);
        formDataMultipart.field("keyword_list", "java,python,hibernate");
        FormDataMultiPart multiPart = (FormDataMultiPart)(formDataMultipart.bodyPart(cvZipFileDataBodyPart).bodyPart(jobDescFileDataBodyPart));

        try {
            Response response = webtarget.request().post(Entity.entity(multiPart, multiPart.getMediaType()));
            multiPart.close();
            System.out.println(response.getStatus() + " " + response.getStatus() + " " + response);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

}
