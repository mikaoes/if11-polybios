# if11-polybios
Polybios Chiffre in Python und Java implementiert

## Python
```python
import src_py as src

ch = src.chiffre("katzen")

enc = ch.encrypt("Geheime Nachricht")
print(enc) # O: [(3, 3), (0, 4), (1, 1), (0, 4), (1, 2), (1, 5), (0, 4), (2, 6), (4, 0), (0, 1), (0, 7), (1, 1), (1, 9), (1, 2), (0, 7), (1, 1), (0, 2)]
print(ch.encrypt("Geheime Nachricht", string=True)) # O: 3304110412150426400107111912071102

dec = ch.decrypt(enc)
print(dec) # O: Geheime Nachricht
```
## Java
```java
import src_java.Chiffre;

public class main {
    public static void main(String[] args) {
        Chiffre Chiffre = new Chiffre(0, "katzen");
        Chiffre.printSquare();
        System.out.println(Chiffre.encrypt("Geheime Nachricht")); // O: 4104130414170432500107132314071302
        System.out.println(Chiffre.decrypt(Chiffre.encrypt("Gehemeime Nachricht"))); // O: Geheime Nachricht
    }
}
```