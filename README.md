# 🚀 Azure Data Engineering: Customer Churn Pipeline

## 📌 Descripción del Proyecto
Este proyecto implementa una **Arquitectura Medallón** en la nube de Azure para procesar, transformar y analizar datos de retención de clientes (Churn) de una empresa de telecomunicaciones. El flujo de datos va desde la ingesta de archivos crudos hasta la visualización de indicadores estratégicos.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python (Pandas) en Visual Studio Code.
* **Nube:** Azure Data Lake Storage Gen2, Azure Data Factory, Azure SQL Database.
* **Visualización:** Power BI.

## 🏗️ Arquitectura del Pipeline (Medallion Architecture)
1. **Capa Bronce (Ingesta):** Almacenamiento del dataset original en formato CSV dentro de Azure Data Lake.
2. **Capa Plata (Transformación):** Script en Python (`script.py`) que extrae los datos, limpia duplicados, normaliza valores y guarda el resultado optimizado en formato columnar (Parquet).
3. **Capa Oro (Modelado):** Orquestación automatizada usando Azure Data Factory para inyectar los datos limpios hacia Azure SQL Database, estructurados en un modelo en estrella (`Dim_Customer` y `Fact_Churn`).

## 📊 Resultados y Visualización
Se desarrolló un Dashboard ejecutivo en Power BI conectado directamente a la base de datos SQL (DirectQuery/Import) que revela:
* Una **Tasa de Abandono Total** del 26.54%.
* Una concentración crítica de pérdida de clientes durante los primeros 5 meses de servicio.
* El impacto directo de los contratos de tipo "Mensual" y los pagos por "Cheque electrónico" en la fuga de ingresos.

*(Aquí insertas una captura de pantalla de tu dashboard de Power BI)*
