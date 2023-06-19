import src_java.Chiffre;

public class main {
    public static void main(String[] args) {
        Chiffre Chiffre = new Chiffre(0, "katzen");
        Chiffre.printSquare();
        System.out.println(Chiffre.encrypt("Hallo Welt!"));
        System.out.println(Chiffre.decrypt(Chiffre.encrypt("Hallo Welt!")));
    }
}