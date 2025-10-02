#### Prometheus and opentelemetry analytics

OpenTelemetry is an open-source observability framework for instrumenting, collecting, and exporting telemetry data—traces, metrics, and logs—from distributed systems and modern applications



<p align="center">
  <a href="https://opentelemetry.io/docs/what-is-opentelemetry/">
    <img src="./assets/opentelemetry.png" width="150" alt="ally" style="margin: 0 15px;" />
  </a>
</p>

<h1 align="center">
  opentelemetry Analytics
</h1>



### Steps to run the project locally


```bash
git clone https://github.com/uchiha-vivek/Monitoring-performance-with-opentelemetry-and-prometheus.git
cd Monitoring-performance-with-opentelemetry-and-prometheus
```

Make virtual environment

```bash
python -m venv venv
```

Activate the environment

```bash
venv\Scripts\activate
```

Install the requirements

```bash
pip install -r requirements.txt
```

run the main file

```bash
python app.py
```



Make sure to run docker dameon :

- open the docker desktop

 ```bash
docker-compose up -d
```

Hit the following endpoint to view the **JAEGER GUI** 
```http://localhost:16686/search```


Hit the following endpoints 

Endpoint 1:

```bash
http://localhost:5000/api/v1/products
```

endpoint 2:
```bash
http://localhost:5000/api/v1/products/1
```

