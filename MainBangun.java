import java.util.InputMismatchException;
import java.util.Scanner;

abstract class Bangun2D{
	int id;
	float p, t, l;

	abstract float hitungLuas();
	
	public void deskripsi(){
		System.out.println("Ini adalah sebuah bangun datar");
	}
	public int getId(){
		return id;
	}
	public float getPanjang(){
		return p;
	}
	public float getTinggi(){
		return t;
	}
	public void setPanjang(float pNew){
		p = pNew;
	}
	public void setTinggi(float tNew){
		t = tNew;
	}
}
class Segitiga extends Bangun2D{
	public Segitiga(int id_bangun, float p_bangun, float t_bangun){
	
		id = id_bangun;
		p = p_bangun;
		t = t_bangun;
	}
	public float hitungLuas(){
		l = (p * t) / 2;
		return l;
	}
	@Override
	public void deskripsi(){
		System.out.println("[Bangun = Segitiga; ID = " + id + "; Alas = " + p + "cm; Tinggi = " + t + "cm; Luas = " + hitungLuas() + "cm^2]");
	}
}
class Segiempat extends Bangun2D{
	public Segiempat(int id_bangun, float p_bangun, float t_bangun){
		
		id = id_bangun;
		p = p_bangun;
		t = t_bangun;
	}
	public float hitungLuas(){
		l = p * t;
		return l;
	}
	@Override
	public void deskripsi(){
		System.out.println("[Bangun = Segiempat; ID = " + id + "; Panjang = " + p + "cm; Lebar = " + t + "; Luas = " + hitungLuas() + "cm^2]");
	}
}
public class MainBangun{
	
	public static int TampilMenu(){
		Scanner inp = new Scanner(System.in);
		System.out.println("\n---------[[Simulasi Bangun]]---------\n   | 1. Buat objek bangun      |\n   | 2. Ubah atribut           |\n   | 3. Deskripsi sebuah objek |\n   | 4. Deskripsi semua objek  |\n   | 5. Keluar program         |");
		System.out.println("-------------------------------------");
		System.out.print("Pilih?>: ");
		int menuHome = inp.nextInt();
		return menuHome;
	}
	public static void main (String args[]){
		System.out.println("============ KELOMPOK PBO SIMULASI BANGUN ============");
		System.out.println("Nama	: I Made Novandy Asardi ---- NIM: 064002100030");
		System.out.println("Nama	: Sarah Sakinah         ---- NIM: 064002100033");
		System.out.println("Nama	: Nathanael Widjaya     ---- NIM: 064002100020");
		System.out.println("======================================================");
		Scanner inp = new Scanner(System.in);
		int pilih;
		int countId = 1;
		Bangun2D[] arrBangun = new Bangun2D[100];
		for(;;){
			pilih = TampilMenu();
			if (pilih == 1){
				System.out.println("Buat objek apa?\n(0-Segitiga atau 1-Segiempat)");
				int menu1 = inp.nextInt();
				for (;;){
					if (menu1 == 0){
						System.out.println("Nomor ID: " + countId);
						System.out.print("Alas? ");
						float alas = inp.nextFloat();
						System.out.print("Tinggi? ");
						float tinggi = inp.nextFloat();
						arrBangun[countId] = new Segitiga(countId, alas, tinggi);
						System.out.println("Objek Segitiga dengan ID = " + countId + " berhasil dibuat!");
						countId++;
						break;
					}
					else if (menu1 == 1){
						System.out.println("Nomor ID: " + countId);
						System.out.print("Panjang? ");
						float panjang = inp.nextFloat();
						System.out.print("Lebar? ");
						float lebar = inp.nextFloat();
						arrBangun[countId] = new Segiempat(countId, panjang, lebar);
						System.out.println("Objek Segiempat dengan ID = " + countId + " berhasil dibuat!");
						countId++;
						break;
					}
					else{
						System.out.println("Masukkan 0 untuk objek Segitiga atau 1 untuk objek Segiempat");
					}
				}
			}
			else if (pilih == 2){
				try{
					for (;;){
						System.out.println("Nomor ID?\n(Masukkan angka 1-" + countId + ") ");
						int id = inp.nextInt();
						arrBangun[id].deskripsi();
						if (id <= countId){
							System.out.print("Masukkan alas/panjang baru: ");
							float alpa = inp.nextFloat();
							System.out.print("Masukkan tinggi/lebar baru: ");
							float tile = inp.nextFloat();
							arrBangun[id].setPanjang(alpa);
							arrBangun[id].setTinggi(tile);
							break;
						}
						else{
							System.out.println("(Masukkan angka 1-" + countId + ")");
						}
					}
				}
				catch(NullPointerException e){
					System.out.println("Belum ada bangun datar yang telah dibuat.");
				}
			}
				
			else if (pilih == 3){
				try{
					for (;;){
						System.out.println("Nomor ID?\n(Masukkan angka 1-" + countId + ") ");
						int id = inp.nextInt();
						arrBangun[id].deskripsi();
						break;
					}
				}
				catch(NullPointerException e){
					System.out.println("Belum ada bangun datar yang telah dibuat.");
				}
			}
			else if (pilih == 4){
				for(int i = 0; i < arrBangun.length; i++){
					try {
						arrBangun[i].deskripsi();
					}
					catch(NullPointerException e){
						continue;
					}
				}
			}
			else if (pilih == 5){
					break;
				}
			else{
				System.out.println("Masukkan angka 1-5");
				}
		}
	}
}
