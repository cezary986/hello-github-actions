
public class Main {

    public void sampleMethod() {
        System.out.println("do something..");
    }

    public static void main(String[] args){
        VersionService versionService = new VersionService();
        System.out.println("Hello word2");
        System.out.println(versionService.getVersion());
    }
}
