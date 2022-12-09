from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import array as array

driver = webdriver.Chrome(executable_path="Driver/chromedriver.exe")

driver.maximize_window()

driver.get("https://www.viajesexito.com/")

#ir a la pagina de paquetes vuelo + hotel
paquetes = driver.find_element(By.XPATH, "/html/body/form/header/div[2]/div/div/nav/div[2]/a")
paquetes.click()

time.sleep(1)
#fin

#busqueda destino punta cana
destinoTxt = "punta cana"
destino = driver.find_element(By.XPATH, "/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[3]/div/div/input")
destino.click()
destino.send_keys(destinoTxt)
destino2 = driver.find_element(By.XPATH, "/html/body/ul[21]")
destino2.click()

time.sleep(1)

fechaIdaBtn = driver.find_element(By.XPATH, "/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/input")
fechaIdaBtn.click()

fechaIda = driver.find_element(By.XPATH, "/html/body/div[21]/div[1]/table/tbody/tr[3]/td[3]/a")
fechaIda.click()

fechaRegreso = driver.find_element(By.XPATH, "/html/body/div[21]/div[1]/table/tbody/tr[4]/td[4]/a")
fechaRegreso.click()

time.sleep(1)

habitaciones = driver.find_element(By.XPATH, "/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div/p")
habitaciones.click()

adultos = driver.find_element(By.XPATH, "/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div/span[2]/button/span")
adultos.click()

aplicarAdultos = driver.find_element(By.XPATH, "/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/button")
aplicarAdultos.click()

time.sleep(1)

buscar = driver.find_element(By.XPATH, "/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[4]/a/span")
buscar.click()
#fin

#tiempo de 10 segundos porque la pagina es demorada para cargar completamente
time.sleep(20)

#Impresion de informacion en consola

print("----------------------Precios----------------------")
    #PROFE INTENTE HACER ESTO POR UN CICLO PERO TENIA UN ERROR MUY RARO ENTONCES LO HICE 1 POR 1 (Aqui esta el ciclo por si lo quiere ver y me dice porfa que esta mal)

    # for i in range (10):
    #     precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[" + str(i+1) + "]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
    #     print(precio)

precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[2]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[3]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[4]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[5]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[6]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[7]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[8]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[9]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[10]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
#fin

#Seleccionar avianca
avianca = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[2]/div[1]/div/div[5]/div/div/div[1]/div[1]/input")
avianca.click()

print("----------------------Precios Avianca----------------------")

time.sleep(5)

precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[2]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[3]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[4]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[5]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[6]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[7]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[8]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[9]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
precio = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[10]/div/div/div[2]/div/div[1]/div/p[1]/span[2]").text
print(precio)
#fin