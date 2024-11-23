import turtle
import random
import time

"""
delay değişkeni, yılanın hareket ettikten sonra ne kadar süre bekleyeceğini (geçireceği zaman) belirtir. 
Başlangıç değeri 0.1 saniye olarak ayarlanmıştır.
"""
delay = 0.1
skor = 0
max_skor = 0

# Ekran Oluşturma

ekran = turtle.Screen()
ekran.title("Yılan Oyunu")
ekran.bgcolor("black")
# genişlik ve yükseklik kullanıcının tercihine göre ayarlanabilir
ekran.setup(width=600,height=600)
ekran.tracer(0)

"""
wn.tracer(0) ifadesi, Python'un turtle kütüphanesinde kullanılır ve animasyon hızını kontrol etmek için işlev görür. wn.tracer() fonksiyonu, 
ekranda yapılan güncellemelerin sayısını ayarlamaya yarar.

wn.tracer(0) şeklinde bir değer verildiğinde, ekrandaki çizim işlemleri anında güncellenmez. Bunun yerine, yapılan değişiklikler wn.update() 
fonksiyonu çağrıldığında toplu olarak ekrana yansıtılır. Bu sayede, çizimlerin hızlandırılması ve ekranın daha hızlı güncellenmesi sağlanabilir. Özellikle grafik performansını artırmak için veya animasyon akışını kontrol etmek istediğinizde faydalıdır.
"""

# Yılanın Kafası

kafa = turtle.Turtle()
kafa.shape("circle")
kafa.color("red")
kafa.penup()
kafa.goto(0,0)
kafa.direction = "Stop"   # Başlangıçta  yılanın hareket etmediği belirtilir. Yani yılan durur.

"""
kafa.direction

kafa.direction ifadesi, yılanın hareket yönünü belirtmek için kullanılan bir değişkendir. Oyun boyunca yılanın hareket yönünü kontrol etmek 
ve bu yönü değiştirmek için kullanılır. Kodunuza göre direction değişkeninin bazı önemli işlevleri ve kullanımı şu şekildedir:
"""

# Oyundaki̇ Yi̇yecek

renkler = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
sekiller = ["square","turtle","circle"]
yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape(random.choice(sekiller))
yemek.color(random.choice(renkler))
yemek.penup()
yemek.goto(0,100)

puan = turtle.Turtle()
puan.speed(0)
puan.shape("circle")
puan.color("white")
puan.penup()
puan.hideturtle()    # Burda kalemin izlerinin görünmesini istemiyoruz
puan.goto(0,250)
puan.write("Skor : 0           Yüksek Skor : 0",align="center",font=("candara",24,"bold"))

# Tuş Yönlerinin Atanması

"""
Çarpışma Kontrolü: Eğer kafa.direction değişkeninin mevcut değeri ile yeni yön arasında bir çelişki varsa (örneğin, yılan aşağıya doğru 
hareket ederken yukarıya gitmek isteniyorsa), bu durumda yılan kendisine çarpabilir. Bu tür bir çarpışmayı önlemek için bu tür kontroller kullanılır.
"""
def yukari_git():
    if (kafa.direction != "down"):
        kafa.direction = "up"

def assagi_git():
    if(kafa.direction != "up"):
        kafa.direction = "down"

def saga_git():
    if(kafa.direction != "left"):
        kafa.direction = "right"

def sola_git():
    if(kafa.direction != "right"):
        kafa.direction = "left"

def hareket():
    if(kafa.direction == "up"):
        y = kafa.ycor() 
        kafa.sety(y + 20)
    
    if (kafa.direction == "down"):
        y = kafa.ycor()
        kafa.sety(y - 20)

    if (kafa.direction == "right"):
        x = kafa.xcor()
        kafa.setx(x + 20)

    if (kafa.direction == "left"):
        x = kafa.xcor()
        kafa.setx(x - 20)

ekran.listen()
ekran.onkeypress(yukari_git,"Up")
ekran.onkeypress(assagi_git,"Down")
ekran.onkeypress(saga_git,"Right")
ekran.onkeypress(sola_git,"Left")

