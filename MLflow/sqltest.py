import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5001/")
mlflow.set_experiment("Test Experiment")

with mlflow.start_run():
    mlflow.log_param("param1", 5)
    mlflow.log_metric("metric1", 0.89)
