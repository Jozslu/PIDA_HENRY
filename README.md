# PIDA_HENRY

## Proyecto Individual N°2

Alumno: José Luis Martínez Chávez


> En este README encontrarán toda la documentación, e instrucciones necesarias, para poder visualizar el Dashboard, 
  con sus respectivos KPIs que se  solicitó desarrollar.

link del Dashborad: https://jozslu-streamlit-prueba-main-il21qs.streamlit.app/


**MENU:** 

* **KPI** - _carpeta que contiene los archivos necesarios para la creación de los KPIs._ 
	* **data_final.csv** - _data normalizada para la creación de los KPIs._
	* **KPIs.ipynb** - _notebook con los análisis necesarios para la creación de cada KPI._
	* **main.py** - _contiene la construcción del Dashboard._
	* **requirements.txt** - _ Lista de librerias o dependencias necesarias para la realización del deployment._
* **ETL.py** - _archivo.py con las transformaciones requeridas._
* **EDA.ipynb** - _notebook con las transformaciones requeridas._
* **README** - _Instrucciones de uso._
* **requirements.txt** - _ Lista de librerias o dependencias necesarias para la realización del deployment._
* **data_final.csv** - _data normalizada para la creación de los KPIs._
* **data_normalizada.csv** - _data normalizada que usamos para el EDA._
* **AccidentesAviones.csv** - _data inical del proyecto._

**INFORME DEL EDA**

   - Cantidad de variables y su respectivos tipos:
	   fecha                      datetime64[ns]
 	   HORA declarada             object        
 	   Ruta                       object        
 	   OperadOR                   object        
 	   flight_no                  object        
 	   route                      object        
 	   ac_type                    object        
 	   registration               object        
 	   cn_ln                      object        
 	   all_aboard                 Int64         
 	   PASAJEROS A BORDO          Int64         
 	   crew_aboard                Int64         
 	   cantidad de fallecidos     Int64         
 	   passenger_fatalities       Int64         
 	   crew_fatalities            Int64         
 	   ground                     Int64         
 	   summary                    object        
 	   Año                        int64         
 	   tasa_mortalidad            Float64       

	Total: Float64(1), Int64(7), datetime64[ns](1), int64(1), object(9)

   - Datos faltantes:
	   fecha			            0
	   HORA declarada		      2449
	   Ruta				            5
	   OperadOR			          10
	   flight_no			        3682
	   route			            762
	   ac_type			          13
	   registration			      272
	   cn_ln			            667
	   all_aboard			        17
     PASAJEROS A BORDO		  221
	   crew_aboard			      219
	   cantidad de fallecidos	8
 	   passenger_fatalities		235
	   crew_fatalities		    235
     ground			            44
	   summary	  	      	  59     
	
   - Análisis respecto a la Tasa de Mortalidad
	+ Con el análisis pudimos centrar nuestra atención en ciertas variables para la cración de los KPIs:
	  - fecha
	  - all_aboard
	  - cantidad de fallecidos
	  - PASAJEROS A BORDO
	  - OperadOR
	  - Ruta 


**Informa del análisis**
   - Realizando los análisis y las visualizaciones pudimos crear los KPIS:
	+ KPI-1: Tasa de mortalidad.
	+ KPI-2: Número de vidas salvadas a nivel anual. 
	+ KPI-3: Tasa de mortalidad promedia por operador.
	+ KPI-4: Tasa de mortalidad por ruta.
