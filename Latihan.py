#fungsi untuk menghitung kalori yang terbakar
def kalori_terbakar(durasi, latihan):
    kaloripermenit = 0
    if latihan == "berlari":
        kaloripermenit = 100

elif latihan == "bersepeda":
    kaloripermenit = 200

elif latihan == "berenang":
    kaloripermenit = 300

return kaloripermenit * durasi

#fungsi
def main():
    result = kalori_terbakar(60, "berlari")
    print(result)

if __name__=="__main__":
main()
