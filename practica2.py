from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA
from PIL import ImageTk, Image
import tkinter as tk

raiz=Tk()
raiz.title("Cipher/Deciphered")
raiz.resizable(0,0)
raiz.iconbitmap("huella.ico")
raiz.geometry("400x250")
raiz.config(bg="cyan")

myFrame=Frame()
myFrame.pack(side="top")
myFrame.config(bg="white")
#myFrame.config(width="350", height="350")
#Logo ESCOM
imagen=tk.PhotoImage(file="logoescom.png")
imagen_sub=imagen.subsample(12)
widget=ttk.Label(image=imagen_sub)
widget.place(x=5,y=5)

#Logo IPN
imageni=tk.PhotoImage(file="ipn.png")
imageni_sub=imageni.subsample(15)
widgeti=ttk.Label(image=imageni_sub)
widgeti.place(x=315,y=5)
text = Label(text="Escuela Superior de Computo\n Oswaldo Aguilar Martinez\n Miguel Anguel Arevalo Andrade")
text.place(x=125,y=7)
combo=ttk.Combobox(raiz)
combo.place(x=200,y=100)
combo['values']=('Vigenére','Affine')
combo1=ttk.Combobox(raiz)
text1= Label(text="Alfabeto")
text1.place(x=120,y=130)
combo1.place(x=200,y=130)
combo1['values']=('Español','Ingles')

def seleccionar_funcion():
        combo_sel=combo.get()
        if combo_sel == "Español":
            n=27
        elif combo_sel == "Ingles":
            n=26
        else:
            messagebox.showinfo("Error ","You must select an option")
        return n

def Euclides(m, n):
	r=0
	while (n!=0):
		r=m%n
		m=n
		n=r
	return m

def Inverse(y,p):
    (b,z,x)=ExtEuclidean(y,p)
    if(z<0):
        z=z+p
    return z

def ExtEuclidean(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    numiteraciones = 0
    while a:
        (q, a), b = (b // a, b % a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
        numiteraciones += 1
    return b, x0, y0


def Encrypt(String plain_text, int alphabet_length, int alpha, int beta)
    {
        f=open("mensaje_d.txt","wb")
        f.write(decifrarmensaje)
        f.close
        for (int i=0; i<plain_text.length(); i++)
        {
            int P_n = (int)plain_text.charAt(i);
            int C_n = ((alpha * P_n) + beta) % alphabet_length;
            cipher_text.append((char)C_n);
        }

        return cipher_text.toString();
    }

     #/*
     #*  Aplicando la formula de des cifrado: P_n = alpha^-1 * [ C_n + (-beta) ] mod longitud_del_alfabeto, donde:
     #*  C_n, es el carácter del texto en claro descifrado
     #*  P_n, es la letra de la posicion n del texto cifrado
     #*  alpha, es el valor multiplicativo de la llave en inverso multiplicativo
     #*  beta, es el valor aditivo de la llave en inverso aditivo
     #* */
    public static String Decrypt(String cipher_text, int alphabet_length, int alpha, int beta)
    {
        StringBuilder decipher_text = new StringBuilder();

        for (int i=0; i<cipher_text.length(); i++)
        {
            int C_n = (int)cipher_text.charAt(i);
            int alpha_inverso_multiplicativo = AritmeticaModular.InversoMultiplicativo(alpha, alphabet_length);
            int beta_inverso_aditivo = AritmeticaModular.InversoAditivo(beta, alphabet_length);
            int P_n = ( alpha_inverso_multiplicativo * ( C_n + beta_inverso_aditivo ) ) % alphabet_length;

            decipher_text.append((char)P_n);
        }
        return decipher_text.toString();
    }

m=int(input("Ingresa el valor de alpha: "))
n=int(input("Ingresa el valor de n: "))
print("GCD: ",Euclides(m,n))
if(Euclides(m,n)==1):
	print("Llave valida\n")
else:
	print("Llave invalida\n")
print("Inverso Multiplicativo: ",Inverse(m,n))
print(seleccionar_funcion)
