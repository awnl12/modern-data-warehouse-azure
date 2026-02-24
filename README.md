# 🚀 Azure Data Engineering: Customer Churn Pipeline (Modern Data Warehouse)

## 📌 Descripción del Proyecto
Este proyecto simula un escenario real del sector de telecomunicaciones implementando un **Modern Data Warehouse** en Azure bajo una **Arquitectura Medallón**. El objetivo principal fue construir un pipeline de datos (ETL) automatizado que procese información cruda de clientes, aplique reglas de limpieza y seguridad (anonimización), y disponibilice los datos en un modelo dimensional para descubrir patrones de abandono (Churn) a través de inteligencia de negocios.

## 🛠️ Stack Tecnológico
* **Procesamiento y ETL:** Python (Pandas, Hashlib) ejecutado en Visual Studio Code.
* **Almacenamiento Big Data:** Azure Data Lake Storage Gen2 (ADLS Gen2).
* **Orquestación y Movimiento:** Azure Data Factory (ADF).
* **Almacenamiento Relacional:** Azure SQL Database.
* **Consumo y BI:** Power BI Desktop.

## ☁️ Infraestructura en la Nube
Para este proyecto se provisionó un grupo de recursos (`rg-medallon`) que centraliza los servicios administrados (PaaS) de orquestación, almacenamiento estructurado y no estructurado:

> <img width="1907" height="869" alt="GrupoRecurso" src="https://github.com/user-attachments/assets/ebe05d7e-dc96-4bf6-8d1f-61b99591b6c3" />

---

## 🏗️ Arquitectura del Pipeline (Medallion Architecture)

### 1. Capa Bronce (Landing Zone)
Se estableció el contenedor `bronze` en **Azure Data Lake Storage Gen2** (`datalakeproject2026`) como zona de aterrizaje. Aquí se ingirió el dataset original (`.csv` con +7,000 registros), manteniéndolo en su estado crudo e inmutable para preservar el historial de origen.

> <img width="1916" height="728" alt="AlmacenamientoContenedores" src="https://github.com/user-attachments/assets/3c1784e6-2bfd-4385-8356-2ef8ab229119" />


### 2. Capa Plata (Transformación y Limpieza con Python)
Se desarrolló un script de **Python (Pandas)** para ejecutar las siguientes reglas de negocio y calidad de datos:
* **Limpieza:** Identificación y eliminación de registros duplicados (`drop_duplicates`) y manejo de valores inconsistentes.
* **Estandarización:** Normalización de variables categóricas (ej. traducción de métodos de pago y contratos al español para facilitar el consumo del usuario final).
* **Gobernanza y Seguridad (PII):** Aplicación de una función de encriptación (Hashing SHA-256) a la columna `CustomerID` para proteger la Identidad Personal del cliente, cumpliendo con las mejores prácticas de privacidad.
* **Optimización:** Exportación del dataframe resultante al contenedor `silver` en formato columnar **Parquet**, reduciendo drásticamente el peso del archivo y acelerando los tiempos de lectura.

PARTE 1
> <img width="1901" height="1002" alt="ScriptPy-1" src="https://github.com/user-attachments/assets/f78b8316-e458-4d23-934a-d0c0c2744385" />
PARTE 2
> <img width="1860" height="856" alt="ScriptPy-2" src="https://github.com/user-attachments/assets/7ad01575-4050-40ce-a035-ac17b6ace0d4" />


### 3. Capa Oro (Orquestación con Azure Data Factory)
Diseño de canalizaciones (Pipelines) automatizadas en `adf-telco-project-2026` para el movimiento de datos hacia la capa de consumo:
* Configuración de *Linked Services* y *Datasets* dinámicos para la conexión segura entre el Data Lake y Azure SQL.
* Uso de actividades **Copy Data** secuenciales (dependencias de éxito) para respetar la integridad referencial del modelo dimensional.
* Implementación de **Idempotencia** mediante scripts de truncación de destino (`TRUNCATE TABLE`) previos a la copia, asegurando que el pipeline soporte cargas completas (Full Load) repetitivas sin colisiones de llaves primarias.

> <img width="1882" height="833" alt="ADF-CANALIZACION" src="https://github.com/user-attachments/assets/968ea094-c9c0-49e4-b626-b6d33c6d3a4c" />


### 4. Almacenamiento Estructurado (Azure SQL Database)
Implementación de un **Modelo en Estrella (Star Schema)** utilizando DDL (Data Definition Language) en `sqldb-telco-gold`:
* **Dim_Customer:** Tabla dimensional que almacena atributos demográficos (género, edad, dependientes).
* **Fact_Churn:** Tabla de hechos que centraliza las métricas financieras (cargos mensuales/totales), la vigencia del servicio y el indicador binario de abandono.

> <img width="1894" height="892" alt="ConsultaSQL" src="https://github.com/user-attachments/assets/ab4b0e33-34f7-42af-9a46-7ce6e1b08d5d" />

---

## 📊 Business Intelligence y Resultados (Power BI)
Se conectó un modelo semántico en Power BI mediante importación directa desde la base de datos SQL. Se modeló una relación `1:N` entre la dimensión y la tabla de hechos para crear un Dashboard Ejecutivo que reveló los siguientes insights accionables:
* **Métrica Principal:** Una Tasa de Abandono Total del **26.54%**.
* **Alerta de Early Churn:** Identificación de un pico crítico de pérdida de clientes durante el primer mes de servicio, sugiriendo fallas en el proceso de *onboarding* o expectativa del servicio.
* **Impacto Financiero:** Demostración gráfica de que los contratos "Mes a mes" y los pagos vía "Cheque electrónico" concentran el mayor riesgo de fuga de capital de la compañía.

> <img width="1428" height="675" alt="Dashboard-PowerBi" src="https://github.com/user-attachments/assets/ac43f8c5-cb2d-48ac-bd15-433ce3e1c305" />
