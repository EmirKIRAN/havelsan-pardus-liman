# HAVELSAN PARDUS - LİMAN KAMP

### 1 - Fibonacci
#### KURULUM

>> pip install py-fibonacci
#### Uçbirim üzerinden çalıştırma

-   python3
-   from fibonacci import fibonacci
-   for item in fibonacci(length=10):
    - print(item)


![alt text](./images/fibo_.png)

### 2 - Genel değişken tanımı

    Normal olarak oluşturulan yerel değişkenler diğer kullanıcılar için saklanmazlar. Bunun için her kullanıcı için geçerli olan, sistem her açıldığında ve herhangi bir kullanıcı tarafından yerel olarak veya uzaktan oturum açıldığında yüklenen bir ortamda oluşturulması gerekecektir.

    /etc/environment, /etc/profile, /etc/profile.d/, /etc/bash.bashrc Bunlar, sistem genelinde mevcut olan ortam değişkenleridir, yani o sistemde bulunan tüm kullanıcılar içindir. Oluşturmak istediğimiz değişkenleri bu dosyaların ile birlikte oluşturduğumuzda tüm kullanıcılar için kullanılabilir olacaktır.

