# Projekt python 2023 - Cheat Menu dla gry Crab Game

## Wprowadzenie

W tym repozytorium znajduje się oprogramowana przeze mnie aplikacja działająca w terminalu, która modyfikuje pamięć gry Crab Game w taki sposób, że podmienione wartości w pamięci zapewnią **nieuczciwą** przewagę nad innymi graczami.

#### UWAGA!
Ten skrypt **nie został** zaprogramowany w celach oszukiwania w grach, ma wyłącznie na celu pokazanie jak python radzi sobie z inżynierią odwrotną oraz z zabawą z odczytem i modyfikacją pamięci.

## Wymagane pakiety

Jedyną wymaganą biblioteką do zainstalowania jest `pymem`, która umożliwi nadpisanie pamięci gry, nad którą pracuje program:

```python
pip install pymem
```

Poza biblioteką `pymem` posłużyłem się pakietem `re`, który jest domyślnie wgrany wraz z Pythonem.
Używany on jest tu ze względu na jego potężny RegEx, za pomocą którego można łatwo i szybko odnaleźć odpowiednie szukane dane.

## Działanie

Program na start zapyta o prawidłowy argument [od 1 do 3], i adekwatnie do wyboru użytkownika, podmieni odpowiednio bajty zeskanowane z modułu. Dzięki bibliotece pymem skrypt jest w stanie zdefiniować moduły samego procesu, jak i pozyskać wszelkie informacje dotyczące go.

## Demonstracja