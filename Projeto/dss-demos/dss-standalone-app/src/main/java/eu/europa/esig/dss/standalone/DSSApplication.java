package eu.europa.esig.dss.standalone;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import eu.europa.esig.dss.RemoteDocument;
import eu.europa.esig.dss.RemoteSignatureParameters;
import eu.europa.esig.dss.signature.RemoteDocumentSignatureService;
import eu.europa.esig.dss.signature.RemoteDocumentSignatureServiceImpl;
import eu.europa.esig.dss.standalone.controller.SignatureController;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;

public class DSSApplication extends Application {

	private static final Logger LOG = LoggerFactory.getLogger(DSSApplication.class);

	private RemoteDocumentSignatureService<RemoteDocument, RemoteSignatureParameters> signatureService;

	private Stage stage;

	@Override
	public void start(Stage stage) {
		this.stage = stage;
		this.stage.setTitle("Digital Signature Service Application");
		this.stage.setResizable(true);
		this.stage.getIcons().add(new Image("/dss-logo.png"));

		ApplicationContext ctx = new ClassPathXmlApplicationContext("spring/applicationContext.xml");
		signatureService = ctx.getBean(RemoteDocumentSignatureServiceImpl.class);

		initLayout();
	}

	private void initLayout() {
		try {
			FXMLLoader loader = new FXMLLoader();
			loader.setLocation(DSSApplication.class.getResource("/fxml/screen.fxml"));
			Pane pane = loader.load();

			Scene scene = new Scene(pane);
			scene.getStylesheets().add("/styles/style.css");
			stage.setScene(scene);
			stage.show();

			SignatureController controller = loader.getController();
			controller.setStage(stage);
			controller.setSignatureService(signatureService);
		} catch (Exception e) {
			LOG.error("Unable to init layout : " + e.getMessage(), e);
		}
	}

	public static void main(String[] args) {
		launch(DSSApplication.class, args);
	}

	public Stage getStage() {
		return stage;
	}

}
