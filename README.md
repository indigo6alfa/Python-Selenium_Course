# Python-Selenium_Course 

# Pytest - Decorators

Dekoratörler, fonksiyonların işlevini değiştirir. Başı "@" ile başlar ve kodun anlaşılabilirliğini artırır ve hız kazandırır.

Temel Dekoratörler:

* usefixtures
* filterwarnings
* skip
* xfail
* parametrize
* timeout

Dekoratörlerin Kullanımı:

@pytest.usefixtures: Bu dekoratör ile bir veritabanı veya kaynak ataması yapılır.

@pytest.mark.parametrize: Bu dekoratör ile birden fazla parametre ile test edilmesi sağlanır.

@pytest.mark.skip: Bu dekoratör ile bir testin atlanması sağlanır.

@pytest.mark.xfail: Bu dekoratör ile bir koşula bağlı başarısız test sonucu üretilir.

@pytest.mark.timeout: Bu dekoratör ile bir testin belirli bir sürede yapılması aksi halde başarısız sonuç vermesini sağlar.

@pytest.marks.filterwarnings: Bu dekoratör ile uyarı filtreleri eklenir.
