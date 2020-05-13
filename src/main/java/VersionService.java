import java.io.IOException;
import java.util.Properties;

class VersionService {

    private Properties versionProperties;

    VersionService() {
        versionProperties = new Properties();
        try {
            versionProperties.load(this.getClass().getResourceAsStream("/version.properties"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String getVersion() {
        return versionProperties.getProperty("version");
    }
}