kuyruk = []

while True:

    ekran.update()

    # Sınıra çarpınca zıt yönden çıkma

    if (kafa.xcor() > 290 or kafa.xcor() < -290 or kafa.ycor() > 290 or kafa.ycor() < -290): # Sınır Kontürolü
        kafa.penup()
        kafa.goto(kafa.xcor() * -1,kafa.ycor() * -1)
        
        puan.write(f"Skor : {skor}         Yüksek Skor : {max_skor}",align="center",font=("candara",24,"bold"))

        """
        Bu kod parçası, yılanın başı ile yiyecek arasındaki mesafeyi kontrol ederek, yılan yiyeceğe ulaştığında yiyeceğin ekranda 
        rastgele bir konuma taşınmasını sağlar
        """
    if (kafa.distance(yemek) < 20):   # Yılan yem ile çarpıştıysa
        
        #Yemi rastgele bir konuma yerleştir
        
        x = random.randint(-270,270)
        y = random.randint(-270,250)
        yemek.goto(x,y)

        # Kuyruk Ekleme
        yeni_kuyruk = turtle.Turtle()
        yeni_kuyruk.speed(0)
        yeni_kuyruk.shape("circle")
        yeni_kuyruk.color("green")
        yeni_kuyruk.penup()
        kuyruk.append(yeni_kuyruk)     # Yeni parçayı kuyruğa ekle
        delay -= 0.001
        skor += 10

        """
        Kuyruk Ekleme ile Hızlandırma: Yılan bir yem yediğinde, delay değeri azaltılır.Bu işlem, yılanın daha uzun bir kuyruk oluşturmasıyla 
        birlikte yılanın hızını artırır. Bu, oyunun zorluk seviyesinin arttığını ve yılanın daha hızlı hareket ettiğini gösterir.
        (Ne kadar düşük o kadar hızlı)
        """

        if (skor > max_skor):  
            max_skor = skor
            
        puan.clear()
        puan.write(f"Skor : {skor}         Yüksek Skor : {max_skor}",align="center",font=("candara",24,"bold"))

    for j in range(len(kuyruk)-1, 0, -1):       # Kuyruğun sonundan başına doğru
        x = kuyruk[j - 1].xcor()                # Önceki parçanın koordinatlarını al
        y = kuyruk[j - 1].ycor()
        kuyruk[j].goto(x,y)                     # Mevcut parçayı bir öncekine yönlendir

    """
    Ters Döngü: Kuyruğun parçaları, son parçadan başlayarak başa doğru güncellenir. Bu sayede yılanın gövdesi düzgün bir şekilde başı takip eder.

    Başın Koordinatları: Eğer kuyrukta en az bir parça varsa, başın (kafa) koordinatları kuyruğun ilk parçasına atanır. 
    Bu, yılanın hareketinin akışını sağlar.
    """
    if (len(kuyruk) > 0):
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruk[0].goto(x,y)                     # Başın koordinatlarını kuyruğun ilk parçasına ata
    
    hareket()

    # Kuyruk ile baş çarpışmalarını kontrol etme

    for k in kuyruk:
        if (k.distance(kafa) < 20):
            time.sleep(1)
            kafa.goto(0,0)
            kafa.direction = "stop"
            yemek.color(random.choice(renkler))
            yemek.shape(random.choice(sekiller))
            
            # Aşşağıdaki kodun amacı. Yılan kendine çarptığında oyun bittiğinde kalan kuyruğu ekrandan uzaklaştırmaktır.

            for l in kuyruk:
                l.goto(1000,1000)
            
            kuyruk.clear()
            skor = 0
            delay = 0.1
            puan.clear()
            puan.write(f"Skor : {skor}         Yüksek Skor : {max_skor}",align="center",font=("candara",24,"bold"))

    time.sleep(delay)

    """
    Yılanın Hareketi: Yılan her güncelleme döngüsünde hareket eder ve hareket ettikten sonra bir süre bekler. 
    Bu bekleme süresi time.sleep(delay) fonksiyonu ile gerçekleştirilir:
    """

















