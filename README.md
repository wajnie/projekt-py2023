# Projekt python 2023 - Cheat Menu dla gry Crab Game

## Wprowadzenie

W tym repozytorium znajduje się oprogramowana przeze mnie aplikacja konsolowa, która modyfikuje pamięć procesu gry Crab Game tak, że podmienione wartości w pamięci zapewnią **nieuczciwą** przewagę nad innymi graczami.

##### UWAGA!
> Ten skrypt **nie został** zaprogramowany w celach oszukiwania w grach, ma wyłącznie na celu pokazanie jak python radzi sobie z inżynierią odwrotną oraz z zabawą z odczytem i modyfikacją pamięci.

## Wymagane pakiety

Aby projekt mógł działać poprawnie, wymaga on do zainstalowania bibliotek poniżej w tym dziale:

`pymem` - Pymem jest biblioteką do manipulowania procesami w systemie Windows (32 i 64 bitowymi). Dzięki tej bibliotece możliwa jest inżyniera odwrotna aplikacji, jak i operowanie pamięcia procesów systemu Windows (odczyt/zapis).

`re` - Moduł re zapewnia nam szeroki wybór narzędzi o tematyce wyrażeń regularnych, które pozwalają szybko sprawdzić, czy dany ciąg pasuje do danego wzorca (za pomocą funkcji match), albo czy ma taki wzorzec (za pomocą funkcji search).

`os` - Biblioteka os w Pythonie zapewnia programiście funkcje umożliwiające interakcję z systemem operacyjnym.

`time` - W tym projekcie, importując moduł time, posłużyłem się tylko funkcją `sleep()`, jednak jest wymagany cały moduł, żeby program zadziałał bez problemu.


## Pobieranie projektu

Ostateczna wersja projektu została przeze mnie udostępniona w zakładce po prawej **Releases** i jest wersją gotową do pobrania. W razie wszelkich problemów, zamieszczam bezpośrednio hiperłączę [tutaj](https://github.com/wajnie/projekt-py2023/releases/tag/Fina%C5%82)

## Działanie

Program na start zapyta o prawidłowy argument [od 1 do 3], i adekwatnie do wyboru użytkownika, podmieni odpowiednio bajty zeskanowane z modułu. Dzięki bibliotece pymem skrypt jest w stanie zdefiniować moduły samego procesu, po czym może zmodyfikować odpowiednie adresy odpowiadające za reguły gry.

## Demonstracja

Film prezentujący działanie programu opublikowałem na serwisie Youtube, ponieważ Github posiada limit 10 megabajtów, dla plików które mogę włożyć do tego pliku README.

### **https://www.youtube.com/watch?v=mBAb47E9Ocg**
