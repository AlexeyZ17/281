# 281

1.Устанавливаем в Terminal библиотеки Pytest и Selenium:
 используя команды pip install Pytest и pip install Pytest-selenium.

2.Скачиваем драйвер соотествующего браузер и копируем в PyCharm, после распаковки файл переносим в папку C:\Windows,
в нашем случае это ChromeDriver для Chrome version 108.

3. Создаём файл tests.py и наполняем его сходя из тест-кейса:
- дымовое тестирование страницы регистрация;
Составляем тесты позитивного тестирования:
- тестирование страницы авторизации вход по валидному телефону и паролю;
- тестирование страницы авторизации вход по валидной почте и паролю;
- тестирование страницы авторизации: автоматическое переключение таб на вход по валидной почте и паролю;
- тестирование страницы авторизации: проверка работоспособности кнопки "забыли пароль";
- тестирование страницы авторизации: проверка работоспособности кнопки "Зарегистрироваться";
- тестирование страницы авторизации: проверка работоспособности кнопки "пользовательское соглашение";

НЕГАТИВНОЕ ТЕСТИРОВАНИЕ:
- тестирование страницы авторизации вход по НЕ валидному телефону и валидному паролю;
- тестирование страницы авторизации вход по НЕ валидному паролю и валидному телефону;
- тестирование страницы авторизации вход по НЕ валидной почте и валидному паролю;
- тестирование страницы авторизации вход по НЕ валидному паролю и валидной почте;

4. Создаём файл "conftest", для написания фикстур и создаём фикстуру.

5. Создаём файл: base_page.py Создание базового слоя для работы браузера:

6. Описание локаторов Page Obgect, на созданной странице: ya_pages.py

7. Создаём файл setings отдельный для указания валидных данных: номер телефона, почты и пароль.  
