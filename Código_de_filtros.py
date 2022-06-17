DICT = {"Amazonas": ["Chachapoyas","Bagua","Bongara","Condorcanqui","Luya","Rodriguez de Mendoza","Utcubamba"], 
        "Áncash": ["Huaraz", "Aija", "Antonio Raimondi", "Asuncion","Bolognesi",
                   "Carhuaz","Carlos Fermín Fitzcarrald","Corongo","Huari",
                   "Huarmey","Mariscal Luzuriaga","Ocros","Pallasca",
                   "Pomabamba","Recuay","Santa","Sihuas","Yungay"],
        "Apurímac": ["Abancay","Andahuaylas","Antabamba","Aymaraes","Cotabambas","Chincheros","Grau"],
        "Arequipa":["Arequipa	","Camana","Caraveli","Caylloma","Condesuyos","Islay","La Union"],
        "Ayacucho":["Huamanga","Cangallo","Huanca Sancos","Huanta","La Mar",
                    "Lucanas","Parinacochas","Paucar del Sara Sara","Sucre","Victor Fajardo","Vilcas Huaman"],
        "Cajamarca":["Cajamarca","Cajabamba","Celendin","Chota","Contumazá","Cutervo",
                     "Hualgayoc","Jaen","San Ignacio","San Marcos","San Miguel","San Pablo","Santa Cruz"],
        "Callao":["Callao"],
        "Cusco":["Cusco","Acomayo","Calca","Canchis",
                 "Chumbivilcas","Espinar","La Convencion","Paruro","Paucartambo","Quispicanchi","Urubamba"],
        "Huancavelica":["Huancavelica","Acobamba","Angaraes","Castrovirreyna","Churcampa","Huaytara","Tayacaja"],
        "Huánuco":["Huánuco","Dos de Mayo","Huacaybamba","Huamalies",
                   "Leoncio Prado","Pachitea","Puerto Inca","Lauricocha","Yarowilca"],
        "Ica":["Chincha","Nazca","Palpa","Pisco"],
        "Junín":["Huancayo","Concepción","Chanchamayo","Jauja",
                 "Junín","Satipo","Tarma","Yauli","Chupaca"],
        "La Libertad":["Trujillo","Ascope","Bolivar","Chepen","Julcán","Otuzco",
                       "Pacasmayo","Pataz","Sanchez Carrion","Santiago de Chuco","Gran Chimu","Viru"],
        "Lambayeque":["Chiclayo","Ferreñafe","Lambayeque"],
        "Lima":["Lima","Barranca","Cajatambo","Canta","Cañete",
                "Huaral","Huarochiri","Huaura","Oyon","Yauyos"],
        "Loreto":["Maynas","Alto Amazonas","Loreto","Mariscal Ramon Castilla",
                  "Requena","Ucayali","Datem del Marañon","Putumayo"],
        "Madre de Dios":["Tambopata","Tahuamanu"],
        "Moquegua":["Mariscal Nieto","General Sanchez Cerro","Ilo"],
        "Pasco":["Pasco","Daniel Alcides Carrión","Oxapampa"],
        "Piura":["Piura","Ayabaca","Huancabamba","Morropón",
                 "Paita","Sullana","Talara","Sechura"],
        "Puno":["Puno","Azangaro","Carabaya","Chucuito","El Collao","Huancane",
                "Lampa","Melgar","Moho","San Antonio de Putina","San Román","Sandia","Yunguyo"],
        "San Martín":["Moyobamba","Bellavista","El Dorado","Huallaga","Lamas",
                      "Mariscal Cáceres","Picota","Rioja","San Martin","Tocache"],
        "Tacna":["Tacna","Candarave","Jorge Basadre","Tarata"],
        "Tumbes":["Tumbes","Contralmirante Villar","Zarumilla"],
        "Ucayali":["Coronel Portillo","Atalaya","Padre Abad","Purús"]}

LD = {"Amazonas","Áncash","Apurímac","Arequipa","Ayacucho",
      "Cajamarca","Callao","Cusco","Huancavelica","Huánuco",
      "Ica","Junín","La Libertad","Lambayeque","Lima",
      "Loreto","Madre de Dios","Moquegua","Pasco","Piura",
      "Puno","San Martín","Tacna","Tumbes","Ucayali"}

print("Seleccione un departamento:")
print(LD)

Dep = str(input("Ingrese el nombre del departamento:"))

if Dep in DICT:
  print("Seleccione una provincia dentro del departamento escogido:")
  print(DICT[Dep])
  P = str(input("Ingrese el nombre de la provincia: "))
  if P in DICT[Dep]:
    print("Los datos positivos de Covid-19 en la zona escogida son: ")
  else:
    print("Los párametros registrados corresponden a los casos positivos de Covid-19 de la siguiente zona: ")
else:
  print("Los párametros registrados corresponden a los casos positivos de Covid-19 de la siguiente zona: ")
