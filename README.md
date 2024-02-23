# E-Ticaret Projesi

Merhaba! Bu projede Python Django kullanarak geliştirdiğim kendi e-ticaret sitemini paylaşıyorum. Bu proje, çeşitli özellikleri içeriyor ve bir dizi deneyim kazanmama neden oldu.

## Deneyimler

1. **Ödeme Entegrasyonu (İyzico):**
   Projede İyzico ödeme alt yapısını kullanarak güvenli ödeme entegrasyonunu başarıyla sağladım.

2. **Mail Gönderimi (SMTP):**
   Smtp altyapısını kullanarak müşterilere sipariş onayları, indirim bildirimleri ve diğer önemli güncellemeler için mail gönderimini başarıyla entegre ettim.

3. **Filtreleme ve Sıralama:**
   Kullanıcının tercihlerine bağlı olarak ürünleri A-Z veya Z-A gibi kriterlere göre listeleyebilme özelliği ekledim. Alışveriş deneyimini kişiselleştiriyoruz!

4. **Ürün Arama:**
   Kullanıcılar, istedikleri ürünleri hızlıca bulabilmeleri için geliştirdiğim arama özelliği sayesinde kolaylıkla arayabilirler.

5. **Sepet İşlemleri:**
   Sepetteki ürün bilgilerini statik olarak veritabanından çekerek, kullanıcıların alışveriş sepetlerini daha etkili bir şekilde yönetmelerini sağladım.

## Proje Detayları

- Proje, hazır bir şablon üzerinden alınarak kendi kodlarım ile geliştirildi.
- Bu projem, kendi geliştirdiğim ilk e-ticaret sitesi oldu.

## Admin Paneli

Ayrıca, projenin admin panelini Jasmine çekerek yönetimi daha kolay ve kullanıcı dostu hale getirdim.

## Kurulum

1. Projeyi klonlayın:

```bash
git clone https://github.com/kullaniciadi/proje.git
````

2. Virtual environment oluşturun:
```bash
python -m venv venv
````

3. Virtual environment'ı aktifleştirin:
  - Linux/Mac:
     ```bash
      source venv/bin/activate
     ````
  - Windows:
    ```bash
      .\venv\Scripts\activate
    ````
    
4. Gerekli bağımlılıkları yükleyin:
```bash
      pip install -r requirements.txt
````

5.Veritabanını oluşturun ve migrate edin:
```bash
      python manage.py migrate
````

6.Projeyi başlatın:
```bash
      python manage.py runserver
````
Projeniz şimdi kullanıma hazır!

Umarım projemi beğenirsiniz! İyi kodlamalar! 👩‍💻🚀
