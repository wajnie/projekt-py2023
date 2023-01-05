# Projekt python 2023 - Cheat Menu dla gry Crab Game

## Wprowadzenie

W tym repozytorium znajduje się oprogramowana przeze mnie aplikacja konsolowa, która modyfikuje pamięć procesu gry Crab Game tak, że podmienione wartości w pamięci zapewnią **nieuczciwą** przewagę nad innymi graczami.

#### zastrzeżenie;
> Ten skrypt **nie został** zaprogramowany w celach oszukiwania w grach,
> ma wyłącznie na celu pokazanie jak python radzi sobie z inżynierią odwrotną oraz z zabawą z odczytem i modyfikacją pamięci.

## Wymagane pakiety

Aby skrypt mógł działać poprawnie, wymaga on posiadania/zainstalowania bibliotek wymienionych poniżej:

`pymem` - Pymem jest biblioteką do manipulowania procesami w systemie Windows (32 i 64 bitowymi). Dzięki tej bibliotece możliwa jest inżyniera odwrotna aplikacji, jak i operowanie pamięcia procesów systemu Windows (odczyt/zapis).

`re` - Moduł re zapewnia nam szeroki wybór narzędzi o tematyce wyrażeń regularnych, które pozwalają szybko sprawdzić, czy dany ciąg pasuje do danego wzorca (za pomocą funkcji match), albo czy ma taki wzorzec (za pomocą funkcji search).

`os` - Biblioteka os w Pythonie zapewnia programiście funkcje umożliwiające interakcję z systemem operacyjnym.

`time` - W tym projekcie, importując moduł time, posłużyłem się tylko funkcją `sleep()`, jednak jest wymagany cały moduł, żeby program zadziałał bez problemu.


## Pobieranie projektu

Ostateczna wersja projektu została przeze mnie udostępniona w zakładce po prawej **Releases** i jest wersją gotową do pobrania. W razie wszelkich problemów, zamieszczam bezpośrednio hiperłączę [tutaj](https://github.com/wajnie/projekt-py2023/releases/tag/Fina%C5%82)

## Działanie

Do wybrania są 3 prawidłowe argumenty:
`1` - odpowiadający za nieskończony skok
`2` - odpowiadający za zmniejszenie odrzutu
`3` - odpowiadający za szybkie uderzanie

Po wybraniu jednego z tych argumentów program zacznie pobierać wszystkie bajty z modułu gry. Gdy mu się to powiedzie, zacznie on pracę z biblioteką `re`, która z danymi jej kryteriami, zacznie szukać poszczególnych adresów w pamięci procesu gry.

Na końcu skrypt zapisuje dane w obszarze pamięci w instancji gry, zmieniając jej zasady i prawa.

Gdy 
## Demonstracja

Film prezentujący działanie programu opublikowałem na serwisie Youtube, ponieważ Github posiada limit 10 megabajtów, dla plików które mogę włożyć do tego pliku README.

### **https://www.youtube.com/watch?v=mBAb47E9Ocg**
