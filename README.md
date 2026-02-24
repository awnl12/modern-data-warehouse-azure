# 🚀 Azure Data Engineering: Customer Churn Pipeline

## 📌 Descripción del Proyecto
Este proyecto implementa una **Arquitectura Medallón** (Bronce, Plata, Oro) en la nube de Azure para procesar, transformar y analizar datos de retención de clientes (Churn) de una empresa de telecomunicaciones. El flujo de datos va desde la ingesta de archivos crudos hasta la visualización de indicadores estratégicos para la toma de decisiones.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python (Pandas) en Visual Studio Code.
* **Nube (Azure):** Azure Data Lake Storage Gen2, Azure Data Factory, Azure SQL Database.
* **Visualización:** Power BI (Import Mode).

## ☁️ Infraestructura en la Nube
Para este proyecto se provisionó un grupo de recursos (`rg-medallon`) que centraliza los servicios de orquestación, almacenamiento de big data y bases de datos relacionales:

> <img width="1907" height="869" alt="GrupoRecurso" src="https://github.com/user-attachments/assets/ebe05d7e-dc96-4bf6-8d1f-61b99591b6c3" />

---

## 🏗️ Arquitectura del Pipeline (Medallion Architecture)

### 1. Capa Bronce (Ingesta en Data Lake)
Almacenamiento del dataset original en formato CSV dentro de los contenedores de `datalakeproject2026`, estableciendo la zona de aterrizaje (Landing Zone) de los datos crudos.

> <img width="1916" height="728" alt="AlmacenamientoContenedores" src="https://github.com/user-attachments/assets/3c1784e6-2bfd-4385-8356-2ef8ab229119" />


### 2. Capa Plata (Transformación con Python)
Script de Python (Pandas) que extrae los datos, elimina duplicados, normaliza valores de texto, realiza hashing de IDs por seguridad y guarda el resultado optimizado en formato columnar (Parquet).

PARTE 1
> <img width="1901" height="1002" alt="ScriptPy-1" src="https://github.com/user-attachments/assets/f78b8316-e458-4d23-934a-d0c0c2744385" />
PARTE 2
> <img width="1860" height="856" alt="ScriptPy-2" src="https://github.com/user-attachments/assets/7ad01575-4050-40ce-a035-ac17b6ace0d4" />


### 3. Capa Oro (Orquestación con Azure Data Factory)
Orquestación automatizada para inyectar los datos limpios hacia la base de datos relacional. Se configuraron actividades de copia (`Copy Data`) asegurando la secuencia correcta para un modelo en estrella, manejando colisiones de llaves primarias mediante truncación de destino.

> <img width="1882" height="833" alt="ADF-CANALIZACION" src="https://github.com/user-attachments/assets/968ea094-c9c0-49e4-b626-b6d33c6d3a4c" />


### 4. Almacenamiento Estructurado (Azure SQL Database)
Los datos modelados residen en `sqldb-telco-gold`, divididos en tablas dimensionales (`Dim_Customer`) y de hechos (`Fact_Churn`), listos para el consumo analítico.

> <img width="1894" height="892" alt="ConsultaSQL" src="https://github.com/user-attachments/assets/ab4b0e33-34f7-42af-9a46-7ce6e1b08d5d" />


---

## 📊 Resultados y Visualización (Power BI)
Se desarrolló un Dashboard ejecutivo conectado directamente a la Capa Oro que revela:
* Una **Tasa de Abandono Total** del 26.54%.
* Una concentración crítica de pérdida de clientes durante los primeros meses de servicio (Early Churn).
* El impacto directo de los contratos de tipo "Mensual" y los pagos por "Cheque electrónico" en la fuga de ingresos.

> <img width="1428" height="675" alt="Dashboard-PowerBi" src="https://github.com/user-attachments/assets/ac43f8c5-cb2d-48ac-bd15-433ce3e1c305" />
