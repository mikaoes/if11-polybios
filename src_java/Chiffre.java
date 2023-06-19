class Chiffre {

    String key;
    String[][] square;

    public Chiffre(int size, String key) {

        int zeilen = 9;
        int spalten = 8;
        if (size != 0) {
            zeilen = size;
            spalten = size;
        }

        this.key = key;
        this.square = new String[zeilen][spalten];

        String abc = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!?,()#+-"; // alphabet (72 chars)
        for (int i = 0; i < key.length(); i++) { // remove key from within abc
            abc = abc.replace(String.valueOf(key.charAt(i)), "");
        }
        abc = key + abc; // add key to front of abc

        for (int i = 0; i < zeilen; i++) {
            for (int j = 0; j < spalten; j++) {
                square[i][j] = String.valueOf(abc.charAt(i * spalten + j));
            }
        }
    }
    public void printSquare() {
        for (int i = 0; i < square.length; i++) {
            for (int j = 0; j < square[0].length; j++) {
                System.out.print(square[i][j] + " ");
            }
            System.out.println();
        }
    }
    public String encrypt(String text) {
        // replace äöüß with ae, oe, ue, ss
        text = text.replace("ä", "ae");
        text = text.replace("ö", "oe");
        text = text.replace("ü", "ue");
        text = text.replace("ß", "ss");

        String encrypted = "";
        for (int i = 0; i < text.length(); i++) {
            String letter = String.valueOf(text.charAt(i));
            for (int j = 0; j < square.length; j++) {
                for (int k = 0; k < square[0].length; k++) {
                    if (square[j][k].equals(letter)) {
                        encrypted += String.valueOf(j) + String.valueOf(k);
                    }
                }
            }
        }
        return encrypted;
    }
    public String decrypt(String text) {
        String decrypted = "";
        for (int i = 0; i < text.length(); i += 2) {
            int zeile = Integer.parseInt(String.valueOf(text.charAt(i)));
            int spalte = Integer.parseInt(String.valueOf(text.charAt(i + 1)));
            decrypted += square[zeile][spalte];
        }
        return decrypted;
    }
}