using System.Text;

static class Program {
    const string BaseString = "O rato roeu a roupa do rei de Roma!";

    static void Main(string[] args) {
        StringBuilder stringBulder = new StringBuilder(BaseString);
        int left = 0;
        int right = BaseString.Count() - 1;
        char sub;

        while(left < right) {
            sub = stringBulder[left];
            stringBulder[left] = stringBulder[right];
            stringBulder[right] = sub;
            left++;
            right--;
        }

        Console.WriteLine(stringBulder.ToString());
    }
}